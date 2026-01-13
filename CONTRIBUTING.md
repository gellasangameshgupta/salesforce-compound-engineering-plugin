# Contributing to SF Compound Engineering

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

- Check existing issues before creating a new one
- Use issue templates when available
- Provide detailed reproduction steps
- Include relevant environment information (Python version, OS, etc.)

### Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test locally (see Testing section)
5. Commit with a descriptive message
6. Push to your branch
7. Open a Pull Request

## Project Structure

```
sf-compound-engineering/
├── sfce.py              # Main CLI application
├── __init__.py          # Package init
├── commands/            # Slash command definitions
│   ├── plan.md          # /sf:plan
│   ├── work.md          # /sf:work
│   ├── review.md        # /sf:review
│   ├── triage.md        # /sf:triage
│   ├── resolve.md       # /sf:resolve
│   ├── test.md          # /sf:test
│   ├── document.md      # /sf:document
│   ├── health.md        # /sf:health
│   └── deploy.md        # /sf:deploy
├── pyproject.toml       # Python package config
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

## Adding/Modifying Commands

### Command File Format

Commands are markdown files with YAML frontmatter:

```yaml
---
name: sf:command-name
description: What the command does
arguments:
  - name: arg1
    description: Argument description
    required: true/false
---

# Command Title

Description and workflow steps...
```

### Best Practices for Commands

1. **Clear Structure**: Include workflow steps with headers
2. **Examples**: Provide real-world usage examples
3. **Salesforce-Specific**: Reference governor limits, security, patterns
4. **Output Format**: Define expected output structure

## Modifying the CLI

### Key Functions in `sfce.py`

- `create_directory_structure()` - Creates `.specify/` folder
- `install_commands()` - Installs commands to `.claude/commands/`
- `setup_ai_agent()` - Configures for specific AI agents
- `init_command()` - Main initialization logic

### Adding New AI Agent Support

1. Add entry to `AI_AGENTS` dictionary
2. Implement any agent-specific setup in `setup_ai_agent()`
3. Update README with new agent info

## Testing

### Local Testing

```bash
# Test the CLI
python sfce.py --help
python sfce.py init --help

# Test initialization in a temp directory
mkdir /tmp/test-project
cd /tmp/test-project
python /path/to/sfce.py init . --ai claude

# Verify structure
find . -type f | sort
```

### Verify Commands

```bash
# Count command files
ls commands/*.md | wc -l  # Should be 9

# Validate command frontmatter
head -10 commands/plan.md
```

## Code Style

### Python

- Follow PEP 8
- Use type hints where possible
- Keep functions focused and documented

### Markdown

- Use ATX-style headers (`#`, `##`, `###`)
- Include code examples with syntax highlighting
- Keep lines under 100 characters when possible

### Command Examples (Apex)

- Follow Salesforce naming conventions
- Include proper error handling
- Show bulk-safe patterns
- Include CRUD/FLS checks

### Command Examples (LWC)

- Use modern ES6+ syntax
- Follow LWC best practices
- Include accessibility considerations

## Questions?

Feel free to open an issue for any questions about contributing.
