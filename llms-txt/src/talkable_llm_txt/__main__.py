"""
Main entry point for talkable-llm-txt package.

This module allows the package to be run with `python -m talkable_llm_txt`.
"""

import asyncio

from talkable_llm_txt.main import main as app_main


def main():
    """Entry point for console script."""
    asyncio.run(app_main())


if __name__ == "__main__":
    main()
