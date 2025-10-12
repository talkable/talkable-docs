import pytest
from talkable_llm_txt import HTMLPreprocessor


class TestHeaderLinkRemoval:
    def setup_method(self):
        """Setup test instance before each test method."""
        self.processor = HTMLPreprocessor()

    @pytest.mark.parametrize("header_level", ["h1", "h2", "h3", "h4", "h5", "h6"])
    def test_remove_header_links_all_levels(self, header_level):
        """Test removing headerlinks from all header levels (h1-h6)."""
        html = f"""
        <article>
            <{header_level}>Title<a class="headerlink" href="#title">#</a></{header_level}>
            <p>Content here.</p>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert f"<{header_level}>Title</{header_level}>" in result
        assert "headerlink" not in result

    def test_remove_header_links_with_attributes(self):
        """Test removing headerlinks with various attributes."""
        html = """
        <article>
            <h1>Title<a class="headerlink" href="#title" title="Link to this heading">#</a></h1>
            <h2>Subtitle<a class="headerlink" href="#subtitle" title="Link to this subtitle">¶</a></h2>
            <p>Content here.</p>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>Title</h1>" in result
        assert "<h2>Subtitle</h2>" in result
        assert "headerlink" not in result
        assert "title=" not in result

    def test_remove_header_links_mixed_content(self):
        """Test removing headerlinks when some headers have them and others don't."""
        html = """
        <article>
            <h1>Title with link<a class="headerlink" href="#title">#</a></h1>
            <h2>Subtitle without link</h2>
            <h3>Another with link<a class="headerlink" href="#another">#</a></h3>
            <h4>Final without link</h4>
            <p>Content here.</p>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>Title with link</h1>" in result
        assert "<h2>Subtitle without link</h2>" in result
        assert "<h3>Another with link</h3>" in result
        assert "<h4>Final without link</h4>" in result
        assert "headerlink" not in result

    def test_remove_header_links_nested_elements(self):
        """Test removing headerlinks with nested elements in headers."""
        html = """
        <article>
            <h1>Title <span>with span</span><a class="headerlink" href="#title">#</a></h1>
            <h2>Subtitle <em>with emphasis</em><a class="headerlink" href="#subtitle">#</a></h2>
            <p>Content here.</p>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>Title <span>with span</span></h1>" in result
        assert "<h2>Subtitle <em>with emphasis</em></h2>" in result
        assert "headerlink" not in result
        assert "<span>with span</span>" in result
        assert "<em>with emphasis</em>" in result

    def test_remove_header_links_other_links_preserved(self):
        """Test that non-headerlink links are preserved."""
        html = """
        <article>
            <h1>Title<a class="headerlink" href="#title">#</a></h1>
            <p>Content with <a href="external-link">external link</a></p>
            <p>Another <a class="other-class" href="#other">other link</a></p>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>Title</h1>" in result
        assert "headerlink" not in result
        assert '<a href="external-link">external link</a>' in result
        assert '<a class="other-class" href="#other">other link</a>' in result

    def test_remove_header_links_complex_structure(self):
        """Test headerlink removal in complex article structure."""
        html = """
        <article>
            <section>
                <h1>Main Title<a class="headerlink" href="#main">#</a></h1>
                <div>
                    <h2>Sub Title<a class="headerlink" href="#sub">#</a></h2>
                    <p>Content here.</p>
                </div>
            </section>
            <footer>
                <h6>Footer Title<a class="headerlink" href="#footer">#</a></h6>
            </footer>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>Main Title</h1>" in result
        assert "<h2>Sub Title</h2>" in result
        assert "<h6>Footer Title</h6>" in result
        assert "headerlink" not in result
        assert "<section>" in result
        assert "<div>" in result
        assert "<footer>" in result
