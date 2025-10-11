"""
Test that monitoring is enabled by default.
"""

from talkable_llm_txt.config import Settings


def test_monitoring_enabled_by_default():
    """Test that monitoring is enabled by default in configuration."""
    # Create settings with minimal required config
    settings = Settings(
        sitemap={"url": "https://example.com/sitemap.xml"},
        monitoring={},  # Empty monitoring config should use defaults
        output={},
        processing={},
        content={},
        performance={},
        sitemap_fetching={},
        logging={},
    )

    # Check that monitoring is enabled by default
    assert settings.monitoring.enabled is True

    # Check other defaults
    assert settings.monitoring.check_interval_minutes == 60
    assert settings.monitoring.etag_cache_file == "etag_cache.json"

    # Check that check_url defaults to empty string (will fallback to sitemap URL)
    assert settings.monitoring.check_url == ""
