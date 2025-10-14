# Talkable Documentation Deployment Guide

## 1. Overview

This guide explains the deployment architecture and procedures for the Talkable Documentation system. The documentation platform consists of three main components working together to serve both human-readable HTML documentation and AI-friendly markdown content in staging and production environments.

## 2. System Components

### 2.1 Nginx

**Role**: Web server and reverse proxy that serves the generated documentation files.

**Configuration and Purpose**:

- Serves HTML documentation from `/var/www/html`
- Serves markdown files for AI consumption from `/var/www/md`
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
- Container exits after successful build

### 2.3 LLMS-TXT Builder

**Role**: Converts HTML documentation into markdown format optimized for AI/LLM consumption.

**Static Mode Operation**:

- Runs once during deployment to generate markdown files
- Generates `llms.txt` and `llms-full.txt` files
- Built using Docker image from `llms-txt/Dockerfile`
- Container exits after successful conversion

## 3. Deployment Mode

### Static Mode

**Description**: Builders run once per deployment to generate static files, then terminate.

**Deployment Process**:

1. `sphinx-init` container builds initial HTML documentation
2. `llms-txt-init` container converts HTML to markdown
3. Both containers exit after completion
4. Nginx serves the generated static files continuously

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

### Deploy Using Deployment Script

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
- Starts services with `docker up -d --force-recreate`

**Verification Steps**:

1. Check container status: `docker ps`
2. Verify Nginx is serving content: `curl -I https://docs.talkable.com/`
3. Check logs for errors: `docker logs`
4. Test documentation accessibility in browser
5. Verify `llms.txt` endpoint: `curl https://docs.talkable.com/llms.txt`

### 5.3 Environment-Specific Notes

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
