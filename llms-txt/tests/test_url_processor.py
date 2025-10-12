"""
Tests for URL processing classes and link transformation functionality.
"""

from talkable_llm_txt.url_processor import (
    URLNormalizer,
    MarkdownFileConverter,
    LinkProcessor,
)


class TestURLNormalizer:
    """Test cases for URLNormalizer class"""

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

    def test_normalize_parent_directory_reference(self):
        """Test normalizing paths with parent directory references"""
        url = "../terminology/#reward"
        result = self.normalizer.process(url)
        assert result == "http://localhost:8080/terminology/#reward"

    def test_normalize_current_directory_reference(self):
        """Test normalizing paths with current directory references"""
        url = "./current_page/#section"
        result = self.normalizer.process(url)
        assert result == "http://localhost:8080/current_page/#section"

    def test_normalize_with_query_params(self):
        """Test normalizing URLs with query parameters"""
        url = "/search?q=test&page=1"
        result = self.normalizer.process(url)
        assert result == "http://localhost:8080/search?q=test&page=1"

    def test_base_url_trailing_slash_handling(self):
        """Test that base URL trailing slash is handled correctly"""
        normalizer = URLNormalizer("http://localhost:8080/")
        url = "/test"
        result = normalizer.process(url)
        assert result == "http://localhost:8080/test"


class TestMarkdownFileConverter:
    """Test cases for MarkdownFileConverter class"""

    def setup_method(self):
        """Setup for each test method"""
        self.converter = MarkdownFileConverter()

    def test_convert_simple_path(self):
        """Test converting simple path to markdown file"""
        url = "http://localhost:8080/customer_service_portal/use_case_2/"
        result = self.converter.process(url)
        assert result == "http://localhost:8080/customer_service_portal/use_case_2.md"

    def test_convert_with_fragment(self):
        """Test converting URL with fragment to markdown file"""
        url = "http://localhost:8080/customer_service_portal/overview/#logging-in"
        result = self.converter.process(url)
        assert (
            result
            == "http://localhost:8080/customer_service_portal/overview.md#logging-in"
        )

    def test_convert_root_path(self):
        """Test converting root path to index.md"""
        url = "http://localhost:8080/"
        result = self.converter.process(url)
        assert result == "http://localhost:8080/index.md"

    def test_convert_empty_path(self):
        """Test converting empty path to index.md"""
        url = "http://localhost:8080"
        result = self.converter.process(url)
        assert result == "http://localhost:8080/index.md"

    def test_convert_with_query_params(self):
        """Test converting URL with query parameters"""
        url = "http://localhost:8080/search?term=test"
        result = self.converter.process(url)
        assert result == "http://localhost:8080/search.md?term=test"

    def test_convert_with_fragment_and_query(self):
        """Test converting URL with both fragment and query parameters"""
        url = "http://localhost:8080/page?param=value#section"
        result = self.converter.process(url)
        assert result == "http://localhost:8080/page.md?param=value#section"

    def test_convert_without_trailing_slash(self):
        """Test converting URL without trailing slash"""
        url = "http://localhost:8080/customer_service_portal/use_case_2"
        result = self.converter.process(url)
        assert result == "http://localhost:8080/customer_service_portal/use_case_2.md"


class TestLinkProcessor:
    """Test cases for LinkProcessor class"""

    def setup_method(self):
        """Setup for each test method"""
        self.base_url = "http://localhost:8080"
        self.processor = LinkProcessor(self.base_url)

    def test_process_relative_link(self):
        """Test processing a relative link"""
        href = "customer_service_portal/use_case_2/"
        result = self.processor.process_link(href)
        assert result == "http://localhost:8080/customer_service_portal/use_case_2.md"

    def test_process_root_relative_link(self):
        """Test processing a root-relative link"""
        href = "/customer_service_portal/overview/#logging-in"
        result = self.processor.process_link(href)
        assert (
            result
            == "http://localhost:8080/customer_service_portal/overview.md#logging-in"
        )

    def test_process_parent_directory_link(self):
        """Test processing a parent directory reference"""
        href = "../terminology/#reward"
        result = self.processor.process_link(href)
        assert result == "http://localhost:8080/terminology.md#reward"

    def test_skip_external_link(self):
        """Test that external links are skipped"""
        href = "https://example.com/page"
        result = self.processor.process_link(href)
        assert result is None

    def test_skip_mailto_link(self):
        """Test that mailto links are skipped"""
        href = "mailto:test@example.com"
        result = self.processor.process_link(href)
        assert result is None

    def test_skip_tel_link(self):
        """Test that tel links are skipped"""
        href = "tel:+1234567890"
        result = self.processor.process_link(href)
        assert result is None

    def test_skip_javascript_link(self):
        """Test that javascript links are skipped"""
        href = "javascript:void(0)"
        result = self.processor.process_link(href)
        assert result is None

    def test_skip_anchor_only_link(self):
        """Test that anchor-only links are skipped"""
        href = "#section"
        result = self.processor.process_link(href)
        assert result is None

    def test_skip_empty_link(self):
        """Test that empty links are skipped"""
        href = ""
        result = self.processor.process_link(href)
        assert result is None

    def test_skip_whitespace_only_link(self):
        """Test that whitespace-only links are skipped"""
        href = "   "
        result = self.processor.process_link(href)
        assert result is None

    def test_process_complex_relative_link(self):
        """Test processing complex relative link with query and fragment"""
        href = "./docs/guide?version=2.0#installation"
        result = self.processor.process_link(href)
        assert result == "http://localhost:8080/docs/guide.md?version=2.0#installation"

    def test_integration_complete_pipeline(self):
        """Test complete pipeline integration with various link types"""
        test_cases = [
            (
                "customer_service_portal/overview/",
                "http://localhost:8080/customer_service_portal/overview.md",
            ),
            (
                "/customer_service_portal/use_case_2/#logging-in",
                "http://localhost:8080/customer_service_portal/use_case_2.md#logging-in",
            ),
            ("../terminology/#reward", "http://localhost:8080/terminology.md#reward"),
            ("./", "http://localhost:8080/index.md"),
        ]

        for input_href, expected_output in test_cases:
            result = self.processor.process_link(input_href)
            assert result == expected_output, f"Failed for {input_href}"


class TestLinkProcessorEdgeCases:
    """Test edge cases for LinkProcessor"""

    def setup_method(self):
        """Setup for each test method"""
        self.base_url = "http://localhost:8080"
        self.processor = LinkProcessor(self.base_url)

    def test_process_url_encoded_path(self):
        """Test processing URL with encoded characters"""
        href = "/path%20with%20spaces/file%20name/"
        result = self.processor.process_link(href)
        assert result == "http://localhost:8080/path%20with%20spaces/file%20name.md"

    def test_process_multiple_parent_references(self):
        """Test processing multiple parent directory references"""
        href = "../../grandparent/page/"
        result = self.processor.process_link(href)
        assert result == "http://localhost:8080/grandparent/page.md"

    def test_process_special_characters_in_path(self):
        """Test processing path with special characters"""
        href = "/api/v1.0/endpoints/"
        result = self.processor.process_link(href)
        assert result == "http://localhost:8080/api/v1.0/endpoints.md"

    def test_skip_ftp_protocol(self):
        """Test that FTP protocol links are skipped"""
        href = "ftp://example.com/file.txt"
        result = self.processor.process_link(href)
        assert result is None

    def test_skip_file_protocol(self):
        """Test that file protocol links are skipped"""
        href = "file:///path/to/file"
        result = self.processor.process_link(href)
        assert result is None
