# Talkable Documentation Deployment Guide

## 1. Overview

This guide explains the deployment architecture and procedures for the Talkable Documentation system. The documentation platform consists of three main components working together to serve both human-readable HTML documentation and AI-friendly markdown content in staging and production environments.

## 2. System Components

### 2.1 Nginx

**Role**: Web server and reverse proxy that serves the generated documentation files.

**Configuration and Purpose**:

- Serves HTML documentation from `/var/www/html`
- Serves markdown files for AI consumption from `/var/www/md`
- Uses shared volume `docs_www` for content storage
- Handles URL rewriting and redirects
- Provides security headers and gzip compression
- Serves environment-specific robots.txt files
- Configured via `nginx/templates/default.conf.template`

### 2.2 Sphinx Builder

**Role**: Converts reStructuredText (`.rst`) source files into HTML documentation.

**Static Mode Operation**:

- Runs once during deployment to generate HTML files
- Source files located in `source/` directory
- Built using Docker image from `sphinx/Dockerfile`
- Container exits after successful build (restart: "no")
- Uses `service_completed_successfully` dependency pattern

### 2.3 LLMS-TXT Builder

**Role**: Converts HTML documentation into markdown format optimized for AI/LLM consumption.

**Static Mode Operation**:

- Runs once during deployment to generate markdown files
- Generates `llms.txt` and `llms-full.txt` files
- Built using Docker image from `llms-txt/Dockerfile`
- Container exits after successful conversion (restart: "no")
- Waits for Sphinx to complete successfully before starting

## 3. Deployment Mode

### Static Mode

**Description**: Builders run once per deployment to generate static files, then terminate.

**Deployment Process**:

1. `docs-sphinx-{ENVIRONMENT}` container builds HTML documentation
2. `docs-llms-txt-{ENVIRONMENT}` container waits for Sphinx completion, then converts HTML to markdown
3. Both builder containers exit after successful completion
4. `docs-nginx-{ENVIRONMENT}` serves the generated static files continuously

## 4. Environment Setup

### 4.1 Environment Files

**Critical Requirement**: Each deployment environment (staging, production) requires a dedicated `.env` file with specific configuration. Using the wrong environment file will cause broken links, incorrect URLs, and deployment failures.

**Required Variables**:

```bash
# Port for Nginx to serve documentation
LOCAL_PORT=8080

# Environment type: staging or production
ENVIRONMENT=production

# Base URL used in sitemaps and internal linking
# Production: https://docs.talkable.com/
# Staging: https://docs.bastion.talkable.com/
BASE_URL=https://docs.talkable.com/
```

**Security Considerations**:

- Never commit `.env` files to version control
- Use `.env.template` as the base for creating environment-specific files
- Ensure `BASE_URL` matches the actual accessible URL for each environment
- Verify `ENVIRONMENT` value matches the deployment target

### 4.2 Prerequisites

**System Requirements**:

- Docker and Docker Compose installed
- Git for repository management
- SSH access for remote deployments
- Sufficient disk space for Docker images and volumes

**Dependencies**:

- All dependencies are containerized in Docker images
- Images are built from `sphinx/Dockerfile` and `llms-txt/Dockerfile`
- Platform: `linux/arm64/v8` (specified in common configuration)
- Shared volume: `docs_www` for HTML and markdown output

## 5. Deployment Procedure

### 5.1 Environment Preparation

**Creating Environment-Specific .env File**:

1. Copy the template: `cp .env.template .env`
2. Configure variables for your target environment:
   - **Staging**: Set `ENVIRONMENT=staging` and `BASE_URL=https://docs.bastion.talkable.com/`
   - **Production**: Set `ENVIRONMENT=production` and `BASE_URL=https://docs.talkable.com/`

**Environment Variable Configuration**:

- Verify `LOCAL_PORT` is available on the target system
- Ensure `BASE_URL` is accessible from the deployment environment
- Double-check `ENVIRONMENT` value matches the deployment target

### 5.2 Manual Deployment (Alternative)

For manual deployment or troubleshooting:

```bash
# Set environment variables
export ENVIRONMENT=production
export BASE_URL=https://docs.talkable.com/
export LOCAL_PORT=8080

# Deploy using only base compose file (production)
docker compose -f docker-compose.yml up -d --force-recreate
```

**Important**: Production deployment uses only `docker-compose.yml` (no override files).

### 5.3 Deploy Using Deployment Script

Identical for staging and production

> [!NOTE]
> While the deployment script and installation approach are identical for both environments, they use different Git branches:
>
> - **Production**: Uses the `master` branch
> - **Staging**: Uses the `staging` branch

```bash
./deploy/deploy.sh deploy
```

This script automatically:

- Checks CI status for successful builds
- SSHs to the target environment
- Pulls latest code changes
- Builds Docker images with `--no-cache`
- Starts services with `docker compose -f docker-compose.yml up -d --force-recreate`

**Verification Steps**:

1. Check container status: `docker compose ps`
2. Verify Nginx is serving content: `curl -I https://docs.talkable.com/`
3. Check logs for errors: `docker compose logs`
4. Test documentation accessibility in browser
5. Verify `llms.txt` endpoint: `curl https://docs.talkable.com/llms.txt`
6. Confirm builder containers exited successfully: `docker compose ps -a`

### 5.4 Dependency Management

**Service Dependencies in Production**:

The production deployment uses Docker Compose's `service_completed_successfully` dependency pattern:

```yaml
services:
  llms-txt:
    depends_on:
      sphinx:
        condition: service_completed_successfully
      nginx:
        condition: service_started
```

**Deployment Sequence**:

1. **Nginx starts** immediately (service_started dependency)
2. **Sphinx builds** HTML documentation and exits with code 0
3. **LLM's TXT waits** for Sphinx to complete successfully
4. **LLM's TXT processes** the generated HTML and exits
5. **Nginx continues** serving the static files

This ensures reliable build order and prevents race conditions.

### 5.5 Environment-Specific Notes

**Staging Environment**:

- URL: `https://docs.bastion.talkable.com/`
- Uses staging robots.txt file
- Ideal for pre-production testing
- May have different content versions than production

**Production Environment**:

- URL: `https://docs.talkable.com/`
- Uses production robots.txt file
- Requires careful testing before deployment
- Serves as the official documentation source
- Higher availability and performance requirements
