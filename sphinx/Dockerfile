FROM python:3.12-alpine3.22

ARG MODE
ENV MODE=${MODE:-init}

RUN pip install uv

WORKDIR /docs

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

# Runtime command - autobuild for local, build once for production
CMD if [ "$MODE" = "init" ]; then \
    echo "Building init HTML..."; \
    uv run sphinx-build --builder dirhtml --write-all --fresh-env /docs/source /var/www/html; \
    else \
    echo "Starting HTML builder..."; \
    uv run sphinx-autobuild --builder dirhtml /docs/source /var/www/html; \
    fi
