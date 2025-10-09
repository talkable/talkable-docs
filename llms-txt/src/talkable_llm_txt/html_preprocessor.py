import logging
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup
from bs4.element import Tag

# Module-level logger following official Python documentation best practices
logger = logging.getLogger(__name__)


class HTMLPreprocessor:
    """
    HTML preprocessing for extracting article content from web pages.

    This class handles the extraction of article elements from HTML content
    fetched by Playwright, providing clean content for markdown conversion.
    """

    def extract_article(self, html: Optional[str]) -> Optional[str]:
        """
        Extract article element from Playwright-rendered HTML.

        Args:
            html: HTML content from PlaywrightFetcher (can be None)

        Returns:
            Article HTML as string, or None if no article element found
        """
        if html is None or not html.strip():
            return None

        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")

        if article:
            # Apply preprocessing to the article
            self._preprocess_article(article)
            return str(article)
        return None

    def _preprocess_article(self, article):
        """
        Apply preprocessing steps to article content.

        Args:
            article: BeautifulSoup article element to preprocess
        """
        self._remove_header_links(article)
        self._remove_copy_buttons(article)

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
                article_html = self.extract_article(result["html"])
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
