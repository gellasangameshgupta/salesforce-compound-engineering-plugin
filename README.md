# SF Compound Engineering

**Spec-Driven Development for Salesforce** — A CLI tool to initialize structured development workflows in any Salesforce project.

Similar to GitHub's [`specify init`](https://github.com/github/spec-kit), but with Salesforce-specific commands and best practices.

---

## Quick Start

```bash
# Initialize in your Salesforce project (no install required)
uvx --from git+https://github.com/gellasangameshgupta/sf-compound-engineering.git sfce init . --ai claude
```

That's it! You now have:
- **9 slash commands** (`/sf:plan`, `/sf:work`, `/sf:review`, etc.)
- **23 specialized agents** (apex, lwc, automation, integration, architecture)
- **6 skills** (governor-limits, apex-patterns, security-guide, etc.)
- Spec-driven workflow structure
- Salesforce best practices baked in

---

## Installation Options

### Option 1: Using uvx (Recommended)

```bash
# One-time run, no install needed
uvx --from git+https://github.com/gellasangameshgupta/sf-compound-engineering.git sfce init .

# With Claude Code setup (installs commands)
uvx --from git+https://github.com/gellasangameshgupta/sf-compound-engineering.git sfce init . --ai claude
```

### Option 2: Permanent Install

```bash
# Install globally
uv tool install --from git+https://github.com/gellasangameshgupta/sf-compound-engineering.git sfce-cli

# Then use anywhere
sfce init .
sfce init my-project --ai claude
```

### Option 3: pip install

```bash
pip install git+https://github.com/gellasangameshgupta/sf-compound-engineering.git

sfce init . --ai claude
```

---

## What Gets Created

```
your-salesforce-project/
├── .claude/
│   ├── commands/                # 9 slash commands
│   │   ├── plan.md              # /sf:plan - Create implementation plans
│   │   ├── work.md              # /sf:work - Implement with best practices
│   │   ├── review.md            # /sf:review - Multi-agent code review
│   │   ├── triage.md            # /sf:triage - Prioritize findings
│   │   ├── resolve.md           # /sf:resolve - Fix issues
│   │   ├── test.md              # /sf:test - Generate tests
│   │   ├── document.md          # /sf:document - Auto-generate docs
│   │   ├── health.md            # /sf:health - Deployment readiness
│   │   └── deploy.md            # /sf:deploy - Deployment checklist
│   ├── agents/                  # 23 specialized review agents
│   │   ├── apex/                # Governor limits, security, bulkification
│   │   ├── lwc/                 # Performance, accessibility, architecture
│   │   ├── automation/          # Flow complexity, governor monitoring
│   │   ├── integration/         # REST API, callouts, platform events
│   │   └── architecture/        # Data model, sharing, patterns
│   └── skills/                  # 6 reference skills
│       ├── governor-limits/     # All Salesforce limits with thresholds
│       ├── apex-patterns/       # Trigger handler, service, selector patterns
│       ├── security-guide/      # CRUD/FLS, injection prevention
│       ├── lwc-patterns/        # Component communication, state management
│       ├── integration-patterns/# REST, callouts, platform events
│       └── test-factory/        # TestDataFactory patterns
├── .specify/
│   ├── memory/
│   │   └── constitution.md      # Project principles
│   ├── scripts/
│   │   ├── create-new-feature.sh
│   │   ├── list-specs.sh
│   │   └── check-prerequisites.sh
│   ├── specs/                   # Your feature specifications
│   └── templates/               # Templates for new specs
└── ... your existing code
```

---

## The Workflow

After initialization, use the commands in sequence:

```
/sf:plan → /sf:work → /sf:review → /sf:triage → /sf:resolve → /sf:test → /sf:document → /sf:health → /sf:deploy
```

| Phase | Command | What It Does |
|-------|---------|--------------|
| **Specify** | `/sf:plan` | Generate spec & implementation plan from requirements |
| **Implement** | `/sf:work` | Build following Salesforce best practices |
| **Validate** | `/sf:review` | Multi-agent code review (governor limits, security, patterns) |
| **Prioritize** | `/sf:triage` | Categorize and prioritize review findings |
| **Fix** | `/sf:resolve` | Fix prioritized issues |
| **Test** | `/sf:test` | Generate comprehensive tests (bulk, negative, mocks) |
| **Document** | `/sf:document` | Auto-generate ApexDoc and documentation |
| **Assess** | `/sf:health` | Codebase health check, Go/No-Go decision |
| **Ship** | `/sf:deploy` | Deployment checklist and validation |

---

## Usage Examples

### Start a New Feature

```bash
# Create spec structure
.specify/scripts/create-new-feature.sh lead-scoring

# Generate the plan with Claude
/sf:plan "Build a lead scoring system that calculates scores based on
email opens, web visits, and form submissions"
```

### Review Existing Code

```
/sf:review

Review the AccountTriggerHandler and AccountService classes
for governor limits and security issues.
```

### Generate Tests

```
/sf:test

Generate bulk tests for LeadScoringService with 200+ records.
Include negative tests and mock callouts.
```

---

## CLI Commands

```bash
sfce init .                    # Initialize in current directory
sfce init my-project           # Create new project and initialize
sfce init . --ai claude        # Set up for Claude Code (installs commands)
sfce init . --ai copilot       # Set up for GitHub Copilot
sfce init . --ai cursor        # Set up for Cursor
sfce init . --force            # Overwrite existing .specify folder
sfce --version                 # Show version
sfce --help                    # Show help
```

---

## Supported AI Agents

| Agent | Flag | What Gets Installed |
|-------|------|---------------------|
| Claude Code | `--ai claude` | 9 commands + 23 agents + 6 skills in `.claude/` |
| GitHub Copilot | `--ai copilot` | `.github/prompts/` with workflow prompts |
| Cursor | `--ai cursor` | `.cursor/` with rules |
| Gemini | `--ai gemini` | `.gemini/` with prompts |

---

## Agents (23)

Specialized AI reviewers that provide deep Salesforce expertise:

| Category | Count | What They Check |
|----------|-------|-----------------|
| **Apex** | 6 | Governor limits, CRUD/FLS, injection, bulk patterns, test quality |
| **LWC** | 5 | Wire adapters, XSS, ARIA, component patterns, Aura migration |
| **Automation** | 4 | Flow design, DML in loops, Flow vs Apex decisions |
| **Integration** | 4 | API design, Named Credentials, retry patterns |
| **Architecture** | 4 | Schema design, OWD, anti-patterns |

---

## Skills (6)

Reference documentation that Claude consults automatically:

| Skill | What It Contains |
|-------|------------------|
| `governor-limits` | All Salesforce limits with thresholds |
| `apex-patterns` | Trigger handler, selector, service patterns |
| `security-guide` | CRUD/FLS patterns, injection prevention |
| `lwc-patterns` | Component communication, state management |
| `integration-patterns` | REST, callouts, platform events |
| `test-factory` | TestDataFactory patterns |

---

## Project Principles

The generated `constitution.md` includes Salesforce best practices:

- **Governor Limit Awareness** — All code considers limits, bulk-safe by default
- **Security by Default** — CRUD/FLS enforcement mandatory
- **Separation of Concerns** — Triggers → Handlers → Services → Selectors
- **Testability First** — 80% coverage is baseline, behavior verification required
- **Declarative First** — Flows before Apex when equivalent

---

## Requirements

- Python 3.8+
- Git (recommended)

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## License

MIT License - see [LICENSE](./LICENSE)

---

## Credits

- Inspired by [GitHub Spec-Kit](https://github.com/github/spec-kit)
- Built for the Salesforce developer community
