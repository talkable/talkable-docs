import asyncio
import logging
from urllib.parse import urlparse

from talkable_llm_txt import (
    FileWriter,
    HTMLPreprocessor,
    MarkdownConverter,
    PlaywrightFetcher,
    SitemapProcessor,
)
from talkable_llm_txt.config import Settings
from talkable_llm_txt.logging_config import setup_logging

# Module-level logger following official Python documentation best practices
logger = logging.getLogger(__name__)


async def main():
    """Main application entry point with configuration management."""

    # Load configuration from TOML file
    try:
        config = Settings.load_from_toml()
        logger.info("Configuration loaded from config.toml")
    except FileNotFoundError as e:
        logger.error(f"Configuration file not found: {e}")
        raise
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        raise

    # Setup logging with configuration
    logging_config = config.get_logging_config()
    setup_logging(level=logging_config["level"])

    # Process sitemap to get URLs
    logger.info("Processing sitemap...")
    sitemap_config = config.get_sitemap_processor_config()
    processor = SitemapProcessor(sitemap_url=config.sitemap.url, **sitemap_config)
    logger.info(f"Found {len(processor.processed_urls)} URLs")

    # Get URLs to process (limited by configuration or all if None)
    if config.processing.max_urls_to_process is None:
        # Process all URLs found in sitemap
        urls_to_fetch = [entry["url"] for entry in processor.processed_urls]
        logger.info(f"Processing all {len(urls_to_fetch)} URLs found in sitemap...")
    else:
        # Process limited number of URLs
        urls_to_fetch = [
            entry["url"]
            for entry in processor.processed_urls[
                : config.processing.max_urls_to_process
            ]
        ]
        logger.info(f"Processing first {len(urls_to_fetch)} URLs...")

    # Fetch HTML content
    fetcher_config = config.get_playwright_fetcher_config()
    fetcher = PlaywrightFetcher(**fetcher_config)
    results = await fetcher.fetch_urls(urls_to_fetch)

    # Process HTML to extract articles
    # Extract base URL from sitemap URL for link processing
    parsed_url = urlparse(config.sitemap.url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    preprocessor_config = config.get_html_preprocessor_config()
    preprocessor = HTMLPreprocessor(base_url=base_url, **preprocessor_config)
    processed_results = preprocessor.process_urls(results)

    # Convert articles to markdown
    converter_config = config.get_markdown_converter_config()
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
    file_writer_config = config.get_file_writer_config()
    file_writer = FileWriter(**file_writer_config)
    saved_files = []

    for result in markdown_results:
        filepath = file_writer.save_markdown(result["url"], result["markdown"])
        saved_files.append(filepath)

    # Show summary
    logger.info("")
    logger.info(f"{'=' * 80}")
    logger.info("SUMMARY")
    logger.info(f"{'=' * 80}")
    logger.info(f"Total URLs processed: {len(urls_to_fetch)}")
    logger.info(f"Successfully converted to markdown: {len(markdown_results)}")
    logger.info(f"Files saved to disk: {len(saved_files)}")
    if len(urls_to_fetch) > 0:
        logger.info(
            f"Success rate: {(len(markdown_results) / len(urls_to_fetch) * 100):.1f}%"
        )


if __name__ == "__main__":
    asyncio.run(main())
