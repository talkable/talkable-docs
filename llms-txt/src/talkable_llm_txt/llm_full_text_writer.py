"""
LLM Full Text Writer Stage

This module provides the LLMFullTextWriter class for aggregating all converted
markdown content into a single llms-full.txt file with source URL tracking
and memory-efficient batch processing.
"""

import logging
from pathlib import Path
from typing import Optional

# Module-level logger following official Python documentation best practices
logger = logging.getLogger(__name__)


class LLMFullTextWriter:
    """
    Aggregates markdown content into a single LLM full text file.

    This class handles the collection and aggregation of all converted markdown
    content into a single llms-full.txt file with source URL tracking and
    memory-efficient batch processing.
    """

    DOCUMENT_START_MARKER = "<!-- DOCUMENT_START -->"
    DOCUMENT_END_MARKER = "<!-- DOCUMENT_END -->"
    SEPARATOR_LINE = "==============================================================================="

    def __init__(
        self,
        output_dir: str = "output",
        filename: str = "llms-full.txt",
        include_source_urls: bool = True,
        base_url: Optional[str] = None,
    ):
        """
        Initialize the LLM full text writer.

        Args:
            output_dir: Directory where the llms-full.txt file will be saved
            filename: Name of the aggregated file (default: "llms-full.txt")
            include_source_urls: Whether to include source URLs for each document
            base_url: Base URL for generating source markdown URLs
        """
        self.output_dir = Path(output_dir)
        self.filename = filename
        self.include_source_urls = include_source_urls
        self.base_url = base_url
        self.file_path = self.output_dir / filename
        self.file_handle = None
        self.is_initialized = False
        self.documents_written = 0

    def initialize(self) -> None:
        """Initialize the full text file for writing."""
        try:
            # Create parent directories
            self.file_path.parent.mkdir(parents=True, exist_ok=True)

            # Open file for writing (truncate existing file)
            self.file_handle = open(self.file_path, "w", encoding="utf-8")

            # Write header
            self._write_header()

            self.is_initialized = True
            logger.info(f"Initialized LLM full text file: {self.file_path}")

        except Exception as e:
            logger.error(f"Failed to initialize LLM full text file: {e}")
            raise

    def _write_header(self) -> None:
        """Write the header for the LLM full text file."""
        if self.file_handle is not None:
            self.file_handle.write("# LLM Full Text Content\n\n")
            self.file_handle.write(
                "This file contains aggregated content from all documentation pages.\n\n"
            )
            if self.include_source_urls:
                self.file_handle.write(
                    "Each document section includes the source URL for reference.\n\n"
                )
            self.file_handle.write("---\n\n")

    def add_document(
        self, url: str, markdown_content: str, relative_filepath: Optional[Path] = None
    ) -> None:
        """
        Add a document to the full text file.

        Args:
            url: Original URL of the document
            markdown_content: Converted markdown content
            relative_filepath: Relative path to the markdown file (for source URL generation)
        """
        if not self.is_initialized:
            self.initialize()

        try:
            # Generate source URL if enabled
            source_url = ""
            if self.include_source_urls:
                source_url = self._generate_source_url(url, relative_filepath)

            # Write document block
            document_block = self._format_document_block(source_url, markdown_content)

            if self.file_handle is not None:
                self.file_handle.write(document_block)
                self.documents_written += 1
                logger.debug(f"Added document to LLM full text: {url}")
            else:
                logger.error("File handle is None, cannot write document")

        except Exception as e:
            logger.error(f"Failed to add document {url} to LLM full text: {e}")
            # Continue processing other documents even if one fails

    def _generate_source_url(
        self, original_url: str, relative_filepath: Optional[Path]
    ) -> str:
        """
        Generate source URL for the markdown file.

        Args:
            original_url: Original URL of the document
            relative_filepath: Relative path to the markdown file

        Returns:
            Source URL pointing to the markdown file
        """
        if relative_filepath and self.base_url:
            # Convert relative path to URL format
            # Replace backslashes with forward slashes for URL compatibility
            relative_path_str = str(relative_filepath).replace("\\", "/")
            return f"{self.base_url}/{relative_path_str}"
        else:
            # Fallback to original URL with .md extension
            return f"{original_url}.md"

    def _format_document_block(self, source_url: str, markdown_content: str) -> str:
        """
        Format a document block with source URL and separators.

        Args:
            source_url: Source URL for the document
            markdown_content: The markdown content

        Returns:
            Formatted document block as string
        """
        block_parts = [self.DOCUMENT_START_MARKER]

        if source_url:
            block_parts.append(f"Source: {source_url}")

        block_parts.append(self.SEPARATOR_LINE)
        block_parts.append("")
        block_parts.append(markdown_content.strip())
        block_parts.append("")
        block_parts.append(self.DOCUMENT_END_MARKER)
        block_parts.append("")
        block_parts.append("")

        return "\n".join(block_parts)

    def finalize(self) -> None:
        """Finalize the full text file and write summary."""
        if not self.is_initialized:
            return

        try:
            # Write summary
            self._write_summary()

            # Close file handle
            if self.file_handle:
                self.file_handle.close()
                self.file_handle = None

            logger.info(f"Finalized LLM full text file: {self.file_path}")
            logger.info(f"Total documents written: {self.documents_written}")

        except Exception as e:
            logger.error(f"Failed to finalize LLM full text file: {e}")
            raise
        finally:
            self.is_initialized = False

    def _write_summary(self) -> None:
        """Write summary information at the end of the file."""
        if self.file_handle is not None:
            try:
                self.file_handle.write("---\n\n")
                self.file_handle.write("## Summary\n\n")
                self.file_handle.write(
                    f"Total documents aggregated: {self.documents_written}\n"
                )
                self.file_handle.write("Generated by talkable-llm-txt\n\n")
            except (ValueError, OSError) as e:
                logger.error(f"Failed to write summary: {e}")
                # Don't re-raise, just log the error

    def __enter__(self):
        """Context manager entry."""
        self.initialize()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit with cleanup."""
        if self.is_initialized:
            self.finalize()
