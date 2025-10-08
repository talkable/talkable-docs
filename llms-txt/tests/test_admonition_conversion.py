"""
Tests for admonition conversion functionality in MarkdownConverter.
"""

import pytest
from markdown_converter import MarkdownConverter


class TestAdmonitionConversion:
    """Test admonition conversion functionality."""

    def test_convert_admonition_note(self):
        """Test conversion of note admonition."""
        converter = MarkdownConverter()
        html = '<div class="admonition note"><p class="admonition-title">Note</p><p>This is a note.</p></div>'
        result = converter.convert_article(html)
        
        expected = "> **Note:**\n>\n> This is a note."
        assert result == expected

    def test_convert_admonition_warning(self):
        """Test conversion of warning admonition."""
        converter = MarkdownConverter()
        html = '<div class="admonition warning"><p class="admonition-title">Warning</p><p>This is a warning.</p></div>'
        result = converter.convert_article(html)
        
        expected = "> **Warning:**\n>\n> This is a warning."
        assert result == expected

    def test_convert_admonition_tip(self):
        """Test conversion of tip admonition."""
        converter = MarkdownConverter()
        html = '<div class="admonition tip"><p class="admonition-title">Tip</p><p>This is a tip.</p></div>'
        result = converter.convert_article(html)
        
        expected = "> **Tip:**\n>\n> This is a tip."
        assert result == expected

    def test_convert_admonition_multiple_paragraphs(self):
        """Test conversion of admonition with multiple paragraphs."""
        converter = MarkdownConverter()
        html = '''
        <div class="admonition note">
            <p class="admonition-title">Note</p>
            <p>First paragraph.</p>
            <p>Second paragraph.</p>
        </div>
        '''
        result = converter.convert_article(html)
        
        lines = result.split('\n')
        assert lines[0] == "> **Note:**"
        assert lines[1] == ">"
        assert "First paragraph." in result
        assert "Second paragraph." in result

    def test_convert_admonition_with_list(self):
        """Test conversion of admonition with list content."""
        converter = MarkdownConverter()
        html = '''
        <div class="admonition warning">
            <p class="admonition-title">Warning</p>
            <ul>
                <li>First item</li>
                <li>Second item</li>
            </ul>
        </div>
        '''
        result = converter.convert_article(html)
        
        assert "> **Warning:**" in result
        assert "* First item" in result
        assert "* Second item" in result

    def test_convert_admonition_with_formatted_text(self):
        """Test conversion of admonition with formatted text."""
        converter = MarkdownConverter()
        html = '''
        <div class="admonition important">
            <p class="admonition-title">Important</p>
            <p>This has <strong>bold</strong> and <em>italic</em> text.</p>
        </div>
        '''
        result = converter.convert_article(html)
        
        assert "> **Important:**" in result
        assert "**bold**" in result
        assert "*italic*" in result

    def test_convert_admonition_with_link(self):
        """Test conversion of admonition with links."""
        converter = MarkdownConverter()
        html = '''
        <div class="admonition note">
            <p class="admonition-title">Note</p>
            <p>Check <a href="https://example.com">this link</a> for more info.</p>
        </div>
        '''
        result = converter.convert_article(html)
        
        assert "> **Note:**" in result
        assert "[this link](https://example.com)" in result

    def test_convert_admonition_without_title_class(self):
        """Test conversion of admonition without explicit title class."""
        converter = MarkdownConverter()
        html = '''
        <div class="admonition note">
            <p>Content without title class.</p>
        </div>
        '''
        result = converter.convert_article(html)
        
        assert "> **Note:**" in result
        assert "Content without title class." in result

    def test_convert_non_admonition_div(self):
        """Test that non-admonition divs are not affected."""
        converter = MarkdownConverter()
        html = '<div class="regular"><p>This is a regular div.</p></div>'
        result = converter.convert_article(html)
        
        expected = "This is a regular div."
        assert result.strip() == expected

    def test_convert_admonition_multiple_classes(self):
        """Test conversion of admonition with multiple classes."""
        converter = MarkdownConverter()
        html = '''
        <div class="admonition note extra-class">
            <p class="admonition-title">Note</p>
            <p>Content with multiple classes.</p>
        </div>
        '''
        result = converter.convert_article(html)
        
        assert "> **Note:**" in result
        assert "Content with multiple classes." in result

    def test_extract_admonition_type_note(self):
        """Test extraction of 'note' type from classes."""
        converter = MarkdownConverter()
        classes = ['admonition', 'note']
        result = converter._extract_admonition_type(classes)
        assert result == 'note'

    def test_extract_admonition_type_warning(self):
        """Test extraction of 'warning' type from classes."""
        converter = MarkdownConverter()
        classes = ['admonition', 'warning']
        result = converter._extract_admonition_type(classes)
        assert result == 'warning'

    def test_extract_admonition_type_no_admonition(self):
        """Test extraction when 'admonition' class is not present."""
        converter = MarkdownConverter()
        classes = ['regular', 'div']
        result = converter._extract_admonition_type(classes)
        assert result is None

    def test_extract_admonition_type_only_admonition(self):
        """Test extraction when only 'admonition' class is present."""
        converter = MarkdownConverter()
        classes = ['admonition']
        result = converter._extract_admonition_type(classes)
        assert result is None

    def test_extract_admonition_type_empty_list(self):
        """Test extraction with empty class list."""
        converter = MarkdownConverter()
        classes = []
        result = converter._extract_admonition_type(classes)
        assert result is None

    def test_format_as_blockquote_single_line(self):
        """Test blockquote formatting with single line content."""
        converter = MarkdownConverter()
        content = "Single line content."
        result = converter._format_as_blockquote(content, "note")
        
        expected = "> **Note:**\n>\n> Single line content."
        assert result == expected

    def test_format_as_blockquote_multiple_lines(self):
        """Test blockquote formatting with multiple lines."""
        converter = MarkdownConverter()
        content = "First line.\nSecond line."
        result = converter._format_as_blockquote(content, "warning")
        
        lines = result.split('\n')
        assert lines[0] == "> **Warning:**"
        assert lines[1] == ">"
        assert lines[2] == "> First line."
        assert lines[3] == "> Second line."

    def test_custom_converters_initialization(self):
        """Test that custom converters are properly initialized."""
        converter = MarkdownConverter()
        assert 'div' in converter.custom_converters
        assert converter.custom_converters['div'] == converter._div_converter

    def test_custom_converters_preserved(self):
        """Test that existing custom converters are preserved."""
        def dummy_converter(*, tag, text, **kwargs):
            return "DUMMY"
        
        converter = MarkdownConverter(custom_converters={'span': dummy_converter})
        assert 'span' in converter.custom_converters
        assert 'div' in converter.custom_converters  # Admonition converter should be added