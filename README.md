# <span data-proof="authored" data-by="ai:claude">SF Compound Engineering Plugin v2.1.0</span>

**<span data-proof="authored" data-by="ai:claude">Instruction-Based Compound Engineering for Salesforce</span>** <span data-proof="authored" data-by="ai:claude">— a Claude Code plugin where each iteration becomes smarter than the last through institutional knowledge capture and parallel agent dispatch.</span>

<span data-proof="authored" data-by="ai:claude">Inspired by</span> [<span data-proof="authored" data-by="ai:claude">Every's Compound Engineering</span>](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) <span data-proof="authored" data-by="ai:claude">and</span> [<span data-proof="authored" data-by="ai:claude">GitHub Spec-Kit</span>](https://github.com/github/spec-kit)<span data-proof="authored" data-by="ai:claude">.</span>

***

## <span data-proof="authored" data-by="ai:claude">The Compound Engineering Loop</span>

```
Brainstorm → Plan (40%) → Deepen → Work (20%) → Review (20%) → Compound (20%) → Repeat
     │            │           │          │              │               │
     │            │           │          │              │               └── Capture to docs/solutions/
     │            │           │          │              └── Parallel agent dispatch (33 agents)
     │            │           │          └── Implement with pre-research + test checks
     │            │           └── Enhance plan with section-level parallel research
     │            └── Research & design using 12 skills + 5 research agents
     └── Explore requirements through collaborative dialogue
```

**<span data-proof="authored" data-by="ai:claude">Each iteration starts smarter</span>** <span data-proof="authored" data-by="ai:claude">because learnings compound into</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`, agents, skills, and CLAUDE.md.</span>

***

## Quick Start

### Claude Code (Native)

```bash
# Add as a Claude Code plugin
/plugin marketplace add https://github.com/sangameshgupta/sf-compound-engineering-plugin

# Install
/plugin install sf-compound-engineering
```

### Other AI Coding Tools (11 platforms)

```bash
# GitHub Copilot
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to copilot

# Cursor
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to cursor

# Windsurf
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to windsurf

# Gemini CLI
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to gemini

# OpenCode
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to opencode

# Codex
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to codex

# Kiro
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to kiro

# Factory Droid
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to droid

# Pi
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to pi

# OpenClaw
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to openclaw

# Qwen Code
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to qwen

# Auto-detect and install to all detected tools
bunx @sangameshgupta/sf-compound-plugin install sf-compound-engineering --to all

# Sync from current directory to all detected tools
bunx @sangameshgupta/sf-compound-plugin sync
```

### What Gets Converted

| Platform     | Commands                   | Agents                          | Skills                       | MCP Config                |
| ------------ | -------------------------- | ------------------------------- | ---------------------------- | ------------------------- |
| **Copilot**  | `.github/skills/`          | `.github/agents/*.agent.md`     | `.github/skills/`            | `copilot-mcp-config.json` |
| **Cursor**   | Sync only                  | Sync only                       | `.cursor/skills/` (symlinks) | `.cursor/mcp.json`        |
| **Windsurf** | `workflows/*.md`           | `skills/*/SKILL.md`             | `skills/`                    | `mcp_config.json`         |
| **Gemini**   | `.gemini/commands/*.toml`  | `.gemini/skills/`               | `.gemini/skills/`            | `settings.json`           |
| **OpenCode** | `commands/*.md`            | `agents/*.md`                   | `skills/`                    | `opencode.json`           |
| **Codex**    | `prompts/*.md` + `skills/` | `skills/*/SKILL.md`             | `skills/`                    | `config.toml`             |
| **Kiro**     | `.kiro/skills/`            | `.kiro/agents/*.json` + prompts | `.kiro/skills/`              | `mcp.json`                |
| **Droid**    | `commands/*.md`            | `agents/*.md`                   | `skills/`                    | `mcp.json`                |
| **Pi**       | `prompts/*.md`             | `skills/*/SKILL.md`             | `skills/`                    | `mcp.json`                |
| **OpenClaw** | `commands/*.md`            | `agents/*.md`                   | `skills/`                    | TS entry point            |
| **Qwen**     | `commands/*.md`            | `agents/*.yaml`                 | `skills/`                    | N/A                       |

The plugin provides:

* **7 slash commands** for the full compound engineering workflow

* **33 specialized agents** across 7 categories

* **<span data-proof="suggestion" data-id="m1775681125163_3" data-by="ai:claude" data-kind="replace">12 skills</span>** <span data-proof="suggestion" data-id="m1775681125163_3" data-by="ai:claude" data-kind="replace">with Salesforce domain knowledge</span>

* **<span data-proof="suggestion" data-id="m1775681125163_3" data-by="ai:claude" data-kind="replace">MCP integration</span>** <span data-proof="suggestion" data-id="m1775681125163_3" data-by="ai:claude" data-kind="replace">with Context7 for live framework documentation</span>

* **Institutional knowledge system** in `docs/solutions/` with YAML schema

* **Index-based routing** for low-context, selective agent/skill dispatch

***

## <span data-proof="authored" data-by="ai:claude">How It Works</span>

<span data-proof="authored" data-by="ai:claude">Commands tell Claude the</span> **<span data-proof="authored" data-by="ai:claude">goal</span>** <span data-proof="authored" data-by="ai:claude">and</span> **<span data-proof="authored" data-by="ai:claude">where to find knowledge</span>**<span data-proof="authored" data-by="ai:claude">. Claude decides</span> **<span data-proof="authored" data-by="ai:claude">which agents and skills are relevant</span>** <span data-proof="authored" data-by="ai:claude">for each specific task.</span>

### <span data-proof="authored" data-by="ai:claude">Index-Based Routing</span>

```
agents/index.md  →  Classification → Dispatch relevant agents in parallel
skills/index.md  →  Classification → Read only relevant skill sections
```

<span data-proof="suggestion" data-id="m1775681125157_2" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">Classifications:</span></span> <span data-proof="suggestion" data-id="m1775681125157_2" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">`APEX`,</span></span> <span data-proof="suggestion" data-id="m1775681125157_2" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">`AUTOMATION`,</span></span> <span data-proof="suggestion" data-id="m1775681125157_2" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">`LWC`,</span></span> <span data-proof="suggestion" data-id="m1775681125157_2" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">`INTEGRATION`,</span></span> <span data-proof="suggestion" data-id="m1775681125157_2" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">`ARCHITECTURE`,</span></span> <span data-proof="suggestion" data-id="m1775681125157_2" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">`WORKFLOW`,</span></span> <span data-proof="suggestion" data-id="m1775681125157_2" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">`TOOLING`</span></span>

***

## <span data-proof="authored" data-by="ai:claude">7 Commands</span>

| <span data-proof="authored" data-by="ai:claude">Command</span>          | <span data-proof="authored" data-by="ai:claude">Purpose</span>                                                                                                                                                               |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`/sf-brainstorm`</span> | <span data-proof="authored" data-by="ai:claude">Explore requirements through collaborative dialogue</span>                                                                                                                   |
| <span data-proof="authored" data-by="ai:claude">`/sf-plan`</span>       | <span data-proof="authored" data-by="ai:claude">Research & design specs with parallel agent research (NO CODE)</span>                                                                                                        |
| <span data-proof="authored" data-by="ai:claude">`/sf-deepen`</span>     | <span data-proof="authored" data-by="ai:claude">Enhance plan sections with parallel deep research</span>                                                                                                                     |
| <span data-proof="authored" data-by="ai:claude">`/sf-work`</span>       | <span data-proof="authored" data-by="ai:claude">Implement with pre-research, skills routing, and test checks</span>                                                                                                          |
| <span data-proof="authored" data-by="ai:claude">`/sf-review`</span>     | <span data-proof="authored" data-by="ai:claude">Review with parallel agent dispatch (fast/thorough/comprehensive)</span>                                                                                                     |
| <span data-proof="authored" data-by="ai:claude">`/sf-compound`</span>   | <span data-proof="authored" data-by="ai:claude">Capture learnings to</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`</span> <span data-proof="authored" data-by="ai:claude">with YAML schema</span> |
| <span data-proof="authored" data-by="ai:claude">`/sf-lfg`</span>        | <span data-proof="authored" data-by="ai:claude">Full autonomous pipeline — plan through deploy in one command</span>                                                                                                         |

### <span data-proof="authored" data-by="ai:claude">`/sf-lfg`</span> <span data-proof="authored" data-by="ai:claude">— The Full Pipeline</span>

```
Plan → Deepen → Work → Review → Resolve → Test → Deploy → Compound
```

<span data-proof="authored" data-by="ai:claude">Each stage has gates that must pass before proceeding. Aborts and asks for input on security issues, repeated test failures, or deployment validation problems.</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NzEsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
/sf-lfg "Lead auto-assignment flow based on territory" --deploy=scratch
```

***

## <span data-proof="authored" data-by="ai:claude">33 Agents by Category</span>

### <span data-proof="authored" data-by="ai:claude">Apex (6 agents)</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                  | <span data-proof="authored" data-by="ai:claude">Checks For</span>                              |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Governor Guardian</span>      | <span data-proof="authored" data-by="ai:claude">SOQL/DML in loops, limit compliance</span>     |
| <span data-proof="authored" data-by="ai:claude">Security Sentinel</span>      | <span data-proof="authored" data-by="ai:claude">CRUD/FLS, SOQL injection, credentials</span>   |
| <span data-proof="authored" data-by="ai:claude">Bulkification Reviewer</span> | <span data-proof="authored" data-by="ai:claude">200+ record handling, collections</span>       |
| <span data-proof="authored" data-by="ai:claude">Trigger Architect</span>      | <span data-proof="authored" data-by="ai:claude">One trigger per object, handler pattern</span> |
| <span data-proof="authored" data-by="ai:claude">Test Coverage Analyst</span>  | <span data-proof="authored" data-by="ai:claude">Assertions, bulk tests, coverage</span>        |
| <span data-proof="authored" data-by="ai:claude">Exception Handler</span>      | <span data-proof="authored" data-by="ai:claude">Error handling, custom exceptions</span>       |

### <span data-proof="authored" data-by="ai:claude">LWC (5 agents)</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                   | <span data-proof="authored" data-by="ai:claude">Checks For</span>                            |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Architecture Strategist</span> | <span data-proof="authored" data-by="ai:claude">Component hierarchy, state management</span> |
| <span data-proof="authored" data-by="ai:claude">Performance Oracle</span>      | <span data-proof="authored" data-by="ai:claude">Wire vs imperative, rendering</span>         |
| <span data-proof="authored" data-by="ai:claude">Security Reviewer</span>       | <span data-proof="authored" data-by="ai:claude">XSS, CSP compliance</span>                   |
| <span data-proof="authored" data-by="ai:claude">Accessibility Guardian</span>  | <span data-proof="authored" data-by="ai:claude">ARIA, keyboard navigation</span>             |
| <span data-proof="authored" data-by="ai:claude">Aura Migration Advisor</span>  | <span data-proof="authored" data-by="ai:claude">Migration candidates</span>                  |

### <span data-proof="authored" data-by="ai:claude">Automation (4 agents)</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                         | <span data-proof="authored" data-by="ai:claude">Checks For</span>                      |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Flow Governor Monitor</span>         | <span data-proof="authored" data-by="ai:claude">DML/SOQL in loops, limits</span>       |
| <span data-proof="authored" data-by="ai:claude">Flow Complexity Analyzer</span>      | <span data-proof="authored" data-by="ai:claude">Element count, decision depth</span>   |
| <span data-proof="authored" data-by="ai:claude">Process Automation Strategist</span> | <span data-proof="authored" data-by="ai:claude">Flow vs Apex decisions</span>          |
| <span data-proof="authored" data-by="ai:claude">Validation Rule Reviewer</span>      | <span data-proof="authored" data-by="ai:claude">Rule complexity, error messages</span> |

### <span data-proof="authored" data-by="ai:claude">Integration (4 agents)</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                         | <span data-proof="authored" data-by="ai:claude">Checks For</span>                       |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">REST API Architect</span>            | <span data-proof="authored" data-by="ai:claude">Endpoint design, versioning</span>      |
| <span data-proof="authored" data-by="ai:claude">Callout Pattern Reviewer</span>      | <span data-proof="authored" data-by="ai:claude">Named Credentials, retry logic</span>   |
| <span data-proof="authored" data-by="ai:claude">Platform Event Strategist</span>     | <span data-proof="authored" data-by="ai:claude">Event design, replay handling</span>    |
| <span data-proof="authored" data-by="ai:claude">Integration Security Sentinel</span> | <span data-proof="authored" data-by="ai:claude">Auth, certificates, data transit</span> |

### <span data-proof="authored" data-by="ai:claude">Architecture (4 agents)</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                          | <span data-proof="authored" data-by="ai:claude">Checks For</span>                      |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Data Model Architect</span>           | <span data-proof="authored" data-by="ai:claude">Relationships, field design</span>     |
| <span data-proof="authored" data-by="ai:claude">Sharing Security Analyst</span>       | <span data-proof="authored" data-by="ai:claude">OWD, sharing rules, permissions</span> |
| <span data-proof="authored" data-by="ai:claude">Pattern Recognition Specialist</span> | <span data-proof="authored" data-by="ai:claude">God classes, duplicate code</span>     |
| <span data-proof="authored" data-by="ai:claude">Metadata Consistency Checker</span>   | <span data-proof="authored" data-by="ai:claude">Naming, API versions</span>            |

### <span data-proof="authored" data-by="ai:claude">Research (5 agents)</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                     | <span data-proof="authored" data-by="ai:claude">Model</span>  | <span data-proof="authored" data-by="ai:claude">Purpose</span>                                                                                                                                                    |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Learnings Researcher</span>      | <span data-proof="authored" data-by="ai:claude">haiku</span>  | <span data-proof="authored" data-by="ai:claude">Search</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`</span> <span data-proof="authored" data-by="ai:claude">by YAML frontmatter</span> |
| <span data-proof="authored" data-by="ai:claude">Best Practices Researcher</span> | <span data-proof="authored" data-by="ai:claude">sonnet</span> | <span data-proof="authored" data-by="ai:claude">Skills → Context7 → web validation</span>                                                                                                                         |
| <span data-proof="authored" data-by="ai:claude">Git History Analyzer</span>      | <span data-proof="authored" data-by="ai:claude">haiku</span>  | <span data-proof="authored" data-by="ai:claude">Git archaeology for SF metadata evolution</span>                                                                                                                  |
| <span data-proof="authored" data-by="ai:claude">Repo Research Analyst</span>     | <span data-proof="authored" data-by="ai:claude">haiku</span>  | <span data-proof="authored" data-by="ai:claude">Project structure and conventions</span>                                                                                                                          |
| <span data-proof="authored" data-by="ai:claude">Framework Docs Researcher</span> | <span data-proof="authored" data-by="ai:claude">sonnet</span> | <span data-proof="authored" data-by="ai:claude">SF platform docs via Context7 + web</span>                                                                                                                        |

### <span data-proof="authored" data-by="ai:claude">Workflow (5 agents)</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                      | <span data-proof="authored" data-by="ai:claude">Model</span>  | <span data-proof="authored" data-by="ai:claude">Purpose</span>                                        |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Spec Flow Analyzer</span>         | <span data-proof="authored" data-by="ai:claude">sonnet</span> | <span data-proof="authored" data-by="ai:claude">Trigger permutation matrix, gap identification</span> |
| <span data-proof="authored" data-by="ai:claude">Bug Reproduction Validator</span> | <span data-proof="authored" data-by="ai:claude">sonnet</span> | <span data-proof="authored" data-by="ai:claude">Systematic 6-step bug reproduction</span>             |
| <span data-proof="authored" data-by="ai:claude">PR Comment Resolver</span>        | <span data-proof="authored" data-by="ai:claude">haiku</span>  | <span data-proof="authored" data-by="ai:claude">Parallel PR comment resolution</span>                 |
| <span data-proof="authored" data-by="ai:claude">Code Simplicity Reviewer</span>   | <span data-proof="authored" data-by="ai:claude">haiku</span>  | <span data-proof="authored" data-by="ai:claude">YAGNI enforcement, LOC reduction</span>               |
| <span data-proof="authored" data-by="ai:claude">Deployment Verification</span>    | <span data-proof="authored" data-by="ai:claude">sonnet</span> | <span data-proof="authored" data-by="ai:claude">Go/No-Go checklists, rollback procedures</span>       |

***

## <span data-proof="suggestion" data-id="m1775681150499_4" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">12 Skills</span></span>

### <span data-proof="authored" data-by="ai:claude">Domain Skills</span>

| <span data-proof="authored" data-by="ai:claude">Skill</span>                  | <span data-proof="authored" data-by="ai:claude">Scope</span>            | <span data-proof="authored" data-by="ai:claude">Use When</span>                          |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`governor-limits`</span>      | <span data-proof="authored" data-by="ai:claude">Universal</span>        | <span data-proof="authored" data-by="ai:claude">Any Apex, Flow, or trigger work</span>   |
| <span data-proof="authored" data-by="ai:claude">`apex-patterns`</span>        | <span data-proof="authored" data-by="ai:claude">Apex only</span>        | <span data-proof="authored" data-by="ai:claude">Apex classes, triggers, services</span>  |
| <span data-proof="authored" data-by="ai:claude">`flow-patterns`</span>        | <span data-proof="authored" data-by="ai:claude">Automation only</span>  | <span data-proof="authored" data-by="ai:claude">Building any type of Flow</span>         |
| <span data-proof="authored" data-by="ai:claude">`lwc-patterns`</span>         | <span data-proof="authored" data-by="ai:claude">LWC only</span>         | <span data-proof="authored" data-by="ai:claude">Lightning Web Components</span>          |
| <span data-proof="authored" data-by="ai:claude">`security-guide`</span>       | <span data-proof="authored" data-by="ai:claude">Universal</span>        | <span data-proof="authored" data-by="ai:claude">CRUD/FLS, sharing, permissions</span>    |
| <span data-proof="authored" data-by="ai:claude">`integration-patterns`</span> | <span data-proof="authored" data-by="ai:claude">Integration only</span> | <span data-proof="authored" data-by="ai:claude">Callouts, APIs, Platform Events</span>   |
| <span data-proof="authored" data-by="ai:claude">`test-factory`</span>         | <span data-proof="authored" data-by="ai:claude">Apex only</span>        | <span data-proof="authored" data-by="ai:claude">Test classes, test data factories</span> |

### <span data-proof="authored" data-by="ai:claude">Workflow Skills</span>

| <span data-proof="authored" data-by="ai:claude">Skill</span>           | <span data-proof="authored" data-by="ai:claude">Use When</span>                                             |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`sf-cli`</span>        | <span data-proof="authored" data-by="ai:claude">Deploy, retrieve, test, org management</span>               |
| <span data-proof="authored" data-by="ai:claude">`compound-docs`</span> | <span data-proof="authored" data-by="ai:claude">Writing solution documents with YAML schema</span>          |
| <span data-proof="authored" data-by="ai:claude">`file-todos`</span>    | <span data-proof="authored" data-by="ai:claude">File-based task tracking with status/priority naming</span> |

### <span data-proof="authored" data-by="ai:claude">Tooling Skills</span>

| <span data-proof="authored" data-by="ai:claude">Skill</span>                 | <span data-proof="authored" data-by="ai:claude">Use When</span>                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`git-worktree`</span>        | <span data-proof="authored" data-by="ai:claude">Isolated parallel development branches</span>        |
| <span data-proof="authored" data-by="ai:claude">`create-agent-skills`</span> | <span data-proof="authored" data-by="ai:claude">Creating new agents and skills for the plugin</span> |

***

## <span data-proof="authored" data-by="ai:claude">Knowledge System</span>

<span data-proof="authored" data-by="ai:claude">Learnings are captured in</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`</span> <span data-proof="authored" data-by="ai:claude">with YAML frontmatter and organized by category:</span>

```
docs/solutions/
├── governor-limit-issues/   # Limit handling patterns
├── deployment-issues/       # CI/CD and deployment fixes
├── test-failures/           # Test troubleshooting guides
├── security-issues/         # Security implementations
├── integration-issues/      # External system patterns
├── flow-issues/             # Automation solutions
├── lwc-issues/              # Component solutions
├── data-model-issues/       # Schema design decisions
├── best-practices/          # Proven patterns and approaches
└── patterns/                # Reusable code patterns
```

<span data-proof="authored" data-by="ai:claude">The</span> <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher`</span> <span data-proof="authored" data-by="ai:claude">agent searches these documents by frontmatter metadata before every plan and implementation phase to surface relevant institutional knowledge.</span>

***

## <span data-proof="authored" data-by="ai:claude">Project Structure</span>

```
sf-compound-engineering-plugin/
├── .claude-plugin/
│   ├── plugin.json           # Plugin manifest (v2.0.0)
│   └── marketplace.json      # Marketplace loader schema
├── .mcp.json                 # Context7 MCP server config
├── schema.yaml               # YAML validation for docs/solutions/
├── CLAUDE.md                 # Project context and protected artifacts
├── hooks/
│   └── hooks.json            # Pre/post tool-use hooks
├── cli/                      # Multi-tool installer CLI
│   ├── package.json           # @sangameshgupta/sf-compound-plugin
│   ├── src/
│   │   ├── index.ts           # CLI entry (citty)
│   │   ├── parser/            # Plugin reader + markdown parser
│   │   ├── converters/        # 11 platform converters
│   │   ├── transforms/        # Path, reference, frontmatter rewriting
│   │   └── utils/             # Auto-detect, merge helpers
│   └── tests/
├── commands/                 # 7 slash commands
│   ├── sf-brainstorm.md
│   ├── sf-plan.md
│   ├── sf-deepen.md
│   ├── sf-work.md
│   ├── sf-review.md
│   ├── sf-compound.md
│   └── sf-lfg.md
├── agents/                   # 33 agents
│   ├── index.md              # Agent routing map
│   ├── apex/                 # 6 Apex agents
│   ├── lwc/                  # 5 LWC agents
│   ├── automation/           # 4 Flow/automation agents
│   ├── integration/          # 4 integration agents
│   ├── architecture/         # 4 architecture agents
│   ├── research/             # 5 research agents
│   └── workflow/             # 5 workflow agents
├── skills/                   # 12 skills
│   ├── index.md              # Skill routing map
│   ├── governor-limits/
│   ├── apex-patterns/
│   ├── flow-patterns/
│   ├── lwc-patterns/
│   ├── security-guide/
│   ├── integration-patterns/
│   ├── test-factory/
│   ├── sf-cli/
│   ├── compound-docs/
│   ├── git-worktree/
│   ├── create-agent-skills/
│   └── file-todos/
└── docs/
    ├── brainstorms/          # Brainstorm outputs
    ├── plans/                # Feature plans
    └── solutions/            # Institutional knowledge (10 categories)
```

***

## <span data-proof="authored" data-by="ai:claude">MCP Integration</span>

<span data-proof="suggestion" data-id="m1775681196339_10" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">The plugin includes a Context7 MCP server for live framework documentation lookup:</span></span>

```json proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MzcsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19LHsidHlwZSI6InByb29mU3VnZ2VzdGlvbiIsImZyb20iOjM3LCJ0byI6MTMzLCJhdHRycyI6eyJpZCI6Im0xNzc1NjgxMTk2MzM0XzkiLCJraW5kIjoiaW5zZXJ0IiwiYnkiOiJhaTpjbGF1ZGUiLCJjb250ZW50IjoiXG4gICAgICBcInR5cGVcIjogXCJodHRwXCIsXG4gICAgICBcInVybFwiOiBcImh0dHBzOi8vbWNwLmNvbnRleHQ3LmNvbS9tY3BcIlxuICAgIH0sXG4gICAgXCJzYWxlc2ZvcmNlLWR4XCI6IHsiLCJzdGF0dXMiOiJwZW5kaW5nIiwiY3JlYXRlZEF0IjoiMjAyNi0wNC0wOFQyMDo0NjozNi4zMzRaIiwicnVuSWQiOm51bGwsImZvY3VzQXJlYUlkIjpudWxsLCJmb2N1c0FyZWFOYW1lIjpudWxsLCJhZ2VudElkIjpudWxsLCJwcm9wb3NhbElkIjpudWxsLCJwcm92aXNpb25hbCI6bnVsbCwib3JjaGVzdHJhdG9yIjpudWxsLCJkZWJ1Z0F1dG9GaXhlZFF1b3RlcyI6bnVsbCwiZGVidWdBdXRvRml4ZWRRdW90ZXNSZWFzb24iOm51bGx9fSx7InR5cGUiOiJwcm9vZkF1dGhvcmVkIiwiZnJvbSI6MzcsInRvIjoyMjIsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19LHsidHlwZSI6InByb29mU3VnZ2VzdGlvbiIsImZyb20iOjIyMiwidG8iOjgyOSwiYXR0cnMiOnsiaWQiOiJtMTc3NTY4MTE5NjMyOV84Iiwia2luZCI6Imluc2VydCIsImJ5IjoiYWk6Y2xhdWRlIiwiY29udGVudCI6IlxuU2FsZXNmb3JjZSBEWCBNQ1AgdG9vbHNldHMgKGFsbCBlbmFibGVkKTpcblRvb2xzZXRcbkNhcGFiaWxpdHlcbmNvcmVcbkJhc2UgRFggdG9vbHMgKGFsd2F5cyBvbilcbm9yZ3Ncbk1hbmFnZSBhdXRob3JpemVkIG9yZ3Ncbm1ldGFkYXRhXG5EZXBsb3kvcmV0cmlldmUgbWV0YWRhdGFcbmRhdGFcblNPUUwgcXVlcmllcywgcmVjb3JkIG1hbmFnZW1lbnRcbnVzZXJzXG5QZXJtaXNzaW9uIHNldHMsIHVzZXIgbWFuYWdlbWVudFxuY29kZS1hbmFseXNpc1xuU3RhdGljIGFuYWx5c2lzIHZpYSBDb2RlIEFuYWx5emVyXG5sd2MtZXhwZXJ0c1xuTFdDIGRldmVsb3BtZW50LCB0ZXN0aW5nLCBvcHRpbWl6YXRpb25cbmF1cmEtZXhwZXJ0c1xuQXVyYSBhbmFseXNpcywgTFdDIG1pZ3JhdGlvblxuZXhwZXJ0cy12YWxpZGF0aW9uXG5MV0MgcHJvZHVjdGlvbiByZWFkaW5lc3MgY2hlY2tzXG5kZXZvcHNcbkRldk9wcyBDZW50ZXIgb3BlcmF0aW9uc1xuZW5yaWNobWVudFxuTWV0YWRhdGEgY29tcG9uZW50IGVucmljaG1lbnRcbm1vYmlsZVxuTW9iaWxlIGRldmVsb3BtZW50IHRvb2xzXG50ZXN0aW5nXG5BcGV4IGFuZCBhZ2VudCB0ZXN0IGV4ZWN1dGlvblxuc2NhbGUtcHJvZHVjdHNcbkFwZXggcGVyZm9ybWFuY2UgZGV0ZWN0aW9uIiwic3RhdHVzIjoicGVuZGluZyIsImNyZWF0ZWRBdCI6IjIwMjYtMDQtMDhUMjA6NDY6MzYuMzI5WiIsInJ1bklkIjpudWxsLCJmb2N1c0FyZWFJZCI6bnVsbCwiZm9jdXNBcmVhTmFtZSI6bnVsbCwiYWdlbnRJZCI6bnVsbCwicHJvcG9zYWxJZCI6bnVsbCwicHJvdmlzaW9uYWwiOm51bGwsIm9yY2hlc3RyYXRvciI6bnVsbCwiZGVidWdBdXRvRml4ZWRRdW90ZXMiOm51bGwsImRlYnVnQXV0b0ZpeGVkUXVvdGVzUmVhc29uIjpudWxsfX0seyJ0eXBlIjoicHJvb2ZBdXRob3JlZCIsImZyb20iOjIyMiwidG8iOjgyOSwiYXR0cnMiOnsiYnkiOiJhaTpjbGF1ZGUifX1d
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp"
    },
    "salesforce-dx": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
Salesforce DX MCP toolsets (all enabled):
Toolset
Capability
core
Base DX tools (always on)
orgs
Manage authorized orgs
metadata
Deploy/retrieve metadata
data
SOQL queries, record management
users
Permission sets, user management
code-analysis
Static analysis via Code Analyzer
lwc-experts
LWC development, testing, optimization
aura-experts
Aura analysis, LWC migration
experts-validation
LWC production readiness checks
devops
DevOps Center operations
enrichment
Metadata component enrichment
mobile
Mobile development tools
testing
Apex and agent test execution
scale-products
Apex performance detection
```

<span data-proof="authored" data-by="ai:claude">Research agents use Context7 as the second tier (after local skills) before falling back to web search.</span><span data-proof="suggestion" data-id="m1775681196325_7" data-by="ai:claude" data-kind="insert"><span data-proof="authored" data-by="ai:claude">
Prerequisites for Salesforce DX MCP: Authorize an org first with sf org login web. The server uses DEFAULT_TARGET_ORG — whatever you set with sf config set target-org.</span></span>

***

## <span data-proof="authored" data-by="ai:claude">Requirements</span>

* <span data-proof="authored" data-by="ai:claude">Claude Code</span><span data-proof="suggestion" data-id="m1775681196320_6" data-by="ai:claude" data-kind="insert"><span data-proof="authored" data-by="ai:claude">
  Node.js (for MCP servers)</span></span>

* <span data-proof="authored" data-by="ai:claude">Git (recommended)</span>

* <span data-proof="suggestion" data-id="m1775681196313_5" data-by="ai:claude" data-kind="replace"><span data-proof="authored" data-by="ai:claude">Node.js (for Context7 MCP server)</span></span>

***

## <span data-proof="authored" data-by="ai:claude">Contributing</span>

<span data-proof="authored" data-by="ai:claude">Contributions welcome! Key areas:</span>

* <span data-proof="authored" data-by="ai:claude">Add new agents for specialized reviews</span>

* <span data-proof="authored" data-by="ai:claude">Expand skills with more patterns</span>

* <span data-proof="authored" data-by="ai:claude">Improve index files for better routing</span>

* <span data-proof="authored" data-by="ai:claude">Add solution documents to</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`</span>

<span data-proof="authored" data-by="ai:claude">See</span> <span data-proof="authored" data-by="ai:claude">`skills/create-agent-skills/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">for agent/skill authoring guidance.</span>

***

## <span data-proof="authored" data-by="ai:claude">License</span>

<span data-proof="authored" data-by="ai:claude">MIT License</span>

***

## <span data-proof="authored" data-by="ai:claude">Credits</span>

* <span data-proof="authored" data-by="ai:claude">Built for the Salesforce developer community</span>

* <span data-proof="authored" data-by="ai:claude">Inspired by</span> [<span data-proof="authored" data-by="ai:claude">EveryInc's Compound Engineering Plugin</span>](https://github.com/EveryInc/compound-engineering-plugin)

* <span data-proof="authored" data-by="ai:claude">Inspired by</span> [<span data-proof="authored" data-by="ai:claude">GitHub Spec-Kit</span>](https://github.com/github/spec-kit)

* <span data-proof="authored" data-by="ai:claude">Powered by Claude Code</span>

<!-- PROOF
{
  "version": 2,
  "marks": {
    "m1775681125163_3": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:45:25.163Z",
      "range": {
        "from": 3743,
        "to": 3851
      },
      "content": "14 skills with Salesforce domain knowledge (including Agentforce Agent Script & Prompt Builder)\nMCP integration with Context7 for framework docs + Salesforce DX MCP for live org operations (60+ tools)",
      "status": "pending"
    },
    "m1775681125157_2": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:45:25.157Z",
      "range": {
        "from": 4314,
        "to": 4398
      },
      "content": "Classifications: APEX, AUTOMATION, LWC, INTEGRATION, AGENTFORCE SCRIPT BUILDER, AGENTFORCE PROMPT BUILDER, ARCHITECTURE, WORKFLOW, TOOLING",
      "status": "pending"
    },
    "m1775681150499_4": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:45:50.499Z",
      "range": {
        "from": 7874,
        "to": 7883
      },
      "content": "14 Skills\nAgentforce Skills\nSkill\nScope\nUse When\nagent-script\nAgentforce Script Builder\nBuilding Agentforce agents — language syntax, blocks, variables, flow control, patterns\nprompt-builder\nAgentforce Prompt Builder\nCreating prompt templates — metadata XML generation, Apex/LWC/API integration, merge fields, grounding",
      "status": "pending"
    },
    "m1775681215356_18": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:55.356Z",
      "range": {
        "from": 9866,
        "to": 9924
      },
      "content": "├── .mcp.json                 # MCP server config (Context7 + Salesforce DX)",
      "status": "pending"
    },
    "m1775681215352_17": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:55.352Z",
      "range": {
        "from": 11231,
        "to": 11272
      },
      "content": "├── skills/                   # 14 skills",
      "status": "pending"
    },
    "m1775681215346_16": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:55.346Z",
      "range": {
        "from": 11322,
        "to": 11459
      },
      "content": "\n│   ├── agent-script/         # Agentforce Agent Script language\n│   ├── prompt-builder/       # Prompt Builder templates & metadata XML",
      "status": "pending"
    },
    "m1775681215338_15": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:55.338Z",
      "range": {
        "from": 11937,
        "to": 12019
      },
      "content": "The plugin integrates two MCP servers:\nMCP Server\nPurpose\nTools\nContext7\nFramework documentation lookup\nDocs search, library resolution\nSalesforce DX (@salesforce/mcp)\nLive org operations\n60+ tools — SOQL, deploy, retrieve, code analysis, LWC experts, DevOps, mobile, testing",
      "status": "pending"
    },
    "m1775681196334_9": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:36.334Z",
      "range": {
        "from": 12058,
        "to": 12154
      },
      "content": "\n      \"type\": \"http\",\n      \"url\": \"https://mcp.context7.com/mcp\"\n    },\n    \"salesforce-dx\": {",
      "status": "pending"
    },
    "m1775681196329_8": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:36.329Z",
      "range": {
        "from": 12243,
        "to": 12850
      },
      "content": "\nSalesforce DX MCP toolsets (all enabled):\nToolset\nCapability\ncore\nBase DX tools (always on)\norgs\nManage authorized orgs\nmetadata\nDeploy/retrieve metadata\ndata\nSOQL queries, record management\nusers\nPermission sets, user management\ncode-analysis\nStatic analysis via Code Analyzer\nlwc-experts\nLWC development, testing, optimization\naura-experts\nAura analysis, LWC migration\nexperts-validation\nLWC production readiness checks\ndevops\nDevOps Center operations\nenrichment\nMetadata component enrichment\nmobile\nMobile development tools\ntesting\nApex and agent test execution\nscale-products\nApex performance detection",
      "status": "pending"
    },
    "m1775681196325_7": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:36.325Z",
      "range": {
        "from": 12955,
        "to": 13123
      },
      "content": "\nPrerequisites for Salesforce DX MCP: Authorize an org first with sf org login web. The server uses DEFAULT_TARGET_ORG — whatever you set with sf config set target-org.",
      "status": "pending"
    },
    "m1775681196320_6": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:36.320Z",
      "range": {
        "from": 13153,
        "to": 13179
      },
      "content": "\nNode.js (for MCP servers)",
      "status": "pending"
    },
    "m1775681215332_14": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:55.332Z",
      "range": {
        "from": 13204,
        "to": 13237
      },
      "content": "Salesforce CLI + authorized org (for Salesforce DX MCP — optional, plugin works without it)",
      "status": "pending"
    }
  }
}
-->

<!-- PROOF:END -->
