"""
pytest tests for SitemapProcessor class
"""

from unittest.mock import patch

from talkable_llm_txt import SitemapProcessor


class TestSitemapProcessor:
    """Test suite for SitemapProcessor functionality - Happy Flow Only"""

    @patch("requests.Session.get")
    def test_sitemap_processor_initialization(self, mock_get, mock_sitemap_response):
        """Test that SitemapProcessor initializes and processes sitemap successfully"""
        mock_get.return_value = mock_sitemap_response

        processor = SitemapProcessor("http://localhost:8080/sitemap.xml")

        # Check that processed_urls is populated
        assert hasattr(processor, "processed_urls")
        assert isinstance(processor.processed_urls, list)
        assert len(processor.processed_urls) > 0

        # Verify we have real URLs from the sitemap
        urls = [entry["url"] for entry in processor.processed_urls]
        assert any("docs.talkable.com" in url for url in urls)
        assert any("advanced_features" in url for url in urls)

        # Verify the mock was called correctly
        mock_get.assert_called_once_with(
            "http://localhost:8080/sitemap.xml", timeout=30
        )

    @patch("requests.Session.get")
    def test_processed_urls_structure(self, mock_get, mock_sitemap_response):
        """Test that processed_urls has correct structure"""
        mock_get.return_value = mock_sitemap_response

        processor = SitemapProcessor("http://localhost:8080/sitemap.xml")

        # Check that each entry has required keys
        for entry in processor.processed_urls:
            assert "url" in entry
            assert "path" in entry
            assert isinstance(entry["url"], str)
            assert isinstance(entry["path"], str)
            assert entry["url"].startswith("http")
            assert len(entry["path"]) > 0
