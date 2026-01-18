# SF Compound Engineering

**Instruction-Based Compound Engineering for Salesforce** — A CLI tool that provides domain knowledge and expertise for Salesforce development, where each iteration becomes smarter than the last.

Inspired by [Every's Compound Engineering](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) and [GitHub Spec-Kit](https://github.com/github/spec-kit).

---

## The Compound Engineering Loop

```
Plan (40%) → Work (20%) → Review (20%) → Compound (20%) → Repeat
     │            │             │              │
     │            │             │              └── Capture learnings to skills, agents, CLAUDE.md
     │            │             └── Review with relevant agents
     │            └── Implement following patterns from skills
     └── Research & design using relevant skills/agents
```

**Each iteration starts smarter** because learnings compound into agents, skills, and project context.

---

## Quick Start

```bash
# Initialize in your Salesforce project (no install required)
uvx --from git+https://github.com/gellasangameshgupta/sf-compound-engineering-plugin.git sfce init . --ai claude
```

That's it! You now have:
- **4 slash commands** for the compound engineering workflow
- **23 specialized agents** (apex, lwc, automation, integration, architecture)
- **7 skills** with domain knowledge (governor-limits, apex-patterns, flow-patterns, etc.)
- **Index files** that help Claude find relevant resources automatically

---

## How It Works: Instruction-Based Architecture

Unlike procedural tools that force fixed steps, SF Compound Engineering uses an **instruction-based approach**:

### Commands = Goal + Resources

Commands tell Claude:
- **What** the goal is (plan, implement, review, compound)
- **Where** to find relevant knowledge (index files → agents/skills)
- **What** constraints apply (no code in planning, security requirements)

Claude decides:
- **Which** agents and skills are relevant for THIS specific task
- **Whether** to use WebSearch based on what's needed
- **How** to approach the implementation

### Index Files = Smart Routing

```
agents/index.md  →  "Building a Flow? Read automation/flow-*.md agents"
skills/index.md  →  "Building a Flow? Read flow-patterns and governor-limits skills"
```

---

## The 4 Commands

| Command | Effort | Purpose |
|---------|--------|---------|
| `/sf-plan` | 40% | Research & design specs (NO CODE) |
| `/sf-work` | 20% | Implement following the plan |
| `/sf-review` | 20% | Review code with relevant agents |
| `/sf-compound` | 20% | Capture learnings to improve future work |

### `/sf-plan` - Design Without Code

```bash
/sf-plan "Lead auto-assignment flow based on territory and workload"
```

What happens:
1. Claude reads `agents/index.md` → finds Flow-related agents
2. Claude reads `skills/index.md` → finds `flow-patterns`, `governor-limits`
3. Claude explores codebase for existing patterns
4. Claude designs the solution (architecture, not code)
5. Output saved to `.specify/specs/<NNN>-<feature>/`

### `/sf-work` - Implement

```bash
/sf-work .specify/specs/001-lead-assignment/plan.md
```

What happens:
1. Claude reads the plan
2. Claude reads relevant skills for patterns
3. Claude follows existing codebase conventions
4. Claude implements and creates tests

### `/sf-review` - Quality Check

```bash
/sf-review
```

What happens:
1. Claude identifies changed files
2. Claude reads relevant agents based on file types
3. Claude reviews using agent checklists
4. Output: findings by severity with fix suggestions

### `/sf-compound` - Capture Learnings

```bash
/sf-compound
```

What happens:
1. Claude analyzes recent work
2. Claude identifies new patterns → adds to skills
3. Claude finds preventable issues → adds checks to agents
4. Claude updates CLAUDE.md with project context

---

## What Gets Created

```
your-salesforce-project/
├── .claude/
│   ├── commands/                # 4 instruction-based commands
│   │   ├── sf-plan.md           # Goal: design, no code
│   │   ├── sf-work.md           # Goal: implement
│   │   ├── sf-review.md         # Goal: find issues
│   │   └── sf-compound.md       # Goal: capture learnings
│   │
│   ├── agents/                  # 23 specialized review agents
│   │   ├── index.md             # ← Master lookup (which agent for which task)
│   │   ├── apex/                # Governor, security, bulk, triggers, tests
│   │   ├── lwc/                 # Performance, a11y, security, architecture
│   │   ├── automation/          # Flow complexity, governors, strategy
│   │   ├── integration/         # REST, callouts, events, security
│   │   └── architecture/        # Data model, sharing, patterns
│   │
│   └── skills/                  # 7 domain knowledge skills
│       ├── index.md             # ← Master lookup (which skill for which task)
│       ├── governor-limits/     # All SF limits and patterns
│       ├── apex-patterns/       # Trigger handlers, services, selectors
│       ├── flow-patterns/       # Flow design patterns, bulkification
│       ├── lwc-patterns/        # Component architecture, wire vs imperative
│       ├── security-guide/      # CRUD/FLS, sharing, AppExchange
│       ├── integration-patterns/# Callouts, Named Credentials, events
│       └── test-factory/        # TestDataFactory, mocks, strategies
│
├── .specify/
│   ├── memory/constitution.md   # Project principles
│   ├── specs/                   # Feature specifications
│   │   └── 001-feature/
│   │       ├── spec.md          # Business requirements
│   │       ├── plan.md          # Technical design
│   │       └── tasks.md         # Implementation checklist
│   ├── compounds/               # Learning capture reports
│   └── templates/
│
└── CLAUDE.md                    # Project-specific context (updated by /sf-compound)
```

---

## 23 Agents by Category

### Apex (6 agents)
| Agent | Checks For |
|-------|------------|
| Governor Guardian | SOQL/DML in loops, limit compliance |
| Security Sentinel | CRUD/FLS, SOQL injection, credentials |
| Bulkification Reviewer | 200+ record handling, collections |
| Trigger Architect | One trigger per object, handler pattern |
| Test Coverage Analyst | Assertions, bulk tests, coverage |
| Exception Handler | Error handling, custom exceptions |

### LWC (5 agents)
| Agent | Checks For |
|-------|------------|
| Architecture Strategist | Component hierarchy, state management |
| Performance Oracle | Wire vs imperative, rendering |
| Security Reviewer | XSS, CSP compliance |
| Accessibility Guardian | ARIA, keyboard navigation |
| Aura Migration Advisor | Migration candidates |

### Automation (4 agents)
| Agent | Checks For |
|-------|------------|
| Flow Governor Monitor | DML/SOQL in loops, limits |
| Flow Complexity Analyzer | Element count, decision depth |
| Process Automation Strategist | Flow vs Apex decisions |
| Validation Rule Reviewer | Rule complexity, error messages |

### Integration (4 agents)
| Agent | Checks For |
|-------|------------|
| REST API Architect | Endpoint design, versioning |
| Callout Pattern Reviewer | Named Credentials, retry logic |
| Platform Event Strategist | Event design, replay handling |
| Integration Security Sentinel | Auth, certificates, data transit |

### Architecture (4 agents)
| Agent | Checks For |
|-------|------------|
| Data Model Architect | Relationships, field design |
| Sharing Security Analyst | OWD, sharing rules, permissions |
| Pattern Recognition Specialist | God classes, duplicate code |
| Metadata Consistency Checker | Naming, API versions |

---

## 7 Skills

| Skill | Contains |
|-------|----------|
| `governor-limits` | All SF limits, patterns to avoid exceptions |
| `apex-patterns` | Trigger handlers, services, selectors, domains |
| `flow-patterns` | Flow design, bulkification, subflows, invocables |
| `lwc-patterns` | Component architecture, wire, events, state |
| `security-guide` | CRUD/FLS enforcement, sharing, AppExchange reqs |
| `integration-patterns` | Named Credentials, callouts, Platform Events |
| `test-factory` | TestDataFactory, mocks, bulk test strategies |

---

## CLI Commands

```bash
# Initialize
sfce init .                    # Initialize in current directory
sfce init . --ai claude        # Set up for Claude Code (recommended)
sfce init . --force            # Overwrite existing .specify

# Update
sfce update                    # Update all components to latest
sfce update --commands-only    # Only update commands
sfce update --agents-only      # Only update agents
sfce update --skills-only      # Only update skills

# Info
sfce --version
sfce --help
```

---

## Example: Building a Flow

```bash
# 1. Plan the Flow (Claude reads flow-patterns skill automatically)
/sf-plan "Lead auto-assignment flow based on territory and rep workload"

# 2. Implement the Flow
/sf-work .specify/specs/001-lead-assignment/plan.md

# 3. Review (Claude uses automation agents automatically)
/sf-review

# 4. Capture learnings
/sf-compound
```

Because commands are instruction-based, Claude:
- **DOES** read Flow-specific agents and skills
- **DOES NOT** research Apex architecture (not needed for a Flow)
- **DOES NOT** research LWC patterns (not needed for a Flow)

---

## Why Instruction-Based?

### Before (Procedural)
```
Step 1: Call Apex research subagent
Step 2: Call LWC research subagent
Step 3: Call Flow research subagent
... same steps regardless of task
```

### After (Instruction-Based)
```
Goal: Plan this feature
Resources: agents/index.md, skills/index.md
Constraints: No code, save to .specify/specs/
... Claude decides what's relevant
```

**Benefits:**
- No hallucination from irrelevant research
- Faster execution (only reads what's needed)
- Adapts to the actual task

---

## Requirements

- Python 3.8+
- Git (recommended)
- Claude Code (for full support)

---

## Contributing

Contributions welcome! Key areas:
- Add new agents for specialized reviews
- Expand skills with more patterns
- Improve index files for better routing

---

## License

MIT License

---

## Credits

- Built for the Salesforce developer community
- Inspired by [EveryInc's Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin)
- Inspired by [GitHub Spec-Kit](https://github.com/github/spec-kit)
- Powered by Claude Code
