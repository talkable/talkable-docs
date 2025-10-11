"""
Configuration management for talkable-llm-txt application.

This module provides centralized configuration management using Pydantic-Settings
with TOML file support. All application parameters are defined here with
proper validation and defaults.
"""

from typing import Literal, Set, Optional
from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class SitemapConfig(BaseModel):
    """Sitemap configuration settings."""

    url: str = Field(description="URL of the sitemap to process")

    @field_validator("url", mode="after")
    @classmethod
    def validate_sitemap_url(cls, v: str) -> str:
        """Validate sitemap URL format."""
        if not v.startswith(("http://", "https://")):
            raise ValueError("Sitemap URL must start with http:// or https://")
        if not v.strip():
            raise ValueError("Sitemap URL cannot be empty")
        return v


class OutputConfig(BaseModel):
    """Output configuration settings."""

    dir: str = Field(
        default="output", description="Directory where markdown files will be saved"
    )


class ProcessingConfig(BaseModel):
    """Processing configuration settings."""

    max_urls_to_process: Optional[int] = Field(
        default=None,
        ge=1,
        description="Maximum number of URLs to process from the sitemap. If None, processes all URLs.",
    )

    max_concurrent_requests: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Maximum concurrent requests for fetching URLs",
    )

    batch_size: int = Field(
        default=50, ge=1, le=200, description="Number of URLs to process in each batch"
    )

    request_timeout: int = Field(
        default=30000,
        ge=1000,
        le=300000,
        description="Timeout for individual URL requests in milliseconds",
    )


class ContentConfig(BaseModel):
    """Content processing configuration settings."""

    keep_images: bool = Field(
        default=False, description="Whether to keep images in the markdown output"
    )

    heading_style: Literal["atx", "atx_closed", "underlined"] = Field(
        default="atx", description="Markdown heading style to use"
    )


class PerformanceConfig(BaseModel):
    """Performance configuration settings."""

    wait_until: Literal["commit", "domcontentloaded", "load", "networkidle"] = Field(
        default="domcontentloaded", description="Page load wait condition"
    )

    blocked_resource_types: str = Field(
        default="image,media,font",
        description="Comma-separated list of resource types to block",
    )

    @field_validator("blocked_resource_types", mode="after")
    @classmethod
    def parse_blocked_resource_types(cls, v: str) -> str:
        """Validate and normalize blocked resource types."""
        if not v.strip():
            return ""

        valid_types = {"image", "media", "font", "stylesheet", "script"}
        types = [t.strip().lower() for t in v.split(",") if t.strip()]

        # Validate each type
        for resource_type in types:
            if resource_type not in valid_types:
                raise ValueError(
                    f"Invalid resource type: {resource_type}. Valid types: {valid_types}"
                )

        return ",".join(types)

    def get_blocked_resource_types_set(self) -> Set[str]:
        """Get blocked resource types as a set."""
        if not self.blocked_resource_types.strip():
            return set()
        return set(self.blocked_resource_types.split(","))


class SitemapFetchingConfig(BaseModel):
    """Sitemap fetching configuration settings."""

    timeout: int = Field(
        default=30,
        ge=1,
        le=300,
        description="Timeout for sitemap HTTP requests in seconds",
    )

    retries: int = Field(
        default=3,
        ge=0,
        le=10,
        description="Number of retry attempts for failed sitemap requests",
    )

    user_agent: str = Field(
        default="Mozilla/5.0 (compatible; SitemapProcessor/1.0)",
        description="User agent string for HTTP requests",
    )


class MonitoringConfig(BaseModel):
    """Monitoring configuration settings."""

    enabled: bool = Field(
        default=True,
        description="Enable scheduled monitoring for documentation changes (enabled by default)",
    )

    check_url: str = Field(
        default="",
        description="URL to monitor for changes (typically main documentation page)",
    )

    check_interval_minutes: int = Field(
        default=60, ge=1, le=1440, description="Interval in minutes between checks"
    )

    etag_cache_file: str = Field(
        default="etag_cache.json", description="File to store ETag cache"
    )


class LoggingConfig(BaseModel):
    """Logging configuration settings."""

    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO", description="Logging level for application output"
    )


class Settings(BaseSettings):
    """
    Main application settings class.

    This class loads configuration from config.toml file and provides
    centralized access to all application parameters with validation.
    """

    model_config = SettingsConfigDict(
        env_file=None,  # Disable .env file loading
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="forbid",  # Reject extra fields
    )

    # Configuration groups
    sitemap: SitemapConfig = Field(description="Sitemap configuration")
    output: OutputConfig = Field(description="Output configuration")
    processing: ProcessingConfig = Field(description="Processing configuration")
    content: ContentConfig = Field(description="Content configuration")
    performance: PerformanceConfig = Field(description="Performance configuration")
    sitemap_fetching: SitemapFetchingConfig = Field(
        description="Sitemap fetching configuration"
    )
    monitoring: MonitoringConfig = Field(description="Monitoring configuration")
    logging: LoggingConfig = Field(description="Logging configuration")

    def __init__(self, **kwargs):
        """Initialize settings with config file support."""
        super().__init__(**kwargs)

    @classmethod
    def create(cls, config_file: str = "config.toml") -> "Settings":
        """
        Factory method that loads configuration from TOML file.

        Args:
            config_file: Path to the TOML configuration file

        Returns:
            Settings instance loaded from the configuration file

        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If config file is invalid
        """
        import toml
        from pathlib import Path

        config_path = Path(config_file)
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config_data = toml.load(f)

            # Create settings instance
            config = cls(**config_data)
            return config
        except Exception as e:
            raise ValueError(f"Error loading configuration from {config_file}: {e}")

    def get_playwright_fetcher_config(self) -> dict:
        """Get configuration for PlaywrightFetcher."""
        return {
            "max_concurrent": self.processing.max_concurrent_requests,
            "timeout": self.processing.request_timeout,
            "wait_until": self.performance.wait_until,
            "batch_size": self.processing.batch_size,
            "blocked_resource_types": self.performance.get_blocked_resource_types_set(),
        }

    def get_html_preprocessor_config(self) -> dict:
        """Get configuration for HTMLPreprocessor."""
        return {
            "images": self.content.keep_images,
        }

    def get_markdown_converter_config(self) -> dict:
        """Get configuration for MarkdownConverter."""
        return {
            "heading_style": self.content.heading_style,
        }

    def get_sitemap_processor_config(self) -> dict:
        """Get configuration for SitemapProcessor."""
        return {
            "timeout": self.sitemap_fetching.timeout,
            "retries": self.sitemap_fetching.retries,
            "user_agent": self.sitemap_fetching.user_agent,
        }

    def get_file_writer_config(self) -> dict:
        """Get configuration for FileWriter."""
        return {
            "output_dir": self.output.dir,
        }

    def get_logging_config(self) -> dict:
        """Get configuration for logging."""
        return {
            "level": self.logging.level,
        }

    def get_monitoring_config(self) -> dict:
        """Get configuration for monitoring."""
        return {
            "enabled": self.monitoring.enabled,
            "check_url": self.monitoring.check_url,
            "check_interval_minutes": self.monitoring.check_interval_minutes,
            "etag_cache_file": self.monitoring.etag_cache_file,
        }
