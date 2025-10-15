"""
Tests for HTML preprocessing functionality
"""

from bs4 import BeautifulSoup

from talkable_llm_txt import HTMLPreprocessor


class TestHTMLPreprocessor:
    """Test cases for HTMLPreprocessor class - Happy Flow Only"""

    def setup_method(self):
        """Set up test fixtures."""
        self.preprocessor = HTMLPreprocessor()

    def test_extract_article_basic(self):
        """Test basic article extraction."""
        html = """
        <html>
            <head><title>Test</title></head>
            <body>
                <article>
                    <h1>Test Article</h1>
                    <p>This is test content.</p>
                </article>
            </body>
        </html>
        """
        result = self.preprocessor.extract_article(html)

        assert result is not None
        assert "<h1>Test Article</h1>" in result
        assert "<p>This is test content.</p>" in result

    def test_extract_article_removes_copy_buttons(self):
        """Test that extract_article removes copy buttons."""
        html = """
        <article>
            <p>Some content</p>
            <button class="copybtn o-tooltip--left" data-clipboard-target="#code0">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <p>More content</p>
        </article>
        """
        result = self.preprocessor.extract_article(html)

        assert result is not None
        result_soup = BeautifulSoup(result, "html.parser")

        copy_buttons = result_soup.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0
        assert result_soup.find("p") is not None

    def test_extract_article_removes_header_links(self):
        """Test that extract_article removes header links."""
        html = """
        <article>
            <h1>Title <a class="headerlink" href="#title">#</a></h1>
            <p>Content here.</p>
        </article>
        """
        result = self.preprocessor.extract_article(html)

        assert result is not None
        assert "<h1>Title" in result
        assert "headerlink" not in result
        assert "Content here." in result

    def test_extract_article_with_base_url_processes_links(self):
        """Test that extract_article processes internal links with reference internal class."""
        base_url = "http://localhost:8080"
        preprocessor = HTMLPreprocessor(base_url=base_url)

        html = """
        <article>
            <h1>Test Article</h1>
            <p>Visit <a class="reference internal" href="docs/guide/">guide</a> for details.</p>
        </article>
        """
        result = preprocessor.extract_article(html)

        assert result is not None
        result_soup = BeautifulSoup(result, "html.parser")

        link = result_soup.find("a", href=True)
        assert link is not None
        assert link["href"] == "http://localhost:8080/docs/guide.md"

    def test_extract_article_preserves_external_links(self):
        """Test that extract_article preserves external links."""
        base_url = "http://localhost:8080"
        preprocessor = HTMLPreprocessor(base_url=base_url)

        html = """
        <article>
            <p>External: <a href="https://example.com">Example</a></p>
            <p>Email: <a href="mailto:test@example.com">Email</a></p>
        </article>
        """
        result = preprocessor.extract_article(html)

        assert result is not None
        result_soup = BeautifulSoup(result, "html.parser")

        links = result_soup.find_all("a", href=True)
        hrefs = [link["href"] for link in links]
        assert "https://example.com" in hrefs
        assert "mailto:test@example.com" in hrefs

    def test_extract_article_complex_structure(self):
        """Test article extraction with complex nested structure."""
        html = """
        <article>
            <section>
                <h1>Main Title <a class="headerlink" href="#main">#</a></h1>
                <div>
                    <h2>Sub Title</h2>
                    <p>Content with <a href="docs/guide/">internal link</a>.</p>
                    <div class="highlight">
                        <pre>code here</pre>
                        <button class="copybtn">Copy</button>
                    </div>
                </div>
            </section>
        </article>
        """
        result = self.preprocessor.extract_article(html)

        assert result is not None
        assert "<h1>Main Title" in result
        assert "<h2>Sub Title</h2>" in result
        assert "headerlink" not in result
        assert "copybtn" not in result
        assert "<pre>code here</pre>" in result


def test_extract_article_with_real_fixture(sample_html_response):
    """Test article extraction using real HTML fixture."""
    preprocessor = HTMLPreprocessor()
    result = preprocessor.extract_article(sample_html_response)

    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0

    # Verify that content from the real fixture is extracted
    assert "Magento" in result
    assert "Talkable offers free extension" in result

    # Verify that unwanted elements are removed
    assert "copybtn" not in result
    assert "headerlink" not in result
