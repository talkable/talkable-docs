"""
HTML to Markdown Converter Stage

This module provides the MarkdownConverter class for converting BeautifulSoup
article objects to clean markdown format using the html-to-markdown library.
"""

import logging
from typing import List, Literal

from bs4.element import Tag
from html_to_markdown import convert_to_markdown

# Module-level logger following official Python documentation best practices
logger = logging.getLogger(__name__)


class MarkdownConverter:
    """
    Converts HTML article strings to markdown format.

    This class handles the conversion of preprocessed HTML articles
    (as strings) to clean, structured markdown using the html-to-markdown
    library with configurable heading styles.
    """

    HIGHLIGHT_PREFIX = "highlight-"
    ADMONITION_CLASS = "admonition"

    def __init__(
        self,
        heading_style: Literal["atx", "atx_closed", "underlined"] = "atx",
        custom_converters=None,
    ):
        """
        Initialize the converter with configurable settings.

        Args:
            heading_style: Style for headings ('atx', 'atx_closed', 'underlined')
                          Default is 'atx' for # style headings
            custom_converters: Dictionary of custom converter functions for specific HTML tags
        """
        self.heading_style: Literal["atx", "atx_closed", "underlined"] = heading_style
        self.custom_converters = custom_converters.copy() if custom_converters else {}
        self._setup_admonition_converter()

    def _setup_admonition_converter(self):
        """Setup converters for admonitions and code blocks"""
        self.custom_converters["div"] = self._div_converter

    def _get_classes(self, tag: Tag) -> List[str]:
        """Extract and normalize class list from tag"""
        classes = tag.get("class") or []
        return list(classes) if classes else []

    def _has_class_prefix(self, classes: List[str], prefix: str) -> bool:
        """Check if any class starts with given prefix"""
        return any(class_name.startswith(prefix) for class_name in classes)

    def _extract_class_prefix_value(self, classes: List[str], prefix: str) -> str:
        """Extract value after prefix from first matching class"""
        for class_name in classes:
            if class_name.startswith(prefix):
                return class_name.replace(prefix, "")
        return ""

    def _div_converter(self, *, tag: Tag, text: str, **kwargs) -> str:
        """Handle div elements - both admonitions and code blocks"""
        classes = self._get_classes(tag)

        # Check if this is an admonition
        admonition_type = self._extract_admonition_type(classes)
        if admonition_type:
            return self._admonition_converter(tag=tag, text=text, **kwargs)

        # Check if this is a syntax-highlighted code block
        if self._has_class_prefix(classes, self.HIGHLIGHT_PREFIX):
            return self._code_block_converter(tag=tag, text=text, **kwargs)

        # Fallback to default behavior
        return text

    def _admonition_converter(self, *, tag: Tag, text: str, **kwargs) -> str:
        """Convert admonition divs to classic blockquote style"""
        classes = self._get_classes(tag)
        admonition_type = self._extract_admonition_type(classes)

        if admonition_type:
            # Remove the title element to avoid duplication
            tag_copy = tag.__copy__()
            title_element = tag_copy.find("p", class_="admonition-title")
            if title_element:
                title_element.decompose()

            # Convert the cleaned HTML to markdown
            admonition_html = str(tag_copy)
            inner_markdown = convert_to_markdown(
                admonition_html, heading_style=self.heading_style
            )

            # Add title and prefix all lines
            return self._format_as_blockquote(inner_markdown, admonition_type)

        return text  # Fallback to default conversion

    def _format_as_blockquote(self, content: str, admonition_type: str) -> str:
        """Format content as blockquote with title as separate line"""
        title = admonition_type.title()

        # Start with title and empty line
        result = f"> **{title}:**\n>\n"

        # Add all content lines with prefix
        lines = content.strip().split("\n")
        for line in lines:
            result += f"> {line}\n"

        return result.rstrip()  # Remove trailing newline

    def _extract_admonition_type(self, classes) -> str | None:
        """Extract admonition type from class list"""
        # Convert to list of strings if needed
        class_list = list(classes) if classes else []

        # Look for admonition class and get the type
        if self.ADMONITION_CLASS in class_list:
            for cls in class_list:
                if cls != self.ADMONITION_CLASS:
                    return cls
        return None

    def _code_block_converter(self, *, tag: Tag, text: str, **kwargs) -> str:
        """Handle syntax-highlighted code blocks with language extraction"""
        classes = self._get_classes(tag)
        language = self._extract_class_prefix_value(classes, self.HIGHLIGHT_PREFIX)

        # Extract code content from nested pre element
        pre_tag = tag.find("pre")
        if pre_tag:
            code_content = pre_tag.get_text().strip()
        else:
            # Fallback to tag text content
            code_content = tag.get_text().strip()

        return f"```{language}\n{code_content}\n```"

    def convert_article(self, article_html: str) -> str:
        """
        Convert a single HTML article string to markdown.

        Args:
            article_html: HTML string containing the article content

        Returns:
            Markdown string representation of the article
        """
        return convert_to_markdown(
            article_html,
            heading_style=self.heading_style,
            custom_converters=self.custom_converters,
            strip=["abbr"],
            escape_asterisks=False,
            escape_underscores=False,
            escape_misc=False,
        )

    def convert_articles(self, articles_html: List[str]) -> List[str]:
        """
        Convert multiple HTML article strings to markdown.

        Args:
            articles_html: List of HTML strings containing articles

        Returns:
            List of markdown strings
        """
        return [self.convert_article(article) for article in articles_html]
