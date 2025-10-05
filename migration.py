from bs4 import BeautifulSoup
from html_to_markdown import convert_to_markdown as html_to_md
from playwright.sync_api import sync_playwright


def fetch_js_content(url):
    """Fetch JavaScript-rendered content using Playwright"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            # Navigate and wait for content to load
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            page.wait_for_selector("article", timeout=10000)

            html = page.content()
            return html
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            raise
        finally:
            context.close()
            browser.close()


def extract_main_content(html):
    """Extract only main content, remove navigation/menus/footers"""
    soup = BeautifulSoup(html, "html.parser")

    # Remove toc elements and UI chrome
    unwanted_selectors = [
        ".toc", 
        ".toctree-wrapper",
        ".icon-tablet",  # Copy to clipboard buttons
        ".btn-clipboard",
        "[data-clipboard-target]",
        ".highlight-copy-btn",
        ".copy-button"
    ]

    for selector in unwanted_selectors:
        for element in soup.select(selector):
            element.decompose()

    # Return the article content or None
    article = soup.find("article")
    if article:
        return str(article)

    return None


def clean_heading_anchors(html):
    """Remove heading anchor links and UI chrome before markdown conversion"""
    soup = BeautifulSoup(html, "html.parser")

    # Remove heading anchor links
    headerlinks = soup.select("a.headerlink")
    for link in headerlinks:
        link.decompose()

    # Remove copy-to-clipboard buttons and UI chrome
    ui_selectors = [
        ".icon-tablet",
        ".btn-clipboard", 
        "[data-clipboard-target]",
        ".highlight-copy-btn",
        ".copy-button",
        ".copy-to-clipboard",
        "img[alt*='Copy to clipboard']",
        "img[src*='clipboard']"
    ]
    
    for selector in ui_selectors:
        for element in soup.select(selector):
            element.decompose()
    
    # Also remove images with base64 data URLs (likely UI icons)
    for img in soup.find_all("img"):
        src = img.get("src")
        if src and isinstance(src, str) and src.startswith("data:image/svg+xml"):
            img.decompose()

    return str(soup)


def preprocess_admonitions(html):
    """Convert HTML admonitions to blockquote format before markdown conversion"""
    soup = BeautifulSoup(html, "html.parser")

    # Find all admonition divs
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

    return str(soup)


def convert_to_markdown(html):
    """Convert HTML to Markdown using html-to-markdown with admonition support"""
    # First preprocess admonitions
    preprocessed_html = preprocess_admonitions(html)

    # Clean heading anchors
    clean_html = clean_heading_anchors(preprocessed_html)

# Convert with standard options
    markdown = html_to_md(
        clean_html,
        heading_style="atx",
        strip=["nav", "header", "footer", "aside"]
    )

    return markdown


def process_urls(urls):
    """Process list of URLs with JavaScript rendering"""
    for url in urls:
        try:
            print(f"Processing: {url}")

            # Fetch JavaScript-rendered content
            js_content = fetch_js_content(url)

            # Extract main content only
            main_content = extract_main_content(js_content)

            # Convert to Markdown
            markdown_content = convert_to_markdown(str(main_content))

            print(f"Markdown from {url}:")
            print(markdown_content)
            print("\\n\\n\\n\\n" + "=" * 80 + "\\n\\n\\n\\n")

        except Exception as e:
            print(f"Error processing {url}: {e}")


if __name__ == "__main__":
    # Example usage - replace with your actual URLs
    urls_to_process = [
        "https://docs.talkable.com/advanced_features/coupons/",
        "https://docs.talkable.com/api_v2/flow/",
        "https://docs.talkable.com/api_v2/intro/",
    ]

    process_urls(urls_to_process)
