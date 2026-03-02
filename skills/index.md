# Salesforce Skills Index

Use this index to route to the right skills for the task.

---

## Routing Map

Use this file as the canonical skill router.

| Classification | Read Skills | Avoid |
|--------------------|-------------------|-------------|
| AUTOMATION | `governor-limits`, `flow-patterns`, `security-guide` | `apex-patterns`, `lwc-patterns` |
| APEX | `governor-limits`, `apex-patterns`, `security-guide`, `test-factory` | `flow-patterns`, `lwc-patterns` |
| LWC | `governor-limits`, `lwc-patterns`, `security-guide` | `flow-patterns`, `apex-patterns` (unless Apex controller) |
| INTEGRATION | `governor-limits`, `integration-patterns`, `security-guide` | `flow-patterns`, `lwc-patterns` |
| ARCHITECTURE | `governor-limits`, `security-guide` | Context-dependent |
| WORKFLOW | `sf-cli`, `compound-docs` | Context-dependent |
| TOOLING | `git-worktree`, `create-agent-skills` | Context-dependent |

---

## Usage Guidance

1. Confirm classification from the command.
2. Route to matching skills.
3. Read only sections needed for the current step.
4. Keep `governor-limits` in scope when limits apply.

---

## Domain Skills

| Skill | File | Scope | Use When |
|-------|------|-------|----------|
| Governor Limits | `governor-limits/SKILL.md` | **UNIVERSAL** | **Always** - Any Apex, Flow, or trigger work |
| Apex Patterns | `apex-patterns/SKILL.md` | **APEX_ONLY** | Writing Apex classes, triggers, services. **NOT for Flows.** |
| Flow Patterns | `flow-patterns/SKILL.md` | **AUTOMATION_ONLY** | Building any type of Flow. **NOT for Apex.** |
| LWC Patterns | `lwc-patterns/SKILL.md` | **LWC_ONLY** | Building Lightning Web Components |
| Security Guide | `security-guide/SKILL.md` | **UNIVERSAL** | CRUD/FLS, sharing, permissions, AppExchange |
| Integration Patterns | `integration-patterns/SKILL.md` | **INTEGRATION_ONLY** | Callouts, APIs, Platform Events |
| Test Factory | `test-factory/SKILL.md` | **APEX_ONLY** | Writing Apex test classes, test data factories |

---

## Workflow Skills

| Skill | File | Scope | Use When |
|-------|------|-------|----------|
| SF CLI | `sf-cli/SKILL.md` | **UNIVERSAL** | Deploy, retrieve, test, org management via `sf` CLI |
| Compound Docs | `compound-docs/SKILL.md` | **UNIVERSAL** | Writing solution documents with YAML schema |
| File Todos | `file-todos/SKILL.md` | **UNIVERSAL** | File-based task tracking with status/priority naming |

---

## Tooling Skills

| Skill | File | Scope | Use When |
|-------|------|-------|----------|
| Git Worktree | `git-worktree/SKILL.md` | **UNIVERSAL** | Isolated parallel development branches |
| Create Agent Skills | `create-agent-skills/SKILL.md` | **UNIVERSAL** | Creating new agents and skills for the plugin |

---

## Quick Reference: Which Skills for Which Task?

| Task | Classification | Read Skills |
|------|----------------|-------------|
| Apex Trigger | APEX | `governor-limits`, `apex-patterns`, `security-guide` |
| Apex Service Class | APEX | `governor-limits`, `apex-patterns` |
| Apex Test Class | APEX | `test-factory`, `governor-limits` |
| Record-Triggered Flow | AUTOMATION | `governor-limits`, `flow-patterns` |
| Screen Flow | AUTOMATION | `flow-patterns` |
| Scheduled Flow | AUTOMATION | `governor-limits`, `flow-patterns` |
| LWC Component | LWC | `lwc-patterns`, `security-guide` |
| LWC with Apex | LWC + APEX | `lwc-patterns`, `apex-patterns`, `governor-limits` |
| REST API | INTEGRATION | `integration-patterns`, `security-guide`, `governor-limits` |
| External Callout | INTEGRATION | `integration-patterns`, `governor-limits` |
| Platform Event | INTEGRATION | `integration-patterns`, `governor-limits` |
| AppExchange Package | UNIVERSAL | `security-guide`, `governor-limits` |
| Deployment | WORKFLOW | `sf-cli` |
| Knowledge Capture | WORKFLOW | `compound-docs` |
| Parallel Development | TOOLING | `git-worktree` |
| Extend Plugin | TOOLING | `create-agent-skills` |

---

## Notes

- Prefer skill subsections relevant to the immediate task rather than reading the full file.
- If skills are insufficient, follow command-level research guidance.
- Use Context7 MCP for additional framework documentation.
