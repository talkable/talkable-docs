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
        """Extract article and return parsed BeautifulSoup"""
        result = self.preprocessor.extract_article(html)
        assert result is not None
        return BeautifulSoup(result, "html.parser")

    def test_internal_links_processing(self):
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
        hrefs = [link["href"] for link in soup.find_all("a", href=True)]

        expected = [
            "http://localhost:8080/customer_service_portal/overview.md",
            "http://localhost:8080/customer_service_portal/use_case_2.md#logging-in",
            "http://localhost:8080/terminology.md#reward",
        ]
        assert hrefs == expected

    def test_mixed_internal_external_links(self):
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
        hrefs = [link["href"] for link in soup.find_all("a", href=True)]

        assert "http://localhost:8080/docs/guide.md" in hrefs  # Internal converted
        assert "https://example.com" in hrefs  # External unchanged
        assert "mailto:test@example.com" in hrefs  # Mailto unchanged
        assert "#section" in hrefs  # Anchor unchanged

    def test_complex_link_structures(self):
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
        hrefs = sorted([link["href"] for link in soup.find_all("a", href=True)])

        expected = sorted(
            [
                "http://localhost:8080/current/page.md#section",
                "http://localhost:8080/search.md?q=test&page=1",
                "http://localhost:8080/index.md",
            ]
        )
        assert hrefs == expected

    def test_integration_with_other_preprocessing(self):
        """Test link processing with other preprocessing (header links, copy buttons)"""
        html = """
        <article>
            <h1>Title <a class="headerlink" href="#title">#</a></h1>
            <p>Content with <a href="docs/guide/">link</a> and <code>code</code>.</p>
            <button class="copybtn">Copy</button>
        </article>
        """

        soup = self._extract_and_parse(html)

        # Header links should be removed
        assert len(soup.find_all("a", class_="headerlink")) == 0
        # Copy buttons should be removed
        assert len(soup.find_all("button", class_="copybtn")) == 0
        # Internal link should be converted
        content_link = soup.find("a", href=True)
        assert content_link is not None
        assert content_link["href"] == "http://localhost:8080/docs/guide.md"
        # Code should be preserved
        code = soup.find("code")
        assert code is not None
        assert code.get_text() == "code"

    def test_processing_without_base_url(self):
        """Test that links are not processed when base_url is not provided"""
        preprocessor = HTMLPreprocessor()  # No base_url
        html = """
        <article>
            <p>Link: <a href="docs/guide/">Guide</a></p>
        </article>
        """

        result = preprocessor.extract_article(html)
        assert result is not None, "Expected to find an article"
        soup = BeautifulSoup(result, "html.parser")

        link = soup.find("a", href=True)
        assert link is not None
        assert link["href"] == "docs/guide/"  # Unchanged

    def test_empty_article_handling(self):
        """Test processing empty article"""
        assert self.preprocessor.extract_article(None) is None
        assert self.preprocessor.extract_article("") is None
        assert self.preprocessor.extract_article("   ") is None
