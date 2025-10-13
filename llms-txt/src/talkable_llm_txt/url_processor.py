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
            url: Relative or absolute URL to normalize
            context_url: Current page URL to provide context for relative links

        Returns:
            Absolute URL with proper context resolution and domain correction
        """
        if url.startswith("/"):
            # Root-relative path
            return self.base_url + url
        elif url.startswith(("http://", "https://")):
            # Absolute URL - check if domain needs correction
            return self._correct_domain(url)
        elif context_url:
            # Relative path - use current page's context for proper resolution
            return urljoin(context_url, url)
        else:
            # Relative path - fallback to base URL
            return urljoin(self.base_url + "/", url)

    def _correct_domain(self, url: str) -> str:
        """
        Correct the domain of absolute URLs to match our base URL.

        Args:
            url: Absolute URL to check and potentially correct

        Returns:
            URL with corrected domain if needed, original URL otherwise
        """
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)

        # If the URL has the same port but different host/IP, correct it
        if (
            parsed.port == base_parsed.port
            and parsed.scheme == base_parsed.scheme
            and parsed.netloc != base_parsed.netloc
        ):
            # Replace the netloc with our base URL's netloc
            return urlunparse(
                (
                    parsed.scheme,
                    base_parsed.netloc,
                    parsed.path,
                    parsed.params,
                    parsed.query,
                    parsed.fragment,
                )
            )

        # Return original URL if no correction needed
        return url


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
        self, href: str, context_url: Optional[str] = None
    ) -> Optional[str]:
        """
        Process a link through the complete pipeline.

        Args:
            href: Link href attribute to process
            context_url: Current page URL to provide context for relative links

        Returns:
            Processed URL pointing to .md file, or None if should not process
        """
        if not self._should_process(href):
            return None

        # Step 1: Normalize URL to absolute with context and domain correction
        normalized = self.normalizer.process(href, context_url)
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

        # Skip special protocols
        if href.startswith(("mailto:", "tel:", "javascript:", "ftp:", "file:")):
            return False

        # Skip anchor-only links
        if href.startswith("#"):
            return False

        # Skip external absolute URLs (different domains)
        if href.startswith(("http://", "https://")):
            # Only process absolute URLs that might need domain correction
            # (same port but different host as our base URL)
            parsed = urlparse(href)
            base_parsed = urlparse(self.normalizer.base_url)

            # Only process if same port and scheme but different host
            if (
                parsed.port == base_parsed.port
                and parsed.scheme == base_parsed.scheme
                and parsed.netloc != base_parsed.netloc
            ):
                return True
            # Skip all other external URLs
            return False

        # Process all other links (relative paths, root-relative paths)
        return True
