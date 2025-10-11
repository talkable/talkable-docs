import asyncio
import logging
import signal
from urllib.parse import urlparse

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from talkable_llm_txt import (
    FileWriter,
    HTMLPreprocessor,
    MarkdownConverter,
    PlaywrightFetcher,
    SitemapProcessor,
)
from talkable_llm_txt.config import Settings
from talkable_llm_txt.etag_monitor import ETagMonitor
from talkable_llm_txt.logging_config import setup_logging

# Module-level variables for application-wide state (Pythonic approach)
config: Settings | None = None
logger: logging.Logger | None = None


async def initialize_app():
    """Initialize application-wide state."""
    global config, logger

    config = Settings.create()
    logging_config = config.get_logging_config()
    setup_logging(level=logging_config["level"])
    logger = logging.getLogger(__name__)
    logger.info("Application initialized successfully")


async def run_pipeline():
    """Main application entry point with configuration management."""

    # Type casting - these are guaranteed to be initialized after initialize_app()
    from typing import cast

    app_config = cast(Settings, config)
    app_logger = cast(logging.Logger, logger)

    # Process sitemap to get URLs
    app_logger.info("Processing sitemap...")
    sitemap_config = app_config.get_sitemap_processor_config()
    processor = SitemapProcessor(sitemap_url=app_config.sitemap.url, **sitemap_config)
    app_logger.info(f"Found {len(processor.processed_urls)} URLs")

    # Get URLs to process (limited by configuration or all if None)
    if app_config.processing.max_urls_to_process is None:
        # Process all URLs found in sitemap
        urls_to_fetch = [entry["url"] for entry in processor.processed_urls]
        app_logger.info(f"Processing all {len(urls_to_fetch)} URLs found in sitemap...")
    else:
        # Process limited number of URLs
        urls_to_fetch = [
            entry["url"]
            for entry in processor.processed_urls[
                : app_config.processing.max_urls_to_process
            ]
        ]
        app_logger.info(f"Processing first {len(urls_to_fetch)} URLs...")

    # Fetch HTML content
    fetcher_config = app_config.get_playwright_fetcher_config()
    fetcher = PlaywrightFetcher(**fetcher_config)
    results = await fetcher.fetch_urls(urls_to_fetch)

    # Process HTML to extract articles
    # Extract base URL from sitemap URL for link processing
    parsed_url = urlparse(app_config.sitemap.url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    preprocessor_config = app_config.get_html_preprocessor_config()
    preprocessor = HTMLPreprocessor(base_url=base_url, **preprocessor_config)
    processed_results = preprocessor.process_urls(results)

    # Convert articles to markdown
    converter_config = app_config.get_markdown_converter_config()
    converter = MarkdownConverter(**converter_config)

    # Collect articles that have content and convert to markdown
    markdown_results = []
    for result in processed_results:
        if result.get("has_article") and result.get("article"):
            markdown_content = converter.convert_article(result["article"])
            markdown_results.append(
                {
                    "url": result["url"],
                    "markdown": markdown_content,
                }
            )

    # Save markdown files to local drive
    file_writer_config = app_config.get_file_writer_config()
    file_writer = FileWriter(**file_writer_config)
    saved_files = []

    for result in markdown_results:
        filepath = file_writer.save_markdown(result["url"], result["markdown"])
        saved_files.append(filepath)

    # Show summary
    app_logger.info("")
    app_logger.info(f"{'=' * 80}")
    app_logger.info("SUMMARY")
    app_logger.info(f"{'=' * 80}")
    app_logger.info(f"Total URLs processed: {len(urls_to_fetch)}")
    app_logger.info(f"Successfully converted to markdown: {len(markdown_results)}")
    app_logger.info(f"Files saved to disk: {len(saved_files)}")
    if len(urls_to_fetch) > 0:
        app_logger.info(
            f"Success rate: {(len(markdown_results) / len(urls_to_fetch) * 100):.1f}%"
        )


async def main():
    """Main entry point with scheduler support."""

    # Initialize application-wide state
    await initialize_app()

    # Check if monitoring is enabled
    from typing import cast

    app_config = cast(Settings, config)
    monitoring_config = app_config.get_monitoring_config()
    if monitoring_config["enabled"]:
        await run_scheduler()
    else:
        # Run pipeline once
        await run_pipeline()


async def run_scheduler():
    """Run the documentation scheduler."""

    # Type casting - these are guaranteed to be initialized after initialize_app()
    from typing import cast

    app_config = cast(Settings, config)
    app_logger = cast(logging.Logger, logger)

    monitoring_config = app_config.get_monitoring_config()

    # Use sitemap URL as default if no monitoring URL is configured
    monitor_url = monitoring_config["check_url"] or app_config.sitemap.url

    app_logger.info("Starting documentation scheduler...")
    app_logger.info(f"Monitoring URL: {monitor_url}")
    app_logger.info(
        f"Check interval: {monitoring_config['check_interval_minutes']} minutes"
    )

    # Create ETag monitor
    etag_monitor = ETagMonitor(monitoring_config["etag_cache_file"])

    # Setup shutdown event
    shutdown_event = asyncio.Event()

    def signal_handler():
        app_logger.info("Received shutdown signal...")
        shutdown_event.set()

    # Setup signal handlers
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, signal_handler)

    async def check_documentation():
        """Check for documentation changes and run pipeline if needed."""
        try:
            app_logger.info("Checking for documentation changes...")
            changed = etag_monitor.has_changed(monitor_url)

            if changed:
                app_logger.info("Documentation changed - running pipeline...")
                await run_pipeline()
                app_logger.info("Pipeline completed successfully")
            else:
                app_logger.info("Documentation unchanged - skipping pipeline")
        except Exception as e:
            app_logger.error(f"Error during documentation check: {e}")
            app_logger.debug(f"Exception details: {type(e).__name__}: {e}")
            import traceback

            app_logger.debug(f"Traceback: {traceback.format_exc()}")

    # Create and configure scheduler
    scheduler = AsyncIOScheduler()

    # Add scheduled job
    scheduler.add_job(
        check_documentation,
        IntervalTrigger(minutes=monitoring_config["check_interval_minutes"]),
        id="doc_check",
        max_instances=1,
        coalesce=True,
    )

    # Start scheduler
    scheduler.start()

    # Run initial check immediately with proper exception handling
    app_logger.info("Running initial documentation check...")
    try:
        await check_documentation()
    except Exception as e:
        app_logger.error(f"Initial documentation check failed: {e}")
        app_logger.debug(f"Exception details: {type(e).__name__}: {e}")

    app_logger.info("Scheduler started. Press Ctrl+C to stop.")

    # Wait for shutdown
    await shutdown_event.wait()

    app_logger.info("Shutting down scheduler...")
    scheduler.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
