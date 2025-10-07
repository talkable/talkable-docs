# Talkable Documentation

## Overview

The Talkable documentation stack is a containerized system that uses Docker to simplify deployment and management. It is designed to generate, serve, and manage static documentation across multiple environments, such as staging and production.

## Key Features

1. **Containerized Components**:

   - **Sphinx (Local Development)**: Uses `docker-compose-local.yml` with `sphinx-autobuild` for live reloading, serving on port 8000. Mounts source directory for real-time updates.
   - **Nginx (Production)**: Uses `docker-compose.yml` with multi-stage build to serve static HTML files, manage URL redirection, and dynamically serve environment-specific `robots.txt` files.
   - **Multi-stage Build**: Production builds use a builder stage with Python/UV to generate static HTML files, then copies them to the Nginx stage for serving.

2. **Environment-Specific Behavior**:

   - Configured via a `.env` file for flexibility.
   - Supports dynamic environment-specific behavior, such as serving different `robots.txt` files based on the `ENVIRONMENT` variable.
   - Uses separate Docker Compose files for different deployment scenarios (`docker-compose-local.yml` for development, `docker-compose.yml` for staging/production).
   - `ENVIRONMENT` variable is used for all deployments including local development, with fallback to `production` if not specified.

3. **Efficient Architecture**:

   - Deployed on Amazon AWS Virtual Private Servers (VPS) with an AWS load balancer directing user traffic to the appropriate environment.
   - Multi-stage Docker build process generates static content during build time, eliminating the need for runtime content generation.
   - Uses `uv` for fast Python dependency management and builds.
   - Platform-specific builds targeting `linux/arm64/v8` architecture for consistency across deployment environments.

## Deployment Process

### Prerequisites

- Ensure Docker and Docker Compose are installed on the target VPS.
- Clone the repository containing the stack configuration.

### Steps

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:talkable/talkable-docs.git
   ```

2. **Switch to the Appropriate Branch**:

   - Use the `master` branch for production.

     ```bash
     git checkout master
     ```

   - Use the `staging` branch for staging.

     ```bash
     git checkout staging
     ```

3. **Create and Configure the `.env` File**:

   - Copy `.env.template` to `.env`:

     ```bash
     cp .env.template .env
     ```

   - Update the following variables:
       - **`ENVIRONMENT`**: Set to `staging`, `production`, or `local`. Falls back to `production` if no value provided.
       - **`LOCAL_PORT`**: Adjust if the default port (`8080`) is already in use.
  
4. **Deploy the Stack**:

   For local development:

   ```bash
   docker compose -f docker-compose-local.yml up -d --build
   ```

   For production or staging deployment:

   ```bash
   docker compose -f docker-compose.yml build --no-cache
   docker compose -f docker-compose.yml up -d --force-recreate
   ```

## Environment-Specific Configuration

### Handling `robots.txt`

- The repository includes separate `robots.txt` files for each environment (`production.txt`, `staging.txt`).
- The correct file is dynamically selected based on the `ENVIRONMENT` variable via Nginx template:

  ```nginx
  location = /robots.txt {
      alias /var/www/${ENVIRONMENT}.txt;
      access_log off;
      log_not_found off;
  }
  ```

- Nginx serves the file at `/var/www/${ENVIRONMENT}.txt` in response to `robots.txt` requests.

## Build Process and Data Management

- **Multi-stage Build (Production Only)**:

  - Builder stage uses Python 3.12 with `uv` to generate static HTML files from source documentation using `sphinx-build`.
  - Generated files are copied to the Nginx stage during the build process.
  - No runtime content generation required.
  - Local development uses single-stage build with live reloading capabilities.

- **Dependency Management**:
  - Uses `uv` for fast Python dependency management.
  - Dependencies are defined in `pyproject.toml` and locked in `uv.lock`.
  - Build arguments pass `ENVIRONMENT` variable to the build process.
  - Local development uses `Dockerfile-local` with `sphinx-autobuild` for live reloading and source volume mounting.
  - Production uses `Dockerfile` with multi-stage build for optimized static content generation.
