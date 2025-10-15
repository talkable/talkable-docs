"""
Tests for ETag monitoring functionality
"""

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from talkable_llm_txt.etag_monitor import ETagMonitor


class TestETagMonitor:
    """Test cases for ETagMonitor class - Happy Flow Only"""

    def test_init_and_cache_operations(self):
        """Test basic initialization and cache operations."""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache_file = Path(temp_dir) / "test_cache.json"
            monitor = ETagMonitor(str(cache_file))

            # Test initial state - cache should be empty
            assert monitor._cache == {}

            # Test cache persistence by manually setting cache
            monitor._cache = {"https://example.com": '"test-etag"'}
            monitor._save_cache()

            # Create new monitor to test loading
            monitor2 = ETagMonitor(str(cache_file))
            assert monitor2._cache == {"https://example.com": '"test-etag"'}

    @patch("talkable_llm_txt.etag_monitor.requests.get")
    def test_has_changed_first_request(self, mock_get):
        """Test first request returns True (no stored ETag)."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"etag": '"initial-etag"'}
        mock_get.return_value = mock_response

        monitor = ETagMonitor()
        changed = monitor.has_changed("https://example.com")

        assert changed is True
        assert monitor._cache["https://example.com"] == '"initial-etag"'

    @patch("talkable_llm_txt.etag_monitor.requests.get")
    def test_has_changed_modified(self, mock_get):
        """Test modified content returns True (200 response with new ETag)."""
        monitor = ETagMonitor()
        # Manually set cache to simulate previous request
        monitor._cache = {"https://example.com": '"old-etag"'}

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"etag": '"new-etag"'}
        mock_get.return_value = mock_response

        changed = monitor.has_changed("https://example.com")

        assert changed is True
        assert monitor._cache["https://example.com"] == '"new-etag"'
