"""
pytest configuration and fixtures for talkable_llm_txt tests
"""

from pathlib import Path
from unittest.mock import Mock

import pytest


@pytest.fixture
def sample_sitemap_xml():
    """Load real sitemap XML from file for testing."""
    fixture_path = Path(__file__).parent / "fixtures" / "xml" / "sample_sitemap.xml"
    with open(fixture_path, "r", encoding="utf-8") as f:
        return f.read()


@pytest.fixture
def sample_html_response():
    """Load real HTML response from file for testing."""
    fixture_path = Path(__file__).parent / "fixtures" / "html" / "sample_response.html"
    with open(fixture_path, "r", encoding="utf-8") as f:
        return f.read()


@pytest.fixture
def mock_sitemap_response(sample_sitemap_xml):
    """Mock sitemap XML response using real data"""
    mock_response = Mock()
    mock_response.text = sample_sitemap_xml
    mock_response.raise_for_status.return_value = None
    return mock_response


@pytest.fixture
def mock_sitemap_index_response():
    """Mock sitemap index response with child sitemaps"""
    sitemap_index_xml = """<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <sitemap>
        <loc>http://localhost:8080/sitemap-pages.xml</loc>
    </sitemap>
    <sitemap>
        <loc>http://localhost:8080/sitemap-docs.xml</loc>
    </sitemap>
</sitemapindex>"""

    mock_response = Mock()
    mock_response.text = sitemap_index_xml
    mock_response.raise_for_status.return_value = None
    return mock_response


@pytest.fixture
def mock_child_sitemap_response():
    """Mock child sitemap response"""
    child_sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>http://localhost:8080/docs/guide/</loc>
    </url>
    <url>
        <loc>http://localhost:8080/docs/api/</loc>
    </url>
</urlset>"""

    mock_response = Mock()
    mock_response.text = child_sitemap_xml
    mock_response.raise_for_status.return_value = None
    return mock_response


@pytest.fixture
def mock_html_response(sample_html_response):
    """Mock HTML response for PlaywrightFetcher tests using real data"""
    mock_response = Mock()
    mock_response.text = sample_html_response
    mock_response.status_code = 200
    mock_response.headers = {"content-type": "text/html"}
    return mock_response


@pytest.fixture
def mock_requests_session(mocker):
    """Mock requests.Session for SitemapProcessor tests"""
    mock_session = Mock()
    mock_session.headers = {}
    mock_session.get.return_value.raise_for_status.return_value = None
    return mock_session


@pytest.fixture
def mock_playwright_page(mocker):
    """Mock Playwright page for PlaywrightFetcher tests"""
    mock_page = Mock()
    mock_page.goto.return_value = None
    mock_page.content.return_value = """<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <main>
        <h1>Test Content</h1>
        <p>This is test content.</p>
    </main>
</body>
</html>"""
    mock_page.close.return_value = None
    return mock_page


@pytest.fixture(autouse=True)
def no_external_requests(monkeypatch):
    """Prevent external network requests during testing to ensure local fixtures are used"""
    # Only block actual external requests, not mocked ones
    original_get = __import__("requests").Session.get

    def checked_get(self, *args, **kwargs):
        # Allow calls that are already mocked (will have different call patterns)
        if hasattr(self, "_mock_name") or hasattr(original_get, "_mock_name"):
            return original_get(self, *args, **kwargs)

        # Block actual external requests to localhost/external domains
        url = args[0] if args else kwargs.get("url", "")
        if url and (url.startswith("http://localhost") or url.startswith("https://")):
            raise RuntimeError(
                f"External network request to {url} blocked during testing. Use local fixtures instead."
            )

        return original_get(self, *args, **kwargs)

    monkeypatch.setattr("requests.Session.get", checked_get)
