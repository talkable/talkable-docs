"""
Logging configuration for talkable_llm_txt package.

This module provides centralized logging configuration that works in both
terminal and Docker environments, following official Python documentation
best practices.
"""

import logging
import os
import sys


def setup_logging(level: str = "INFO"):
    """Configure logging for both terminal and Docker environments.

    Detects if running in Docker and adjusts formatting accordingly.
    Uses stdout for Docker compatibility and accepts log level parameter.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        logging.Logger: Configured root logger instance
    """
    # Detect Docker environment
    is_docker = os.path.exists("/.dockerenv") or os.environ.get("DOCKER_CONTAINER")

    # Use provided level, fallback to environment variable, then default to INFO
    if level:
        level = level.upper()
    else:
        level = os.environ.get("LOG_LEVEL", "INFO").upper()

    # Validate log level
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    if level not in valid_levels:
        level = "INFO"

    # Create appropriate formatter based on environment
    if is_docker:
        # Simple format for Docker logs
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
    else:
        # Richer format for terminal development
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)-8s %(message)s", datefmt="%H:%M:%S"
        )

    # Create handler with stdout for Docker compatibility
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(level)

    # Clear existing handlers to avoid duplicates
    logger.handlers = []

    # Add our configured handler
    logger.addHandler(handler)

    return logger
