"""
Integration tests for link processing functionality in HTMLPreprocessor.
"""

from bs4 import BeautifulSoup
from talkable_llm_txt.html_preprocessor import HTMLPreprocessor


class TestLinkProcessingIntegration:
    """Test integration of link processing with HTML preprocessing"""

    def setup_method(self):
        """Setup for each test method"""
        self.base_url = "http://localhost:8080"
        self.preprocessor = HTMLPreprocessor(base_url=self.base_url)

    def _extract_and_parse(self, html: str) -> BeautifulSoup:
        """Helper method to extract article and parse with BeautifulSoup"""
        result = self.preprocessor.extract_article(html)
        assert result is not None, f"Failed to extract article from: {html}"
        return BeautifulSoup(result, "html.parser")

    def test_process_article_with_internal_links(self):
        """Test processing article with internal links"""
        html = """
        <article>
            <h1>Test Article</h1>
            <p>Visit <a href="customer_service_portal/overview/">overview</a> for details.</p>
            <p>Check <a href="/customer_service_portal/use_case_2/#logging-in">use case 2</a> for examples.</p>
            <p>See <a href="../terminology/#reward">terminology</a> for definitions.</p>
        </article>
        """

        soup = self._extract_and_parse(html)

        # Check that internal links were converted
        links = soup.find_all("a", href=True)
        hrefs = [link["href"] for link in links]

        expected_hrefs = [
            "http://localhost:8080/customer_service_portal/overview.md",
            "http://localhost:8080/customer_service_portal/use_case_2.md#logging-in",
            "http://localhost:8080/terminology.md#reward",
        ]

        assert hrefs == expected_hrefs

    def test_process_article_mixed_links(self):
        """Test processing article with mixed internal and external links"""
        html = """
        <article>
            <h1>Mixed Links</h1>
            <p>Internal: <a href="docs/guide/">Guide</a></p>
            <p>External: <a href="https://example.com">Example</a></p>
            <p>Email: <a href="mailto:test@example.com">Email</a></p>
            <p>Anchor: <a href="#section">Section</a></p>
        </article>
        """

        soup = self._extract_and_parse(html)

        links = soup.find_all("a", href=True)
        hrefs = [link["href"] for link in links]

        # Only internal link should be converted
        assert "http://localhost:8080/docs/guide.md" in hrefs
        assert "https://example.com" in hrefs  # External unchanged
        assert "mailto:test@example.com" in hrefs  # Mailto unchanged
        assert "#section" in hrefs  # Anchor unchanged

    def test_process_article_without_base_url(self):
        """Test that links are not processed when base_url is not provided"""
        preprocessor = HTMLPreprocessor()  # No base_url

        html = """
        <article>
            <p>Link: <a href="docs/guide/">Guide</a></p>
        </article>
        """

        result = preprocessor.extract_article(html)
        assert result is not None  # Ensure result is not None
        soup = BeautifulSoup(result, "html.parser")

        link = soup.find("a")
        assert link is not None, "Expected to find a link"
        assert link["href"] == "docs/guide/"  # Unchanged

    def test_process_article_with_complex_links(self):
        """Test processing article with complex link structures"""
        html = """
        <article>
            <h1>Complex Links</h1>
            <p>Nested: <span><a href="./current/page/#section">Current</a></span></p>
            <p>Query: <a href="/search?q=test&page=1">Search</a></p>
            <p>Root: <a href="/">Home</a></p>
        </article>
        """

        soup = self._extract_and_parse(html)

        links = soup.find_all("a", href=True)
        hrefs = sorted([link["href"] for link in links])

        expected_hrefs = sorted(
            [
                "http://localhost:8080/current/page.md#section",
                "http://localhost:8080/search.md?q=test&page=1",
                "http://localhost:8080/index.md",
            ]
        )

        assert hrefs == expected_hrefs

    def test_process_article_with_no_links(self):
        """Test processing article without any links"""
        html = """
        <article>
            <h1>No Links</h1>
            <p>Just some text content.</p>
        </article>
        """

        result = self.preprocessor.extract_article(html)
        assert result is not None

        soup = BeautifulSoup(result, "html.parser")
        links = soup.find_all("a", href=True)
        assert len(links) == 0

    def test_process_article_with_empty_article(self):
        """Test processing empty article"""
        result = self.preprocessor.extract_article(None)
        assert result is None

        result = self.preprocessor.extract_article("")
        assert result is None

        result = self.preprocessor.extract_article("   ")
        assert result is None

    def test_process_article_preserves_other_content(self):
        """Test that link processing preserves other content"""
        html = """
        <article>
            <h1>Title <a class="headerlink" href="#title">#</a></h1>
            <p>Content with <a href="docs/guide/">link</a> and <code>code</code>.</p>
            <button class="copybtn">Copy</button>
        </article>
        """

        soup = self._extract_and_parse(html)

        # Header links should be removed
        header_links = soup.find_all("a", class_="headerlink")
        assert len(header_links) == 0

        # Copy buttons should be removed
        copy_buttons = soup.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0

        # Internal link should be converted
        content_link = soup.find("a", href=True)
        assert content_link is not None, "Expected to find a link with href"
        assert content_link["href"] == "http://localhost:8080/docs/guide.md"

        # Code should be preserved
        code = soup.find("code")
        assert code is not None
        assert code.get_text() == "code"


class TestLinkProcessingEdgeCases:
    """Test edge cases for link processing"""

    def setup_method(self):
        """Setup for each test method"""
        self.base_url = "http://localhost:8080"
        self.preprocessor = HTMLPreprocessor(base_url=self.base_url)

    def _extract_and_parse(self, html: str) -> BeautifulSoup:
        """Helper method to extract article and parse with BeautifulSoup"""
        result = self.preprocessor.extract_article(html)
        assert result is not None, f"Failed to extract article from: {html}"
        return BeautifulSoup(result, "html.parser")

    def test_process_malformed_links(self):
        """Test processing malformed or unusual links"""
        html = """
        <article>
            <p>Strange links:
            <a href="">Empty</a>
            <a href="   ">Spaces</a>
            <a href="javascript:void(0)">JS</a>
            <a href="ftp://example.com">FTP</a>
            </p>
        </article>
        """

        soup = self._extract_and_parse(html)

        links = soup.find_all("a", href=True)
        hrefs = [link["href"] for link in links]

        # All should be unchanged (skipped by processor)
        assert "" in hrefs
        assert "   " in hrefs
        assert "javascript:void(0)" in hrefs
        assert "ftp://example.com" in hrefs

    def test_process_unicode_links(self):
        """Test processing links with unicode characters"""
        html = """
        <article>
            <p><a href="/docs/指南/">Guide</a></p>
        </article>
        """

        soup = self._extract_and_parse(html)

        link = soup.find("a")
        assert link is not None, "Expected to find a link"
        assert link["href"] == "http://localhost:8080/docs/指南.md"

    def test_process_url_encoded_links(self):
        """Test processing links with URL encoding"""
        html = """
        <article>
            <p><a href="/docs/path%20with%20spaces/">Space Path</a></p>
        </article>
        """

        soup = self._extract_and_parse(html)

        link = soup.find("a")
        assert link is not None, "Expected to find a link"
        assert link["href"] == "http://localhost:8080/docs/path%20with%20spaces.md"
