import asyncio
import logging

from talkable_llm_txt import (
    FileWriter,
    HTMLPreprocessor,
    MarkdownConverter,
    PlaywrightFetcher,
    SitemapProcessor,
)
from talkable_llm_txt.logging_config import setup_logging

# Module-level logger following official Python documentation best practices
logger = logging.getLogger(__name__)

# Configuration
MAX_URLS_TO_PROCESS = 10  # Hardcoded parameter to control how many URLs to process


async def main():
    # Setup logging first
    setup_logging()

    # Process sitemap to get URLs
    logger.info("Processing sitemap...")
    processor = SitemapProcessor("http://localhost:8080/sitemap.xml")
    logger.info(f"Found {len(processor.processed_urls)} URLs")

    # Get URLs to process (limited by MAX_URLS_TO_PROCESS)
    urls_to_fetch = [
        entry["url"] for entry in processor.processed_urls[:MAX_URLS_TO_PROCESS]
    ]
    logger.info(f"Processing first {len(urls_to_fetch)} URLs...")

    # Fetch HTML content
    fetcher = PlaywrightFetcher(max_concurrent=3)
    results = await fetcher.fetch_urls(urls_to_fetch)

    # Process HTML to extract articles
    # Extract base URL from sitemap URL for link processing
    base_url = "http://localhost:8080"  # Extract from sitemap URL dynamically
    preprocessor = HTMLPreprocessor(base_url=base_url)
    processed_results = preprocessor.process_urls(results)

    # Convert articles to markdown
    converter = MarkdownConverter()

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
    file_writer = FileWriter("output")
    saved_files = []

    for result in markdown_results:
        filepath = file_writer.save_markdown(result["url"], result["markdown"])
        saved_files.append(filepath)

    # Display final markdown results
    logger.info("")
    logger.info(f"{'=' * 80}")
    logger.info(f"MARKDOWN CONVERSION RESULTS ({len(markdown_results)} articles)")
    logger.info(f"{'=' * 80}")

    for i, result in enumerate(markdown_results, 1):
        logger.info("")
        logger.info(f"{i}. URL: {result['url']}")
        logger.info(f"{'-' * 60}")
        logger.info(result["markdown"])
        logger.info(f"{'-' * 60}")

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
