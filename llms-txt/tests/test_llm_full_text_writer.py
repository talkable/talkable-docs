"""
Tests for LLMFullTextWriter component.
"""

import tempfile
from pathlib import Path


from talkable_llm_txt.llm_full_text_writer import LLMFullTextWriter


class TestLLMFullTextWriter:
    """Test cases for LLMFullTextWriter class."""

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

            with writer:
                # Add document with relative filepath
                relative_path = Path("docs/test.md")
                writer.add_document(
                    url="https://example.com/docs/test",
                    markdown_content="# Test Document\n\nThis is test content.",
                    relative_filepath=relative_path,
                )

                assert writer.documents_written == 1

            # Check file content
            content = writer.file_path.read_text(encoding="utf-8")
            assert "Source: https://example.com/docs/test.md" in content
            assert "# Test Document" in content
            assert "This is test content." in content
            assert "<!-- DOCUMENT_START -->" in content
            assert "<!-- DOCUMENT_END -->" in content

    def test_add_document_without_source_url(self):
        """Test adding a document without source URL."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(output_dir=temp_dir, include_source_urls=False)

            with writer:
                writer.add_document(
                    url="https://example.com/docs/test",
                    markdown_content="# Test Document\n\nThis is test content.",
                )

                assert writer.documents_written == 1

            # Check file content
            content = writer.file_path.read_text(encoding="utf-8")
            assert "Source:" not in content
            assert "# Test Document" in content
            assert "This is test content." in content

    def test_source_url_fallback(self):
        """Test source URL fallback when no relative filepath provided."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(
                output_dir=temp_dir,
                include_source_urls=True,
                base_url="https://example.com",
            )

            with writer:
                # Add document without relative filepath
                writer.add_document(
                    url="https://example.com/docs/test",
                    markdown_content="# Test Document",
                )

                assert writer.documents_written == 1

            # Check file content - should use fallback URL
            content = writer.file_path.read_text(encoding="utf-8")
            assert "Source: https://example.com/docs/test.md" in content

    def test_multiple_documents(self):
        """Test adding multiple documents."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(output_dir=temp_dir)

            with writer:
                # Add multiple documents
                for i in range(3):
                    writer.add_document(
                        url=f"https://example.com/docs/test{i}",
                        markdown_content=f"# Document {i}\n\nContent for document {i}.",
                    )

                assert writer.documents_written == 3

            # Check file content
            content = writer.file_path.read_text(encoding="utf-8")
            assert "Document 0" in content
            assert "Document 1" in content
            assert "Document 2" in content
            assert content.count("<!-- DOCUMENT_START -->") == 3
            assert content.count("<!-- DOCUMENT_END -->") == 3

    def test_context_manager(self):
        """Test using LLMFullTextWriter as context manager."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(output_dir=temp_dir)

            with writer as w:
                assert w is writer
                assert w.is_initialized
                w.add_document(
                    url="https://example.com/test", markdown_content="# Test"
                )

            # After context manager, should be finalized
            assert not writer.is_initialized
            assert writer.file_path.exists()

    def test_error_handling(self):
        """Test error handling during document addition."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(output_dir=temp_dir)

            with writer:
                # Add a valid document first
                writer.add_document(
                    url="https://example.com/test1", markdown_content="# Valid Document"
                )

                # Simulate an error by closing the file handle
                if writer.file_handle is not None:
                    writer.file_handle.close()

                # Try to add another document - should not raise exception
                writer.add_document(
                    url="https://example.com/test2",
                    markdown_content="# Invalid Document",
                )

                # Should still have 1 document (the first one)
                assert writer.documents_written == 1

    def test_summary_generation(self):
        """Test summary generation at the end of file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = LLMFullTextWriter(output_dir=temp_dir)

            with writer:
                writer.add_document(
                    url="https://example.com/test", markdown_content="# Test Document"
                )

            # Check summary content
            content = writer.file_path.read_text(encoding="utf-8")
            assert "## Summary" in content
            assert "Total documents aggregated: 1" in content
            assert "Generated by talkable-llm-txt" in content
