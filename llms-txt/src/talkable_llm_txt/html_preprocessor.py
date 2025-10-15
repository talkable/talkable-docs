import logging
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup
from bs4.element import Tag

try:
    from .url_processor import LinkProcessor
except ImportError:
    # Fallback for when url_processor is not yet available
    LinkProcessor = None

# Module-level logger following official Python documentation best practices
logger = logging.getLogger(__name__)


class HTMLPreprocessor:
    """
    HTML preprocessing for extracting article content from web pages.

    This class handles the extraction of article elements from HTML content
    fetched by Playwright, providing clean content for markdown conversion.
    """

    def __init__(self, images: bool = False, base_url: Optional[str] = None):
        """
        Initialize the HTML preprocessor.

        Args:
            images: If True, keep images as-is. If False, replace with placeholder descriptions.
                   Default is False (images replaced with descriptions).
            base_url: Base URL for normalizing relative links to point to markdown files.
                     If provided, internal links will be converted to .md file URLs.
        """
        self.images = images
        self.link_processor = (
            LinkProcessor(base_url) if base_url and LinkProcessor else None
        )

    def extract_article(
        self, html: Optional[str], current_page_url: Optional[str] = None
    ) -> Optional[str]:
        """
        Extract article element from Playwright-rendered HTML.

        Args:
            html: HTML content from PlaywrightFetcher (can be None)
            current_page_url: Current page URL to provide context for relative links

        Returns:
            Article HTML as string, or None if no article element found
        """
        if html is None or not html.strip():
            return None

        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")

        if article:
            # Apply preprocessing to the article
            self._preprocess_article(article, current_page_url)
            return str(article)
        return None

    def _preprocess_article(self, article, current_page_url: Optional[str] = None):
        """
        Apply preprocessing steps to article content.

        Args:
            article: BeautifulSoup article element to preprocess
            current_page_url: Current page URL to provide context for relative links
        """
        self._remove_header_links(article)
        self._remove_copy_buttons(article)
        self._remove_images(article)
        self._process_links(article, current_page_url)

    def _remove_header_links(self, article: Optional[Tag]) -> None:
        """
        Remove all headerlink anchor elements from article.

        Args:
            article: BeautifulSoup article element (can be None)
        """
        if not article:
            return
        header_links = article.find_all("a", class_="headerlink")
        for link in header_links:
            link.decompose()

    def _remove_copy_buttons(self, article: Optional[Tag]) -> None:
        """
        Remove all copy button elements from article.

        Args:
            article: BeautifulSoup article element (can be None)
        """
        if not article:
            return
        copy_buttons = article.find_all("button", class_="copybtn")
        for button in copy_buttons:
            button.decompose()

    def _remove_images(self, article: Optional[Tag]) -> None:
        """
        Replace images with placeholder or keep them as-is.

        Args:
            article: BeautifulSoup article element (can be None)
        """
        if not article or self.images:
            return

        for img in article.find_all("img"):
            img.replace_with("[Image]")

    def _process_links(
        self, article: Optional[Tag], current_page_url: Optional[str] = None
    ) -> None:
        """
        Process all links using the LinkProcessor to convert to markdown file URLs.

        Args:
            article: BeautifulSoup article element (can be None)
            current_page_url: Current page URL to provide context for relative links
        """
        if not article or not self.link_processor:
            return

        for link in article.find_all("a", href=True):
            href = str(link["href"])  # Convert _AttributeValue to string
            link_class = link.get("class")
            link_class_str = " ".join(link_class) if link_class else None

            processed_href = self.link_processor.process_link(
                href, current_page_url, link_class_str
            )

            if processed_href:
                link["href"] = processed_href

    def process_urls(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process multiple fetch results to extract article content.

        Args:
            results: List of fetch results from PlaywrightFetcher

        Returns:
            List of results with article content extracted
        """
        processed_results = []

        for result in results:
            processed_result = result.copy()

            if result.get("html") and not result.get("error"):
                article_html = self.extract_article(result["html"], result.get("url"))
                if article_html:
                    processed_result["article"] = article_html
                    processed_result["has_article"] = True
                else:
                    processed_result["article"] = None
                    processed_result["has_article"] = False
                    processed_result["error"] = "No article element found"
            else:
                processed_result["article"] = None
                processed_result["has_article"] = False

            processed_results.append(processed_result)

        return processed_results
