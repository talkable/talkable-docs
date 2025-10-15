FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production

# Install system dependencies for Playwright
RUN apt update && apt install -y --no-install-recommends \
    libnss3 libatk-bridge2.0-0 libdrm2 libxkbcommon0 libxcomposite1 \
    libxdamage1 libxrandr2 libgbm1 libxss1 libasound2 libxfixes3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install Python dependencies
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv && \
    uv sync --locked --no-dev

# Install Playwright browsers
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
