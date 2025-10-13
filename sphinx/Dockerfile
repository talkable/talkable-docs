FROM python:3.12-alpine3.22

ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT:-production}

RUN pip install uv

WORKDIR /docs

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

# Runtime command - autobuild for local, build once for production
CMD if [ "$ENVIRONMENT" = "local" ]; then \
        uv run sphinx-autobuild --builder dirhtml /docs/source /var/www/html; \
    else \
        echo "Building production HTML..."; \
        uv run sphinx-build --builder dirhtml --write-all --fresh-env /docs/source /var/www/html; \
        echo "Production build complete - serving static files from /var/www/html"; \
        sleep infinity; \
    fi
