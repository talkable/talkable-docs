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

    def process(self, url: str) -> str:
        """
        Convert relative URL to absolute URL.

        Args:
            url: Relative or absolute URL to normalize

        Returns:
            Absolute URL with base URL prepended
        """
        if url.startswith("/"):
            # Root-relative path
            return self.base_url + url
        else:
            # Relative path - use urljoin for proper resolution
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
        return urlunparse((
            parsed.scheme,
            parsed.netloc,
            path,
            parsed.params,
            parsed.query,
            parsed.fragment,  # Preserve #anchor
        ))


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

    def process_link(self, href: str) -> Optional[str]:
        """
        Process a link through the complete pipeline.

        Args:
            href: Link href attribute to process

        Returns:
            Processed URL pointing to .md file, or None if should not process
        """
        if not self._should_process(href):
            return None

        # Step 1: Normalize URL to absolute
        normalized = self.normalizer.process(href)
        # Step 2: Convert to markdown file URL
        return self.markdown_converter.process(normalized)

    def _should_process(self, href: str) -> bool:
        """
        Determine if link should be processed.

        Args:
            href: Link href attribute to check

        Returns:
            True if link should be processed, False otherwise
        """
        # Skip empty links
        if not href or not href.strip():
            return False

        # Skip external links (already absolute with http/https)
        if href.startswith(("http://", "https://")):
            return False

        # Skip special protocols
        if href.startswith(("mailto:", "tel:", "javascript:", "ftp:", "file:")):
            return False

        # Skip anchor-only links
        if href.startswith("#"):
            return False

        # Process all other links (relative paths, root-relative paths)
        return True
