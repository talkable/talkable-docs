import asyncio
from typing import Any, Dict, List, Literal, Optional

from playwright.async_api import BrowserContext, async_playwright


class PlaywrightFetcher:
    # PEP 8 compliant constants
    DEFAULT_MAX_CONCURRENT = 5
    DEFAULT_TIMEOUT = 30000
    DEFAULT_WAIT_UNTIL: Literal["commit", "domcontentloaded", "load", "networkidle"] = (
        "domcontentloaded"
    )
    BLOCKED_RESOURCE_TYPES = {"image", "media"}
    BLOCKED_FILE_PATTERNS = [
        "**/*.{png,jpg,jpeg,gif,svg,webp}",
        "**/*.{mp4,webm,mp3,wav}",
        "**/*.{pdf,doc,docx,xls,xlsx}",
    ]

    def __init__(
        self,
        max_concurrent: Optional[int] = None,
        timeout: Optional[int] = None,
        wait_until: Optional[
            Literal["commit", "domcontentloaded", "load", "networkidle"]
        ] = None,
    ):
        self.max_concurrent = max_concurrent or self.DEFAULT_MAX_CONCURRENT
        self.timeout = timeout or self.DEFAULT_TIMEOUT
        self.wait_until = wait_until or self.DEFAULT_WAIT_UNTIL
        self.semaphore = asyncio.Semaphore(self.max_concurrent)

    def _create_result_dict(self, url: str, **kwargs) -> Dict[str, Any]:
        """Create a consistent result dictionary"""
        return {"url": url, "html": None, "status": None, "error": None, **kwargs}

    def _create_error_result(self, url: str, error: str) -> Dict[str, Any]:
        """Create an error result dictionary"""
        return self._create_result_dict(url, error=error)

    async def fetch_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        """
        Fetch HTML content for multiple URLs using single browser with context pool

        Args:
            urls: List of URLs to fetch

        Returns:
            List of dictionaries containing url, html, and status/error info
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            context = None
            try:
                context = await browser.new_context()
                await self._setup_resource_blocking(context)

                tasks = [self._fetch_single_url(context, url) for url in urls]
                results = await asyncio.gather(*tasks, return_exceptions=True)

                return self._process_results(results, urls)

            finally:
                if context:
                    await context.close()
                await browser.close()

    def _process_results(self, results: List, urls: List[str]) -> List[Dict[str, Any]]:
        """Process and normalize results from asyncio.gather"""
        processed_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                processed_results.append(
                    self._create_error_result(urls[i], str(result))
                )
            else:
                processed_results.append(result)
        return processed_results

    async def _setup_resource_blocking(self, context: BrowserContext) -> None:
        """Setup unified resource blocking with single routing mechanism"""
        await context.route("**/*", self._block_resources)

    async def _block_resources(self, route) -> None:
        """Unified resource blocking logic - eliminates duplication"""
        request = route.request
        resource_type = request.resource_type
        url = request.url

        # Check file patterns first (more specific)
        if any(pattern in url for pattern in self.BLOCKED_FILE_PATTERNS):
            await route.abort()
            return

        # Check resource types
        if resource_type in self.BLOCKED_RESOURCE_TYPES:
            await route.abort()
        else:
            await route.continue_()

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

            try:
                # Use configured timeout and wait_until
                response = await page.goto(
                    url,
                    timeout=self.timeout,
                    wait_until=self.wait_until,  # type: ignore
                )

                if response:
                    html = await page.content()
                    return self._create_result_dict(
                        url, html=html, status=response.status
                    )
                else:
                    return self._create_error_result(url, "No response received")

            except Exception as e:
                return self._create_error_result(url, str(e))

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
        return results[0] if results else self._create_error_result(url, "No results")

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
