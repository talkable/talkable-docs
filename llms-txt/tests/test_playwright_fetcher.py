"""
pytest tests for PlaywrightFetcher class
"""

from unittest.mock import AsyncMock, Mock, patch

import pytest

from talkable_llm_txt import PlaywrightFetcher


class TestPlaywrightFetcher:
    """Test suite for PlaywrightFetcher functionality - Happy Flow Only"""

    @pytest.mark.asyncio
    async def test_fetcher_initialization(self):
        """Test that PlaywrightFetcher initializes correctly"""
        fetcher = PlaywrightFetcher(max_concurrent=3, timeout=15000)

        assert fetcher.max_concurrent == 3
        assert fetcher.timeout == 15000
        assert hasattr(fetcher, "semaphore")

    @pytest.mark.asyncio
    async def test_fetch_single_url_structure(self, sample_html_response):
        """Test fetching a single URL returns correct structure using local HTML fixture"""
        fetcher = PlaywrightFetcher(max_concurrent=1)

        # Mock the browser context and page to return our local HTML fixture
        with patch(
            "talkable_llm_txt.playwright_fetcher.async_playwright"
        ) as mock_playwright:
            mock_browser = AsyncMock()
            mock_context = AsyncMock()
            mock_page = AsyncMock()
            mock_response = AsyncMock()

            # Mock the event handler methods to avoid async warnings
            mock_context.on = Mock()
            mock_page.on = Mock()

            mock_response.status = 200
            mock_page.goto.return_value = mock_response
            mock_page.content.return_value = sample_html_response
            mock_page.close.return_value = None

            mock_context.new_page.return_value = mock_page
            mock_browser.new_context.return_value = mock_context

            # Create proper async context manager mock
            mock_playwright_instance = AsyncMock()
            mock_playwright_instance.__aenter__ = AsyncMock(
                return_value=mock_playwright_instance
            )
            mock_playwright_instance.__aexit__ = AsyncMock(return_value=None)
            mock_playwright_instance.chromium.launch.return_value = mock_browser

            mock_playwright.return_value = mock_playwright_instance

            # Test that the method exists and can be called
            result = await fetcher.fetch_single_url("http://localhost:8080/")

            # Should return a dict with expected keys
            assert isinstance(result, dict)
            assert "url" in result
            assert result["url"] == "http://localhost:8080/"

            # Should have html content from our local fixture
            assert "html" in result
            assert result["html"] is not None
            assert result["status"] is not None
            assert isinstance(result["html"], str)
            assert len(result["html"]) > 0

            # Verify the HTML contains content from our fixture
            assert "Magento" in result["html"]
            assert "Talkable offers free extension" in result["html"]

    @pytest.mark.asyncio
    async def test_fetch_urls(self, sample_html_response):
        """Test fetching multiple URLs concurrently using local HTML fixture"""
        fetcher = PlaywrightFetcher(max_concurrent=2)
        urls = [
            "http://localhost:8080/",
            "http://localhost:8080/docs/",
        ]

        # Mock the browser context and page to return our local HTML fixture
        with patch(
            "talkable_llm_txt.playwright_fetcher.async_playwright"
        ) as mock_playwright:
            mock_browser = AsyncMock()
            mock_context = AsyncMock()
            mock_page = AsyncMock()
            mock_response = AsyncMock()

            # Mock the event handler methods to avoid async warnings
            mock_context.on = Mock()
            mock_page.on = Mock()

            mock_response.status = 200
            mock_page.goto.return_value = mock_response
            mock_page.content.return_value = sample_html_response
            mock_page.close.return_value = None

            mock_context.new_page.return_value = mock_page
            mock_browser.new_context.return_value = mock_context

            # Create proper async context manager mock
            mock_playwright_instance = AsyncMock()
            mock_playwright_instance.__aenter__ = AsyncMock(
                return_value=mock_playwright_instance
            )
            mock_playwright_instance.__aexit__ = AsyncMock(return_value=None)
            mock_playwright_instance.chromium.launch.return_value = mock_browser

            mock_playwright.return_value = mock_playwright_instance

            results = await fetcher.fetch_urls(urls)

            # Should return list of results
            assert isinstance(results, list)
            assert len(results) == len(urls)

            # Each result should have expected structure
            for result in results:
                assert isinstance(result, dict)
                assert "url" in result
                assert "html" in result
                assert result["html"] is not None
                assert result["status"] is not None
                assert "Magento" in result["html"]  # Verify fixture content
