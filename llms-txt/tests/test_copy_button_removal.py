import pytest
from bs4 import BeautifulSoup
from talkable_llm_txt import HTMLPreprocessor


class TestCopyButtonRemoval:
    """Test cases for copy button removal functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.preprocessor = HTMLPreprocessor()

    def test_extract_article_removes_copy_buttons(self):
        """Test that extract_article removes copy buttons."""
        html = """
        <article>
            <p>Some content</p>
            <button class="copybtn o-tooltip--left" data-clipboard-target="#code0">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <p>More content</p>
        </article>
        """
        result = self.preprocessor.extract_article(html)

        assert result is not None
        result_soup = BeautifulSoup(result, "html.parser")

        copy_buttons = result_soup.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0
        assert result_soup.find("p") is not None

    @pytest.mark.parametrize(
        "copy_button_class",
        [
            "copybtn",
            "copybtn o-tooltip--left",
            "copybtn another-class",
            "some-class copybtn more-classes",
        ],
    )
    def test_extract_article_removes_various_copy_button_classes(
        self, copy_button_class
    ):
        """Test that extract_article removes copy buttons with various class combinations."""
        html = f"""
        <article>
            <button class="{copy_button_class}" data-clipboard-target="#code0">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <p>Content</p>
        </article>
        """
        result = self.preprocessor.extract_article(html)

        assert result is not None
        result_soup = BeautifulSoup(result, "html.parser")

        copy_buttons = result_soup.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0
        assert result_soup.find("p") is not None

    def test_extract_article_preserves_non_copy_buttons(self):
        """Test that extract_article preserves non-copy buttons."""
        html = """
        <article>
            <button class="copybtn" data-clipboard-target="#code0">
                <svg><title>Copy to clipboard</title></svg>
            </button>
            <button class="other-button">Click me</button>
            <button class="btn btn-primary">Save</button>
            <p>Content</p>
        </article>
        """
        result = self.preprocessor.extract_article(html)

        assert result is not None
        result_soup = BeautifulSoup(result, "html.parser")

        copy_buttons = result_soup.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0

        other_buttons = result_soup.find_all("button")
        assert len(other_buttons) == 2
        assert result_soup.find("p") is not None

    def test_extract_article_integration_with_header_links(self):
        """Test that extract_article removes both copy buttons and header links."""
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

        header_links = result_soup.find_all("a", class_="headerlink")
        copy_buttons = result_soup.find_all("button", class_="copybtn")

        assert len(header_links) == 0
        assert len(copy_buttons) == 0
        assert result_soup.find("h1") is not None
        assert result_soup.find("p") is not None

    def test_extract_article_real_world_copy_button_structure(self):
        """Test with real-world copy button structure."""
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
        result = self.preprocessor.extract_article(html)

        assert result is not None
        result_soup = BeautifulSoup(result, "html.parser")

        copy_buttons = result_soup.find_all("button", class_="copybtn")
        assert len(copy_buttons) == 0

        assert result_soup.find("div", class_="highlight") is not None
        assert result_soup.find("pre") is not None
