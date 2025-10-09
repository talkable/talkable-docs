import logging
import time
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

import requests

# Module-level logger following official Python documentation best practices
logger = logging.getLogger(__name__)


class SitemapProcessor:
    # PEP 8 compliant constants
    SITEMAP_NAMESPACE = {"sitemap": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    BACKOFF_BASE = 2

    def __init__(
        self,
        sitemap_url: str,
        timeout: int = 30,
        retries: int = 3,
        user_agent: str = "Mozilla/5.0 (compatible; SitemapProcessor/1.0)",
        auto_process: bool = True,
    ):
        self.sitemap_url = self._validate_sitemap_url(sitemap_url)
        self.timeout = timeout
        self.retries = retries
        self.user_agent = user_agent
        self._processed_urls: List[Dict[str, str]] = []
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": self.user_agent})

        # Process sitemap immediately after initialization if requested
        if auto_process:
            self._process_sitemap()

    @property
    def processed_urls(self) -> List[Dict[str, str]]:
        """Return list of objects with URL and path properties"""
        return self._processed_urls

    def _process_sitemap(self) -> None:
        """Process the sitemap and populate processed_urls"""
        urls = self._fetch_all_urls()
        self._processed_urls = [
            {"url": url, "path": self._extract_path(url)} for url in urls
        ]

    def _fetch_all_urls(self) -> List[str]:
        """Fetch all URLs from sitemap, handling sitemap indexes"""
        sitemap_content = self._fetch_sitemap(self.sitemap_url)
        if not sitemap_content:
            return []

        urls, sitemap_urls = self._parse_xml_content(sitemap_content)

        if sitemap_urls:
            # This is a sitemap index - fetch all child sitemaps
            return self._fetch_child_sitemaps(sitemap_urls)
        else:
            # This is a regular sitemap
            return urls

    def _fetch_child_sitemaps(self, sitemap_urls: List[str]) -> List[str]:
        """Fetch and parse all child sitemaps"""
        all_urls = []
        for sitemap_url in sitemap_urls:
            child_content = self._fetch_sitemap(sitemap_url)
            if child_content:
                urls, _ = self._parse_xml_content(child_content)
                all_urls.extend(urls)
        return all_urls

    def _parse_xml_content(self, xml_content: str) -> Tuple[List[str], List[str]]:
        """Parse XML content and return (urls, sitemap_urls)"""
        try:
            root = ET.fromstring(xml_content)
            urls = self._extract_urls_from_elements(root, ".//sitemap:url")
            sitemap_urls = self._extract_urls_from_elements(root, ".//sitemap:sitemap")
            return urls, sitemap_urls
        except ET.ParseError as e:
            self._log_error(f"XML parsing error: {e}")
            return [], []

    def _extract_urls_from_elements(self, root: ET.Element, xpath: str) -> List[str]:
        """Extract URLs from XML elements using XPath"""
        urls = []
        for elem in root.findall(xpath, self.SITEMAP_NAMESPACE):
            loc = elem.find("sitemap:loc", self.SITEMAP_NAMESPACE)
            if loc is not None and loc.text:
                urls.append(loc.text)
        return urls

    def _fetch_sitemap(self, url: str, retries: Optional[int] = None) -> Optional[str]:
        """Fetch sitemap XML with error handling and retries"""
        retries = retries or self.retries
        for attempt in range(retries):
            try:
                response = self.session.get(url, timeout=self.timeout)
                response.raise_for_status()
                return response.text
            except requests.exceptions.RequestException as e:
                if attempt == retries - 1:
                    self._log_error(f"Failed to fetch {url}: {e}")
                    return None
                time.sleep(self.BACKOFF_BASE**attempt)  # Exponential backoff
        return None

    def _validate_sitemap_url(self, url: str) -> str:
        """Validate and normalize sitemap URL"""
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError(f"Invalid sitemap URL: {url}")
        if parsed.scheme not in ("http", "https"):
            raise ValueError(f"Unsupported scheme: {parsed.scheme}")
        return url

    def _log_error(self, message: str) -> None:
        """Centralized error logging"""
        logger.info(message)  # Replaced with proper logging

    def _extract_path(self, url: str) -> str:
        """Extract path from full URL, removing query parameters"""
        return urlparse(url).path

    def process(self) -> None:
        """Manually trigger sitemap processing"""
        if not self._processed_urls:
            self._process_sitemap()

    def close(self) -> None:
        """Clean up resources"""
        if hasattr(self, "session"):
            self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
