FROM python:3.12-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production
ENV DEBIAN_FRONTEND=noninteractive

# Install minimal system dependencies (Playwright will install browser-specific deps via --with-deps)
# Following official Playwright Docker documentation
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install Python dependencies
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv && \
    uv sync --locked --no-dev

# Install Playwright browsers with system dependencies (official approach)
RUN PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright uv run python -m playwright install --with-deps chromium

ENV PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright

# Runtime command - run once for production, monitor for local
CMD if [ "$ENVIRONMENT" = "local" ]; then \
    echo "Starting LLM TXT builder with monitoring..."; \
    export LLMS_TXT_MONITORING__ENABLED="true"; \
    uv run talkable-llm-txt; \
    else \
    echo "Running LLM TXT builder once..."; \
    export LLMS_TXT_MONITORING__ENABLED="false"; \
    uv run talkable-llm-txt; \
    fi
