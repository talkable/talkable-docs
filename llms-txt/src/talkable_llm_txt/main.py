import asyncio
import logging
import signal

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from talkable_llm_txt import (
    FileWriter,
    HTMLPreprocessor,
    LLMFullTextWriter,
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
    processor = SitemapProcessor(
        sitemap_url=app_config.core.get_effective_sitemap_url(), **sitemap_config
    )
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

    # Initialize components once for reuse across batches
    fetcher_config = app_config.get_playwright_fetcher_config()
    fetcher = PlaywrightFetcher(**fetcher_config)

    # Use base URL from core configuration for link processing
    preprocessor_config = app_config.get_html_preprocessor_config()
    preprocessor = HTMLPreprocessor(
        base_url=app_config.core.get_base_url_str(), **preprocessor_config
    )

    converter_config = app_config.get_markdown_converter_config()
    converter = MarkdownConverter(**converter_config)

    file_writer_config = app_config.get_file_writer_config()
    file_writer = FileWriter(**file_writer_config)

    # Initialize LLM full text writer if enabled
    llm_full_text_writer = None
    if app_config.is_llm_full_text_enabled():
        llm_full_text_config = app_config.get_llm_full_text_config()
        llm_full_text_writer = LLMFullTextWriter(**llm_full_text_config)
        app_logger.info("LLM full text generation enabled")

    # Process URLs in batches with end-to-end processing
    batch_size = app_config.processing.batch_size
    total_batches = (len(urls_to_fetch) + batch_size - 1) // batch_size

    # Track cumulative statistics
    total_processed = 0
    total_converted = 0
    total_saved = 0
    total_added_to_full_text = 0

    app_logger.info(
        f"Processing {len(urls_to_fetch)} URLs in {total_batches} batches of {batch_size}..."
    )

    for batch_num in range(total_batches):
        start_idx = batch_num * batch_size
        end_idx = min(start_idx + batch_size, len(urls_to_fetch))
        batch_urls = urls_to_fetch[start_idx:end_idx]

        app_logger.info(
            f"Processing batch {batch_num + 1}/{total_batches} ({len(batch_urls)} URLs)..."
        )

        # Fetch HTML content for this batch
        batch_results = await fetcher.fetch_urls(batch_urls)

        # Process HTML to extract articles for this batch
        batch_processed_results = preprocessor.process_urls(batch_results)

        # Convert articles to markdown and save immediately for this batch
        batch_converted = 0
        batch_saved = 0

        for result in batch_processed_results:
            total_processed += 1

            if result.get("has_article") and result.get("article"):
                # Convert to markdown
                markdown_content = converter.convert_article(result["article"])
                total_converted += 1
                batch_converted += 1

                # Save immediately
                try:
                    saved_filepath = file_writer.save_markdown(
                        result["url"], markdown_content
                    )
                    total_saved += 1
                    batch_saved += 1

                    # Add to LLM full text if enabled
                    if llm_full_text_writer:
                        try:
                            # Get relative filepath for source URL generation
                            relative_filepath = saved_filepath.relative_to(
                                file_writer.output_dir
                            )
                            llm_full_text_writer.add_document(
                                result["url"], markdown_content, relative_filepath
                            )
                            total_added_to_full_text += 1
                        except Exception as e:
                            app_logger.error(
                                f"Failed to add {result['url']} to LLM full text: {e}"
                            )

                except Exception as e:
                    app_logger.error(f"Failed to save {result['url']}: {e}")

        # Log batch completion
        app_logger.info(
            f"Batch {batch_num + 1} completed: "
            f"{batch_converted}/{len(batch_urls)} converted, "
            f"{batch_saved}/{len(batch_urls)} saved"
        )

    # Finalize LLM full text file if enabled
    if llm_full_text_writer:
        try:
            llm_full_text_writer.finalize()
            app_logger.info(
                f"LLM full text file generated with {total_added_to_full_text} documents"
            )
        except Exception as e:
            app_logger.error(f"Failed to finalize LLM full text file: {e}")

    # Show final summary
    app_logger.info("")
    app_logger.info(f"{'=' * 80}")
    app_logger.info("FINAL SUMMARY")
    app_logger.info(f"{'=' * 80}")
    app_logger.info(f"Total URLs processed: {total_processed}")
    app_logger.info(f"Successfully converted to markdown: {total_converted}")
    app_logger.info(f"Files saved to disk: {total_saved}")
    if llm_full_text_writer:
        app_logger.info(f"Documents added to LLM full text: {total_added_to_full_text}")
    if total_processed > 0:
        app_logger.info(
            f"Success rate: {(total_converted / total_processed * 100):.1f}%"
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

    # Use monitoring file URL as default if no monitoring URL is configured
    monitor_url = (
        monitoring_config["check_url"] or app_config.core.get_effective_monitoring_url()
    )

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
