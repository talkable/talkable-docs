"""
Tests for code language extraction functionality in MarkdownConverter.
"""

import pytest
from talkable_llm_txt import MarkdownConverter


class TestCodeLanguageExtraction:
    """Test code language extraction functionality."""

    @pytest.mark.parametrize(
        "language,content",
        [
            ("liquid", "{{ site_setup.url }}"),
            ("ruby", "def ruby_method; end"),
            ("python", "def python_function(): pass"),
            ("javascript", "function jsFunction() { return true; }"),
            ("css", ".class { color: red; }"),
        ],
    )
    def test_language_extraction(self, language, content):
        """Test extraction of different programming languages."""
        converter = MarkdownConverter()
        html = f"""
        <div class="highlight-{language} notranslate">
            <div class="highlight">
                <pre>{content}</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert f"```{language}" in result
        assert content in result

    def test_no_language_extraction_without_highlight_class(self):
        """Test that regular divs without highlight classes use default behavior."""
        converter = MarkdownConverter()
        html = '<div class="regular"><pre>regular code</pre></div>'
        result = converter.convert_article(html)

        # Should use default html-to-markdown behavior (fenced code blocks without language)
        assert "```\nregular code\n```" in result

    def test_multiple_code_blocks_different_languages(self):
        """Test multiple code blocks with different languages in same content."""
        converter = MarkdownConverter()
        html = """
        <div class="highlight-liquid notranslate">
            <div class="highlight">
                <pre>{{ liquid_var }}</pre>
            </div>
        </div>
        <div class="highlight-ruby notranslate">
            <div class="highlight">
                <pre>ruby_method</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "```liquid" in result
        assert "```ruby" in result
        assert "liquid_var" in result
        assert "ruby_method" in result

    def test_code_block_with_multiple_classes(self):
        """Test code block extraction with multiple CSS classes."""
        converter = MarkdownConverter()
        html = """
        <div class="highlight-python notranslate extra-class another-class">
            <div class="highlight">
                <pre>python code here</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "```python" in result
        assert "python code here" in result

    def test_code_block_preserves_content_formatting(self):
        """Test that code content formatting is preserved."""
        converter = MarkdownConverter()
        html = """
        <div class="highlight-ruby notranslate">
            <div class="highlight">
                <pre>def method
  puts "indented text"
  if condition
    nested_code
  end
end</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "```ruby" in result
        assert "def method" in result
        assert '  puts "indented text"' in result
        assert "    nested_code" in result

    def test_admonition_and_code_block_coexistence(self):
        """Test that admonitions and code blocks work together."""
        converter = MarkdownConverter()
        html = """
        <div class="admonition note">
            <p class="admonition-title">Note</p>
            <p>Here's some code:</p>
        </div>
        <div class="highlight-python notranslate">
            <div class="highlight">
                <pre>python_code()</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "> **Note:**" in result
        assert "```python" in result
        assert "python_code" in result

    def test_language_extraction_edge_cases(self):
        """Test edge cases in language extraction."""
        converter = MarkdownConverter()

        # Test with class that contains 'highlight' but not as prefix
        html = '<div class="some-highlight-style notranslate"><pre>code</pre></div>'
        result = converter.convert_article(html)

        # Should not extract language since it doesn't start with 'highlight-'
        assert "```" not in result or "some-highlight-style" not in result
