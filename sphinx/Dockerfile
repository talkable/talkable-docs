FROM python:3.12-alpine3.22

ENV ENVIRONMENT=production

RUN pip install uv

WORKDIR /docs

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

# Runtime command - autobuild for local, build once for production
CMD if [ "$ENVIRONMENT" = "local" ]; then \
    echo "Starting HTML builder..."; \
    uv run sphinx-autobuild --builder dirhtml /docs/source /var/www/html; \
    else \
    echo "Building init HTML..."; \
    uv run sphinx-build --builder dirhtml --write-all --fresh-env /docs/source /var/www/html; \
    fi
