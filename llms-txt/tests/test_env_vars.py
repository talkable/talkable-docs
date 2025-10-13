"""Test environment variable configuration overrides."""

import os

from talkable_llm_txt.config import Settings


class TestEnvironmentVariables:
    """Test environment variable configuration overrides."""

    def setup_method(self):
        """Setup test environment."""
        # Clear any existing env vars
        env_vars_to_clear = [
            "LLMS_TXT_MONITORING__ENABLED",
            "LLMS_TXT_PROCESSING__MAX_CONCURRENT_REQUESTS",
            "LLMS_TXT_CORE__OUTPUT_DIR",
        ]
        for var in env_vars_to_clear:
            os.environ.pop(var, None)

    def test_monitoring_enabled_env_override(self):
        """Test monitoring.enabled can be overridden by environment variable."""
        # Set environment variable
        os.environ["LLMS_TXT_MONITORING__ENABLED"] = "false"

        # Load settings
        settings = Settings.create("config.toml.template")

        # Check that env var overrides TOML default
        assert settings.monitoring.enabled is False

    def test_processing_max_concurrent_env_override(self):
        """Test processing.max_concurrent_requests can be overridden."""
        # Set environment variable
        os.environ["LLMS_TXT_PROCESSING__MAX_CONCURRENT_REQUESTS"] = "8"

        # Load settings
        settings = Settings.create("config.toml.template")

        # Check that env var overrides TOML default
        assert settings.processing.max_concurrent_requests == 8

    def test_output_dir_env_override(self):
        """Test core.output_dir can be overridden."""
        # Set environment variable
        os.environ["LLMS_TXT_CORE__OUTPUT_DIR"] = "/tmp/custom-output"

        # Load settings
        settings = Settings.create("config.toml.template")

        # Check that env var overrides TOML default
        assert settings.core.output_dir == "/tmp/custom-output"
