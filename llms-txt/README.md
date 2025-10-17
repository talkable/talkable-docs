# talkable-llm-txt

Documentation processing pipeline that converts Talkable documentation websites to Markdown format for AI agent consumption. Generates comprehensive `llm.txt` files and all corresponding documentation assets required for AI agents to effectively read and understand Talkable documentation.

## 🚀 Local Development Setup

### Prerequisites

- **Docker** (required for Playwright browser installation)
- **uv** package manager (installs its own Python, no system Python needed)

### Quick Start

```bash
# Navigate to the llms-txt directory
cd llms-txt

# Install dependencies and Playwright browsers
make install

# Configure the application
cp config.toml.template config.toml
# Edit config.toml with your settings

# Run the application
make run
```

## 🎯 Key Features

- **JavaScript-Rendered Content**: Uses Playwright to fetch fully rendered HTML pages
- **Flexible Sitemap Processing**: Separate sitemap URL configuration for URL discovery
- **Concurrent Processing**: High-performance parallel URL fetching
- **Resource Optimization**: Configurable blocking of images, media, fonts, stylesheets, scripts
- **ETag-based Change Detection**: Efficient monitoring using HTTP ETag headers with configurable files
- **Scheduled Monitoring**: Automatic periodic checks with configurable intervals (1 minute to 24 hours)

## 🛠️ Technology Stack

### Core Dependencies

- **Playwright** (`>=1.55.0`): Browser automation for JavaScript-rendered content, installed as Python dependency
- **BeautifulSoup4** (`>=4.14.2`): HTML parsing and content extraction
- **html-to-markdown** (`>=4.14.2`): HTML to Markdown conversion
- **APScheduler** (`>=3.11.0`): Scheduled task execution
- **Pydantic** (`>=2.12.0`): Configuration management and validation

### Playwright Integration

Following official best practices, Playwright is installed as a Python dependency within the virtual environment:

- **Virtual Environment Installation**: Via `uv` package manager
- **Browser Management**: Separate installation using `playwright install --with-deps`
- **System Dependencies**: Automatically handled by the `--with-deps` flag
- **Browser Support**: Chromium for content extraction

## ⚙️ Configuration

The package uses a comprehensive configuration system managed through `config.toml` with a template provided at `config.toml.template`.

### Configuration Management

- **Config File**: Copy `config.toml.template` to `config.toml` and modify settings
- **Environment Variables**: Override any setting using `LLMS_TXT_<SECTION>__<SETTING>` format
- **Defaults**: Automatic fallback to default values when no configuration is provided

### Key Configuration Sections

- **Core**: Base URL, sitemap URL, output directory, monitoring file (default: `searchindex.js`)
- **Processing**: Concurrency limits, batch sizes, timeouts
- **Performance**: Page load conditions, resource blocking
- **Monitoring**: Scheduling, ETag cache, intervals (1-1440 minutes)
- **Content**: Image handling, markdown formatting

## 📋 Development Commands

All development operations are managed through the Makefile:

```bash
make install          # Install deps, package, and Playwright browsers
make run              # Run the application (monitoring mode)
make monitor          # Run the documentation scheduler (alias for run)
make test             # Run tests
make fmt              # Format Python code with ruff
make lint             # Run ruff linting
make lint-fix         # Auto-fix linting issues and format code
make typecheck        # Run Pyright type checking
make check            # Run all checks (lint-fix + typecheck + test)
make clean            # Clean build artifacts and cache files
make help             # Show all available commands
```

## 🧪 Testing

The project includes comprehensive test coverage with different test categories:

- **Unit Tests**: Individual component testing
- **Integration Tests**: End-to-end pipeline testing
- **Slow Tests**: Network-dependent tests

All testing is done through the Makefile commands to ensure consistency.

## 🔧 Development Workflow

1. **Setup**: Run `make install` to install dependencies and Playwright browsers
2. **Configure**: Copy and edit `config.toml.template`
3. **Develop**: Make changes to source code
4. **Test**: Run `make check` to run all quality checks
5. **Run**: Use `make run` to test the application locally

## 📚 Architecture

### Modular Pipeline Components

- **Settings** (`config.py`): Pydantic-based configuration with TOML support
- **SitemapProcessor** (`sitemap_processor.py`): XML sitemap parsing with retry logic
- **PlaywrightFetcher** (`playwright_fetcher.py`): Async HTML fetching with JS rendering
- **HTMLPreprocessor** (`html_preprocessor.py`): Article content extraction and filtering
- **MarkdownConverter** (`markdown_converter.py`): HTML to Markdown conversion
- **FileWriter** (`file_writer.py`): Local filesystem operations
- **ETagMonitor** (`etag_monitor.py`): Change detection and caching
- **URLProcessor** (`url_processor.py`): URL processing utilities

### Monitoring and Change Detection

- **ETag Headers**: Efficient HTTP-based change detection
- **Configurable Monitoring Files**: Default `searchindex.js` for Sphinx sites
- **Persistent Cache**: JSON-based ETag cache for reliability
- **Flexible Scheduling**: Configurable intervals from 1 minute to 24 hours

## 🌐 Integration

This package is part of the overall Talkable documentation deployment system. For Docker deployment details and infrastructure setup, please refer to the documentation at the upper level of this repository.

## 🤝 Contributing

When contributing to this project:

1. Follow the existing code style (enforced by `ruff`)
2. Add type hints (checked by `pyright`)
3. Write tests for new functionality
4. Update documentation as needed
5. Ensure all checks pass with `make check`

## 📄 License

This project is part of the Talkable documentation system. See the main repository for license information.
