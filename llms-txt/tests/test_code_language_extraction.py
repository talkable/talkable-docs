"""
Tests for code language extraction functionality in MarkdownConverter.
"""

from talkable_llm_txt import MarkdownConverter


class TestCodeLanguageExtraction:
    """Test code language extraction functionality."""

    def test_extract_liquid_language(self):
        """Test extraction of liquid language from highlight-liquid class."""
        converter = MarkdownConverter()
        html = """
        <div class="highlight-liquid notranslate">
            <div class="highlight">
                <pre>{{ site_setup.url }}</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "```liquid" in result
        assert "site_setup.url" in result

    def test_extract_ruby_language(self):
        """Test extraction of ruby language from highlight-ruby class."""
        converter = MarkdownConverter()
        html = """
        <div class="highlight-ruby notranslate">
            <div class="highlight">
                <pre>def ruby_method; end</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "```ruby" in result
        assert "ruby_method" in result

    def test_extract_python_language(self):
        """Test extraction of python language from highlight-python class."""
        converter = MarkdownConverter()
        html = """
        <div class="highlight-python notranslate">
            <div class="highlight">
                <pre>def python_function(): pass</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "```python" in result
        assert "python_function" in result

    def test_extract_javascript_language(self):
        """Test extraction of javascript language from highlight-javascript class."""
        converter = MarkdownConverter()
        html = """
        <div class="highlight-javascript notranslate">
            <div class="highlight">
                <pre>function jsFunction() { return true; }</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "```javascript" in result
        assert "jsFunction" in result

    def test_extract_css_language(self):
        """Test extraction of css language from highlight-css class."""
        converter = MarkdownConverter()
        html = """
        <div class="highlight-css notranslate">
            <div class="highlight">
                <pre>.class { color: red; }</pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "```css" in result
        assert "color: red" in result

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

    def test_code_block_with_empty_content(self):
        """Test code block with empty content."""
        converter = MarkdownConverter()
        html = """
        <div class="highlight-python notranslate">
            <div class="highlight">
                <pre></pre>
            </div>
        </div>
        """
        result = converter.convert_article(html)

        assert "```python" in result
        assert "```python\n\n```" in result

    def test_code_block_without_pre_element(self):
        """Test code block div without nested pre element."""
        converter = MarkdownConverter()
        html = '<div class="highlight-python notranslate">direct code content</div>'
        result = converter.convert_article(html)

        # Should extract language and use text content
        assert "```python" in result
        assert "direct code content" in result

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

    def test_extract_language_method_directly(self):
        """Test the _code_block_converter method directly."""
        converter = MarkdownConverter()

        # Create a mock tag with highlight class
        from bs4 import BeautifulSoup

        html = '<div class="highlight-python notranslate"><pre>test code</pre></div>'
        soup = BeautifulSoup(html, "html.parser")
        tag = soup.find("div")

        result = converter._code_block_converter(tag=tag, text="test code")

        assert "```python" in result
        assert "test code" in result

    def test_language_extraction_edge_cases(self):
        """Test edge cases in language extraction."""
        converter = MarkdownConverter()

        # Test with class that contains 'highlight' but not as prefix
        html = '<div class="some-highlight-style notranslate"><pre>code</pre></div>'
        result = converter.convert_article(html)

        # Should not extract language since it doesn't start with 'highlight-'
        assert "```" not in result or "some-highlight-style" not in result

    def test_div_converter_integration(self):
        """Test that the unified div converter handles both cases."""
        converter = MarkdownConverter()

        # Test that div converter is properly set up
        assert "div" in converter.custom_converters
        assert converter.custom_converters["div"] == converter._div_converter
