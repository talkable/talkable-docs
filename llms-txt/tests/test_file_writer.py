import pytest
from pathlib import Path
from talkable_llm_txt.file_writer import FileWriter
import tempfile
import shutil


class TestFileWriter:
    def setup_method(self):
        """Setup temporary directory for each test"""
        self.temp_dir = tempfile.mkdtemp()
        self.file_writer = FileWriter(self.temp_dir)

    def teardown_method(self):
        """Clean up temporary directory after each test"""
        shutil.rmtree(self.temp_dir)

    def test_url_to_filepath_simple(self):
        """Test simple URL to filepath conversion"""
        url = "http://example.com/path/to/page"
        expected = Path(self.temp_dir) / "path" / "to" / "page.md"
        result = self.file_writer.url_to_filepath(url)
        assert result == expected

    def test_url_to_filepath_root(self):
        """Test root URL conversion"""
        url = "http://example.com/"
        expected = Path(self.temp_dir) / "index.md"
        result = self.file_writer.url_to_filepath(url)
        assert result == expected

    def test_url_to_filepath_trailing_slash(self):
        """Test URL with trailing slash"""
        url = "http://example.com/path/to/page/"
        expected = Path(self.temp_dir) / "path" / "to" / "page.md"
        result = self.file_writer.url_to_filepath(url)
        assert result == expected

    def test_url_to_filepath_with_query_params(self):
        """Test URL with query parameters"""
        url = "http://example.com/path/to/page?param=value&other=123"
        expected = Path(self.temp_dir) / "path" / "to" / "page.md"
        result = self.file_writer.url_to_filepath(url)
        assert result == expected

    def test_url_to_filepath_with_encoded_chars(self):
        """Test URL with URL-encoded characters"""
        url = "http://example.com/path%20with%20spaces/file%20name"
        expected = Path(self.temp_dir) / "path with spaces" / "file name.md"
        result = self.file_writer.url_to_filepath(url)
        assert result == expected

    def test_save_markdown_creates_directories(self):
        """Test that save_markdown creates parent directories"""
        url = "http://example.com/deep/nested/path/file"
        content = "# Test Content\n\nThis is test content."

        result = self.file_writer.save_markdown(url, content)

        # Verify file was created
        assert result.exists()
        assert result.is_file()

        # Verify content is correct
        assert result.read_text(encoding="utf-8") == content

        # Verify directory structure was created
        assert result.parent.exists()
        assert result.parent.is_dir()

    def test_save_markdown_overwrites_existing(self):
        """Test that save_markdown overwrites existing files"""
        url = "http://example.com/test/file"
        content1 = "# First Content"
        content2 = "# Second Content"

        # Save first content
        result1 = self.file_writer.save_markdown(url, content1)
        assert result1.read_text(encoding="utf-8") == content1

        # Save second content (should overwrite)
        result2 = self.file_writer.save_markdown(url, content2)
        assert result2 == result1  # Same path
        assert result2.read_text(encoding="utf-8") == content2

    def test_sanitize_path_invalid_chars(self):
        """Test path sanitization with invalid characters"""
        # Test with characters that are invalid on Windows
        path_with_invalid = "path<>:with|invalid?*chars"
        sanitized = self.file_writer._sanitize_path(path_with_invalid)

        # Should replace invalid chars with underscores
        assert "<" not in sanitized
        assert ">" not in sanitized
        assert ":" not in sanitized or Path().anchor != "\\"  # Allow colon on Unix
        assert "|" not in sanitized
        assert "?" not in sanitized
        assert "*" not in sanitized

    def test_complex_url_structure(self):
        """Test complex URL structure similar to real documentation"""
        url = "http://localhost:8080/advanced_features/customer_service_portal/use_case_1/"
        expected = (
            Path(self.temp_dir)
            / "advanced_features"
            / "customer_service_portal"
            / "use_case_1.md"
        )
        result = self.file_writer.url_to_filepath(url)
        assert result == expected
