"""
pytest tests for PlaywrightFetcher class
"""

import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from playwright_fetcher import PlaywrightFetcher


class TestPlaywrightFetcher:
    """Test suite for PlaywrightFetcher functionality"""

    @pytest.mark.asyncio
    async def test_fetcher_initialization(self):
        """Test that PlaywrightFetcher initializes correctly"""
        fetcher = PlaywrightFetcher(max_concurrent=3, timeout=15000)

        assert fetcher.max_concurrent == 3
        assert fetcher.timeout == 15000
        assert hasattr(fetcher, "semaphore")

    @pytest.mark.asyncio
    async def test_fetch_single_url(self):
        """Test fetching a single URL"""
        fetcher = PlaywrightFetcher(max_concurrent=1)
        result = await fetcher.fetch_single_url("http://localhost:8080/")

        assert isinstance(result, dict)
        assert "url" in result
        assert "html" in result
        assert "status" in result
        assert "error" in result
        assert result["url"] == "http://localhost:8080/"

        if result["error"] is None:
            assert result["html"] is not None
            assert result["status"] is not None
            assert isinstance(result["html"], str)
            assert len(result["html"]) > 0

    @pytest.mark.asyncio
    async def test_fetch_multiple_urls(self):
        """Test fetching multiple URLs concurrently"""
        fetcher = PlaywrightFetcher(max_concurrent=2)
        urls = [
            "http://localhost:8080/",
            "http://localhost:8080/advanced_features/",
            "http://localhost:8080/getting_started/",
        ]

        results = await fetcher.fetch_urls(urls)

        assert len(results) == len(urls)
        assert isinstance(results, list)

        for i, result in enumerate(results):
            assert isinstance(result, dict)
            assert "url" in result
            assert "html" in result
            assert "status" in result
            assert "error" in result
            assert result["url"] == urls[i]

    @pytest.mark.asyncio
    async def test_fetch_invalid_url(self):
        """Test handling of invalid URLs"""
        fetcher = PlaywrightFetcher(max_concurrent=1)
        result = await fetcher.fetch_single_url("http://nonexistent-domain-12345.com/")

        assert isinstance(result, dict)
        assert result["url"] == "http://nonexistent-domain-12345.com/"
        # Should have either an error or some response
        assert result["error"] is not None or result["status"] is not None

    @pytest.mark.asyncio
    async def test_get_stats(self):
        """Test statistics calculation"""
        fetcher = PlaywrightFetcher()

        # Mock results
        results = [
            {
                "url": "http://example.com/1",
                "html": "<html>...</html>",
                "status": 200,
                "error": None,
            },
            {
                "url": "http://example.com/2",
                "html": "<html>...</html>",
                "status": 200,
                "error": None,
            },
            {
                "url": "http://example.com/3",
                "html": None,
                "status": None,
                "error": "Timeout",
            },
        ]

        stats = fetcher.get_stats(results)

        assert stats["total_urls"] == 3
        assert stats["successful"] == 2
        assert stats["failed"] == 1
        assert stats["success_rate"] == 66.66666666666666

    @pytest.mark.asyncio
    async def test_empty_url_list(self):
        """Test handling of empty URL list"""
        fetcher = PlaywrightFetcher()
        results = await fetcher.fetch_urls([])

        assert results == []

        stats = fetcher.get_stats(results)
        assert stats["total_urls"] == 0
        assert stats["successful"] == 0
        assert stats["failed"] == 0
        assert stats["success_rate"] == 0


class TestPlaywrightFetcherPerformance:
    """Performance and resource management tests"""

    @pytest.mark.asyncio
    @pytest.mark.slow
    async def test_concurrent_fetching(self):
        """Test that concurrent fetching works correctly"""
        fetcher = PlaywrightFetcher(max_concurrent=3)

        # Use a few URLs to test concurrency
        urls = [
            "http://localhost:8080/",
            "http://localhost:8080/advanced_features/",
            "http://localhost:8080/getting_started/",
        ]

        import time

        start_time = time.time()
        results = await fetcher.fetch_urls(urls)
        end_time = time.time()

        assert len(results) == len(urls)
        # Should complete faster than sequential fetching
        assert end_time - start_time < 30  # 30 seconds max

    @pytest.mark.asyncio
    async def test_minimal_resource_blocking(self):
        """Test that minimal resource blocking preserves CSS and JavaScript"""
        fetcher = PlaywrightFetcher(max_concurrent=1)

        # Test that CSS and JavaScript are allowed (should render properly)
        result = await fetcher.fetch_single_url("http://localhost:8080/")
        assert isinstance(result, dict)

        # Verify that the page content includes CSS classes and JavaScript
        if result["html"] and result["error"] is None:
            html = result["html"]
            # Check that CSS is present (should have stylesheets)
            assert "stylesheet" in html or "css" in html.lower()
            # Check that JavaScript is present (should have scripts)
            assert "script" in html.lower() or "javascript" in html.lower()


if __name__ == "__main__":
    # Allow running tests directly
    pytest.main([__file__, "-v"])
