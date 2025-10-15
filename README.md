# Talkable Documentation

Welcome to the Talkable Documentation repository! This guide will help you understand how to contribute to our documentation and run the development environment locally.

## 📚 About Our Documentation

Our documentation is built using **Sphinx**, a powerful documentation generator that converts reStructuredText (`.rst`) files into beautiful HTML websites. Sphinx is the industry standard for Python documentation and provides excellent features for technical documentation.

### Why Sphinx?

- **Structured Content**: Uses reStructuredText for semantic markup
- **Cross-References**: Automatic linking between documentation sections
- **Code Highlighting**: Built-in syntax highlighting for code examples
- **Search Functionality**: Full-text search across all documentation
- **Responsive Design**: Mobile-friendly output with modern themes
- **Extensible**: Rich ecosystem of extensions for enhanced functionality

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed on your system
- Git for cloning the repository

### 1. Clone the Repository

```bash
git clone git@github.com:talkable/talkable-docs.git
cd talkable-docs
```

### 2. Set Up Environment Configuration

The documentation requires environment variables to function properly. You **must** create a `.env` file before starting the services.

```bash
cp .env.template .env
```

### 3. Configure Your Environment

Edit the `.env` file with your local settings:

```bash
# The port to access the documentation locally
LOCAL_PORT=8080

# Environment type (use "local" for development)
ENVIRONMENT=local

# Your local machine's IP address for accessing the docs
BASE_URL=http://192.168.1.100:8080/
```

**⚠️ Important**: Replace `192.168.1.100` with your actual local IP address. You can find it by running:

- macOS/Linux: `ifconfig | grep "inet " | grep -v 127.0.0.1`
- Windows: `ipconfig | findstr "IPv4"`

### 4. Start the Documentation Services

```bash
make up
```

This will start all services for **local development**:

- **Nginx**: Web server serving the documentation (stays running)
- **Sphinx Builder**: Automatically rebuilds documentation when files change (stays running)
- **LLM Text Processor**: Continuously monitors and processes documentation changes (stays running)

> [!IMPORTANT]
> The Sphinx builder is configured with the `-a` flag to force complete rebuilds. This prevents a known issue where sphinx-sitemap generates partial sitemaps during incremental builds. See the "Known Issues" section below for details.

### 5. Access the Documentation

Open your browser and navigate to: `http://192.168.1.100:8080/`

## 📝 Environment Variables Explained

The `.env` file contains three critical variables:

### `LOCAL_PORT`

- **Purpose**: The port on which Nginx serves the documentation locally
- **Default**: `8080`
- **Example**: `LOCAL_PORT=8080`
- **Note**: Ensure this port is not already in use on your system

### `ENVIRONMENT`

- **Purpose**: Determines the deployment environment and affects container naming
- **Values**: `local`, `staging`, or `production`
- **Development**: Always use `local` for local development
- **Example**: `ENVIRONMENT=local`

### `BASE_URL`

- **Purpose**: Base URL used in sitemaps and for internal linking
- **Critical**: Must match your actual local IP address and port
- **Format**: `http://<your-ip>:<port>/`
- **Example**: `BASE_URL=http://192.168.1.100:8080/`
- **Why it matters**: The LLM text processor uses this URL to fetch and process documentation

## 🛠️ Development Workflow

### Making Changes

1. **Edit Documentation Files**: All documentation source files are in the `source/` directory
2. **File Format**: Use reStructuredText (`.rst`) format
3. **Auto-Rebuild**: Changes are automatically detected and rebuilt by Sphinx (takes a few seconds)
4. **Live Preview**: Refresh your browser to see changes
5. **Continuous Processing**: LLM Text Processor automatically updates markdown files when documentation changes

### Common File Locations

- **Main Documentation**: `source/`
- **Campaign Documentation**: `source/campaigns/`
- **API Documentation**: `source/api_v2/`
- **Integration Guides**: `source/integration/`
- **SDK Documentation**: `source/android_sdk/`, `source/ios_sdk/`

### reStructuredText Basics

```rst
# Section Header
## Subsection Header

Paragraph text with **bold** and *italic* formatting.

.. code-block:: python

    def example_function():
        return "Hello, World!"

- Bullet point 1
- Bullet point 2

1. Numbered list item
2. Another numbered item

:doc:`link-to-another-page`
```

## 🧹 Cleaning Up

When you're done working, it's important to clean up your local environment to free up disk space and avoid conflicts.

### Stop Services

```bash
make down
```

This stops and removes all running containers but keeps images and volumes for faster restart.

### Complete Cleanup

```bash
make clean
```

This performs a complete cleanup:

- Stops and removes all containers
- Removes all Docker images
- Removes all volumes (including the `docs_www` shared volume)
- Runs Docker system prune to reclaim disk space

**⚠️ Warning**: `make clean` will remove all cached data, so the next `make up` will take longer as it needs to rebuild everything.

### Rebuild Everything

If you need to force rebuild all images (useful after updating dependencies):

```bash
make rebuild
```

## 📋 Available Make Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make up` | Start local development services (uses docker-compose.local.yml override) |
| `make down` | Stop local development services |
| `make clean` | Complete cleanup including images and volumes |
| `make logs` | View real-time logs from all services |
| `make rebuild` | Force rebuild all images and restart |

## 🔍 Viewing Logs

To see what's happening with the services:

```bash
# View all logs in real-time
make logs

# Or view specific service logs
docker logs -f docs-nginx-local
docker logs -f docs-sphinx-local
docker logs -f docs-llms-txt-local
```

## 🐛 Troubleshooting

### Common Issues

1. **"Error: .env file not found!"**
   - Solution: Run `cp .env.template .env` and configure the variables

2. **"Port already in use"**
   - Solution: Change `LOCAL_PORT` in your `.env` file to an unused port

3. **Documentation not loading**
   - Check that `BASE_URL` uses your correct local IP address
   - Verify all services are running: `docker compose -f docker-compose.yml -f docker-compose.local.yml ps`

4. **Changes not appearing**
   - Wait a few seconds for auto-rebuild
   - Check Sphinx logs: `docker logs docs-sphinx-local`

### Getting Help

- Check the logs for error messages: `make logs`
- Ensure your `.env` file is properly configured
- Verify Docker and Docker Compose are running correctly

## 🐛 Known Issues

### Partial Sitemap Generation During Development

**Issue**: During incremental builds, sphinx-sitemap sometimes generates incomplete sitemaps with only a few URLs instead of the full site.

**Root Cause**: This is a documented bug in sphinx-sitemap related to multiprocessing queue pickling during incremental builds.

**Solution**: The Sphinx builder is configured with the `-a` flag to disable incremental builds and force complete rebuilds.

**Reference**: 
- GitHub Issue: [sphinx-sitemap #62](https://github.com/jdillard/sphinx-sitemap/pull/62)
- Fixed in sphinx-sitemap v2.5.1 (August 2023)
- Official sphinx-autobuild recommendation: Use `-a` flag during development

**Current Status**: 
- ✅ sphinx-sitemap v2.8.0 installed (above problematic version)
- ✅ `-a` flag implemented in Dockerfile for local development
- ✅ Production builds use `--fresh-env` for complete rebuilds

## 📚 Additional Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Docker Documentation](https://docs.docker.com/)

## 🤝 Contributing

Thank you for contributing to Talkable's documentation! Your contributions help developers better understand and use our platform.

### Guidelines

- Write clear, concise documentation
- Use proper reStructuredText formatting
- Test your changes locally before submitting
- Include code examples where helpful
- Keep documentation up-to-date with product changes

Happy documenting! 🎉
