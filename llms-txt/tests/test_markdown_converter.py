"""
Test suite for MarkdownConverter class.

This module tests the conversion of HTML strings to markdown
format using the html-to-markdown library.
"""

from markdown_converter import MarkdownConverter


class TestMarkdownConverter:
    """Test cases for MarkdownConverter class."""

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

    def test_convert_article_with_lists(self):
        """Test converting article with lists."""
        html = """
        <article>
            <h1>Article with Lists</h1>
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

    def test_convert_article_with_code(self):
        """Test converting article with code blocks."""
        html = """
        <article>
            <h1>Article with Code</h1>
            <p>Inline code: <code>print('hello')</code></p>
            <pre><code>def hello():
    print('world')</code></pre>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "`print('hello')`" in markdown
        assert "def hello():" in markdown
        assert "print('world')" in markdown

    def test_convert_article_with_headings(self):
        """Test converting article with multiple heading levels."""
        html = """
        <article>
            <h1>Main Title</h1>
            <h2>Section 1</h2>
            <h3>Subsection 1.1</h3>
            <h4>Sub-subsection</h4>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "Main Title" in markdown
        assert "Section 1" in markdown
        assert "Subsection 1.1" in markdown  # No escaping now
        assert "Sub-subsection" in markdown  # No escaping now

    def test_convert_article_with_images(self):
        """Test converting article with images."""
        html = """
        <article>
            <h1>Article with Image</h1>
            <p>Here's an image:</p>
            <img src="image.jpg" alt="Test image">
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "![Test image](image.jpg)" in markdown

    def test_convert_article_with_tables(self):
        """Test converting article with tables."""
        html = """
        <article>
            <h1>Article with Table</h1>
            <table>
                <tr>
                    <th>Header 1</th>
                    <th>Header 2</th>
                </tr>
                <tr>
                    <td>Cell 1</td>
                    <td>Cell 2</td>
                </tr>
            </table>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "Header 1" in markdown
        assert "Header 2" in markdown
        assert "Cell 1" in markdown
        assert "Cell 2" in markdown

    def test_convert_article_empty(self):
        """Test converting an empty article."""
        html = "<article></article>"

        markdown = self.converter.convert_article(html)

        assert markdown == ""

    def test_convert_article_with_nested_elements(self):
        """Test converting article with deeply nested elements."""
        html = """
        <article>
            <h1>Nested Elements</h1>
            <div>
                <p>This is <em>nested <strong>content</strong></em>.</p>
            </div>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "*nested **content***" in markdown
        assert "This is" in markdown

    def test_convert_articles_multiple(self):
        """Test converting multiple articles."""
        html1 = "<article><h1>Article 1</h1><p>Content 1</p></article>"
        html2 = "<article><h1>Article 2</h1><p>Content 2</p></article>"

        markdowns = self.converter.convert_articles([html1, html2])

        assert len(markdowns) == 2
        assert "Article 1" in markdowns[0]
        assert "Content 1" in markdowns[0]
        assert "Article 2" in markdowns[1]
        assert "Content 2" in markdowns[1]

    def test_convert_articles_empty_list(self):
        """Test converting empty list of articles."""
        markdowns = self.converter.convert_articles([])

        assert markdowns == []

    def test_convert_article_with_blockquotes(self):
        """Test converting article with blockquotes."""
        html = """
        <article>
            <h1>Article with Quote</h1>
            <blockquote>
                <p>This is a quote.</p>
            </blockquote>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "> This is a quote." in markdown

    def test_convert_article_with_emphasis(self):
        """Test converting article with various emphasis elements."""
        html = """
        <article>
            <h1>Emphasis Test</h1>
            <p><em>Italic</em> and <strong>bold</strong> text.</p>
            <p><s>Strikethrough</s> and <u>underline</u>.</p>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "*Italic*" in markdown
        assert "**bold**" in markdown
        assert "Strikethrough" in markdown

    def test_convert_article_real_world_example(self):
        """Test converting a realistic article structure."""
        html = """
        <article>
            <header>
                <h1>Getting Started with Python</h1>
                <p>Published on <time>2024-01-01</time></p>
            </header>
            
            <section>
                <h2>Introduction</h2>
                <p>Python is a <strong>versatile</strong> programming language.</p>
                
                <h3>Features</h3>
                <ul>
                    <li>Easy to learn</li>
                    <li>Powerful libraries</li>
                    <li>Great community</li>
                </ul>
                
                <h3>Example Code</h3>
                <pre><code>def hello_world():
    print("Hello, World!")
    return True</code></pre>
                
                <p>Visit <a href="https://python.org">Python.org</a> for more.</p>
            </section>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "Getting Started with Python" in markdown
        assert "**versatile**" in markdown
        assert "* Easy to learn" in markdown
        assert "def hello_world():" in markdown
        assert "[Python.org](https://python.org)" in markdown

    def test_convert_article_preserves_whitespace(self):
        """Test that conversion handles whitespace appropriately."""
        html = """
        <article>
            <h1>Whitespace Test</h1>
            <p>Line 1
            
            Line 2 with extra spaces</p>
        </article>
        """

        markdown = self.converter.convert_article(html)

        assert "Whitespace Test" in markdown
        assert "Line 1" in markdown
        assert "Line 2 with extra spaces" in markdown

    def test_heading_style_configuration(self):
        """Test that heading style configuration works correctly."""
        from markdown_converter import MarkdownConverter

        # Test ATX style (default)
        converter_atx = MarkdownConverter(heading_style="atx")
        html = "<article><h1>Title</h1><h2>Section</h2></article>"
        markdown_atx = converter_atx.convert_article(html)

        assert "# Title" in markdown_atx
        assert "## Section" in markdown_atx
        assert "Title\n====" not in markdown_atx
        assert "Section\n----" not in markdown_atx

        # Test underlined style
        converter_underlined = MarkdownConverter(heading_style="underlined")
        markdown_underlined = converter_underlined.convert_article(html)

        assert "Title\n====" in markdown_underlined
        assert "Section\n----" in markdown_underlined
        assert "# Title" not in markdown_underlined
        assert "## Section" not in markdown_underlined
