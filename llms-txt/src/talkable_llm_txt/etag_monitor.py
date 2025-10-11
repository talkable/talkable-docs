"""
ETag monitoring for documentation changes.

This module provides ETag-based change detection for monitoring
documentation URLs for changes.
"""

import json
import logging
from pathlib import Path

import requests

logger = logging.getLogger(__name__)


class ETagMonitor:
    """
    ETag monitor for documentation URL.
    """

    def __init__(self, cache_file: str = "etag_cache.json"):
        self.cache_file = Path(cache_file)
        self._cache = self._load_cache()

    def _load_cache(self) -> dict:
        """Load ETag cache from file."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}

    def _save_cache(self) -> None:
        """Save ETag cache to file."""
        with open(self.cache_file, "w") as f:
            json.dump(self._cache, f, indent=2)

    def has_changed(self, url: str) -> bool:
        """
        Check if URL has changed using ETag.

        Returns True if changed, False if unchanged.
        """
        logger.info(f"DEBUG: ETagMonitor.has_changed() called for URL: {url}")
        stored_etag = self._cache.get(url)
        logger.info(f"DEBUG: Stored ETag: {stored_etag}")
        headers = {"If-None-Match": stored_etag} if stored_etag else {}
        logger.info(f"DEBUG: Request headers: {headers}")

        try:
            logger.info(f"DEBUG: Making HTTP request to {url}...")
            response = requests.get(url, headers=headers, timeout=30)
            logger.info(f"DEBUG: Got response with status: {response.status_code}")

            if response.status_code == 304:
                logger.info(f"Documentation unchanged: {url}")
                logger.info(f"DEBUG: Returning False (unchanged)")
                return False
            elif response.status_code == 200:
                new_etag = response.headers.get("etag")
                logger.info(f"DEBUG: New ETag from response: {new_etag}")
                if new_etag:
                    self._cache[url] = new_etag
                    self._save_cache()
                    logger.info(f"Documentation changed: {url}")
                    logger.info(f"DEBUG: Returning True (changed)")
                    return True
                else:
                    logger.warning(f"No ETag header for: {url}")
                    logger.info(f"DEBUG: Returning True (no ETag, assume changed)")
                    return True  # Assume changed if no ETag
            else:
                logger.error(f"Unexpected status {response.status_code} for {url}")
                logger.info(f"DEBUG: Returning False (error)")
                return False

        except Exception as e:
            logger.error(f"Error checking {url}: {e}")
            logger.info(f"DEBUG: Exception in has_changed, returning False")
            return False
