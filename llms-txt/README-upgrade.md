# Maintainer Guide

This guide provides instructions for upgrading dependencies and testing the talkable-llm-txt package.

## Install UV

```bash
# Install UV using Homebrew
brew install uv
```

## Setup Virtual Environment

```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

## Upgrade Dependencies

```bash
# Check current lockfile status
uv lock --check

# Upgrade all dependencies to latest compatible versions
uv lock --upgrade

# Or upgrade specific package
uv lock --upgrade-package package_name

# Sync environment after lockfile changes
uv sync
```

## Configure Application

Before running the application, configure the base URL in `config.toml`:

```bash
# Copy template configuration
cp config.toml.template config.toml

# Edit config file to set base URL
# For production: base_url = "https://docs.talkable.com"
# For staging: base_url = "https://staging-docs.talkable.com"
nano config.toml
```

## Test Application

```bash
# Run the application to test functionality
uv run python -m talkable_llm_txt

# Verify output files are generated
ls -la output/
```

Check that the following files are generated:

- Markdown files in URL-based directory structure
- `llms-full.txt` aggregated content file
- Proper conversion of documentation pages

## Commit Changes

```bash
# Commit updated dependencies
git add uv.lock pyproject.toml
git commit -m "chore: upgrade dependencies"
```
