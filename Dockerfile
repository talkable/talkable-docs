FROM python:3.13-alpine3.21

# Install dependencies
WORKDIR /docs
ADD requirements.txt /docs
RUN python3 -m pip install -r requirements.txt

CMD if [ "$ENVIRONMENT" = "development" ]; then \
        echo "Running Sphinx in Development mode"; \
        sphinx-autobuild -b dirhtml /docs/source /docs/_build; \
    else \
        echo "Running Sphinx in Staging/Production mode"; \
        sphinx-build -b dirhtml -a -E /docs/source /docs/_build; \
    fi
