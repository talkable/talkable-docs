# Talkable Documentation

## Overview

This repository contains the Talkable documentation - a comprehensive set of articles describing Talkable's capabilities, publicly available at [docs.talkable.com](https://docs.talkable.com).

The documentation is built using [Sphinx](https://www.sphinx-doc.org) with [reStructuredText](https://docutils.sourceforge.io/rst.html) markup and the `sphinx_book_theme`.

## Quick Start for Contributors

### Prerequisites

- **Docker** and **Docker Compose** installed on your local machine
  - Follow the [official Docker documentation](https://docs.docker.com/compose/install/)

### One-Command Setup

```bash
# Clone the repository
git clone git@github.com:talkable/talkable-docs.git
cd talkable-docs

# Setup and start development server
make start
```

That's it! Your local documentation will be available at `http://localhost:8080`.

## Development Workflow

### 1. Initial Setup

```bash
# Create .env file from template (if needed)
make setup

# Verify configuration
make help

# Start development server
make up
```

### 2. Daily Development

```bash
# Start server
make up

# Check server status
make status

# View live logs
make logs

# Stop server
make down

# Complete cleanup
make clean
```

### 3. Making Changes

1. Navigate to the [`source`](./source/) directory
2. Edit files using [reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html) syntax
3. Changes are automatically reflected in your browser (live reload)

### 4. Contribution Process

1. Pull latest changes from `master`
2. Create a new branch from `master`
3. Make and test your changes locally
4. Commit changes to the `staging` branch
5. Create a pull request to `master` with staging URL
6. Get QA approval and merge

## Project Structure

```bash
talkable-docs/
├── source/                 # Documentation source files
│   ├── _static/           # Static assets (CSS, images, PDFs)
│   ├── _templates/        # HTML templates
│   ├── advanced_features/ # Advanced feature documentation
│   ├── api_v2/           # API documentation
│   ├── campaigns/        # Campaign documentation
│   ├── integration/      # Integration guides
│   └── *.rst             # Main documentation files
├── nginx/                 # Nginx configuration
├── deploy/               # Deployment scripts
├── docker-compose.yml    # Production Docker configuration
├── docker-compose-local.yml # Local development configuration
├── Makefile              # Development commands
├── .env.template         # Environment variables template
└── pyproject.toml        # Python dependencies
```

## Available Commands

The Makefile provides all necessary commands for local development:

```bash
make help        # Show all available commands
make setup       # Create .env file from template
make up          # Start local development server
make down        # Stop local development server
make clean       # Remove containers and clean up residuals
make logs        # View development server logs
make status      # Check container status
make start       # Quick setup and start (alias for setup + up)
make stop        # Quick stop and cleanup (alias for down + clean)
```

## Writing Documentation

### reStructuredText Basics

The documentation uses reStructuredText syntax. Key conventions:

#### Section Headings

```rst
# Module Heading
================

= Section Heading
----------------

- Subsection Heading
~~~~~~~~~~~~~~~~~~~

. Subsubsection Heading
.......................
```

#### Cross-References

```rst
.. _reference-name:

Section Title
=============

Here's a reference to the section: :ref:`reference-name`
```

### Sphinx Extensions

- `sphinx_sitemap` - Generates sitemaps
- `sphinx_copybutton` - Adds copy buttons to code blocks
- `sphinx_design` - Advanced layout components

### Code Blocks

```rst
.. code-block:: python

   def example_function():
       return "Hello, World!"
```

## Environment Configuration

### .env File

The `.env` file controls your local development environment:

```bash
# Port for local development server
LOCAL_PORT=8080

# Environment type (local, staging, production)
ENVIRONMENT=local
```

### Environment-Specific Behavior

- **local**: `http://localhost:{LOCAL_PORT}/`
- **staging**: `https://docs.bastion.talkable.com/`
- **production**: `https://docs.talkable.com/`

## Redirects

> [!IMPORTANT]
> Update redirect rules when changing file names, paths, or deleting files.

Redirects are managed in [`./nginx/redirects.conf`](./nginx/redirects.conf). After changes:

```bash
# Restart local container to apply changes
docker compose restart docs-local
```

## Deployment

### Local Development

Use the Makefile commands for all local operations:

```bash
make up      # Deploy locally
make clean   # Remove local deployment
```

### Production & Staging

**Do not deploy manually!** Deployment is handled automatically:

- **staging** branch → [docs.bastion.talkable.com](https://docs.bastion.talkable.com/)
- **master** branch → [docs.talkable.com](https://docs.talkable.com/)

Simply commit to the appropriate branch to trigger deployment.

## Troubleshooting

### Common Issues

#### Documentation Not Loading

1. **Check port**: Ensure you're using the correct port from your `.env` file
2. **Check container status**: `make status`
3. **View logs**: `make logs` (shows real-time server logs)

#### Port Already in Use

Edit your `.env` file and change `LOCAL_PORT` to an available port:

```bash
LOCAL_PORT=8081
```

#### Complete Reset

If you encounter persistent issues:

```bash
make clean    # Remove everything
make setup    # Reset environment
make up       # Start fresh
```

### Getting Help

- Run `make help` for available commands
- Check the [GitHub repository](https://github.com/talkable/talkable-docs) for issues
- Review the [reStructuredText Quickref](https://docutils.sourceforge.io/docs/user/rst/quickref.html) for syntax help

## Additional Resources

- [Sphinx Documentation](https://www.sphinx-doc.org)
- [reStructuredText Quickref](https://docutils.sourceforge.io/docs/user/rst/quickref.html)
- [sphinx_book_theme Documentation](https://sphinx-book-theme.readthedocs.io)

## Repository Links

- **GitHub Repository**: [talkable-docs](https://github.com/talkable/talkable-docs)
- **Staging Branch**: [staging](https://github.com/talkable/talkable-docs/tree/staging)
- **Master Branch**: [master](https://github.com/talkable/talkable-docs/tree/master)
- **Staging Site**: [docs.bastion.talkable.com](https://docs.bastion.talkable.com/)
- **Production Site**: [docs.talkable.com](https://docs.talkable.com/)
