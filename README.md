# <span data-proof="authored" data-by="ai:claude">SF Compound Engineering Plugin v3.0.0-beta.1</span>

**<span data-proof="authored" data-by="ai:claude">Instruction-Based Compound Engineering for Salesforce</span>** <span data-proof="authored" data-by="ai:claude">— a multi-platform plugin (Claude Code, Cursor, Codex) where each iteration becomes smarter than the last through institutional knowledge capture and parallel agent dispatch.</span>

> **v3.0.0 is a BREAKING release.** Skills replace commands, agents flatten under `agents/<name>.agent.md`, and multi-platform manifests ship for Cursor and Codex alongside Claude Code. See [`CHANGELOG.md`](./CHANGELOG.md) for the full migration guide for v2.x users.

Multi-platform Salesforce-focused plugin for compound engineering workflows. See the **Credits** section at the bottom for inspiration sources.

***

## <span data-proof="authored" data-by="ai:claude">The Compound Engineering Loop</span>

```
Brainstorm → Plan (40%) → Deepen → Work (20%) → Review (20%) → Compound (20%) → Repeat
     │            │           │          │              │               │
     │            │           │          │              │               └── Capture to docs/solutions/
     │            │           │          │              └── Parallel agent dispatch (59 agents)
     │            │           │          └── Implement with pre-research + test checks
     │            │           └── Enhance plan with section-level parallel research
     │            └── Research & design using 45 skills + parallel research agents
     └── Explore requirements through collaborative dialogue
```

> <span data-proof="authored" data-by="ai:claude">All seven entry points (`/sf-brainstorm`,</span> <span data-proof="authored" data-by="ai:claude">`/sf-plan`,</span> <span data-proof="authored" data-by="ai:claude">`/sf-deepen`,</span> <span data-proof="authored" data-by="ai:claude">`/sf-work`,</span> <span data-proof="authored" data-by="ai:claude">`/sf-review`,</span> <span data-proof="authored" data-by="ai:claude">`/sf-compound`,</span> <span data-proof="authored" data-by="ai:claude">`/sf-lfg`) are</span> **<span data-proof="authored" data-by="ai:claude">skills</span>** <span data-proof="authored" data-by="ai:claude">in V3 — they auto-route from natural-language phrases via their</span> <span data-proof="authored" data-by="ai:claude">`description`</span> <span data-proof="authored" data-by="ai:claude">frontmatter, and direct slash invocation continues to work.</span>

**<span data-proof="authored" data-by="ai:claude">Each iteration starts smarter</span>** <span data-proof="authored" data-by="ai:claude">because learnings compound into</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`, agents, skills, and CLAUDE.md.</span>

***

## <span data-proof="authored" data-by="ai:claude">Quick Start</span>

### <span data-proof="authored" data-by="ai:claude">Claude Code (Native)</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTY5LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
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

| Platform                                                           | Commands                   | <span data-proof="authored" data-by="ai:claude">Agents</span> | Skills                                                                   | MCP Config                                                                       |
| ------------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| **<span data-proof="authored" data-by="ai:claude">Copilot</span>** | `.github/skills/`          | `.github/agents/*.agent.md`                                   | <span data-proof="authored" data-by="ai:claude">`.github/skills/`</span> | <span data-proof="authored" data-by="ai:claude">`copilot-mcp-config.json`</span> |
| **Cursor**                                                         | Sync only                  | Sync only                                                     | `.cursor/skills/` (symlinks)                                             | `.cursor/mcp.json`                                                               |
| **Windsurf**                                                       | `workflows/*.md`           | `skills/*/SKILL.md`                                           | `skills/`                                                                | `mcp_config.json`                                                                |
| **Gemini**                                                         | `.gemini/commands/*.toml`  | `.gemini/skills/`                                             | `.gemini/skills/`                                                        | `settings.json`                                                                  |
| **OpenCode**                                                       | `commands/*.md`            | `agents/*.md`                                                 | `skills/`                                                                | `opencode.json`                                                                  |
| **Codex**                                                          | `prompts/*.md` + `skills/` | `skills/*/SKILL.md`                                           | `skills/`                                                                | `config.toml`                                                                    |
| **Kiro**                                                           | `.kiro/skills/`            | `.kiro/agents/*.json` + prompts                               | `.kiro/skills/`                                                          | `mcp.json`                                                                       |
| **Droid**                                                          | `commands/*.md`            | `agents/*.md`                                                 | `skills/`                                                                | `mcp.json`                                                                       |
| **Pi**                                                             | `prompts/*.md`             | `skills/*/SKILL.md`                                           | `skills/`                                                                | `mcp.json`                                                                       |
| **OpenClaw**                                                       | `commands/*.md`            | `agents/*.md`                                                 | `skills/`                                                                | TS entry point                                                                   |
| **Qwen**                                                           | `commands/*.md`            | `agents/*.yaml`                                               | `skills/`                                                                | N/A                                                                              |

The plugin provides:

* **       

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

## 

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

### 

| <span data-proof="authored" data-by="ai:claude">Agent</span>                         | <span data-proof="authored" data-by="ai:claude">Checks For</span>                       |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">REST API Architect</span>            | <span data-proof="authored" data-by="ai:claude">Endpoint design, versioning</span>      |
| <span data-proof="authored" data-by="ai:claude">Callout Pattern Reviewer</span>      | <span data-proof="authored" data-by="ai:claude">Named Credentials, retry logic</span>   |
| <span data-proof="authored" data-by="ai:claude">Platform Event Strategist</span>     | <span data-proof="authored" data-by="ai:claude">Event design, replay handling</span>    |
| <span data-proof="authored" data-by="ai:claude">Integration Security Sentinel</span> | <span data-proof="authored" data-by="ai:claude">Auth, certificates, data transit</span> |
| MCP Server Config Reviewer                                                           | <br />                                                                                  |
| Hosted MCP setup, ECA configuration, OAuth scopes                                    | <br />                                                                                  |
| MCP Tool Builder                                                                     | <br />                                                                                  |
| Custom MCP tool code quality, @InvocableMethod patterns, descriptions</span></span>  | <br />                                                                                  |

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

## 

### <span data-proof="authored" data-by="ai:claude">Domain Skills</span>

| <span data-proof="authored" data-by="ai:claude">Skill</span>                                            | <span data-proof="authored" data-by="ai:claude">Scope</span>            | <span data-proof="authored" data-by="ai:claude">Use When</span>                          |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`governor-limits`</span>                                | <span data-proof="authored" data-by="ai:claude">Universal</span>        | <span data-proof="authored" data-by="ai:claude">Any Apex, Flow, or trigger work</span>   |
| <span data-proof="authored" data-by="ai:claude">`apex-patterns`</span>                                  | <span data-proof="authored" data-by="ai:claude">Apex only</span>        | <span data-proof="authored" data-by="ai:claude">Apex classes, triggers, services</span>  |
| <span data-proof="authored" data-by="ai:claude">`flow-patterns`</span>                                  | <span data-proof="authored" data-by="ai:claude">Automation only</span>  | <span data-proof="authored" data-by="ai:claude">Building any type of Flow</span>         |
| <span data-proof="authored" data-by="ai:claude">`lwc-patterns`</span>                                   | <span data-proof="authored" data-by="ai:claude">LWC only</span>         | <span data-proof="authored" data-by="ai:claude">Lightning Web Components</span>          |
| <span data-proof="authored" data-by="ai:claude">`security-guide`</span>                                 | <span data-proof="authored" data-by="ai:claude">Universal</span>        | <span data-proof="authored" data-by="ai:claude">CRUD/FLS, sharing, permissions</span>    |
| <span data-proof="authored" data-by="ai:claude">`integration-patterns`</span>                           | <span data-proof="authored" data-by="ai:claude">Integration only</span> | <span data-proof="authored" data-by="ai:claude">Callouts, APIs, Platform Events</span>   |
| <span data-proof="authored" data-by="ai:claude">`test-factory`</span>                                   | <span data-proof="authored" data-by="ai:claude">Apex only</span>        | <span data-proof="authored" data-by="ai:claude">Test classes, test data factories</span> |
| Agentforce Skills                                                                                       | <br />                                                                  | <br />                                                                                   |
| Skill                                                                                                   | <br />                                                                  | <br />                                                                                   |
| Scope                                                                                                   | <br />                                                                  | <br />                                                                                   |
| Use When                                                                                                | <br />                                                                  | <br />                                                                                   |
| agent-script                                                                                            | <br />                                                                  | <br />                                                                                   |
| Agentforce Script Builder                                                                               | <br />                                                                  | <br />                                                                                   |
| Building Agentforce agents — syntax, blocks, variables, patterns                                        | <br />                                                                  | <br />                                                                                   |
| prompt-builder                                                                                          | <br />                                                                  | <br />                                                                                   |
| Agentforce Prompt Builder                                                                               | <br />                                                                  | <br />                                                                                   |
| Prompt templates — metadata XML, merge fields, grounding, deployment                                    | <br />                                                                  | <br />                                                                                   |
| Hosted MCP Skills                                                                                       | <br />                                                                  | <br />                                                                                   |
| Skill                                                                                                   | <br />                                                                  | <br />                                                                                   |
| Scope                                                                                                   | <br />                                                                  | <br />                                                                                   |
| Use When                                                                                                | <br />                                                                  | <br />                                                                                   |
| hosted-mcp-servers                                                                                      | <br />                                                                  | <br />                                                                                   |
| Hosted MCP                                                                                              | <br />                                                                  | <br />                                                                                   |
| Setup, ECA configuration, URL patterns, security model, troubleshooting                                 | <br />                                                                  | <br />                                                                                   |
| mcp-tool-builder                                                                                        | <br />                                                                  | <br />                                                                                   |
| Hosted MCP                                                                                              | <br />                                                                  | <br />                                                                                   |
| Building custom MCP tools — Apex @InvocableMethod, Flows, Named Queries, prompt templates</span></span> | <br />                                                                  | <br />                                                                                   |

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



```json proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MzcsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19LHsidHlwZSI6InByb29mU3VnZ2VzdGlvbiIsImZyb20iOjM3LCJ0byI6MTMzLCJhdHRycyI6eyJpZCI6Im0xNzc1NjgxMTk2MzM0XzkiLCJraW5kIjoiaW5zZXJ0IiwiYnkiOiJhaTpjbGF1ZGUiLCJjb250ZW50IjoiXG4gICAgICBcInR5cGVcIjogXCJodHRwXCIsXG4gICAgICBcInVybFwiOiBcImh0dHBzOi8vbWNwLmNvbnRleHQ3LmNvbS9tY3BcIlxuICAgIH0sXG4gICAgXCJzYWxlc2ZvcmNlLWR4XCI6IHsiLCJzdGF0dXMiOiJwZW5kaW5nIiwiY3JlYXRlZEF0IjoiMjAyNi0wNC0wOFQyMDo0NjozNi4zMzRaIiwicnVuSWQiOm51bGwsImZvY3VzQXJlYUlkIjpudWxsLCJmb2N1c0FyZWFOYW1lIjpudWxsLCJhZ2VudElkIjpudWxsLCJwcm9wb3NhbElkIjpudWxsLCJwcm92aXNpb25hbCI6bnVsbCwib3JjaGVzdHJhdG9yIjpudWxsLCJkZWJ1Z0F1dG9GaXhlZFF1b3RlcyI6bnVsbCwiZGVidWdBdXRvRml4ZWRRdW90ZXNSZWFzb24iOm51bGx9fSx7InR5cGUiOiJwcm9vZlN1Z2dlc3Rpb24iLCJmcm9tIjoyMjIsInRvIjo4MjksImF0dHJzIjp7ImlkIjoibTE3NzU2ODExOTYzMjlfOCIsImtpbmQiOiJpbnNlcnQiLCJieSI6ImFpOmNsYXVkZSIsImNvbnRlbnQiOiJcblNhbGVzZm9yY2UgRFggTUNQIHRvb2xzZXRzIChhbGwgZW5hYmxlZCk6XG5Ub29sc2V0XG5DYXBhYmlsaXR5XG5jb3JlXG5CYXNlIERYIHRvb2xzIChhbHdheXMgb24pXG5vcmdzXG5NYW5hZ2UgYXV0aG9yaXplZCBvcmdzXG5tZXRhZGF0YVxuRGVwbG95L3JldHJpZXZlIG1ldGFkYXRhXG5kYXRhXG5TT1FMIHF1ZXJpZXMsIHJlY29yZCBtYW5hZ2VtZW50XG51c2Vyc1xuUGVybWlzc2lvbiBzZXRzLCB1c2VyIG1hbmFnZW1lbnRcbmNvZGUtYW5hbHlzaXNcblN0YXRpYyBhbmFseXNpcyB2aWEgQ29kZSBBbmFseXplclxubHdjLWV4cGVydHNcbkxXQyBkZXZlbG9wbWVudCwgdGVzdGluZywgb3B0aW1pemF0aW9uXG5hdXJhLWV4cGVydHNcbkF1cmEgYW5hbHlzaXMsIExXQyBtaWdyYXRpb25cbmV4cGVydHMtdmFsaWRhdGlvblxuTFdDIHByb2R1Y3Rpb24gcmVhZGluZXNzIGNoZWNrc1xuZGV2b3BzXG5EZXZPcHMgQ2VudGVyIG9wZXJhdGlvbnNcbmVucmljaG1lbnRcbk1ldGFkYXRhIGNvbXBvbmVudCBlbnJpY2htZW50XG5tb2JpbGVcbk1vYmlsZSBkZXZlbG9wbWVudCB0b29sc1xudGVzdGluZ1xuQXBleCBhbmQgYWdlbnQgdGVzdCBleGVjdXRpb25cbnNjYWxlLXByb2R1Y3RzXG5BcGV4IHBlcmZvcm1hbmNlIGRldGVjdGlvbiIsInN0YXR1cyI6InBlbmRpbmciLCJjcmVhdGVkQXQiOiIyMDI2LTA0LTA4VDIwOjQ2OjM2LjMyOVoiLCJydW5JZCI6bnVsbCwiZm9jdXNBcmVhSWQiOm51bGwsImZvY3VzQXJlYU5hbWUiOm51bGwsImFnZW50SWQiOm51bGwsInByb3Bvc2FsSWQiOm51bGwsInByb3Zpc2lvbmFsIjpudWxsLCJvcmNoZXN0cmF0b3IiOm51bGwsImRlYnVnQXV0b0ZpeGVkUXVvdGVzIjpudWxsLCJkZWJ1Z0F1dG9GaXhlZFF1b3Rlc1JlYXNvbiI6bnVsbH19XQ==
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

* 

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
    "m1777279526790_2": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-27T08:45:26.790Z",
      "range": {
        "from": 520,
        "to": 581
      },
      "content": "Multi-platform Salesforce-focused plugin for compound engineering workflows. See the Credits section at the bottom for inspiration sources.",
      "status": "pending"
    },
    "m1777125750945_7": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-25T14:02:30.945Z",
      "range": {
        "from": 4181,
        "to": 4467
      },
      "content": "7 core workflow skills (/sf-brainstorm, /sf-plan, /sf-deepen, /sf-work, /sf-review, /sf-compound, /sf-lfg) — formerly commands in v2.x; now skills with auto-routing trigger phrases\n45 skills total — 7 core + 11 Salesforce domain knowledge + 5 workflow support + 22 V3 capability ports (sf-debug, sf-doc-review, sf-pr-description, sf-resolve-pr-feedback, etc.)\n59 specialized agents in a flat agents/sf-*.agent.md layout — 35 Salesforce-specific (Apex / Flow / LWC / Integration / Architecture / Research / Workflow) + 24 V3-ported review/research personas\nMulti-platform manifests for Claude Code, Cursor, and Codex (.claude-plugin/, .cursor-plugin/, .codex-plugin/)\nMCP integration with Context7 and Salesforce DX (@salesforce/mcp — 60+ live-org tools)\nInstitutional knowledge system in docs/solutions/ with YAML frontmatter validated against schema.yaml",
      "status": "pending"
    },
    "m1776337295868_17": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-25T14:01:23.933Z",
      "range": {
        "from": 4860,
        "to": 4944
      },
      "content": "Classifications: APEX, AUTOMATION, LWC, INTEGRATION, ARCHITECTURE, WORKFLOW, TOOLING",
      "status": "pending"
    },
    "m1777125750938_6": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-25T14:02:30.938Z",
      "range": {
        "from": 5857,
        "to": 5878
      },
      "content": "59 Agents (flat layout, V3-ported)\nAfter v3.0.0 all agents live in a flat agents/ directory and are named sf-<name>.agent.md. The topical groupings below are documentation aids, not filesystem paths. See agents/index.md for the complete index including the 24 V3-ported review/research personas (sf-correctness-reviewer, sf-maintainability-reviewer, sf-testing-reviewer, sf-project-standards-reviewer, sf-architecture-strategist, sf-feasibility-reviewer, sf-coherence-reviewer, etc.).",
      "status": "pending"
    },
    "m1776337295821_15": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-25T14:01:23.933Z",
      "range": {
        "from": 6924,
        "to": 6946
      },
      "content": "Integration (4 agents)",
      "status": "pending"
    },
    "m1777125750930_5": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-25T14:02:30.930Z",
      "range": {
        "from": 8622,
        "to": 8631
      },
      "content": "45 Skills\n7 core workflow skills + 11 Salesforce domain knowledge skills + 5 workflow support skills + 22 V3-ported skills (sf-debug, sf-doc-review, sf-pr-description, sf-resolve-pr-feedback, sf-update, sf-setup, sf-sessions family, sf-clean-gone-branches, sf-commit, sf-commit-push-pr, sf-ideate, sf-optimize, sf-agent-native-architecture, sf-agent-native-audit, sf-compound-refresh, sf-release-notes, sf-report-bug, sf-slack-research, sf-proof, sf-demo-reel). See skills/index.md for the complete index.",
      "status": "pending"
    },
    "m1775681196339_10": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-16T11:00:40.311Z",
      "range": {
        "from": 13322,
        "to": 13404
      },
      "content": "The plugin includes a Context7 MCP server for live framework documentation lookup:",
      "status": "pending"
    },
    "m1775681196334_9": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:36.334Z",
      "range": {
        "from": 13443,
        "to": 13539
      },
      "content": "\n      \"type\": \"http\",\n      \"url\": \"https://mcp.context7.com/mcp\"\n    },\n    \"salesforce-dx\": {",
      "status": "pending"
    },
    "m1775681196329_8": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:36.329Z",
      "range": {
        "from": 13628,
        "to": 14235
      },
      "content": "\nSalesforce DX MCP toolsets (all enabled):\nToolset\nCapability\ncore\nBase DX tools (always on)\norgs\nManage authorized orgs\nmetadata\nDeploy/retrieve metadata\ndata\nSOQL queries, record management\nusers\nPermission sets, user management\ncode-analysis\nStatic analysis via Code Analyzer\nlwc-experts\nLWC development, testing, optimization\naura-experts\nAura analysis, LWC migration\nexperts-validation\nLWC production readiness checks\ndevops\nDevOps Center operations\nenrichment\nMetadata component enrichment\nmobile\nMobile development tools\ntesting\nApex and agent test execution\nscale-products\nApex performance detection",
      "status": "pending"
    },
    "m1775681196325_7": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:36.325Z",
      "range": {
        "from": 14341,
        "to": 14508
      },
      "content": "\nPrerequisites for Salesforce DX MCP: Authorize an org first with sf org login web. The server uses DEFAULT_TARGET_ORG — whatever you set with sf config set target-org.",
      "status": "pending"
    },
    "m1775681196320_6": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-04-08T20:46:36.320Z",
      "range": {
        "from": 14539,
        "to": 14564
      },
      "content": "\nNode.js (for MCP servers)",
      "status": "pending"
    },
    "m1775681196313_5": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-16T11:00:40.311Z",
      "range": {
        "from": 14589,
        "to": 14622
      },
      "content": "Node.js (for Context7 MCP server)",
      "status": "pending"
    }
  }
}
-->

<!-- PROOF:END -->
