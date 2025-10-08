from talkable_llm_txt import HTMLPreprocessor


class TestHeaderLinkRemoval:
    def setup_method(self):
        """Setup test instance before each test method."""
        self.processor = HTMLPreprocessor()

    def test_remove_header_links_basic_h1(self):
        """Test removing headerlink from h1 element."""
        html = """
        <article>
            <h1>Title<a class="headerlink" href="#title">#</a></h1>
            <p>Content here.</p>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>Title</h1>" in result
        assert "headerlink" not in result
        assert '<a class="headerlink"' not in result

    def test_remove_header_links_all_header_levels(self):
        """Test removing headerlinks from all header levels (h1-h6)."""
        html = """
        <article>
            <h1>H1 Title<a class="headerlink" href="#h1">#</a></h1>
            <h2>H2 Title<a class="headerlink" href="#h2">#</a></h2>
            <h3>H3 Title<a class="headerlink" href="#h3">#</a></h3>
            <h4>H4 Title<a class="headerlink" href="#h4">#</a></h4>
            <h5>H5 Title<a class="headerlink" href="#h5">#</a></h5>
            <h6>H6 Title<a class="headerlink" href="#h6">#</a></h6>
            <p>Content here.</p>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>H1 Title</h1>" in result
        assert "<h2>H2 Title</h2>" in result
        assert "<h3>H3 Title</h3>" in result
        assert "<h4>H4 Title</h4>" in result
        assert "<h5>H5 Title</h5>" in result
        assert "<h6>H6 Title</h6>" in result
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

    def test_remove_header_links_no_headerlinks(self):
        """Test article without headerlinks remains unchanged."""
        html = """
        <article>
            <h1>Regular Title</h1>
            <h2>Regular Subtitle</h2>
            <p>Content here.</p>
            <a href="regular-link">Regular Link</a>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>Regular Title</h1>" in result
        assert "<h2>Regular Subtitle</h2>" in result
        assert '<a href="regular-link">Regular Link</a>' in result

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

    def test_remove_header_links_empty_article(self):
        """Test removing headerlinks from empty article."""
        html = "<article></article>"
        result = self.processor.extract_article(html)

        assert result is not None
        assert result == "<article></article>"

    def test_remove_header_links_multiple_same_class(self):
        """Test removing multiple headerlinks with same class."""
        html = """
        <article>
            <h1>Title<a class="headerlink" href="#title">#</a></h1>
            <h1>Another Title<a class="headerlink" href="#another">#</a></h1>
            <h2>Subtitle<a class="headerlink" href="#subtitle">#</a></h2>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>Title</h1>" in result
        assert "<h1>Another Title</h1>" in result
        assert "<h2>Subtitle</h2>" in result
        assert "headerlink" not in result

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

    def test_remove_header_links_real_world_example(self):
        """Test with real-world example similar to documentation sites."""
        html = """
        <article class="bd-article">
            <span class="target" id="campaigns-campaign-types"></span>
            <section id="campaign-types">
                <h1>Campaign Types<a class="headerlink" href="#campaign-types" title="Link to this heading">#</a></h1>
                <p>Encourage customers to share with their friends from anywhere on your site.</p>
                <section id="invite">
                    <h2>Invite<a class="headerlink" href="#invite" title="Link to this heading">#</a></h2>
                    <p>Invite campaigns allow site visitors to share with their friends from anywhere on your site.</p>
                </section>
            </section>
        </article>
        """
        result = self.processor.extract_article(html)

        assert result is not None
        assert "<h1>Campaign Types</h1>" in result
        assert "<h2>Invite</h2>" in result
        assert "headerlink" not in result
        assert "title=" not in result
        assert '<span class="target" id="campaigns-campaign-types">' in result
        assert '<section id="campaign-types">' in result
        assert '<section id="invite">' in result

    def test_preprocess_article_method_directly(self):
        """Test the _preprocess_article method directly."""
        from bs4 import BeautifulSoup

        html = """
        <article>
            <h1>Title<a class="headerlink" href="#title">#</a></h1>
            <p>Content.</p>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")

        # Preprocess directly
        self.processor._preprocess_article(article)

        result = str(article)
        assert "<h1>Title</h1>" in result
        assert "headerlink" not in result

    def test_remove_header_links_method_directly(self):
        """Test the _remove_header_links method directly."""
        from bs4 import BeautifulSoup

        html = """
        <article>
            <h1>Title<a class="headerlink" href="#title">#</a></h1>
            <h2>Subtitle<a class="headerlink" href="#subtitle">#</a></h2>
        </article>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")

        # Remove header links directly
        self.processor._remove_header_links(article)

        result = str(article)
        assert "<h1>Title</h1>" in result
        assert "<h2>Subtitle</h2>" in result
        assert "headerlink" not in result
