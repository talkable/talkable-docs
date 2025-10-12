import logging
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

# Module-level logger following official Python documentation best practices
logger = logging.getLogger(__name__)


class FileWriter:
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)

    def url_to_filepath(self, url: str) -> Path:
        """Convert URL to local file path preserving structure"""
        parsed = urlparse(url)
        path = parsed.path.rstrip("/")  # Remove trailing slash

        # Handle root path
        if not path or path == "/":
            path = "/index"

        # Convert URL path to local path
        relative_path = unquote(path) + ".md"

        # Sanitize filename
        relative_path = self._sanitize_path(relative_path)

        return self.output_dir / relative_path.lstrip("/")

    def _sanitize_path(self, path: str) -> str:
        """Sanitize path for cross-platform compatibility"""
        # Replace invalid characters (always sanitize for maximum compatibility)
        invalid_chars = r'[<>:"|?*]'
        sanitized = re.sub(invalid_chars, "_", path)
        return sanitized

    def save_markdown(self, url: str, content: str) -> Path:
        """Save markdown content to file preserving URL structure"""
        filepath = self.url_to_filepath(url)

        # Create parent directories
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        filepath.write_text(content, encoding="utf-8")
        logger.info(f"Saved: {filepath}")

        return filepath
