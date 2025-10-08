import pytest
from bs4 import BeautifulSoup
from html_preprocessor import HTMLPreprocessor


class TestCopyButtonRemoval:
    """Test cases for copy button removal functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.preprocessor = HTMLPreprocessor()

    def test_remove_copy_buttons_basic(self):
        """Test basic copy button removal."""
        html = """
        <article>
            <p>Some content</p>
            <button class="copybtn o-tooltip--left" data-clipboard-target="#code0">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <p>More content</p>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        
        self.preprocessor._remove_copy_buttons(article)
        
        copy_buttons = article.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0

    def test_remove_multiple_copy_buttons(self):
        """Test removal of multiple copy buttons."""
        html = """
        <article>
            <button class="copybtn" data-clipboard-target="#code0">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <button class="copybtn" data-clipboard-target="#code1">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <button class="copybtn" data-clipboard-target="#code2">
                <svg><title>Copy to clipboard</title></svg>
            </button>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        
        self.preprocessor._remove_copy_buttons(article)
        
        copy_buttons = article.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0

    def test_preserve_other_buttons(self):
        """Test that non-copy buttons are preserved."""
        html = """
        <article>
            <button class="copybtn" data-clipboard-target="#code0">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <button class="other-button">Click me</button>
            <button class="btn btn-primary">Save</button>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        
        self.preprocessor._remove_copy_buttons(article)
        
        copy_buttons = article.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0
        
        other_buttons = article.find_all("button", class_=lambda x: x and "copybtn" not in str(x))
        assert len(other_buttons) == 2

    def test_preserve_other_elements(self):
        """Test that other elements are preserved during copy button removal."""
        html = """
        <article>
            <h1>Title</h1>
            <p>Paragraph content</p>
            <div class="highlight">
                <pre>Code here</pre>
                <button class="copybtn" data-clipboard-target="#code0">
                    <svg><title>Copy to clipboard</title></svg>
                </button>
            </div>
            <p>More content</p>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        
        original_h1 = article.find("h1")
        original_p = article.find("p")
        original_div = article.find("div", class_="highlight")
        original_pre = article.find("pre")
        
        self.preprocessor._remove_copy_buttons(article)
        
        # Check that other elements are preserved
        assert article.find("h1") == original_h1
        assert len(article.find_all("p")) == 2
        assert article.find("div", class_="highlight") == original_div
        assert article.find("pre") == original_pre
        
        # Check that copy button is removed
        copy_buttons = article.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0

    def test_no_copy_buttons_present(self):
        """Test behavior when no copy buttons are present."""
        html = """
        <article>
            <h1>Title</h1>
            <p>Content without copy buttons</p>
            <button class="regular-button">Click me</button>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        
        original_content = str(article)
        
        self.preprocessor._remove_copy_buttons(article)
        
        # Content should remain unchanged
        assert str(article) == original_content

    def test_copy_button_with_various_classes(self):
        """Test removal of copy buttons with various class combinations."""
        html = """
        <article>
            <button class="copybtn o-tooltip--left" data-clipboard-target="#code0">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <button class="copybtn another-class" data-clipboard-target="#code1">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <button class="some-class copybtn more-classes" data-clipboard-target="#code2">
                <svg><title>Copy to clipboard</title></svg>
            </button>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        
        self.preprocessor._remove_copy_buttons(article)
        
        copy_buttons = article.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0

    def test_real_world_copy_button_structure(self):
        """Test with the actual copy button structure found in the investigation."""
        html = """
        <article>
            <div class="highlight">
                <pre>some code</pre>
                <button class="copybtn o-tooltip--left" data-clipboard-target="#codecell0" data-tooltip="Copy">
                    <svg class="icon icon-tabler icon-tabler-copy" fill="none" height="44" stroke="#000000" 
                         stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewbox="0 0 24 24" 
                         width="44" xmlns="http://www.w3.org/2000/svg">
                        <title>Copy to clipboard</title>
                        <path d="M0 0h24v24H0z" fill="none" stroke="none"></path>
                        <rect height="12" rx="2" width="12" x="8" y="8"></rect>
                        <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
                    </svg>
                </button>
            </div>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        
        self.preprocessor._remove_copy_buttons(article)
        
        copy_buttons = article.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0
        
        # Check that the highlight div and pre are preserved
        assert article.find("div", class_="highlight") is not None
        assert article.find("pre") is not None

    def test_integration_with_preprocess_article(self):
        """Test that copy button removal is integrated into the main preprocessing pipeline."""
        html = """
        <article>
            <h1>Title <a class="headerlink" href="#title">¶</a></h1>
            <p>Content</p>
            <button class="copybtn" data-clipboard-target="#code0">
                <svg><title>Copy to clipboard</title></svg>
            </button>
        </article>
        """
        result = self.preprocessor.extract_article(html)
        
        assert result is not None
        
        result_soup = BeautifulSoup(result, "html.parser")
        
        # Both header links and copy buttons should be removed
        header_links = result_soup.find_all("a", class_="headerlink")
        copy_buttons = result_soup.find_all("button", class_="copybtn")
        
        assert len(header_links) == 0
        assert len(copy_buttons) == 0
        
        # Other content should be preserved
        assert result_soup.find("h1") is not None
        assert result_soup.find("p") is not None

    def test_empty_article(self):
        """Test copy button removal on empty article."""
        html = "<article></article>"
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        
        # Should not raise any errors
        self.preprocessor._remove_copy_buttons(article)
        
        copy_buttons = article.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0

    def test_nested_copy_buttons(self):
        """Test removal of copy buttons nested in complex structures."""
        html = """
        <article>
            <div class="content">
                <div class="code-block">
                    <div class="highlight">
                        <pre>code content</pre>
                        <button class="copybtn" data-clipboard-target="#nested">
                            <svg><title>Copy to clipboard</title></svg>
                        </button>
                    </div>
                </div>
            </div>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        
        self.preprocessor._remove_copy_buttons(article)
        
        copy_buttons = article.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0
        
        # Nested structure should be preserved
        assert article.find("div", class_="content") is not None
        assert article.find("div", class_="code-block") is not None
        assert article.find("div", class_="highlight") is not None
        assert article.find("pre") is not None