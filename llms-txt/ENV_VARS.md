# Environment Variables Configuration

The `talkable-llm-txt` package supports environment variable overrides for all configuration settings. Environment variables use the `LLMS_TXT_` prefix and double underscores (`__`) for nested configuration.

## Usage Examples

### One-Time Execution Mode

```bash
# Run once without monitoring (most common use case)
LLMS_TXT_MONITORING__ENABLED=false python -m talkable_llm_txt
```

### Override Processing Settings

```bash
# Increase concurrent requests
LLMS_TXT_PROCESSING__MAX_CONCURRENT_REQUESTS=10 python -m talkable_llm_txt

# Limit number of URLs to process
LLMS_TXT_PROCESSING__MAX_URLS_TO_PROCESS=50 python -m talkable_llm_txt

# Adjust timeout
LLMS_TXT_PROCESSING__REQUEST_TIMEOUT=60000 python -m talkable_llm_txt
```

### Override Output Settings

```bash
# Custom output directory
LLMS_TXT_OUTPUT__DIR=/tmp/markdown python -m talkable_llm_txt
```

### Override Content Settings

```bash
# Keep images in markdown
LLMS_TXT_CONTENT__KEEP_IMAGES=true python -m talkable_llm_txt

# Use different heading style
LLMS_TXT_CONTENT__HEADING_STYLE=underlined python -m talkable_llm_txt
```

### Override Performance Settings

```bash
# Wait for full page load
LLMS_TXT_PERFORMANCE__WAIT_UNTIL=load python -m talkable_llm_txt

# Block additional resource types
LLMS_TXT_PERFORMANCE__BLOCKED_RESOURCE_TYPES="image,media,font,stylesheet" python -m talkable_llm_txt
```

### Override Sitemap Settings

```bash
# Use different sitemap URL
LLMS_TXT_SITEMAP__URL=https://docs.example.com/sitemap.xml python -m talkable_llm_txt
```

### Override Logging Settings

```bash
# Enable debug logging
LLMS_TXT_LOGGING__LEVEL=DEBUG python -m talkable_llm_txt
```

## Combined Overrides

You can combine multiple environment variables:

```bash
LLMS_TXT_MONITORING__ENABLED=false \
LLMS_TXT_PROCESSING__MAX_CONCURRENT_REQUESTS=5 \
LLMS_TXT_OUTPUT__DIR=/custom/output \
python -m talkable_llm_txt
```

## Environment Variable Naming Pattern

All environment variables follow this pattern:

```text
LLMS_TXT_<SECTION>__<SETTING>=<value>
```

Where:

- `LLMS_TXT_` is the required prefix
- `<SECTION>` is the configuration section (e.g., `MONITORING`, `PROCESSING`)
- `__` (double underscore) separates section from setting
- `<SETTING>` is the specific configuration setting

## Priority Order

Configuration is loaded in this priority order (highest to lowest):

1. **Environment variables** (highest priority)
2. **TOML configuration file** (default values)
3. **Pydantic model defaults** (fallback)

This means environment variables will always override TOML file settings.

## Available Environment Variables

### Monitoring

- `LLMS_TXT_MONITORING__ENABLED` (bool) - Enable/disable scheduled monitoring
- `LLMS_TXT_MONITORING__CHECK_URL` (string) - URL to monitor for changes
- `LLMS_TXT_MONITORING__CHECK_INTERVAL_MINUTES` (int) - Check interval in minutes
- `LLMS_TXT_MONITORING__ETAG_CACHE_FILE` (string) - ETag cache file path

### Processing

- `LLMS_TXT_PROCESSING__MAX_URLS_TO_PROCESS` (int) - Maximum URLs to process
- `LLMS_TXT_PROCESSING__MAX_CONCURRENT_REQUESTS` (int) - Concurrent requests limit
- `LLMS_TXT_PROCESSING__BATCH_SIZE` (int) - Processing batch size
- `LLMS_TXT_PROCESSING__REQUEST_TIMEOUT` (int) - Request timeout in milliseconds

### Content

- `LLMS_TXT_CONTENT__KEEP_IMAGES` (bool) - Keep images in markdown output
- `LLMS_TXT_CONTENT__HEADING_STYLE` (string) - Markdown heading style

### Performance

- `LLMS_TXT_PERFORMANCE__WAIT_UNTIL` (string) - Page load wait condition
- `LLMS_TXT_PERFORMANCE__BLOCKED_RESOURCE_TYPES` (string) - Resource types to block

### Output

- `LLMS_TXT_OUTPUT__DIR` (string) - Output directory path

### Sitemap

- `LLMS_TXT_SITEMAP__URL` (string) - Sitemap URL

### Sitemap Fetching

- `LLMS_TXT_SITEMAP_FETCHING__TIMEOUT` (int) - Sitemap timeout in seconds
- `LLMS_TXT_SITEMAP_FETCHING__RETRIES` (int) - Number of retry attempts
- `LLMS_TXT_SITEMAP_FETCHING__USER_AGENT` (string) - User agent string

### Logging

- `LLMS_TXT_LOGGING__LEVEL` (string) - Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

## Common Use Cases

### CI/CD Pipeline

```bash
# In CI/CD, run once without monitoring
LLMS_TXT_MONITORING__ENABLED=false python -m talkable_llm_txt
```

### Development

```bash
# Development with debug logging and limited URLs
LLMS_TXT_LOGGING__LEVEL=DEBUG \
LLMS_TXT_PROCESSING__MAX_URLS_TO_PROCESS=10 \
python -m talkable_llm_txt
```

### Production

```bash
# Production with custom output and performance settings
LLMS_TXT_OUTPUT__DIR=/var/www/markdown \
LLMS_TXT_PROCESSING__MAX_CONCURRENT_REQUESTS=8 \
LLMS_TXT_PERFORMANCE__WAIT_UNTIL=load \
python -m talkable_llm_txt
```
