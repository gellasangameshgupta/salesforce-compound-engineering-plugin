# SF Compound Engineering

**Spec-Driven Compound Engineering for Salesforce** — A CLI tool that uses **parallel subagents** to make each unit of Salesforce development easier than the last.

Inspired by [Every's Compound Engineering](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) and [GitHub Spec-Kit](https://github.com/github/spec-kit).

---

## The Compound Engineering Loop

```
Plan (40%) → Work (20%) → Review (20%) → Compound (20%) → Repeat
     │            │             │              │
     │            │             │              └── Capture learnings
     │            │             └── 23 parallel review subagents
     │            └── 4 parallel implementation subagents
     └── 8 parallel research/design subagents
```

**Each iteration starts smarter** because learnings compound into agents, skills, and patterns.

---

## Quick Start

```bash
# Initialize in your Salesforce project (no install required)
uvx --from git+https://github.com/gellasangameshgupta/sf-compound-engineering-plugin.git sfce init . --ai claude
```

That's it! You now have:
- **10 slash commands** with parallel subagent architecture
- **23 specialized agents** (apex, lwc, automation, integration, architecture)
- **6 skills** (governor-limits, apex-patterns, security-guide, etc.)
- The compound engineering workflow

---

## How It Works: Parallel Subagents

Unlike simple linear tools, SF Compound Engineering **deploys multiple subagents in parallel** for each phase:

### `/sf-plan` - 8 Parallel Subagents
```
/sf-plan "Lead Scoring Automation"
         │
         ├── [RESEARCH PHASE - 4 parallel]
         │   ├── Codebase Patterns Subagent
         │   ├── SF Best Practices Subagent
         │   ├── Governor Limit Analysis Subagent
         │   └── Security Requirements Subagent
         │
         └── [DESIGN PHASE - 4 parallel]
             ├── Data Model Architect Subagent
             ├── Apex Architecture Subagent
             ├── LWC Architecture Subagent
             └── Integration Architecture Subagent
```

### `/sf-work` - 6 Parallel Subagents
```
/sf-work plan.md
         │
         ├── [IMPLEMENTATION - 4 parallel]
         │   ├── Apex Subagent (triggers, services)
         │   ├── LWC Subagent (components)
         │   ├── Config Subagent (fields, flows)
         │   └── Test Subagent (test classes)
         │
         └── [VALIDATION - 2 parallel]
             ├── Deploy Validation Subagent
             └── Test Execution Subagent
```

### `/sf-review` - 23 Parallel Subagents
```
/sf-review
    │
    ├── APEX AGENTS (6 parallel)
    │   Governor Guardian, Security Sentinel, Bulkification Reviewer,
    │   Trigger Architect, Test Coverage Analyst, Exception Handler
    │
    ├── LWC AGENTS (5 parallel)
    │   Performance Oracle, Security Reviewer, Accessibility Guardian,
    │   Architecture Strategist, Aura Migration Advisor
    │
    ├── AUTOMATION AGENTS (4 parallel)
    │   Flow Complexity Analyzer, Flow Governor Monitor,
    │   Process Automation Strategist, Validation Rule Reviewer
    │
    ├── INTEGRATION AGENTS (4 parallel)
    │   REST API Architect, Callout Pattern Reviewer,
    │   Platform Event Strategist, Integration Security Sentinel
    │
    └── ARCHITECTURE AGENTS (4 parallel)
        Data Model Architect, Sharing Security Analyst,
        Metadata Consistency Checker, Pattern Recognition Specialist
```

---

## The Workflow

| Phase | Command | Subagents | What It Does |
|-------|---------|-----------|--------------|
| **Plan** (40%) | `/sf-plan` | 8 | Research codebase, design architecture |
| **Work** (20%) | `/sf-work` | 6 | Implement Apex, LWC, config in parallel |
| **Review** (20%) | `/sf-review` | 23 | Multi-perspective code review |
| **Fix** | `/sf-resolve` | 5 | Auto-fix security, governor, patterns |
| **Test** | `/sf-test` | 6 | Run tests, generate missing tests |
| **Compound** (20%) | `/sf-compound` | 5 | Capture learnings, update skills |
| **Deploy** | `/sf-deploy` | 3 | Validate and deploy |

---

## What Gets Created

```
your-salesforce-project/
├── .claude/
│   ├── commands/                # 10 slash commands (subagent-powered)
│   │   ├── sf-plan.md           # 8 subagents for planning
│   │   ├── sf-work.md           # 6 subagents for implementation
│   │   ├── sf-review.md         # 23 subagents for review
│   │   ├── sf-resolve.md        # 5 subagents for fixing
│   │   ├── sf-test.md           # 6 subagents for testing
│   │   ├── sf-compound.md       # 5 subagents for learning capture
│   │   ├── sf-deploy.md         # 3 subagents for deployment
│   │   ├── sf-triage.md
│   │   ├── sf-document.md
│   │   └── sf-health.md
│   ├── agents/                  # 23 specialized review agents
│   │   ├── apex/                # Governor, security, bulk, triggers, tests
│   │   ├── lwc/                 # Performance, a11y, architecture
│   │   ├── automation/          # Flow complexity, governors
│   │   ├── integration/         # REST, callouts, events
│   │   └── architecture/        # Data model, sharing, patterns
│   └── skills/                  # 6 reference skills
│       ├── governor-limits/
│       ├── apex-patterns/
│       ├── security-guide/
│       ├── lwc-patterns/
│       ├── integration-patterns/
│       └── test-factory/
├── .specify/
│   ├── memory/constitution.md   # Project principles
│   ├── specs/                   # Feature specifications
│   ├── compounds/               # Captured learnings
│   └── templates/
└── ... your existing code
```

---

## Usage Examples

### Full Compound Engineering Cycle

```bash
# 1. Plan (40% of work) - 8 subagents research and design
/sf-plan "Lead scoring automation with real-time updates"

# 2. Work (20% of work) - 6 subagents implement in parallel
/sf-work .specify/specs/001-lead-scoring/plan.md

# 3. Review (20% of work) - 23 subagents check from different perspectives
/sf-review

# 4. Fix issues found
/sf-resolve critical
/sf-resolve high

# 5. Test
/sf-test

# 6. Compound (20% of work) - Capture learnings
/sf-compound

# 7. Deploy
/sf-deploy sandbox
```

### Review Any Code

```bash
# Review uncommitted changes
/sf-review

# Review specific PR
/sf-review 123

# Review specific file
/sf-review force-app/main/default/classes/AccountService.cls
```

### Generate Tests

```bash
# Run existing tests
/sf-test local

# Generate tests for a class
/sf-test generate AccountService
```

---

## CLI Commands

```bash
# Initialize
sfce init .                    # Initialize in current directory
sfce init . --ai claude        # Set up for Claude Code (recommended)
sfce init . --ai copilot       # Set up for GitHub Copilot

# Update
sfce update                    # Update all components to latest
sfce update --commands-only    # Only update commands
sfce update --agents-only      # Only update agents

# Info
sfce --version
sfce --help
```

---

## Supported AI Agents (17)

| Agent | Flag | Support Level |
|-------|------|---------------|
| **Claude Code** | `--ai claude` | ✅ Full: subagent-powered commands |
| GitHub Copilot | `--ai copilot` | Workflow prompts |
| Cursor | `--ai cursor` | Rules |
| Windsurf | `--ai windsurf` | Rules |
| Gemini CLI | `--ai gemini` | Prompts |
| Amp | `--ai amp` | Prompts |
| + 11 more... | | |

---

## Why Compound Engineering?

Traditional development accumulates **technical debt**. Each feature adds complexity. The codebase becomes harder to work with over time.

**Compound engineering inverts this:**

1. **Plan thoroughly** (40%) - Research with 8 parallel subagents
2. **Implement efficiently** (20%) - Build with parallel subagents
3. **Review comprehensively** (20%) - 23 perspectives catch issues early
4. **Capture learnings** (20%) - Update agents, skills, patterns

**Result:** Each iteration starts smarter. Future features are faster.

---

## Requirements

- Python 3.8+
- Git (recommended)
- Claude Code (for full subagent support)

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## License

MIT License

---

## Credits

- Built for the Salesforce developer community
- Inspired by [EveryInc's Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin)
- Inspired by [GitHub Spec-Kit](https://github.com/github/spec-kit)
- Powered by Claude Code's subagent architecture
