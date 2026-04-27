# <span data-proof="authored" data-by="ai:claude">Salesforce Skills Index</span>

<span data-proof="authored" data-by="ai:claude">After the V3 migration, all skills live under</span> <span data-proof="authored" data-by="ai:claude">`skills/<name>/SKILL.md`. The seven core workflow skills (formerly</span> <span data-proof="authored" data-by="ai:claude">`commands/`) are now first-class skills with auto-routing trigger phrases.</span>

***

## <span data-proof="authored" data-by="ai:claude">Core Workflow Skills</span>

<span data-proof="authored" data-by="ai:claude">These were</span> <span data-proof="authored" data-by="ai:claude">`commands/`</span> <span data-proof="authored" data-by="ai:claude">files in v2.x. In V3 they auto-route from natural-language phrases via their</span> <span data-proof="authored" data-by="ai:claude">`description`</span> <span data-proof="authored" data-by="ai:claude">frontmatter. Direct invocation via</span> <span data-proof="authored" data-by="ai:claude">`/sf-<name>`</span> <span data-proof="authored" data-by="ai:claude">still works.</span>

| <span data-proof="authored" data-by="ai:claude">Skill</span>            | <span data-proof="authored" data-by="ai:claude">File</span>                     | <span data-proof="authored" data-by="ai:claude">Use When</span>                                                                                                                                                                     |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`/sf-brainstorm`</span> | <span data-proof="authored" data-by="ai:claude">`sf-brainstorm/SKILL.md`</span> | <span data-proof="authored" data-by="ai:claude">Pre-planning exploration of a Salesforce feature idea</span>                                                                                                                        |
| <span data-proof="authored" data-by="ai:claude">`/sf-plan`</span>       | <span data-proof="authored" data-by="ai:claude">`sf-plan/SKILL.md`</span>       | <span data-proof="authored" data-by="ai:claude">Structured implementation plan for Apex/LWC/Flow/Integration/metadata work</span>                                                                                                   |
| <span data-proof="authored" data-by="ai:claude">`/sf-deepen`</span>     | <span data-proof="authored" data-by="ai:claude">`sf-deepen/SKILL.md`</span>     | <span data-proof="authored" data-by="ai:claude">Strengthen an existing plan with parallel research agents per section</span>                                                                                                        |
| <span data-proof="authored" data-by="ai:claude">`/sf-work`</span>       | <span data-proof="authored" data-by="ai:claude">`sf-work/SKILL.md`</span>       | <span data-proof="authored" data-by="ai:claude">Execute a plan or feature description with system-wide test checks</span>                                                                                                           |
| <span data-proof="authored" data-by="ai:claude">`/sf-review`</span>     | <span data-proof="authored" data-by="ai:claude">`sf-review/SKILL.md`</span>     | <span data-proof="authored" data-by="ai:claude">Multi-persona parallel review of code, PR, or local diff</span>                                                                                                                     |
| <span data-proof="authored" data-by="ai:claude">`/sf-compound`</span>   | <span data-proof="authored" data-by="ai:claude">`sf-compound/SKILL.md`</span>   | <span data-proof="authored" data-by="ai:claude">Capture a learning into</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`</span> <span data-proof="authored" data-by="ai:claude">for future retrieval</span> |
| <span data-proof="authored" data-by="ai:claude">`/sf-lfg`</span>        | <span data-proof="authored" data-by="ai:claude">`sf-lfg/SKILL.md`</span>        | <span data-proof="authored" data-by="ai:claude">Full autonomous brainstorm → plan → deepen → work → review → resolve → test → deploy pipeline</span>                                                                                |

***

## <span data-proof="authored" data-by="ai:claude">Domain Knowledge Skills (Salesforce-Specific)</span>

<span data-proof="authored" data-by="ai:claude">These are content/reference skills loaded by other skills as needed.</span>

| <span data-proof="authored" data-by="ai:claude">Skill</span>                | <span data-proof="authored" data-by="ai:claude">File</span>                            | <span data-proof="authored" data-by="ai:claude">Scope</span>                     | <span data-proof="authored" data-by="ai:claude">Use When</span>                                                                       |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Governor Limits</span>      | <span data-proof="authored" data-by="ai:claude">`governor-limits/SKILL.md`</span>      | <span data-proof="authored" data-by="ai:claude">UNIVERSAL</span>                 | <span data-proof="authored" data-by="ai:claude">Always when Apex, Flow, or trigger work touches limit-bearing code</span>             |
| <span data-proof="authored" data-by="ai:claude">Apex Patterns</span>        | <span data-proof="authored" data-by="ai:claude">`apex-patterns/SKILL.md`</span>        | <span data-proof="authored" data-by="ai:claude">APEX_ONLY</span>                 | <span data-proof="authored" data-by="ai:claude">Apex classes, triggers, services. Not for Flows.</span>                               |
| <span data-proof="authored" data-by="ai:claude">Flow Patterns</span>        | <span data-proof="authored" data-by="ai:claude">`flow-patterns/SKILL.md`</span>        | <span data-proof="authored" data-by="ai:claude">AUTOMATION_ONLY</span>           | <span data-proof="authored" data-by="ai:claude">Building any Flow. Not for Apex.</span>                                               |
| <span data-proof="authored" data-by="ai:claude">LWC Patterns</span>         | <span data-proof="authored" data-by="ai:claude">`lwc-patterns/SKILL.md`</span>         | <span data-proof="authored" data-by="ai:claude">LWC_ONLY</span>                  | <span data-proof="authored" data-by="ai:claude">Building Lightning Web Components</span>                                              |
| <span data-proof="authored" data-by="ai:claude">Security Guide</span>       | <span data-proof="authored" data-by="ai:claude">`security-guide/SKILL.md`</span>       | <span data-proof="authored" data-by="ai:claude">UNIVERSAL</span>                 | <span data-proof="authored" data-by="ai:claude">CRUD/FLS, sharing, permissions, AppExchange security</span>                           |
| <span data-proof="authored" data-by="ai:claude">Integration Patterns</span> | <span data-proof="authored" data-by="ai:claude">`integration-patterns/SKILL.md`</span> | <span data-proof="authored" data-by="ai:claude">INTEGRATION_ONLY</span>          | <span data-proof="authored" data-by="ai:claude">Callouts, APIs, Platform Events</span>                                                |
| <span data-proof="authored" data-by="ai:claude">Test Factory</span>         | <span data-proof="authored" data-by="ai:claude">`test-factory/SKILL.md`</span>         | <span data-proof="authored" data-by="ai:claude">APEX_ONLY</span>                 | <span data-proof="authored" data-by="ai:claude">Apex test classes and test data factories</span>                                      |
| <span data-proof="authored" data-by="ai:claude">Agent Script</span>         | <span data-proof="authored" data-by="ai:claude">`agent-script/SKILL.md`</span>         | <span data-proof="authored" data-by="ai:claude">AGENTFORCE_SCRIPT_BUILDER</span> | <span data-proof="authored" data-by="ai:claude">Building Agentforce agents using Agent Script language</span>                         |
| <span data-proof="authored" data-by="ai:claude">Prompt Builder</span>       | <span data-proof="authored" data-by="ai:claude">`prompt-builder/SKILL.md`</span>       | <span data-proof="authored" data-by="ai:claude">AGENTFORCE_PROMPT_BUILDER</span> | <span data-proof="authored" data-by="ai:claude">Prompt templates, Apex/LWC/API integration, metadata XML generation</span>            |
| <span data-proof="authored" data-by="ai:claude">Hosted MCP Servers</span>   | <span data-proof="authored" data-by="ai:claude">`hosted-mcp-servers/SKILL.md`</span>   | <span data-proof="authored" data-by="ai:claude">HOSTED_MCP</span>                | <span data-proof="authored" data-by="ai:claude">Setting up and configuring Salesforce Hosted MCP Servers, ECA, troubleshooting</span> |
| <span data-proof="authored" data-by="ai:claude">MCP Tool Builder</span>     | <span data-proof="authored" data-by="ai:claude">`mcp-tool-builder/SKILL.md`</span>     | <span data-proof="authored" data-by="ai:claude">HOSTED_MCP</span>                | <span data-proof="authored" data-by="ai:claude">Building custom MCP tools — InvocableMethod, Flow, Named Queries</span>               |

***

## <span data-proof="authored" data-by="ai:claude">Workflow Support Skills</span>

| <span data-proof="authored" data-by="ai:claude">Skill</span>               | <span data-proof="authored" data-by="ai:claude">File</span>                           | <span data-proof="authored" data-by="ai:claude">Use When</span>                                                                                                                                                              |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">SF CLI</span>              | <span data-proof="authored" data-by="ai:claude">`sf-cli/SKILL.md`</span>              | <span data-proof="authored" data-by="ai:claude">Deploy, retrieve, test, org management via the</span> <span data-proof="authored" data-by="ai:claude">`sf`</span> <span data-proof="authored" data-by="ai:claude">CLI</span> |
| <span data-proof="authored" data-by="ai:claude">Compound Docs</span>       | <span data-proof="authored" data-by="ai:claude">`compound-docs/SKILL.md`</span>       | <span data-proof="authored" data-by="ai:claude">Writing solution documents with YAML schema</span>                                                                                                                           |
| <span data-proof="authored" data-by="ai:claude">File Todos</span>          | <span data-proof="authored" data-by="ai:claude">`file-todos/SKILL.md`</span>          | <span data-proof="authored" data-by="ai:claude">File-based task tracking with status/priority naming</span>                                                                                                                  |
| <span data-proof="authored" data-by="ai:claude">Git Worktree</span>        | <span data-proof="authored" data-by="ai:claude">`git-worktree/SKILL.md`</span>        | <span data-proof="authored" data-by="ai:claude">Isolated parallel development branches</span>                                                                                                                                |
| <span data-proof="authored" data-by="ai:claude">Create Agent Skills</span> | <span data-proof="authored" data-by="ai:claude">`create-agent-skills/SKILL.md`</span> | <span data-proof="authored" data-by="ai:claude">Creating new agents and skills for the plugin</span>                                                                                                                         |

***

## V3 Capability Skills

Salesforce-aware skills covering the full V3 capability surface — debugging, doc review, PR description, PR feedback resolution, ideation, optimization, plugin maintenance, session research, git hygiene, commits, agent-native architecture, knowledge refresh, release notes, bug reports, Slack research, Proof HITL, and demo capture.

| Skill                          | Salesforce angle                                                         |
| ------------------------------ | ------------------------------------------------------------------------ |
| `sf-debug`                     | Trigger / Apex test / LWC error / deploy failure root cause analysis     |
| `sf-doc-review`                | Parallel persona review of Salesforce plans and specs                    |
| `sf-pr-description`            | Salesforce-aware PR descriptions (Apex / metadata / LWC scope)           |
| `sf-resolve-pr-feedback`       | Parallel resolution with metadata-diff awareness                         |
| `sf-ideate`                    | Surprise-me / what-to-build with Salesforce examples                     |
| `sf-optimize`                  | Metric-driven optimization loops (governor-limit thresholds, query plan) |
| `sf-update`                    | Plugin self-update from the upstream GitHub releases endpoint            |
| `sf-setup`                     | Salesforce CLI presence check, `sfdx-project.json`, MCP servers          |
| `sf-sessions`                  | Search past Claude/Codex/Cursor sessions filtered for SF file types      |
| `sf-session-inventory`         | Discover session files for a Salesforce repo                             |
| `sf-session-extract`           | Extract conversation skeleton from one session file                      |
| `sf-clean-gone-branches`       | Prune local branches whose remote is gone                                |
| `sf-commit`                    | Conventional commits with Salesforce scope taxonomy                      |
| `sf-commit-push-pr`            | Commit + push + open PR with Salesforce-aware description                |
| `sf-agent-native-architecture` | Build Salesforce systems where any user action is also agent-accessible  |
| `sf-agent-native-audit`        | Audit human/agent affordance parity on Salesforce surfaces               |
| `sf-compound-refresh`          | Refresh stale `docs/solutions/` Salesforce knowledge                     |
| `sf-release-notes`             | Generate release notes from PRs / commits                                |
| `sf-report-bug`                | Structured bug report (incl. Salesforce-specific environment fields)     |
| `sf-slack-research`            | Slack search for Salesforce org-context decisions                        |
| `sf-proof`                     | Markdown HITL via Proof editor                                           |
| `sf-demo-reel`                 | Capture demos for PRs (UI / CLI / Setup screen)                          |

Out of scope for this Salesforce plugin (intentionally not shipped): generic frontend design tooling, Figma sync, image generation, non-Salesforce test runners (xcode, browser), and personality-tied reviewers tied to non-Salesforce stacks.

***

## <span data-proof="authored" data-by="ai:claude">Notes</span>

* <span data-proof="authored" data-by="ai:claude">Skills auto-route via their</span> <span data-proof="authored" data-by="ai:claude">`description`</span> <span data-proof="authored" data-by="ai:claude">frontmatter. The V3 harness picks a skill when the user types a phrase that matches the description's trigger language.</span>

* <span data-proof="authored" data-by="ai:claude">Direct slash invocation (`/sf-plan`,</span> <span data-proof="authored" data-by="ai:claude">`/sf-debug`) always works regardless of phrasing.</span>

* <span data-proof="authored" data-by="ai:claude">For routing collisions (e.g., "review this" vs. "review this PR"), the more specific phrase wins.</span>

* <span data-proof="authored" data-by="ai:claude">The seven core workflow skills are the primary entry points; domain skills are loaded by them as needed.</span>