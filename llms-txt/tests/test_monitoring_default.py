"""
Test that monitoring is disabled by default.
"""


def test_monitoring_disabled_by_default():
    """Test that monitoring is disabled by default in configuration."""
    from talkable_llm_txt.config import MonitoringConfig

    # Test MonitoringConfig directly with empty config
    monitoring = MonitoringConfig()

    # Check that monitoring is disabled by default
    assert monitoring.enabled is False

    # Check other defaults
    assert monitoring.check_interval_minutes == 1
    assert monitoring.etag_cache_file == "etag_cache.json"

    # Check that check_url defaults to empty string (will fallback to sitemap URL)
    assert monitoring.check_url == ""
