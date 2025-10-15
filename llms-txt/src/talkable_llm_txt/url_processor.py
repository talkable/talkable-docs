"""
URL Processing Module

This module provides classes for processing and transforming URLs
following the single responsibility principle and separation of concerns.
"""

from abc import ABC, abstractmethod
from typing import Optional
from urllib.parse import urljoin, urlparse, urlunparse


class URLProcessor(ABC):
    """Abstract base class for URL processing operations"""

    @abstractmethod
    def process(self, url: str) -> str:
        """Process a URL and return the result"""
        pass


class URLNormalizer(URLProcessor):
    """Normalizes relative URLs to absolute URLs"""

    def __init__(self, base_url: str):
        """
        Initialize the URL normalizer.

        Args:
            base_url: Base URL for normalization (e.g., "http://localhost:8080")
        """
        self.base_url = base_url.rstrip("/")

    def process(self, url: str, context_url: Optional[str] = None) -> str:
        """
        Convert relative URL to absolute URL.

        Args:
            url: Relative URL to normalize (absolute URLs are not processed)
            context_url: Current page URL to provide context for relative links

        Returns:
            Absolute URL with proper context resolution
        """
        if url.startswith("/"):
            # Root-relative path
            return self.base_url + url
        elif context_url:
            # Relative path - use current page's context for proper resolution
            return urljoin(context_url, url)
        else:
            # Relative path - fallback to base URL
            return urljoin(self.base_url + "/", url)


class MarkdownFileConverter(URLProcessor):
    """Converts URLs to point to .md files"""

    def process(self, url: str) -> str:
        """
        Convert URL to point to markdown file.

        Args:
            url: URL to convert

        Returns:
            URL with .md extension and proper path handling
        """
        parsed = urlparse(url)
        path = parsed.path.rstrip("/")

        # Handle root path
        if not path or path == "/":
            path = "/index"

        # Add .md extension
        path = path + ".md"

        # Reconstruct URL with new path, preserving other components
        return urlunparse(
            (
                parsed.scheme,
                parsed.netloc,
                path,
                parsed.params,
                parsed.query,
                parsed.fragment,  # Preserve #anchor
            )
        )


class LinkProcessor:
    """Orchestrates URL processing pipeline for link transformation"""

    def __init__(self, base_url: str):
        """
        Initialize the link processor.

        Args:
            base_url: Base URL for processing (e.g., "http://localhost:8080")
        """
        self.normalizer = URLNormalizer(base_url)
        self.markdown_converter = MarkdownFileConverter()

    def process_link(
        self,
        href: str,
        context_url: Optional[str] = None,
        link_class: Optional[str] = None,
    ) -> Optional[str]:
        """
        Process a link through the complete pipeline.

        Args:
            href: Link href attribute to process
            context_url: Current page URL to provide context for relative links
            link_class: CSS class string from the link element

        Returns:
            Processed URL pointing to .md file, or None if should not process
        """
        if not self._should_process(href, link_class):
            return None

        # Step 1: Normalize URL to absolute with context
        normalized = self.normalizer.process(href, context_url)
        # Step 2: Convert to markdown file URL
        return self.markdown_converter.process(normalized)

    def _should_process(self, href: str, link_class: Optional[str] = None) -> bool:
        """
        Determine if link should be processed using simplified logic.

        Args:
            href: Link href attribute to check
            link_class: CSS class string from the link element

        Returns:
            True if link should be processed (internal), False otherwise (external)
        """
        # Skip empty links and special protocols
        if (
            not href
            or not href.strip()
            or href.startswith(("mailto:", "tel:", "javascript:", "ftp:", "file:", "#"))
        ):
            return False

        # External URLs - don't process (fail safe)
        if href.startswith(("http://", "https://")):
            return False

        # Internal links - process them if we can identify them
        # Use class name if available
        if link_class and "reference internal" in link_class:
            return True

        # If we can't identify the URL type, treat as external (fail safe)
        return False
