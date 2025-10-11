"""
Main entry point for talkable-llm-txt package.

This module allows the package to be run with `python -m talkable_llm_txt`.
"""

import asyncio
from talkable_llm_txt.main import main

if __name__ == "__main__":
    asyncio.run(main())
