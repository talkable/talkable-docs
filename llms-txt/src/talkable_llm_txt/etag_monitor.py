"""
ETag monitoring for documentation changes.

This module provides ETag-based change detection for monitoring
documentation URLs for changes.
"""

import json
import logging
from pathlib import Path

import requests
from requests.exceptions import ConnectionError, HTTPError, RequestException, Timeout

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
        stored_etag = self._cache.get(url)
        headers = {"If-None-Match": stored_etag} if stored_etag else {}

        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()  # Raise HTTPError for bad status codes

            if response.status_code == 304:
                logger.info(f"Documentation unchanged: {url}")
                return False
            elif response.status_code == 200:
                new_etag = response.headers.get("etag")
                if new_etag:
                    self._cache[url] = new_etag
                    self._save_cache()
                    logger.info(f"Documentation changed: {url}")
                    return True
                else:
                    logger.warning(f"No ETag header for: {url}")
                    return True  # Assume changed if no ETag
            else:
                logger.error(f"Unexpected status {response.status_code} for {url}")
                return False

        except ConnectionError as e:
            logger.error(f"Connection error checking {url}: {e}")
            return False
        except Timeout as e:
            logger.error(f"Timeout checking {url}: {e}")
            return False
        except HTTPError as e:
            logger.error(f"HTTP error checking {url}: {e}")
            return False
        except RequestException as e:
            logger.error(f"Request error checking {url}: {e}")
            return False
        except (OSError, IOError) as e:
            logger.error(f"File system error checking {url}: {e}")
            return False
