"""
Tests for URL processing classes and link transformation functionality
"""

from talkable_llm_txt.url_processor import (
    LinkProcessor,
    MarkdownFileConverter,
    URLNormalizer,
)


class TestURLNormalizer:
    """Test cases for URLNormalizer class - Happy Flow Only"""

    def setup_method(self):
        """Setup for each test method"""
        self.base_url = "http://localhost:8080"
        self.normalizer = URLNormalizer(self.base_url)

    def test_normalize_root_relative_path(self):
        """Test normalizing root-relative paths"""
        url = "/customer_service_portal/overview/"
        result = self.normalizer.process(url)
        assert result == "http://localhost:8080/customer_service_portal/overview/"

    def test_normalize_relative_path(self):
        """Test normalizing relative paths"""
        url = "customer_service_portal/use_case_2/"
        result = self.normalizer.process(url)
        assert result == "http://localhost:8080/customer_service_portal/use_case_2/"

    def test_normalize_with_query_params(self):
        """Test normalizing URLs with query parameters"""
        url = "/search?q=test&page=1"
        result = self.normalizer.process(url)
        assert result == "http://localhost:8080/search?q=test&page=1"

    def test_normalize_with_fragment(self):
        """Test normalizing URLs with fragments"""
        url = "/docs/guide/#installation"
        result = self.normalizer.process(url)
        assert result == "http://localhost:8080/docs/guide/#installation"


class TestMarkdownFileConverter:
    """Test cases for MarkdownFileConverter class - Happy Flow Only"""

    def setup_method(self):
        """Setup for each test method"""
        self.converter = MarkdownFileConverter()

    def test_convert_path_to_markdown(self):
        """Test converting URL path to markdown file path"""
        path = "/docs/guide/"
        result = self.converter.process(path)
        assert result == "/docs/guide.md"

    def test_convert_root_path(self):
        """Test converting root path to index.md"""
        path = "/"
        result = self.converter.process(path)
        assert result == "/index.md"

    def test_convert_path_with_query_params(self):
        """Test converting path with query parameters"""
        path = "/search?q=test&page=1"
        result = self.converter.process(path)
        assert result == "/search.md?q=test&page=1"

    def test_convert_path_with_fragment(self):
        """Test converting path with fragment"""
        path = "/docs/guide/#installation"
        result = self.converter.process(path)
        assert result == "/docs/guide.md#installation"


class TestLinkProcessor:
    """Test cases for LinkProcessor class - Happy Flow Only"""

    def setup_method(self):
        """Setup for each test method"""
        self.base_url = "http://localhost:8080"
        self.processor = LinkProcessor(self.base_url)

    def test_process_internal_link_with_class(self):
        """Test processing internal link with reference internal class"""
        href = "docs/guide/"
        link_class = "reference internal"
        result = self.processor.process_link(href, link_class=link_class)
        assert result == "http://localhost:8080/docs/guide.md"

    def test_process_internal_link_without_class(self):
        """Test processing internal link without class returns None (fail safe)"""
        href = "docs/guide/"
        result = self.processor.process_link(href)
        assert result is None

    def test_process_external_link(self):
        """Test processing external link returns None (should not be processed)"""
        href = "https://example.com"
        result = self.processor.process_link(href)
        assert result is None

    def test_process_external_link_with_class(self):
        """Test processing external link with external class returns None"""
        href = "https://example.com"
        link_class = "reference external"
        result = self.processor.process_link(href, link_class=link_class)
        assert result is None

    def test_process_mailto_link(self):
        """Test processing mailto link returns None (should not be processed)"""
        href = "mailto:test@example.com"
        result = self.processor.process_link(href)
        assert result is None

    def test_process_anchor_link(self):
        """Test processing anchor link returns None (should not be processed)"""
        href = "#section"
        result = self.processor.process_link(href)
        assert result is None

    def test_process_complex_internal_link(self):
        """Test processing complex internal link with reference internal class"""
        href = "/customer_service_portal/use_case_1/#getting-started"
        link_class = "reference internal"
        result = self.processor.process_link(href, link_class=link_class)
        assert (
            result
            == "http://localhost:8080/customer_service_portal/use_case_1.md#getting-started"
        )
