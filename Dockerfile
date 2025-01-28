FROM python:3.13-alpine3.21

WORKDIR /docs

ADD requirements.txt /docs
RUN python3 -m pip install -r requirements.txt

RUN apk add --no-cache \
    # gcc \
    # musl-dev \
    # libffi-dev \
    # openssl-dev \
    # make
    nginx

# Create necessary directories for Nginx
RUN mkdir -p /run/nginx

CMD if [ "$ENVIRONMENT" = "development" ]; then \
        echo "Running Sphinx in Development mode"; \
        sphinx-autobuild -b dirhtml --port 8000 --host 0.0.0.0 /docs/source /docs/_build; \
    else \
        echo "Running Sphinx in Staging/Production mode"; \
        sphinx-build -b dirhtml /docs/source /var/www/html; \
        echo "Starting Nginx"; \
        nginx -g "daemon off;"; \
    fi
