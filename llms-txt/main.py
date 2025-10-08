import asyncio

from html_preprocessor import HTMLPreprocessor
from markdown_converter import MarkdownConverter
from playwright_fetcher import PlaywrightFetcher
from sitemap_processor import SitemapProcessor

# Configuration
MAX_URLS_TO_PROCESS = 10  # Hardcoded parameter to control how many URLs to process


async def main():
    # Process sitemap to get URLs
    print("Processing sitemap...")
    processor = SitemapProcessor("http://localhost:8080/sitemap.xml")
    print(f"Found {len(processor.processed_urls)} URLs")

    # Get URLs to process (limited by MAX_URLS_TO_PROCESS)
    urls_to_fetch = [
        entry["url"] for entry in processor.processed_urls[:MAX_URLS_TO_PROCESS]
    ]
    print(f"Processing first {len(urls_to_fetch)} URLs...")

    # Fetch HTML content
    fetcher = PlaywrightFetcher(max_concurrent=3)
    results = await fetcher.fetch_urls(urls_to_fetch)

    # Process HTML to extract articles
    preprocessor = HTMLPreprocessor()
    processed_results = preprocessor.process_urls(results)

    # Convert articles to markdown
    converter = MarkdownConverter()

    # Collect articles that have content and convert to markdown
    markdown_results = []
    for result in processed_results:
        if result.get("has_article") and result.get("article"):
            markdown_content = converter.convert_article(result["article"])
            markdown_results.append(
                {"url": result["url"], "markdown": markdown_content}
            )

    # Display final markdown results
    print(f"\n{'=' * 80}")
    print(f"MARKDOWN CONVERSION RESULTS ({len(markdown_results)} articles)")
    print(f"{'=' * 80}")

    for i, result in enumerate(markdown_results, 1):
        print(f"\n{i}. URL: {result['url']}")
        print(f"{'-' * 60}")
        print(result["markdown"])
        print(f"{'-' * 60}")

    # Show summary
    print(f"\n{'=' * 80}")
    print("SUMMARY")
    print(f"{'=' * 80}")
    print(f"Total URLs processed: {len(urls_to_fetch)}")
    print(f"Successfully converted to markdown: {len(markdown_results)}")
    if len(urls_to_fetch) > 0:
        print(
            f"Success rate: {(len(markdown_results) / len(urls_to_fetch) * 100):.1f}%"
        )


if __name__ == "__main__":
    asyncio.run(main())
