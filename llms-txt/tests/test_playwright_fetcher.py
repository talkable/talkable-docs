"""
pytest tests for PlaywrightFetcher class
"""

import pytest

from talkable_llm_txt import PlaywrightFetcher


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
    async def test_concurrent_fetching(self):
        """Test that concurrent fetching works correctly"""
        fetcher = PlaywrightFetcher(max_concurrent=3)
        urls = [
            "http://localhost:8080/",
            "http://localhost:8080/advanced_features/",
            "http://localhost:8080/getting_started/",
        ]

        results = await fetcher.fetch_urls(urls)
        assert len(results) == len(urls)

    @pytest.mark.asyncio
    async def test_minimal_resource_blocking(self):
        """Test that minimal resource blocking doesn't break page functionality"""
        fetcher = PlaywrightFetcher(max_concurrent=1)
        result = await fetcher.fetch_single_url("http://localhost:8080/")

        assert isinstance(result, dict)
        assert "url" in result
        assert "html" in result
        assert "status" in result
        assert "error" in result

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


if __name__ == "__main__":
    # Allow running tests directly
    pytest.main([__file__, "-v"])
