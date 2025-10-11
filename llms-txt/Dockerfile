# syntax=docker/dockerfile:1

FROM python:3.12-slim AS builder

# Copy uv binary directly
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1

WORKDIR /app

# Install dependencies first (better layer caching)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --locked --no-dev

# Copy source and install project
COPY src/ ./src/ config.toml ./ pyproject.toml ./ uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

# Install Playwright browsers
RUN PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright uv run python -m playwright install --with-deps chromium

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright

# Install only Playwright system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libnss3 libatk-bridge2.0-0 libdrm2 libxkbcommon0 libxcomposite1 \
    libxdamage1 libxrandr2 libgbm1 libxss1 libasound2 libxfixes3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create non-root user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Copy only what's needed
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --from=builder --chown=appuser:appuser /app/src /app/src
COPY --from=builder --chown=appuser:appuser /app/config.toml /app/config.toml

# Copy Playwright browsers
COPY --from=builder --chown=appuser:appuser /app/ms-playwright /app/ms-playwright

# Change ownership of app directory to appuser
RUN chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["/app/.venv/bin/python", "-m", "talkable_llm_txt"]
