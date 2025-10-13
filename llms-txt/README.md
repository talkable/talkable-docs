# talkable-llm-txt

Documentation processing pipeline that converts Talkable documentation websites to Markdown format for AI agent consumption. Generates comprehensive `llm.txt` files and all corresponding documentation assets required for AI agents to effectively read and understand Talkable documentation.

## Configuration

The package uses a comprehensive configuration system managed through `config.toml`. A template is provided at `config.toml.template` with detailed explanations for all parameters.

Configuration options can be managed via:

- **Config File**: Copy `config.toml.template` to `config.toml` and modify settings
- **Environment Variables**: Override any setting using `LLMS_TXT_<SECTION>__<SETTING>` format
- **Defaults**: Automatic fallback to default values when no configuration is provided

## Integration

This package is part of the overall Talkable documentation deployment system. For complete deployment details, infrastructure setup, and integration guidelines, please refer to the documentation at the upper level of this repository.
