"""
Tests for LLMFullTextWriter component
"""

import tempfile
from pathlib import Path

from talkable_llm_txt.llm_full_text_writer import LLMFullTextWriter


class TestLLMFullTextWriter:
    """Test cases for LLMFullTextWriter class - Happy Flow Only"""

    def test_initialization(self):
        """Test LLMFullTextWriter initialization."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(
                output_dir=temp_dir,
                filename="test-full.txt",
                include_source_urls=True,
                base_url="https://example.com",
            )

            assert writer.output_dir == Path(temp_dir)
            assert writer.filename == "test-full.txt"
            assert writer.include_source_urls is True
            assert writer.base_url == "https://example.com"
            assert writer.file_path == Path(temp_dir) / "test-full.txt"
            assert not writer.is_initialized
            assert writer.documents_written == 0

    def test_initialize_and_finalize(self):
        """Test file initialization and finalization."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(output_dir=temp_dir)

            # Test initialization
            writer.initialize()
            assert writer.is_initialized
            assert writer.file_handle is not None
            assert writer.file_path.exists()

            # Test finalization
            writer.finalize()
            assert not writer.is_initialized
            assert writer.file_handle is None

    def test_add_document_with_source_url(self):
        """Test adding a document with source URL."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(
                output_dir=temp_dir,
                include_source_urls=True,
                base_url="https://example.com",
            )
            writer.initialize()

            url = "https://example.com/docs/guide/"
            content = "# Guide\n\nThis is a guide."

            writer.add_document(url, content)
            writer.finalize()

            # Check file content
            file_content = writer.file_path.read_text(encoding="utf-8")
            assert "Guide" in file_content
            assert "This is a guide." in file_content
            assert "https://example.com/docs/guide/" in file_content
            assert writer.documents_written == 1

    def test_add_document_without_source_url(self):
        """Test adding a document without source URL."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(
                output_dir=temp_dir,
                include_source_urls=False,
            )
            writer.initialize()

            url = "https://example.com/docs/guide/"
            content = "# Guide\n\nThis is a guide."

            writer.add_document(url, content)
            writer.finalize()

            # Check file content
            file_content = writer.file_path.read_text(encoding="utf-8")
            assert "Guide" in file_content
            assert "This is a guide." in file_content
            assert "https://example.com/docs/guide/" not in file_content
            assert writer.documents_written == 1
