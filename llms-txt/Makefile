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

check: lint-fix typecheck test ## Run all checks (lint-fix + typecheck + test)

clean: ## Clean build artifacts and cache files
	rm -rf .venv
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	find . -type d -name .pytest_cache -delete
	find . -type d -name .ruff_cache -delete
	find . -type d -name .pyright_cache -delete