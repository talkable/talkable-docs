from html_preprocessor import HTMLPreprocessor


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
        assert "<h1>Article Title</h1>" in result
        assert "<p>Article content goes here.</p>" in result
        assert "<header>" not in result
        assert "<footer>" not in result

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

    def test_extract_article_empty_html(self):
        """Test extracting article from empty HTML."""
        result = self.processor.extract_article("")
        assert result is None

    def test_extract_article_whitespace_only(self):
        """Test extracting article from whitespace-only HTML."""
        result = self.processor.extract_article("   \n\t  ")
        assert result is None

    def test_extract_article_none_input(self):
        """Test extracting article from None input."""
        result = self.processor.extract_article(None)
        assert result is None

    def test_extract_article_multiple_articles(self):
        """Test extracting article from HTML with multiple article elements."""
        html = """
        <html>
            <body>
                <article>
                    <h1>First Article</h1>
                    <p>First content.</p>
                </article>
                <article>
                    <h1>Second Article</h1>
                    <p>Second content.</p>
                </article>
            </body>
        </html>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>First Article</h1>" in result
        assert (
            "<h1>Second Article</h1>" not in result
        )  # Should only return first article

    def test_extract_article_nested_elements(self):
        """Test extracting article with nested elements."""
        html = """
        <html>
            <body>
                <article>
                    <section>
                        <h1>Section Title</h1>
                        <div class="content">
                            <p>Deep nested content.</p>
                            <ul>
                                <li>Item 1</li>
                                <li>Item 2</li>
                            </ul>
                        </div>
                    </section>
                </article>
            </body>
        </html>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<section>" in result
        assert '<div class="content">' in result
        assert "<p>Deep nested content.</p>" in result
        assert "<ul>" in result
        assert "<li>Item 1</li>" in result

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

    def test_process_urls_successful_extraction(self):
        """Test processing multiple URLs with successful article extraction."""
        results = [
            {
                "url": "http://example.com/page1",
                "html": "<html><body><article><h1>Page 1</h1></article></body></html>",
                "status": 200,
            },
            {
                "url": "http://example.com/page2",
                "html": "<html><body><article><h1>Page 2</h1></article></body></html>",
                "status": 200,
            },
        ]

        processed = self.processor.process_urls(results)

        assert len(processed) == 2
        assert processed[0]["has_article"] is True
        assert processed[1]["has_article"] is True
        assert "<article>" in processed[0]["article"]
        assert "<article>" in processed[1]["article"]
        assert "error" not in processed[0]
        assert "error" not in processed[1]

    def test_process_urls_no_article_found(self):
        """Test processing URLs when no article element is found."""
        results = [
            {
                "url": "http://example.com/page1",
                "html": "<html><body><div><h1>No article here</h1></div></body></html>",
                "status": 200,
            }
        ]

        processed = self.processor.process_urls(results)

        assert len(processed) == 1
        assert processed[0]["has_article"] is False
        assert processed[0]["article"] is None
        assert processed[0]["error"] == "No article element found"

    def test_process_urls_with_fetch_errors(self):
        """Test processing URLs that already have fetch errors."""
        results = [
            {
                "url": "http://example.com/page1",
                "html": None,
                "status": None,
                "error": "Connection timeout",
            }
        ]

        processed = self.processor.process_urls(results)

        assert len(processed) == 1
        assert processed[0]["has_article"] is False
        assert processed[0]["article"] is None
        assert processed[0]["error"] == "Connection timeout"  # Original error preserved

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

    def test_process_urls_empty_list(self):
        """Test processing empty list of URLs."""
        processed = self.processor.process_urls([])
        assert processed == []

    def test_extract_article_with_headerlinks(self):
        """Test extracting article with headerlinks gets preprocessed."""
        html = """
        <html>
            <body>
                <article>
                    <h1>Article Title<a class="headerlink" href="#title">#</a></h1>
                    <p>Article content goes here.</p>
                </article>
            </body>
        </html>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<article>" in result
        assert "<h1>Article Title</h1>" in result
        assert "<p>Article content goes here.</p>" in result
        assert "headerlink" not in result
        assert '<a class="headerlink"' not in result

    def test_original_results_not_modified(self):
        """Test that original results are not modified by processing."""
        original_results = [
            {
                "url": "http://example.com/page1",
                "html": "<html><body><article><h1>Original</h1></article></body></html>",
                "status": 200,
            }
        ]

        # Make a copy to compare
        import copy

        expected_original = copy.deepcopy(original_results)

        processed = self.processor.process_urls(original_results)

        # Original should be unchanged
        assert original_results == expected_original
        # Processed should have additional fields
        assert len(processed[0]) > len(original_results[0])
