# Sphinx Dependencies

This folder contains Python dependencies for the Sphinx framework and is used purely to maintain the dependencies for the documentation build system.

## Purpose

- Manages Sphinx framework dependencies
- Isolated dependency management for documentation builds
- Version control of Python packages via `uv.lock`

## Setup

### Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

### Install Dependencies

```bash
# Install dependencies using uv
uv sync
```

## Upgrade Dependencies

To upgrade all dependencies to their latest versions:

```bash
# Update dependencies to latest versions
uv lock --upgrade

# Install updated dependencies
uv sync
```

To upgrade specific packages:

```bash
# Update specific package
uv add package_name@latest

# Or update multiple packages
uv add package1@latest package2@latest
```

## Testing

**Important:** Final testing should be done by deploying the whole setup from the root of the repository, not from this folder.

This folder only manages dependencies - the actual Sphinx documentation build and testing should be performed from the project root where the main documentation configuration and source files are located.

## Files

- `pyproject.toml` - Project dependencies configuration
- `uv.lock` - Locked dependency versions
- `.python-version` - Python version specification (3.12)
- `.envrc` - Environment setup for automatic activation
