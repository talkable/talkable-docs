import asyncio
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from html_to_markdown import convert_to_markdown as html_to_md
from playwright.async_api import TimeoutError as PlaywrightTimeoutError
from playwright.async_api import async_playwright


def get_urls_from_sitemap(sitemap_url="https://docs.talkable.com/sitemap.xml"):
    """Extract all URLs from sitemap XML using BeautifulSoup"""
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "xml")
        urls = []

        # Find all url elements
        for url_element in soup.find_all("url"):
            loc = url_element.find("loc")
            if loc and loc.text:
                urls.append(loc.text)

        print(f"Found {len(urls)} URLs in sitemap")
        return urls

    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []


def clean_docs_directory(output_dir="docs"):
    """Clean the docs directory before processing"""
    import shutil

    docs_path = Path(output_dir)

    if docs_path.exists():
        print(f"Cleaning existing docs directory: {docs_path}")
        shutil.rmtree(docs_path)

    # Create fresh directory
    docs_path.mkdir(parents=True, exist_ok=True)
    print("Docs directory cleaned and ready")


def url_to_filepath(url, base_url="https://docs.talkable.com/"):
    """Convert URL to local file path for markdown output"""
    # Remove base URL
    relative_path = url.replace(base_url, "")

    # Handle trailing slashes - convert to .md file directly
    if relative_path.endswith("/"):
        relative_path = relative_path.rstrip("/") + ".md"
    else:
        # Remove .html extension and add .md
        relative_path = relative_path.replace(".html", ".md")

    # Handle root path
    if relative_path == "":
        relative_path = "index.md"

    return f"docs/{relative_path}"


async def fetch_live_content(url: str, timeout: int = 30000):
    """Fetch JavaScript-rendered content from live website using Playwright

    Args:
        url: URL of the page to fetch
        timeout: Navigation timeout in milliseconds (default: 30s)

    Returns:
        Rendered HTML content as string
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            context = await browser.new_context()
            try:
                page = await context.new_page()

                # Set up error handling
                def handle_page_error(exc):
                    print(f"Page error: {exc}")

                def handle_request_failed(req):
                    failure = req.failure
                    if failure:
                        error_text = (
                            failure.errorText
                            if hasattr(failure, "errorText")
                            else str(failure)
                        )
                    else:
                        error_text = "Unknown error"

                    # Suppress only .woff2 font warnings for local files
                    if ".woff2" in req.url:
                        return

                    print(f"Request failed: {req.url} - {error_text}")

                page.on("pageerror", handle_page_error)
                page.on("requestfailed", handle_request_failed)

                try:
                    # Navigate to live URL
                    await page.goto(url, wait_until="domcontentloaded", timeout=timeout)

                    # Wait for main content to be available
                    await page.wait_for_selector("article", timeout=10000)

                    # Wait for JavaScript transformations to complete (e.g., |term| to <abbr>)
                    try:
                        await page.wait_for_function(
                            """
                            () => {
                                // Check if problematic spans have been transformed to abbr elements
                                const problematicSpans = document.querySelectorAll('.problematic');
                                const hasAbbrElements = document.querySelectorAll('abbr[title]').length > 0;
                                
                                // Consider transformation complete if:
                                // 1. No problematic spans remain, OR
                                // 2. We have abbr elements (transformation happened)
                                return problematicSpans.length === 0 || hasAbbrElements;
                            }
                        """,
                            timeout=5000,
                        )
                    except Exception as e:
                        # Transformation may not be needed or timed out, continue
                        print(f"JavaScript transformation wait timed out: {e}")
                        pass

                    # Get rendered content
                    html = await page.content()
                    return html

                except PlaywrightTimeoutError as e:
                    print(f"Timeout processing {url}: {e}")
                    raise
                except Exception as e:
                    print(f"Error processing {url}: {e}")
                    raise

            finally:
                # Clean up context (closes all pages)
                await context.close()

        finally:
            # Clean up browser
            await browser.close()


def remove_unwanted_elements(soup):
    """Remove all unwanted UI elements, navigation, and hidden content"""

    # Navigation and structural elements
    nav_selectors = [
        ".toc",
        ".bd-sidenav",
        ".navbar",
        "nav",
        "header",
        "footer",
        "aside",
        ".toctree-wrapper",  # Add toctree-wrapper here
    ]

    # Interactive UI elements
    ui_selectors = [
        ".icon-tablet",
        ".btn-clipboard",
        "[data-clipboard-target]",
        ".highlight-copy-btn",
        ".copy-button",
        ".copy-to-clipboard",
        "img[alt*='Copy to clipboard']",
        "img[src*='clipboard']",
    ]

    # Hidden and accessibility elements
    hidden_selectors = [
        ".hidden",
        ".sr-only",
        "[style*='display: none']",
        "[style*='visibility: hidden']",
    ]

    # Remove all unwanted elements
    all_selectors = nav_selectors + ui_selectors + hidden_selectors
    for selector in all_selectors:
        for element in soup.select(selector):
            element.decompose()

    # Additional hidden content detection (class-based)
    for element in soup.find_all(class_=True):
        if any("hidden" in str(cls).lower() for cls in element["class"]):
            element.decompose()


def remove_header_links(soup):
    """Remove headerlink anchor elements from headings completely"""
    for headerlink in soup.select("a.headerlink"):
        headerlink.decompose()


def process_admonitions_in_soup(soup):
    """Convert HTML admonitions to blockquote format in-place"""
    admonitions = soup.find_all("div", class_="admonition")

    for admonition in admonitions:
        # Extract admonition type from CSS classes
        classes = admonition.get("class") or []
        admonition_types = [
            "note",
            "warning",
            "tip",
            "important",
            "attention",
            "caution",
            "danger",
            "error",
            "seealso",
        ]
        admonition_type = "note"  # default

        for cls in classes:
            if cls in admonition_types:
                admonition_type = cls
                break

        # Extract title from admonition-title element
        title_elem = admonition.find("p", class_="admonition-title")
        title = title_elem.get_text().strip() if title_elem else admonition_type.title()

        # Remove title from content to avoid duplication
        if title_elem:
            title_elem.decompose()

        # Get the remaining content
        content = admonition.get_text().strip()

        # Create a pre element to preserve the admonition format
        pre = soup.new_tag("pre")
        pre.string = f'!!! {admonition_type} "{title}"\n    {content}'

        # Replace the original admonition
        admonition.replace_with(pre)


def process_abbreviations_in_soup(soup):
    """Convert HTML abbreviation tags to plain text, preserving original casing"""
    # Find all abbr elements
    for abbr in soup.find_all("abbr"):
        # Get the text content (e.g., "Advocate", "Friend") preserving original case
        text_content = abbr.get_text().strip()
        
        # Replace the abbr element with plain text (no lowercase conversion)
        abbr.replace_with(text_content)


def process_html_pipeline(html):
    """Process HTML through complete pipeline: clean → transform → extract"""
    soup = BeautifulSoup(html, "html.parser")

    # Step 1: Remove unwanted elements
    remove_unwanted_elements(soup)

    # Step 2: Remove header links
    remove_header_links(soup)

    # Step 3: Process admonitions
    process_admonitions_in_soup(soup)

    # Step 4: Process abbreviations
    process_abbreviations_in_soup(soup)

    # Step 5: Extract main content
    article = soup.find("article")
    if article:
        return str(article)

    return None


def convert_to_markdown(html):
    """Convert HTML to Markdown using html-to-markdown"""
    markdown = html_to_md(
        html,
        heading_style="atx",
        strip=["nav", "header", "footer", "aside"],
        escape_asterisks=False,  # Don't escape * characters
        escape_underscores=False,  # Don't escape _ characters
        escape_misc=False,  # Don't escape miscellaneous characters
    )
    return markdown


async def process_single_url(url):
    """Process a single URL and save markdown"""
    try:
        print(f"Processing: {url}")

        # Get JavaScript-rendered content from live site
        js_content = await fetch_live_content(url)

        # Process through unified pipeline
        processed_content = process_html_pipeline(js_content)
        if not processed_content:
            print(f"Warning: No main content found in {url}")
            return None

        # Convert to markdown
        markdown_content = convert_to_markdown(processed_content)

        # Calculate output path from URL
        output_file_path = Path(url_to_filepath(url))

        # Create subdirectories if needed
        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Save markdown file
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        print(f"✓ Converted: {url} → {output_file_path}")
        return output_file_path

    except Exception as e:
        print(f"✗ Failed to process {url}: {e}")
        return None


async def process_live_website_urls(
    sitemap_url: str = "https://docs.talkable.com/sitemap.xml",
    output_dir: str = "docs",
    batch_size: int = 10,
    max_files: int | None = None,
):
    """Process live website URLs from sitemap to markdown files.

    Args:
        sitemap_url: URL of the sitemap.xml to fetch URLs from
        output_dir: Directory to store markdown files
        batch_size: Number of URLs to process per browser instance
        max_files: Maximum number of URLs to process (None for all URLs)
    """
    output_path = Path(output_dir)

    # Get URLs from sitemap
    urls = get_urls_from_sitemap(sitemap_url)

    if not urls:
        print("No URLs found in sitemap")
        return

    # Filter out non-content URLs (search, etc.)
    filtered_urls = [
        url
        for url in urls
        if not any(x in url.lower() for x in ["search", "genindex", "py-modindex"])
    ]

    # Limit to max_files if specified (for testing)
    if max_files is not None:
        filtered_urls = filtered_urls[:max_files]
        print(f"Processing {len(filtered_urls)} URLs (limited for testing)")
    else:
        print(f"Processing {len(filtered_urls)} URLs")

    # Create output directory if it doesn't exist
    output_path.mkdir(exist_ok=True)

    # Process URLs concurrently in batches to manage memory
    for i in range(0, len(filtered_urls), batch_size):
        batch = filtered_urls[i : i + batch_size]
        total_batches = (len(filtered_urls) - 1) // batch_size + 1
        print(f"Processing batch {i // batch_size + 1}/{total_batches}")

        # Process all URLs in the batch concurrently
        tasks = [process_single_url(url) for url in batch]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Handle results
        for result in results:
            if isinstance(result, Exception):
                print(f"✗ Batch processing error: {result}")
            # Success cases are already logged in process_single_url


if __name__ == "__main__":
    # Clean docs directory before processing
    clean_docs_directory("docs")

    # Process live website URLs from sitemap to markdown files
    # Set max_files to a number for testing, or None to process all URLs
    asyncio.run(
        process_live_website_urls(
            "https://docs.talkable.com/sitemap.xml", "docs", max_files=10
        )
    )
