# Use the official Python 3.13 Alpine image as the base
FROM python:3.13-alpine3.21

# Set environment variables to prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    git

# Install Sphinx and common dependencies
RUN pip install --upgrade pip && \
    pip install sphinx sphinx_rtd_theme myst_parser

# Create and set the working directory
WORKDIR /docs

# Copy documentation source files into the container
COPY . /docs

# Default command to build the Sphinx documentation
CMD ["sphinx-build", "-b", "html", ".", "_build"]