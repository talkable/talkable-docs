"""
Configuration management for talkable-llm-txt application.

This module provides centralized configuration management using Pydantic-Settings
with TOML file support. All application parameters are defined here with
proper validation and defaults.
"""

from typing import Literal, Optional, Set

from pydantic import BaseModel, Field, HttpUrl, field_validator
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)
from pydantic_settings.sources import TomlConfigSettingsSource


class CoreConfig(BaseModel):
    """Core configuration settings combining base URL, sitemap, and output."""

    # Base URL (mandatory)
    base_url: HttpUrl = Field(description="Base URL of the documentation site")

    # Sitemap URL (optional - defaults to {base_url}/sitemap.xml)
    sitemap_url: Optional[HttpUrl] = Field(
        default=None,
        description="URL of the sitemap to process. If not provided, will be generated as {base_url}/sitemap.xml",
    )

    # Output directory (existing - moved here)
    output_dir: str = Field(
        default="output", description="Directory where markdown files will be saved"
    )

    def get_effective_sitemap_url(self) -> str:
        """Get the effective sitemap URL (provided or derived from base URL)."""
        if self.sitemap_url:
            return str(self.sitemap_url)
        return f"{self.get_base_url_str()}/sitemap.xml"

    def get_base_url_str(self) -> str:
        """Get base URL as string."""
        return str(self.base_url).rstrip("/")


class ProcessingConfig(BaseModel):
    """Processing configuration settings."""

    max_urls_to_process: Optional[int] = Field(
        default=None,
        ge=1,
        description="Maximum number of URLs to process from the sitemap. If None, processes all URLs.",
    )

    max_concurrent_requests: int = Field(
        default=5,
        ge=1,
        le=10,
        description="Maximum concurrent requests for fetching URLs",
    )

    batch_size: int = Field(
        default=10, ge=1, le=200, description="Number of URLs to process in each batch"
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
        default=False,
        description="Enable scheduled monitoring for documentation changes (disabled by default)",
    )

    check_url: str = Field(
        default="",
        description="URL to monitor for changes (typically main documentation page)",
    )

    check_interval_minutes: int = Field(
        default=1, ge=1, le=1440, description="Interval in minutes between checks"
    )

    etag_cache_file: str = Field(
        default="etag_cache.json", description="File to store ETag cache"
    )


class LLMFullTextConfig(BaseModel):
    """LLM full text file configuration settings."""

    enabled: bool = Field(
        default=True,
        description="Enable generation of aggregated LLM full text file",
    )

    filename: str = Field(
        default="llms-full.txt",
        description="Name of the aggregated LLM full text file",
    )

    include_source_urls: bool = Field(
        default=True,
        description="Include source URLs for each document in the full text file",
    )

    document_separator_style: Literal[
        "html_comments", "markdown_headers", "custom_delimiters"
    ] = Field(
        default="html_comments",
        description="Style of document separators in the full text file",
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
    Environment variables with LLMS_TXT_ prefix can override TOML values.
    """

    model_config = SettingsConfigDict(
        toml_file="config.toml",  # Specify TOML file in config
        env_file=None,  # Disable .env file loading
        env_nested_delimiter="__",
        env_prefix="LLMS_TXT_",
        case_sensitive=False,
        extra="forbid",  # Reject extra fields
        nested_model_default_partial_update=True,  # Better nested field handling
    )

    # Configuration groups
    core: CoreConfig = Field(description="Core configuration")
    processing: ProcessingConfig = Field(
        default_factory=ProcessingConfig, description="Processing configuration"
    )
    content: ContentConfig = Field(
        default_factory=ContentConfig, description="Content configuration"
    )
    performance: PerformanceConfig = Field(
        default_factory=PerformanceConfig, description="Performance configuration"
    )
    sitemap_fetching: SitemapFetchingConfig = Field(
        default_factory=SitemapFetchingConfig,
        description="Sitemap fetching configuration",
    )
    monitoring: MonitoringConfig = Field(
        default_factory=MonitoringConfig, description="Monitoring configuration"
    )
    llm_full_text: LLMFullTextConfig = Field(
        default_factory=LLMFullTextConfig, description="LLM full text configuration"
    )
    logging: LoggingConfig = Field(
        default_factory=LoggingConfig, description="Logging configuration"
    )

    def __init__(self, **kwargs):
        """Initialize settings with config file support."""
        super().__init__(**kwargs)

    @classmethod
    def create(cls, config_file: str = "config.toml") -> "Settings":
        """
        Factory method that loads configuration from TOML file with environment variable overrides.

        Args:
            config_file: Path to the TOML configuration file (optional)

        Returns:
            Settings instance loaded from the configuration file with env var overrides.
            If config file doesn't exist, uses defaults and environment variables.

        Raises:
            ValueError: If required configuration fields are missing from all sources
        """
        from pydantic import ValidationError

        # Update the model config to use the specified config file
        # Pydantic will handle missing files gracefully
        cls.model_config["toml_file"] = config_file

        try:
            # Create settings instance - Pydantic will load TOML if it exists,
            # and apply environment variable overrides, then fall back to defaults
            config = cls()
            return config
        except ValidationError as e:
            # Extract missing required fields for better error message
            missing_fields = []
            for error in e.errors():
                if error["type"] == "missing":
                    # Get the field path as a string
                    field_path = ".".join(str(loc) for loc in error["loc"])
                    missing_fields.append(field_path)

            if missing_fields:
                raise ValueError(
                    f"Missing required configuration fields: {', '.join(missing_fields)}. "
                    f"Please provide these via:\n"
                    f"  1. Environment variables (with LLMS_TXT_ prefix)\n"
                    f"  2. Config file: {config_file}\n"
                    f"  3. Command line arguments\n\n"
                    f"Example environment variables:\n"
                    f"  export LLMS_TXT_CORE__BASE_URL='https://docs.example.com'\n"
                    f"  export LLMS_TXT_CORE__SITEMAP_URL='https://docs.example.com/sitemap.xml'"
                ) from e
            raise

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
            "output_dir": self.core.output_dir,
        }

    def get_logging_config(self) -> dict:
        """Get configuration for logging."""
        return {
            "level": self.logging.level,
        }

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """
        Customize source priority: Environment variables override TOML file.
        Environment variables have highest priority, then TOML file, then init args.
        """
        from pathlib import Path

        toml_file = settings_cls.model_config.get("toml_file", "config.toml")
        sources = []

        # Highest priority: Environment variables (override TOML values)
        sources.append(env_settings)

        # Medium priority: TOML configuration file
        if isinstance(toml_file, (str, Path)) and Path(toml_file).exists():
            sources.append(TomlConfigSettingsSource(settings_cls, str(toml_file)))

        # Lowest priority: Initialization arguments
        sources.append(init_settings)

        return tuple(sources)

    def get_llm_full_text_config(self) -> dict:
        """Get configuration for LLM full text writer."""
        return {
            "output_dir": self.core.output_dir,
            "filename": self.llm_full_text.filename,
            "include_source_urls": self.llm_full_text.include_source_urls,
            "base_url": self.core.get_base_url_str(),
        }

    def is_llm_full_text_enabled(self) -> bool:
        """Check if LLM full text generation is enabled."""
        return self.llm_full_text.enabled

    def get_monitoring_config(self) -> dict:
        """Get configuration for monitoring."""
        return {
            "enabled": self.monitoring.enabled,
            "check_url": self.monitoring.check_url,
            "check_interval_minutes": self.monitoring.check_interval_minutes,
            "etag_cache_file": self.monitoring.etag_cache_file,
        }
