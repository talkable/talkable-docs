# Talkable Documentation Maintenance Routine

This documentation provides instructions for maintaining the Sphinx Builder **framework** used to generate the Talkable Documentation.

It outlines the routine for maintaining the framework and associated workflows.

> [!NOTE]
> This guide does not cover updating the documentation content. 
> Refer to [README.md](README.md) for details on updating the Talkable documentation source, which is available at [https://docs.talkable.com/](https://docs.talkable.com/).

## Scope

The maintenance routine includes the following tasks:

- Updating dependencies:
  - Sphinx and other Python packages
  - Python container
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

## Updating Packages

The goal is to update `requirements.txt` with the latest versions of dependencies.

1. Replace `requirements.txt` with the `packages.txt` file.

    ```bash
    cp packages.txt requirements.txt
    ```

2. Build the Sphinx container.

    ```bash
    docker compose up -d --build
    ```

    This starts the framework and allows you to load the documentation at http://localhost:8080.

    If the documentation fails to load, check the container logs:

    ```bash
    docker logs -f docs-sphinx-development
    ```

3. Test and freeze `requirements.txt`.

    Ensure everything works as expected locally. Once confirmed, update `requirements.txt` to include all installed dependencies with their versions.

    Save the dependencies with the following command:

    ```bash
    docker exec docs-sphinx-development pip freeze > requirements.txt
    ```

4. Stop the containers.

    Once the documentation is fully functional, stop the containers:

    ```bash
    docker compose down -v
    ```

5. Push the updated `requirements.txt` to GitHub.

    Commit and push the updated `requirements.txt` for testing and production.

## Updating the Python Container

The Sphinx framework uses a Python Docker image from DockerHub.

1. Check for the latest Python image on DockerHub: https://hub.docker.com/_/python.

2. Update the image name in the [Dockerfile](./Dockerfile):

    ```dockerfile
    FROM python:3.13-alpine3.21
    ```

3. Test the deployment.

    Deploy the Sphinx container to verify the updates:

    ```bash
    docker compose up -d --build
    ```

    Confirm that the documentation loads at http://localhost:8080.

4. Finalize the update.

    Commit the updated `Dockerfile` to the repository for testing and production.

    Stop the containers:

    ```bash
    docker compose down -v
    ```

## Adding New Extensions

Sphinx is a highly customizable documentation framework. You can extend its functionality with official or third-party extensions.

Here are some resources:

- https://sphinx-extensions.readthedocs.io/en/latest/
- https://www.sphinx-doc.org/en/master/development/index.html
- https://github.com/sphinx-contrib

To add extensions, follow these steps:

1. [Install additional Python packages](#installing-additional-packages).
2. [Adjust the conf.py file](#modifying-configuration-files).
3. Add Python scripts to the [./source/](./source/) directory if necessary.

Start by deploying the framework container:

```bash
docker compose up -d --build
```

### Installing Additional Packages

Add the package to `requirements.txt`.

Append the package name to `requirements.txt` (version specification is optional at this stage).

> [!NOTE]
>
> Version pinning can be done later.

Rebuild the container after modifying `requirements.txt`:

```bash
docker compose up -d --build
```

### Modifying Configuration Files

Most changes involve editing the [./source/conf.py](./source/conf.py) file or other files in the [./source/](./source/) directory.

> [!NOTE]
>
> Rebuilding the container is unnecessary for changes to [./source/conf.py](./source/conf.py) or [./source/](./source/). These changes are applied automatically within 1 second.
