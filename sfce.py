#!/usr/bin/env python3
"""
SF Compound Engineering CLI

A CLI tool to initialize Spec-Driven Development workflow for Salesforce projects.
Similar to GitHub's `specify init`, but uses the SF Compound Engineering commands.

Usage:
    sfce init .                    # Initialize in current directory
    sfce init my-project           # Create and initialize new project
    sfce init . --ai claude        # Specify AI agent
    sfce init . --force            # Overwrite existing .specify folder
"""

import argparse
import os
import sys
import shutil
from pathlib import Path

# Version
__version__ = "1.0.0"

# ANSI colors
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_success(msg):
    print(f"{Colors.GREEN}✅ {msg}{Colors.RESET}")

def print_info(msg):
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.RESET}")

def print_warning(msg):
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.RESET}")

def print_error(msg):
    print(f"{Colors.RED}❌ {msg}{Colors.RESET}")

def print_banner():
    banner = f"""
{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗
║       SF Compound Engineering - Spec-Driven Development     ║
║                                                             ║
║  23 agents • 9 commands • 6 skills                          ║
╚═══════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

# Templates embedded in the CLI
CONSTITUTION_TEMPLATE = '''# Project Constitution

> This document contains the immutable principles that govern all development within this project.

## Development Workflow

This project uses **Spec-Driven Development** powered by SF Compound Engineering commands:

```
/sf:plan → /sf:work → /sf:review → /sf:triage → /sf:resolve → /sf:test → /sf:document → /sf:health → /sf:deploy
```

### Workflow Phases

| Phase | Command | Purpose |
|-------|---------|---------|
| Specify | `/sf:plan` | Define requirements & technical plan |
| Implement | `/sf:work` | Build following the plan |
| Validate | `/sf:review` | 23-agent code review |
| Prioritize | `/sf:triage` | Triage findings |
| Fix | `/sf:resolve` | Fix prioritized issues |
| Test | `/sf:test` | Generate comprehensive tests |
| Document | `/sf:document` | Auto-generate docs |
| Assess | `/sf:health` | Go/No-Go decision |
| Ship | `/sf:deploy` | Deployment checklist |

---

## Immutable Principles

### 1. Governor Limit Awareness
- All code must consider Salesforce governor limits
- Bulk-safe implementations are mandatory
- Query and DML operations must be optimized

### 2. Security by Default
- CRUD/FLS enforcement is mandatory
- Security vulnerabilities are flagged as CRITICAL
- No bypassing security checks without documentation

### 3. Separation of Concerns
- Trigger logic belongs in handlers, not triggers
- Business logic lives in Service classes
- Data access lives in Selector classes
- UI logic stays in Lightning components

### 4. Testability First
- All code must be designed for testability
- Minimum 80% code coverage is baseline
- Bulk testing (200+ records) is mandatory

### 5. Declarative First
- Declarative before programmatic when equivalent
- Flows for simple automation
- Apex for complex business logic

---

## Quality Gates

- All changes must pass `/sf:review`
- CRITICAL issues block deployment
- Security findings have zero tolerance

---

*Customize this constitution for your project's specific needs.*
'''

SPEC_TEMPLATE = '''# [Feature Name] - Specification

> **Status:** Draft | In Review | Approved | Implemented
> **Version:** 0.1.0
> **Created:** YYYY-MM-DD
> **Author:** [Author Name]
> **Generated with:** `/sf:plan`

## Overview

[Brief description - 2-3 sentences explaining what and why]

## Problem Statement

[What problem does this solve?]

## Goals

1. [Primary goal]
2. [Secondary goal]
3. [Tertiary goal]

## Non-Goals

- [What this will NOT do]

---

## User Stories

### US-001: [User Story Title]

**As a** [role]
**I want to** [action]
**So that** [benefit]

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

---

## Constraints

### Governor Limits
- [Limit consideration]

### Security
- [Security requirement]

---

## Next Steps

1. `/sf:work` - Implement the feature
2. `/sf:review` - Multi-agent code review
3. `/sf:test` - Generate tests
4. `/sf:deploy` - Deployment checklist

---

*See [constitution.md](../../memory/constitution.md) for project principles.*
'''

PLAN_TEMPLATE = '''# [Feature Name] - Technical Plan

> **Status:** Draft | In Review | Approved | Implemented
> **Version:** 0.1.0
> **Spec Reference:** [spec.md](./spec.md)
> **Generated with:** `/sf:plan`

## Technical Context

### Salesforce Environment
- **API Version:** [e.g., v59.0]
- **Edition:** [e.g., Enterprise]
- **Features Required:** [e.g., Platform Events]

### Components to Build
- **Apex Classes:** [List]
- **Triggers:** [List]
- **LWC Components:** [List]
- **Flows:** [List]

---

## Architecture Overview

```
[Component diagram or description]
```

---

## Governor Limit Analysis

| Limit | Budget | This Feature | Remaining | Risk |
|-------|--------|--------------|-----------|------|
| SOQL Queries | 100 | X | 100-X | Low/Med/High |
| DML Statements | 150 | Y | 150-Y | Low/Med/High |
| CPU Time (ms) | 10,000 | Z | 10,000-Z | Low/Med/High |

### Bulk Scenario (200 records)
- [ ] SOQL not in loops
- [ ] DML not in loops
- [ ] Collections used for bulkification

---

## Security Considerations

- [ ] CRUD/FLS enforcement
- [ ] Sharing rules respected
- [ ] No injection vulnerabilities

---

## Workflow Commands

Execute in order:
1. `/sf:work` - Implement components
2. `/sf:review` - 23-agent code review
3. `/sf:triage` - Prioritize findings
4. `/sf:resolve` - Fix issues
5. `/sf:test` - Generate tests
6. `/sf:document` - Generate docs
7. `/sf:health` - Final check
8. `/sf:deploy` - Deploy checklist

---

*See [constitution.md](../../memory/constitution.md) for project principles.*
'''

TASKS_TEMPLATE = '''# [Feature Name] - Tasks

> **Status:** Not Started | In Progress | Completed
> **Spec Reference:** [spec.md](./spec.md)
> **Plan Reference:** [plan.md](./plan.md)

## Legend

- `[x]` - Completed
- `[ ]` - Pending
- `[P]` - Can run in parallel

---

## Phase 1: Implement (`/sf:work`)

- [ ] [P] Create Apex classes
- [ ] [P] Create LWC components
- [ ] Create triggers
- [ ] Wire up components

---

## Phase 2: Review (`/sf:review`)

- [ ] Run multi-agent review
- [ ] Address CRITICAL findings
- [ ] Address HIGH findings

---

## Phase 3: Test (`/sf:test`)

- [ ] Generate unit tests
- [ ] Generate bulk tests (200+ records)
- [ ] Verify 90%+ coverage

---

## Phase 4: Ship (`/sf:health` → `/sf:deploy`)

- [ ] Run health assessment
- [ ] Generate deployment checklist
- [ ] Execute deployment

---

## Summary

| Phase | Tasks | Completed | Remaining |
|-------|-------|-----------|-----------|
| Implement | X | 0 | X |
| Review | X | 0 | X |
| Test | X | 0 | X |
| Ship | X | 0 | X |

---

*See [constitution.md](../../memory/constitution.md) for project principles.*
'''

COMMON_SH = '''#!/bin/bash
# Common utilities for SF Compound Engineering scripts

# Colors
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[0;33m'
BLUE='\\033[0;34m'
NC='\\033[0m' # No Color

# Directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SPECIFY_DIR="$PROJECT_ROOT/.specify"
SPECS_DIR="$SPECIFY_DIR/specs"
TEMPLATES_DIR="$SPECIFY_DIR/templates"
MEMORY_DIR="$SPECIFY_DIR/memory"

# Print functions
print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }

# Get next spec number
get_next_spec_number() {
    local max=0
    if [[ -d "$SPECS_DIR" ]]; then
        for dir in "$SPECS_DIR"/*/; do
            if [[ -d "$dir" ]]; then
                local name=$(basename "$dir")
                local num="${name%%-*}"
                if [[ "$num" =~ ^[0-9]+$ ]] && [[ $num -gt $max ]]; then
                    max=$num
                fi
            fi
        done
    fi
    printf "%03d" $((max + 1))
}

# Count tasks in a file
count_tasks() {
    local file="$1"
    local total=$(grep -c "^- \\[" "$file" 2>/dev/null || echo "0")
    local completed=$(grep -c "^- \\[x\\]" "$file" 2>/dev/null || echo "0")
    echo "$completed/$total"
}
'''

CHECK_PREREQUISITES_SH = '''#!/bin/bash
# Check prerequisites for SF Compound Engineering

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

print_info "Checking prerequisites for SF Compound Engineering..."
echo ""

# Check Git
if command -v git &> /dev/null; then
    print_success "Git installed: v$(git --version | cut -d' ' -f3)"
else
    print_error "Git not installed"
    exit 1
fi

# Check if in git repo
if git rev-parse --git-dir > /dev/null 2>&1; then
    print_success "Inside a Git repository"
else
    print_warning "Not inside a Git repository"
fi

# Check .specify structure
[[ -d "$SPECIFY_DIR" ]] && print_success ".specify directory exists" || print_error ".specify directory missing"
[[ -d "$MEMORY_DIR" ]] && print_success ".specify/memory directory exists" || print_error ".specify/memory missing"
[[ -d "$SPECIFY_DIR/scripts" ]] && print_success ".specify/scripts directory exists" || print_error ".specify/scripts missing"
[[ -d "$SPECS_DIR" ]] && print_success ".specify/specs directory exists" || print_error ".specify/specs missing"
[[ -d "$TEMPLATES_DIR" ]] && print_success ".specify/templates directory exists" || print_error ".specify/templates missing"

# Check constitution
[[ -f "$MEMORY_DIR/constitution.md" ]] && print_success "Constitution exists" || print_warning "constitution.md missing"

# Count specs
if [[ -d "$SPECS_DIR" ]]; then
    spec_count=$(find "$SPECS_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
    print_success "Found $spec_count specification(s)"
fi

echo ""
print_success "Prerequisites check complete!"
'''

CREATE_NEW_FEATURE_SH = '''#!/bin/bash
# Create a new feature specification

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

usage() {
    echo "Usage: $0 <feature-name>"
    echo ""
    echo "Creates a new feature specification from templates."
    echo ""
    echo "Example:"
    echo "  $0 lead-scoring"
    exit 1
}

validate_name() {
    if [[ ! "$1" =~ ^[a-z][a-z0-9-]*$ ]]; then
        print_error "Name must be lowercase with hyphens only"
        exit 1
    fi
}

main() {
    [[ $# -lt 1 ]] && usage

    local name="$1"
    validate_name "$name"

    local num=$(get_next_spec_number)
    local dir="$SPECS_DIR/${num}-${name}"

    print_info "Creating: $num-$name"

    mkdir -p "$dir"

    # Copy templates
    for tmpl in spec plan tasks; do
        if [[ -f "$TEMPLATES_DIR/${tmpl}-template.md" ]]; then
            cp "$TEMPLATES_DIR/${tmpl}-template.md" "$dir/${tmpl}.md"
            sed -i.bak "s/\\[Feature Name\\]/${name}/g" "$dir/${tmpl}.md"
            rm -f "$dir/${tmpl}.md.bak"
            print_success "Created ${tmpl}.md"
        fi
    done

    print_success "Created: $dir"
    echo ""
    print_info "SF Compound Engineering Workflow:"
    echo ""
    echo "  1. /sf:plan    → Generate spec and plan"
    echo "  2. /sf:work    → Implement the feature"
    echo "  3. /sf:review  → Multi-agent code review"
    echo "  4. /sf:triage  → Prioritize findings"
    echo "  5. /sf:resolve → Fix issues"
    echo "  6. /sf:test    → Generate tests"
    echo "  7. /sf:document→ Generate documentation"
    echo "  8. /sf:health  → Final health check"
    echo "  9. /sf:deploy  → Deployment checklist"
    echo ""
    echo "Start with: /sf:plan \\"$name\\""
}

main "$@"
'''

LIST_SPECS_SH = '''#!/bin/bash
# List all specifications

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

print_info "SF Compound Engineering - Specifications"
echo ""

if [[ ! -d "$SPECS_DIR" ]] || [[ -z "$(ls -A "$SPECS_DIR" 2>/dev/null)" ]]; then
    print_warning "No specifications found"
    echo ""
    echo "Create one with:"
    echo "  .specify/scripts/create-new-feature.sh <feature-name>"
    exit 0
fi

printf "%-30s %-15s %-15s\\n" "SPECIFICATION" "STATUS" "TASKS"
printf "%-30s %-15s %-15s\\n" "-------------" "------" "-----"

for dir in "$SPECS_DIR"/*/; do
    if [[ -d "$dir" ]]; then
        name=$(basename "$dir")
        status="Unknown"
        tasks="-"

        if [[ -f "$dir/spec.md" ]]; then
            status=$(grep -m1 "Status:" "$dir/spec.md" | sed 's/.*Status:[[:space:]]*//' | sed 's/[[:space:]]*$//' || echo "Unknown")
        fi

        if [[ -f "$dir/tasks.md" ]]; then
            tasks=$(count_tasks "$dir/tasks.md")
        fi

        printf "%-30s %-15s %-15s\\n" "$name" "$status" "$tasks"
    fi
done

echo ""
print_info "Use: cat .specify/specs/<name>/spec.md"
'''

# AI agent configurations
AI_AGENTS = {
    'claude': {
        'name': 'Claude Code',
        'prompt_dir': '.claude',
        'prompt_file': 'commands.md'
    },
    'copilot': {
        'name': 'GitHub Copilot',
        'prompt_dir': '.github/prompts',
        'prompt_file': None  # Creates individual files
    },
    'cursor': {
        'name': 'Cursor',
        'prompt_dir': '.cursor',
        'prompt_file': 'rules.md'
    },
    'gemini': {
        'name': 'Gemini CLI',
        'prompt_dir': '.gemini',
        'prompt_file': 'prompts.md'
    }
}

def create_directory_structure(project_path: Path, force: bool = False):
    """Create the .specify directory structure."""
    specify_dir = project_path / '.specify'

    if specify_dir.exists() and not force:
        print_warning(f".specify already exists in {project_path}")
        print_info("Use --force to overwrite")
        return False

    # Create directories
    dirs = [
        specify_dir / 'memory',
        specify_dir / 'scripts',
        specify_dir / 'specs',
        specify_dir / 'templates'
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print_success(f"Created {d.relative_to(project_path)}")

    # Create files
    files = {
        specify_dir / 'memory' / 'constitution.md': CONSTITUTION_TEMPLATE,
        specify_dir / 'templates' / 'spec-template.md': SPEC_TEMPLATE,
        specify_dir / 'templates' / 'plan-template.md': PLAN_TEMPLATE,
        specify_dir / 'templates' / 'tasks-template.md': TASKS_TEMPLATE,
        specify_dir / 'scripts' / 'common.sh': COMMON_SH,
        specify_dir / 'scripts' / 'check-prerequisites.sh': CHECK_PREREQUISITES_SH,
        specify_dir / 'scripts' / 'create-new-feature.sh': CREATE_NEW_FEATURE_SH,
        specify_dir / 'scripts' / 'list-specs.sh': LIST_SPECS_SH,
    }

    for path, content in files.items():
        path.write_text(content.strip() + '\n')
        print_success(f"Created {path.relative_to(project_path)}")

    # Make scripts executable
    for script in (specify_dir / 'scripts').glob('*.sh'):
        script.chmod(0o755)

    return True

def install_commands(project_path: Path):
    """Install SF Compound Engineering commands to .claude/commands/"""
    commands_dir = project_path / '.claude' / 'commands'
    commands_dir.mkdir(parents=True, exist_ok=True)

    # Get the directory where this script is located
    cli_dir = Path(__file__).parent
    source_commands_dir = cli_dir / 'commands'

    if source_commands_dir.exists():
        # Copy commands from package
        for cmd_file in source_commands_dir.glob('*.md'):
            dest_file = commands_dir / cmd_file.name
            shutil.copy(cmd_file, dest_file)
            print_success(f"Installed command: /sf:{cmd_file.stem}")
    else:
        # Fallback: create minimal command stubs
        print_warning("Command files not found in package, creating stubs...")
        create_command_stubs(commands_dir)

    return True

def install_agents(project_path: Path):
    """Install SF Compound Engineering agents to .claude/agents/"""
    cli_dir = Path(__file__).parent
    source_agents_dir = cli_dir / 'agents'

    if not source_agents_dir.exists():
        print_warning("Agents not found in package")
        return False

    dest_agents_dir = project_path / '.claude' / 'agents'

    # Copy all agent categories
    agent_count = 0
    for category in source_agents_dir.iterdir():
        if category.is_dir():
            dest_category = dest_agents_dir / category.name
            dest_category.mkdir(parents=True, exist_ok=True)
            for agent_file in category.glob('*.md'):
                shutil.copy(agent_file, dest_category / agent_file.name)
                agent_count += 1

    print_success(f"Installed {agent_count} agents (apex, lwc, automation, integration, architecture)")
    return True

def install_skills(project_path: Path):
    """Install SF Compound Engineering skills to .claude/skills/"""
    cli_dir = Path(__file__).parent
    source_skills_dir = cli_dir / 'skills'

    if not source_skills_dir.exists():
        print_warning("Skills not found in package")
        return False

    dest_skills_dir = project_path / '.claude' / 'skills'

    # Copy all skills
    skill_count = 0
    for skill in source_skills_dir.iterdir():
        if skill.is_dir():
            dest_skill = dest_skills_dir / skill.name
            dest_skill.mkdir(parents=True, exist_ok=True)
            for skill_file in skill.glob('*.md'):
                shutil.copy(skill_file, dest_skill / skill_file.name)
            skill_count += 1

    print_success(f"Installed {skill_count} skills (governor-limits, apex-patterns, security-guide, lwc-patterns, integration-patterns, test-factory)")
    return True

def create_command_stubs(commands_dir: Path):
    """Create minimal command stubs if full commands aren't available."""
    commands = {
        'plan': 'Create implementation plans from feature descriptions',
        'work': 'Implement features following Salesforce best practices',
        'review': 'Multi-agent code review (23 specialized agents)',
        'triage': 'Prioritize and categorize review findings',
        'resolve': 'Fix prioritized issues from review',
        'test': 'Generate comprehensive test suites',
        'document': 'Auto-generate documentation',
        'health': 'Assess codebase health and deployment readiness',
        'deploy': 'Create deployment checklists and validate deployments',
    }

    for name, desc in commands.items():
        stub = f'''---
name: sf:{name}
description: {desc}
---

# /sf:{name}

{desc}

See `.specify/memory/constitution.md` for project principles.

## Usage

```
/sf:{name} [description]
```
'''
        (commands_dir / f'{name}.md').write_text(stub)
        print_success(f"Created stub: /sf:{name}")

def setup_ai_agent(project_path: Path, agent: str):
    """Set up prompts for the specified AI agent."""
    if agent not in AI_AGENTS:
        print_warning(f"Unknown agent: {agent}")
        return

    config = AI_AGENTS[agent]
    print_info(f"Setting up for {config['name']}...")

    # For Claude, install commands, agents, and skills
    if agent == 'claude':
        install_commands(project_path)
        install_agents(project_path)
        install_skills(project_path)

    prompt_dir = project_path / config['prompt_dir']
    prompt_dir.mkdir(parents=True, exist_ok=True)

    # Create a simple prompt file that references the workflow
    prompt_content = f'''# SF Compound Engineering Workflow

This project uses Spec-Driven Development with the following commands:

```
/sf:plan → /sf:work → /sf:review → /sf:triage → /sf:resolve → /sf:test → /sf:document → /sf:health → /sf:deploy
```

## Commands

| Command | Purpose |
|---------|---------|
| `/sf:plan` | Generate spec & plan from requirements |
| `/sf:work` | Implement following the plan |
| `/sf:review` | 23-agent code review |
| `/sf:triage` | Prioritize findings |
| `/sf:resolve` | Fix prioritized issues |
| `/sf:test` | Generate comprehensive tests |
| `/sf:document` | Auto-generate documentation |
| `/sf:health` | Go/No-Go decision |
| `/sf:deploy` | Deployment checklist |

## Project Principles

See `.specify/memory/constitution.md` for project principles including:
- Governor limit awareness
- Security by default
- Separation of concerns
- Testability first

## Creating New Features

```bash
.specify/scripts/create-new-feature.sh <feature-name>
```
'''

    if config['prompt_file']:
        prompt_path = prompt_dir / config['prompt_file']
        prompt_path.write_text(prompt_content)
        print_success(f"Created {prompt_path.relative_to(project_path)}")

    print_success(f"Configured for {config['name']}")

def init_command(args):
    """Initialize SF Compound Engineering in a project."""
    print_banner()

    # Determine project path
    if args.project == '.' or args.here:
        project_path = Path.cwd()
    else:
        project_path = Path(args.project)
        if not project_path.exists():
            project_path.mkdir(parents=True)
            print_success(f"Created project directory: {project_path}")

    project_path = project_path.resolve()
    print_info(f"Initializing in: {project_path}")
    print()

    # Create structure
    if not create_directory_structure(project_path, args.force):
        return 1

    # Set up AI agent if specified
    if args.ai:
        print()
        setup_ai_agent(project_path, args.ai)

    # Print success message
    print()
    print_success("SF Compound Engineering initialized!")
    print()
    print_info("Next steps:")
    print()
    print("  1. Review and customize:")
    print(f"     {project_path}/.specify/memory/constitution.md")
    print()
    print("  2. Create your first feature spec:")
    print("     .specify/scripts/create-new-feature.sh my-feature")
    print()
    print("  3. Start the workflow:")
    print('     /sf:plan "Describe your feature"')
    print()
    print("  Full workflow:")
    print("  /sf:plan → /sf:work → /sf:review → /sf:triage → /sf:resolve → /sf:test → /sf:document → /sf:health → /sf:deploy")
    print()

    return 0

def main():
    parser = argparse.ArgumentParser(
        description='SF Compound Engineering - Spec-Driven Development for Salesforce',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  sfce init .                    Initialize in current directory
  sfce init my-project           Create and initialize new project
  sfce init . --ai claude        Set up for Claude Code
  sfce init . --force            Overwrite existing .specify

Workflow:
  /sf:plan → /sf:work → /sf:review → /sf:triage → /sf:resolve → /sf:test → /sf:document → /sf:health → /sf:deploy
        '''
    )

    parser.add_argument('--version', action='version', version=f'sfce {__version__}')

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize SF Compound Engineering')
    init_parser.add_argument('project', nargs='?', default='.', help='Project directory (default: current)')
    init_parser.add_argument('--here', action='store_true', help='Initialize in current directory')
    init_parser.add_argument('--force', action='store_true', help='Overwrite existing .specify')
    init_parser.add_argument('--ai', choices=['claude', 'copilot', 'cursor', 'gemini'],
                            help='Set up for specific AI agent')

    args = parser.parse_args()

    if args.command == 'init':
        return init_command(args)
    else:
        parser.print_help()
        return 0

if __name__ == '__main__':
    sys.exit(main())
