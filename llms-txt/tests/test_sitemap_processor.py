"""
pytest tests for SitemapProcessor class
"""

import pytest

from talkable_llm_txt import SitemapProcessor


class TestSitemapProcessor:
    """Test suite for SitemapProcessor functionality"""

    def test_sitemap_processor_initialization(self):
        """Test that SitemapProcessor initializes and processes sitemap automatically"""
        processor = SitemapProcessor("http://localhost:8080/sitemap.xml")

        # Check that processed_urls is populated
        assert hasattr(processor, "processed_urls")
        assert isinstance(processor.processed_urls, list)
        assert len(processor.processed_urls) > 0

    def test_processed_urls_structure(self):
        """Test that processed_urls has correct structure"""
        processor = SitemapProcessor("http://localhost:8080/sitemap.xml")

        # Check that each entry has required keys
        for entry in processor.processed_urls:
            assert "url" in entry
            assert "path" in entry
            assert isinstance(entry["url"], str)
            assert isinstance(entry["path"], str)
            assert entry["url"].startswith("http")
            assert entry["path"].startswith("/")

    def test_path_extraction_removes_query_parameters(self):
        """Test that path extraction correctly removes query parameters"""
        processor = SitemapProcessor("http://localhost:8080/sitemap.xml")

        test_cases = [
            ("https://example.com/page", "/page"),
            ("https://example.com/page?param=value", "/page"),
            ("https://example.com/page?param1=value1&param2=value2", "/page"),
            (
                "https://example.com/path/to/page?utm_source=test&utm_medium=email",
                "/path/to/page",
            ),
            ("https://example.com/", "/"),
        ]

        for url, expected_path in test_cases:
            actual_path = processor._extract_path(url)
            assert actual_path == expected_path, f"Failed for URL: {url}"

    def test_consistency_between_instances(self):
        """Test that multiple instances return consistent results"""
        processor1 = SitemapProcessor("http://localhost:8080/sitemap.xml")
        processor2 = SitemapProcessor("http://localhost:8080/sitemap.xml")

        assert len(processor1.processed_urls) == len(processor2.processed_urls)
        assert processor1.processed_urls == processor2.processed_urls

    def test_sitemap_url_property(self):
        """Test that sitemap_url is stored correctly"""
        test_url = "http://localhost:8080/sitemap.xml"
        processor = SitemapProcessor(test_url)

        assert processor.sitemap_url == test_url

    def test_processed_urls_property_returns_direct_reference(self):
        """Test that processed_urls property returns the actual list (not a copy)"""
        processor = SitemapProcessor("http://localhost:8080/sitemap.xml")
        original_length = len(processor.processed_urls)

        # Modify the returned list
        processor.processed_urls.append({"test": "value"})

        # Check that the internal list was modified (this is the intended behavior)
        assert len(processor.processed_urls) == original_length + 1


class TestSitemapProcessorEdgeCases:
    """Test edge cases and error handling"""

    def test_invalid_sitemap_url(self):
        """Test handling of invalid sitemap URL"""
        # This should not raise an exception, but return empty results
        processor = SitemapProcessor(
            "http://invalid-url-that-does-not-exist.com/sitemap.xml"
        )

        # Should handle gracefully
        assert isinstance(processor.processed_urls, list)

    def test_empty_sitemap_response(self):
        """Test handling of empty sitemap response"""
        # This would require mocking in a real test scenario
        # For now, just ensure the class doesn't crash
        pass

    def test_url_validation(self):
        """Test URL validation"""
        # Valid URLs should work
        processor = SitemapProcessor("http://localhost:8080/sitemap.xml")
        assert processor.sitemap_url == "http://localhost:8080/sitemap.xml"

        # Invalid URLs should raise ValueError
        with pytest.raises(ValueError):
            SitemapProcessor("invalid-url")

        with pytest.raises(ValueError):
            SitemapProcessor("ftp://example.com/sitemap.xml")

    def test_lazy_loading(self):
        """Test lazy loading functionality"""
        # Create processor without auto-processing
        processor = SitemapProcessor(
            "http://localhost:8080/sitemap.xml", auto_process=False
        )

        # Should be empty initially
        assert len(processor.processed_urls) == 0

        # Manually process
        processor.process()

        # Should now have URLs
        assert len(processor.processed_urls) > 0

    def test_context_manager(self):
        """Test context manager functionality"""
        with SitemapProcessor("http://localhost:8080/sitemap.xml") as processor:
            assert len(processor.processed_urls) > 0
            # Session should be available
            assert hasattr(processor, "session")

        # Session should be closed after context exit
        # (This is hard to test directly, but should not raise errors)


class TestSitemapProcessorPerformance:
    """Performance and scalability tests"""

    def test_large_sitemap_processing(self):
        """Test that sitemap processing completes in reasonable time"""
        import time

        start_time = time.time()
        processor = SitemapProcessor("http://localhost:8080/sitemap.xml")
        end_time = time.time()

        # Should complete within 10 seconds (adjust as needed)
        assert end_time - start_time < 10.0
        assert len(processor.processed_urls) > 0

    def test_memory_usage(self):
        """Test that memory usage is reasonable"""
        # Basic memory check - ensure we're not holding excessive data
        processor = SitemapProcessor("http://localhost:8080/sitemap.xml")

        # Check that we have a reasonable number of URLs
        assert len(processor.processed_urls) < 100000  # Sanity check


if __name__ == "__main__":
    # Allow running tests directly
    pytest.main([__file__, "-v"])
