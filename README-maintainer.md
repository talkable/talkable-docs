# Talkable Documentation Maintenance Routine

This documentation provides instructions for maintaining the Sphinx Builder **framework** used to generate the Talkable Documentation.

It outlines the routine for maintaining the framework and associated workflows.

> [!NOTE]
> This guide does not cover updating the documentation content.
> Refer to [README.md](README.md) for details on updating the Talkable documentation source, which is available at [https://docs.talkable.com/](https://docs.talkable.com/).

## Scope

The maintenance routine includes the following tasks:

- Updating dependencies:
  - Sphinx and other Python packages (using `uv`)
  - Python container
  - Nginx container
- Adding new extensions
- Introducing Talkable-specific customizations (Python scripts)

## Preparations

1. Clone the documentation repository.

    ```bash
    git clone git@github.com:talkable/talkable-docs.git
    cd talkable-docs
    ```

2. Create a new branch from `master`.

    ```bash
    git checkout -b new-branch
    ```

3. Generate a `.env` file from the `.env.template`.

    ```bash
    cp .env.template .env
    ```

4. Ensure Docker and Docker Compose are installed and running.

    ```bash
    docker --version
    docker compose --version
    ```

## Updating Packages

The goal is to update `pyproject.toml` with the latest versions of dependencies.

1. Update dependencies using `uv`.

    ```bash
    uv add package-name  # For new packages
    uv sync --upgrade    # To upgrade existing packages
    ```

2. Build the local development container.

    ```bash
    docker compose --profile local up -d --build
    ```

    This starts the local development environment with live reloading and allows you to load the documentation at <http://localhost:8080>.

    If the documentation fails to load, check the container logs:

    ```bash
    docker compose logs -f docs-local
    ```

3. Test production build.

    Test the production build process to ensure compatibility:

    ```bash
    docker compose --profile prod build --no-cache
    ```

4. Test and lock dependencies.

    Ensure everything works as expected locally. Once confirmed, update the lock file with the latest versions:

    ```bash
    uv lock --upgrade
    ```

5. Stop the containers.

    Once the documentation is fully functional, stop the containers:

    ```bash
    docker compose down -v
    ```

6. Push the updated `pyproject.toml` and `uv.lock` to GitHub.

    Commit and push the updated dependency files for testing and production.

## Updating the Python Container

The Sphinx framework uses Python Docker images from DockerHub for both local development and production.

1. Check for the latest Python image on DockerHub: <https://hub.docker.com/_/python>.

2. Update the image name in both Dockerfiles:

   In [Dockerfile-local](./Dockerfile-local):
   ```dockerfile
   FROM python:3.12-alpine3.22
   ```

   In [Dockerfile-prod](./Dockerfile-prod):
   ```dockerfile
   FROM python:3.12-alpine3.22 AS builder
   ```

3. Test the deployment.

    Deploy the local development container to verify the updates:

    ```bash
    docker compose --profile local up -d --build
    ```

    Confirm that the documentation loads at <http://localhost:8080>.

4. Test production build.

    Test the production build process:

    ```bash
    docker compose --profile prod build --no-cache
    ```

5. Finalize the update.

    Commit the updated Dockerfiles to the repository for testing and production.

    Stop the containers:

    ```bash
    docker compose down -v
    ```

## Updating the Nginx Container

The production deployment uses Nginx to serve static content.

1. Check for the latest Nginx image on DockerHub: <https://hub.docker.com/_/nginx>.

2. Update the image name in [Dockerfile-prod](./Dockerfile-prod):

   ```dockerfile
   FROM nginx:1.29-alpine3.22
   ```

3. Test the production build:

   ```bash
   docker compose --profile prod build --no-cache
   docker compose --profile prod up -d --force-recreate
   ```

4. Finalize the update.

   Commit the updated `Dockerfile-prod` to the repository for testing and production.

   Stop the containers:

   ```bash
   docker compose down -v
   ```

## Adding New Extensions

Sphinx is a highly customizable documentation framework. You can extend its functionality with official or third-party extensions.

Here are some resources:

- <https://sphinx-extensions.readthedocs.io/en/latest/>
- <https://www.sphinx-doc.org/en/master/development/index.html>
- <https://github.com/sphinx-contrib>

To add extensions, follow these steps:

1. [Install additional Python packages](#installing-additional-packages).
2. [Adjust the conf.py file](#modifying-configuration-files).
3. Add Python scripts to the [./source/](./source/) directory if necessary.

Start by deploying the local development container:

```bash
docker compose --profile local up -d --build
```

### Currently Used Extensions

The documentation currently uses these Sphinx extensions:
- `sphinx_sitemap` - Generates sitemap.xml for SEO
- `sphinx_copybutton` - Adds copy buttons to code blocks
- `sphinx_design` - Provides advanced layout components like cards, grids, and tabs

### Installing Additional Packages

Add the package using `uv`.

```bash
uv add package-name
```

> [!NOTE]
> `uv` will automatically handle version constraints and update the lock file.

Rebuild the container after adding the package:

```bash
docker compose --profile local up -d --build
```

For production deployment, test with:

```bash
docker compose --profile prod build --no-cache
docker compose --profile prod up -d --force-recreate
```

### Modifying Configuration Files

Most changes involve editing the [./source/conf.py](./source/conf.py) file or other files in the [./source/](./source/) directory.

> [!NOTE]
> Rebuilding the container is unnecessary for changes to [./source/conf.py](./source/conf.py) or [./source/](./source/). These changes are applied automatically within 1 second when using the local development profile with `sphinx-autobuild`.

### Important Configuration Files

- **[./source/conf.py](./source/conf.py)**: Main Sphinx configuration file
- **[./source/_utils/baseurl.py](./source/_utils/baseurl.py)**: Handles environment-specific base URL configuration
- **[./pyproject.toml](./pyproject.toml)**: Python dependencies and project metadata
- **[./docker-compose.yml](./docker-compose.yml)**: Container orchestration configuration
- **[./nginx/templates/default.conf.template](./nginx/templates/default.conf.template)**: Nginx configuration for production deployments
