# talkable-llm-txt: Documentation to Markdown Pipeline

**Purpose**: Web scraping pipeline that converts documentation websites from HTML to Markdown format for LLM training/consumption. Supports both one-time processing and scheduled monitoring with automatic change detection.

## Core Functionality

Processes sitemaps to discover documentation URLs, fetches HTML content using Playwright (JavaScript-rendered pages), extracts articles, converts to clean Markdown, and saves locally. Configurable via TOML file.

**Key Features:**

- **Dual Mode**: One-time processing OR scheduled monitoring
- **ETag Change Detection**: Efficient monitoring using HTTP ETag headers
- **Concurrent Processing**: High-performance parallel URL fetching (1-10 simultaneous)
- **Resource Optimization**: Configurable blocking of images, media, fonts, stylesheets, scripts
- **Flexible Output**: URL-based directory structure, configurable markdown styles

## Architecture

**Modular pipeline components:**

- **Settings** (`config.py`): Pydantic-based configuration with TOML support
- **SitemapProcessor** (`sitemap_processor.py`): XML sitemap parsing with retry logic
- **PlaywrightFetcher** (`playwright_fetcher.py`): Async HTML fetching with JS rendering
- **HTMLPreprocessor** (`html_preprocessor.py`): Article content extraction and filtering
- **MarkdownConverter** (`markdown_converter.py`): HTML to Markdown conversion
- **FileWriter** (`file_writer.py`): Local filesystem operations
- **ETagMonitor** (`etag_monitor.py`): Change detection and caching
- **URLProcessor** (`url_processor.py`): URL processing utilities

## Entry Points & Execution Flow

### **Main Entry Point** (`main.py`)

Two execution modes controlled by configuration:

1. **One-time Pipeline**: Process sitemap → fetch URLs → extract → convert → save
2. **Scheduled Monitoring**: Run scheduler → periodic ETag checks → trigger pipeline on changes

### **Package Entry Point** (`__main__.py`)

Run with `python -m talkable_llm_txt`

### **Application Flow**

1. `initialize_app()` - Setup module-level config and logging
2. Load configuration from `config.toml`
3. Based on monitoring setting: run pipeline once OR start scheduler
4. Pipeline: sitemap → fetch → extract → convert → save → summary

## Project Structure

```bash
src/talkable_llm_txt/
├── __init__.py              # Package exports
├── __main__.py              # Package entry point
├── config.py                # Configuration management
├── main.py                  # Main orchestration and scheduling
├── sitemap_processor.py     # Sitemap parsing
├── playwright_fetcher.py    # HTML fetching
├── html_preprocessor.py     # Content extraction
├── url_processor.py         # URL utilities
├── markdown_converter.py    # HTML→Markdown conversion
├── file_writer.py           # File operations
├── etag_monitor.py          # Change detection
└── logging_config.py        # Logging setup

tests/                      # Test suite (unit, integration, slow)
```

## Configuration System

**config.toml groups:**

- **Core**: Sitemap URL, output directory
- **Processing**: URL limits, concurrency, batch size, timeouts
- **Content**: Image handling, heading styles
- **Performance**: Page load conditions, resource blocking
- **Sitemap Fetching**: Timeouts, retries, user agent
- **Monitoring**: Scheduling, ETag cache, intervals (1-1440 minutes)
- **Logging**: Log levels and output

**Key features:**

- Monitoring enable/disable control
- ETag-based change detection with persistent cache
- Flexible scheduling intervals
- Resource optimization for performance

## Development Environment

**Setup:**

- **Package Manager**: `uv` for Python dependency management
- **Python Version**: 3.12+
- **Key Dependencies**: APScheduler, BeautifulSoup4, html-to-markdown, Playwright, Pydantic-Settings, requests, toml
- **Testing**: pytest with asyncio, test markers (unit, integration, slow)
- **Code Quality**: ruff (linting/formatting), Pyright (type checking)

**Architecture Patterns:**

- **Module-Level State**: Application-wide config and logging variables
- **Async/Await**: Full async pipeline for concurrency
- **Type Safety**: Comprehensive type hints with Pyright
- **Error Handling**: Specific exception types with robust fallbacks

## Quick Start

```bash
# Installation
make install                    # Install deps, package, Playwright browsers

# Configuration
cp config.toml.template config.toml
nano config.toml                # Edit sitemap URL and settings

# Development
make test                      # Run tests
make lint-fix                  # Auto-fix and format code
make typecheck                 # Type checking
make check                     # Run all checks

# Execution
make run                       # Start application (monitoring mode by default)
uv run talkable_llm_txt     # Direct execution
```

## Usage Examples

**One-time processing:**

```bash
# Set monitoring.enabled = false in config.toml
python -m talkable_llm_txt
```

**Scheduled monitoring:**

```bash
# Set monitoring.enabled = true in config.toml (default)
python -m talkable_llm_txt
# Runs scheduler, checks every 60 minutes (configurable)
```

## Testing Strategy

- **Unit Tests**: Individual component testing
- **Integration Tests**: End-to-end pipeline testing  
- **Slow Tests**: Network-dependent tests (use `-m "not slow"` to skip)
- **Component Coverage**: All major components including ETag monitoring

## Recent Architecture Changes

**Module-Level State Management:**

- `config` and `logger` are module-level variables
- Clean function signatures (no parameter passing for shared state)
- `initialize_app()` handles centralized setup
- Type casting ensures static type checking

**Configuration Separation:**

- `Settings.create()` handles pure configuration loading
- Logging setup happens independently after config loading
- Clear separation of concerns

## Extensibility

**Extension points:**

- Custom processors for different documentation formats
- Alternative fetchers for various web technologies
- Specialized markdown converters
- Monitoring plugins for different change detection strategies
- Additional output formats

The modular architecture supports easy extension while maintaining clean separation of concerns.
