.PHONY: help install fmt lint lint-fix typecheck typecheck-watch test check clean

.DEFAULT_GOAL := help

help: ## Show this help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies via uv, install package in editable mode, and install Playwright browsers with system dependencies
	uv sync
	uv pip install -e .
	uv run playwright install --with-deps chromium

fmt: ## Format Python code with ruff
	uv run ruff format .

lint: ## Run ruff linting
	uv run ruff check .

lint-fix: ## Auto-fix linting issues and format code
	uv run ruff check --fix .
	uv run ruff format .

typecheck: ## Run Pyright type checking (PyLance equivalent)
	uv run pyright

typecheck-watch: ## Run Pyright in watch mode for continuous checking
	uv run pyright --watch

test: ## Run tests with pytest
	uv run pytest

run: ## Run the documentation processor (monitoring enabled by default)
	uv run python -m talkable_llm_txt

monitor: ## Run the documentation scheduler (alias for run command)
	uv run python -m talkable_llm_txt

check: lint-fix typecheck test ## Run all checks (lint-fix + typecheck + test)

.PHONY: clean
clean: ## Clean build artifacts and cache files
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -type d -exec rm -rf {} +
	rm -rf .coverage
	rm -rf .venv/
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .pyright_cache/
	rm -rf output/
	rm -f etag_cache.json
