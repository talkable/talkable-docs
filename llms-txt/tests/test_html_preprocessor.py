import pytest
from talkable_llm_txt import HTMLPreprocessor


class TestHTMLPreprocessor:
    def setup_method(self):
        """Setup test instance before each test method."""
        self.processor = HTMLPreprocessor()

    def test_extract_article_with_valid_article(self):
        """Test extracting article from HTML with valid article element."""
        html = """
        <html>
            <head><title>Test Page</title></head>
            <body>
                <header>Navigation</header>
                <main>
                    <article>
                        <h1>Article Title</h1>
                        <p>Article content goes here.</p>
                    </article>
                </main>
                <footer>Footer</footer>
            </body>
        </html>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<article>" in result
        assert "Article Title" in result
        assert "Article content goes here." in result
        assert "Navigation" not in result
        assert "Footer" not in result

    def test_extract_article_no_article_element(self):
        """Test extracting article from HTML without article element."""
        html = """
        <html>
            <head><title>Test Page</title></head>
            <body>
                <div class="content">
                    <h1>Page Title</h1>
                    <p>Page content goes here.</p>
                </div>
            </body>
        </html>
        """
        result = self.processor.extract_article(html)
        assert result is None

    @pytest.mark.parametrize(
        "nested_html,expected_content",
        [
            (
                """<article><section><h1>Section Title</h1><div class="content"><p>Deep nested content.</p><ul><li>Item 1</li></ul></div></section></article>""",
                ["<section>", "Section Title", "Deep nested content", "Item 1"],
            ),
            (
                """<article><h1>First Article</h1><p>First content.</p></article><article><h1>Second</h1></article>""",
                ["First Article", "First content"],
            ),
        ],
    )
    def test_extract_article_nested_structures(self, nested_html, expected_content):
        """Test extracting articles with different nested structures."""
        result = self.processor.extract_article(
            f"<html><body>{nested_html}</body></html>"
        )

        assert result is not None
        for content in expected_content:
            assert content in result

    def test_extract_article_with_attributes(self):
        """Test extracting article with attributes."""
        html = """
        <html>
            <body>
                <article id="main-article" class="content-article" data-type="blog">
                    <h1>Article with Attributes</h1>
                    <p>Content.</p>
                </article>
            </body>
        </html>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert 'id="main-article"' in result
        assert 'class="content-article"' in result
        assert 'data-type="blog"' in result

    def test_process_urls_mixed_results(self):
        """Test processing URLs with mixed success and failure results."""
        results = [
            {
                "url": "http://example.com/success",
                "html": "<html><body><article><h1>Success</h1></article></body></html>",
                "status": 200,
            },
            {
                "url": "http://example.com/no_article",
                "html": "<html><body><div><h1>No article</h1></div></body></html>",
                "status": 200,
            },
            {
                "url": "http://example.com/error",
                "html": None,
                "status": None,
                "error": "Fetch failed",
            },
        ]

        processed = self.processor.process_urls(results)

        assert len(processed) == 3
        assert processed[0]["has_article"] is True
        assert processed[1]["has_article"] is False
        assert processed[2]["has_article"] is False
        assert processed[0].get("error") is None
        assert processed[1]["error"] == "No article element found"
        assert processed[2]["error"] == "Fetch failed"

    def test_extract_article_with_headerlinks(self):
        """Test extracting article with headerlinks gets preprocessed."""
        html = """<html><body><article><h1>Article Title<a class="headerlink" href="#title">#</a></h1><p>Content</p></article></body></html>"""
        result = self.processor.extract_article(html)

        assert result is not None
        assert "Article Title" in result
        assert "Content" in result
        assert "headerlink" not in result

    def test_original_results_not_modified(self):
        """Test that original results are not modified by processing."""
        import copy

        original_results = [
            {
                "url": "http://example.com/page1",
                "html": "<html><body><article><h1>Original</h1></article></body></html>",
                "status": 200,
            }
        ]
        expected_original = copy.deepcopy(original_results)
        processed = self.processor.process_urls(original_results)

        assert original_results == expected_original
        assert len(processed[0]) > len(original_results[0])

    def test_remove_images(self):
        """Test that images are replaced with placeholder when images=False."""
        processor = HTMLPreprocessor(images=False)
        html = """<html><body><article><h1>Title</h1><img src="test.jpg" alt="A test image"><img src="test2.jpg"><p>Content</p></article></body></html>"""
        result = processor.extract_article(html)

        assert result is not None
        assert "[Image]" in result
        assert "<img" not in result
        assert result.count("[Image]") == 2

    def test_keep_images(self):
        """Test that images are preserved when images=True."""
        processor = HTMLPreprocessor(images=True)
        html = """<html><body><article><h1>Title</h1><img src="test.jpg" alt="A test image"><p>Content</p></article></body></html>"""
        result = processor.extract_article(html)

        assert result is not None
        assert "<img" in result
        assert 'src="test.jpg"' in result
        assert 'alt="A test image"' in result
        assert "[Image]" not in result
