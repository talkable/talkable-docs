import asyncio
import logging
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Literal, Optional, Set

from playwright.async_api import (
    BrowserContext,
    async_playwright,
)
from playwright.async_api import (
    TimeoutError as PlaywrightTimeoutError,
)

# Module-level logger following official Python documentation best practices
logger = logging.getLogger(__name__)


class PlaywrightFetcher:
    # PEP 8 compliant constants
    DEFAULT_MAX_CONCURRENT = 5
    DEFAULT_TIMEOUT = 30000
    DEFAULT_WAIT_UNTIL: Literal["commit", "domcontentloaded", "load", "networkidle"] = (
        "domcontentloaded"
    )
    BLOCKED_RESOURCE_TYPES = {"image", "media", "font"}

    def __init__(
        self,
        max_concurrent: Optional[int] = None,
        timeout: Optional[int] = None,
        wait_until: Optional[
            Literal["commit", "domcontentloaded", "load", "networkidle"]
        ] = None,
        batch_size: int = 10,
        blocked_resource_types: Optional[Set[str]] = None,
    ):
        self.max_concurrent = max_concurrent or self.DEFAULT_MAX_CONCURRENT
        self.timeout = timeout or self.DEFAULT_TIMEOUT
        self.wait_until = wait_until or self.DEFAULT_WAIT_UNTIL
        self.batch_size = batch_size
        self.blocked_resource_types = (
            blocked_resource_types or self.BLOCKED_RESOURCE_TYPES
        )
        self.semaphore = asyncio.Semaphore(self.max_concurrent)

    def _create_result(
        self, url: str, html=None, status=None, error=None
    ) -> Dict[str, Any]:
        """Create a consistent result dictionary"""
        return {"url": url, "html": html, "status": status, "error": error}

    def _handle_request_failed(self, request, page_url: str) -> None:
        """Simplified requestfailed event handling following documentation best practices"""
        logger.debug(f"Request failed: {request.url}")

    @asynccontextmanager
    async def _browser_context(self):
        """Context manager for browser lifecycle with proper cleanup"""
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            context = None
            try:
                context = await browser.new_context()
                await self._setup_resource_blocking(context)

                # Add error handling for context
                context.on(
                    "weberror",
                    lambda web_error: logger.error(f"Context error: {web_error.error}"),
                )

                yield context
            finally:
                if context:
                    # Clean up routes before closing
                    await context.unroute_all()
                    await context.close()
                await browser.close()

    async def fetch_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        """
        Fetch HTML content for multiple URLs using batch processing

        Args:
            urls: List of URLs to fetch

        Returns:
            List of dictionaries containing url, html, and status/error info
        """
        all_results = []

        # Process URLs in batches to manage memory
        for i in range(0, len(urls), self.batch_size):
            batch = urls[i : i + self.batch_size]

            async with self._browser_context() as context:
                tasks = [self._fetch_single_url(context, url) for url in batch]
                batch_results = await asyncio.gather(*tasks, return_exceptions=True)
                processed_batch = self._process_results(batch_results, batch)
                all_results.extend(processed_batch)

        return all_results

    def _process_results(self, results: List, urls: List[str]) -> List[Dict[str, Any]]:
        """Process and normalize results from asyncio.gather"""
        processed_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                processed_results.append(
                    self._create_result(urls[i], error=str(result))
                )
            else:
                processed_results.append(result)
        return processed_results

    async def _setup_resource_blocking(self, context: BrowserContext) -> None:
        """Setup simplified resource blocking with single route handler"""

        async def handle_route(route):
            if route.request.resource_type in self.blocked_resource_types:
                await route.abort()
            else:
                await route.continue_()

        await context.route("**/*", handle_route)

    async def _fetch_single_url(
        self, context: BrowserContext, url: str
    ) -> Dict[str, Any]:
        """
        Fetch a single URL with proper error handling and resource management

        Args:
            context: Browser context to use
            url: URL to fetch

        Returns:
            Dictionary with url, html, status, and error information
        """
        async with self.semaphore:
            page = await context.new_page()

            # Add error event handlers for monitoring
            page.on(
                "pageerror", lambda exc: logger.error(f"Page error for {url}: {exc}")
            )
            page.on("requestfailed", lambda req: self._handle_request_failed(req, url))

            try:
                # Use configured timeout and wait_until
                response = await page.goto(
                    url,
                    timeout=self.timeout,
                    wait_until=self.wait_until,  # type: ignore
                )

                if response:
                    html = await page.content()
                    return self._create_result(url, html=html, status=response.status)
                else:
                    return self._create_result(url, error="No response received")

            except PlaywrightTimeoutError:
                return self._create_result(url, error=f"Timeout after {self.timeout}ms")
            except Exception as e:
                return self._create_result(url, error=str(e))

            finally:
                await page.close()

    async def fetch_single_url(self, url: str) -> Dict[str, Any]:
        """
        Efficient single URL fetching without full browser recreation

        Args:
            url: URL to fetch

        Returns:
            Dictionary with url, html, status, and error information
        """
        results = await self.fetch_urls([url])
        return results[0] if results else self._create_result(url, error="No results")

    def get_stats(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Get statistics about the fetching results

        Args:
            results: List of fetch results

        Returns:
            Dictionary with success/failure statistics
        """
        total = len(results)
        successful = sum(
            1 for r in results if r.get("html") is not None and r.get("error") is None
        )
        failed = total - successful

        return {
            "total_urls": total,
            "successful": successful,
            "failed": failed,
            "success_rate": (successful / total * 100) if total > 0 else 0,
        }
