FROM python:3.13-alpine3.22

# Install dependencies
WORKDIR /docs
ADD requirements.txt /docs
RUN python3 -m pip install -r requirements.txt

CMD if [ "$ENVIRONMENT" = "development" ]; then \
        echo "Running Sphinx in Development mode"; \
        sphinx-autobuild --builder dirhtml /docs/source /docs/_build; \
    else \
        echo "Running Sphinx in Staging/Production mode"; \
        sphinx-build --builder dirhtml --write-all --fresh-env /docs/source /docs/_build; \
    fi
