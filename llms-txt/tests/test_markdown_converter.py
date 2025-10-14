"""
Test suite for MarkdownConverter class

This module tests the conversion of HTML strings to markdown
format using the html-to-markdown library.
"""

from talkable_llm_txt import MarkdownConverter


class TestMarkdownConverter:
    """Test cases for MarkdownConverter class - Happy Flow Only"""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.converter = MarkdownConverter()

    def test_init(self):
        """Test MarkdownConverter initialization."""
        converter = MarkdownConverter()
        assert converter is not None

    def test_convert_article_basic_html(self):
        """Test converting a simple article with basic HTML elements."""
        html = """
        <article>
            <h1>Test Article</h1>
            <p>This is a <strong>test</strong> paragraph.</p>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "Test Article" in markdown
        assert "**test**" in markdown
        assert "This is a" in markdown

    def test_convert_article_with_links(self):
        """Test converting article with links."""
        html = """
        <article>
            <h1>Article with Links</h1>
            <p>Visit <a href="https://example.com">Example</a> for more info.</p>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "[Example](https://example.com)" in markdown
        assert "Article with Links" in markdown

    def test_convert_article_with_code_blocks(self):
        """Test converting article with code blocks."""
        html = """
        <article>
            <h1>Code Example</h1>
            <div class="highlight-python notranslate">
                <div class="highlight">
                    <pre>def hello():
    print("Hello, World!")</pre>
                </div>
            </div>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "```python" in markdown
        assert "def hello():" in markdown
        assert 'print("Hello, World!")' in markdown

    def test_convert_article_with_admonitions(self):
        """Test converting article with admonitions."""
        html = """
        <article>
            <div class="admonition note">
                <p class="admonition-title">Note</p>
                <p>This is an important note.</p>
            </div>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "> **Note:**" in markdown
        assert "This is an important note." in markdown

    def test_convert_article_with_lists(self):
        """Test converting article with lists."""
        html = """
        <article>
            <h1>Lists</h1>
            <ul>
                <li>First item</li>
                <li>Second item</li>
            </ul>
            <ol>
                <li>First ordered</li>
                <li>Second ordered</li>
            </ol>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "* First item" in markdown
        assert "* Second item" in markdown
        assert "1. First ordered" in markdown
        assert "2. Second ordered" in markdown

    def test_convert_article_complex_structure(self):
        """Test converting article with complex mixed content."""
        html = """
        <article>
            <h1>Complex Article</h1>
            <p>Introduction with <strong>bold</strong> and <em>italic</em> text.</p>
            
            <div class="admonition warning">
                <p class="admonition-title">Warning</p>
                <p>Pay attention to this code:</p>
            </div>
            
            <div class="highlight-javascript notranslate">
                <div class="highlight">
                    <pre>console.log("Hello");</pre>
                </div>
            </div>
            
            <p>Visit <a href="https://example.com">Example</a> for more.</p>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "Complex Article" in markdown
        assert "**bold**" in markdown
        assert "*italic*" in markdown
        assert "> **Warning:**" in markdown
        assert "```javascript" in markdown
        assert 'console.log("Hello");' in markdown
        assert "[Example](https://example.com)" in markdown
