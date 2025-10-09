"""
Tests for admonition conversion functionality in MarkdownConverter.
"""

import pytest
from talkable_llm_txt import MarkdownConverter


class TestAdmonitionConversion:
    """Test admonition conversion functionality."""

    @pytest.mark.parametrize("admonition_type", ["note", "warning", "tip"])
    def test_convert_admonition_basic(self, admonition_type):
        """Test basic conversion of different admonition types."""
        converter = MarkdownConverter()
        html = f'<div class="admonition {admonition_type}"><p class="admonition-title">{admonition_type.capitalize()}</p><p>This is a {admonition_type}.</p></div>'
        result = converter.convert_article(html)

        assert f"> **{admonition_type.capitalize()}:**" in result
        assert f"This is a {admonition_type}." in result

    def test_convert_admonition_complex_content(self):
        """Test conversion of admonition with complex content (multiple paragraphs, lists, formatting)."""
        converter = MarkdownConverter()
        html = """
        <div class="admonition note">
            <p class="admonition-title">Note</p>
            <p>First paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
            <p>Second paragraph with <a href="https://example.com">a link</a>.</p>
            <ul>
                <li>List item 1</li>
                <li>List item 2</li>
            </ul>
        </div>
        """
        result = converter.convert_article(html)

        assert "> **Note:**" in result
        assert "**bold**" in result
        assert "*italic*" in result
        assert "[a link](https://example.com)" in result
        assert "* List item 1" in result
        assert "* List item 2" in result

    def test_convert_non_admonition_div(self):
        """Test that non-admonition divs are not affected."""
        converter = MarkdownConverter()
        html = '<div class="regular"><p>This is a regular div.</p></div>'
        result = converter.convert_article(html)

        assert "This is a regular div." in result.strip()
        assert ">" not in result

    def test_convert_admonition_multiple_classes(self):
        """Test conversion of admonition with multiple classes."""
        converter = MarkdownConverter()
        html = """
        <div class="admonition note extra-class another-class">
            <p class="admonition-title">Note</p>
            <p>Content with multiple classes.</p>
        </div>
        """
        result = converter.convert_article(html)

        assert "> **Note:**" in result
        assert "Content with multiple classes." in result
