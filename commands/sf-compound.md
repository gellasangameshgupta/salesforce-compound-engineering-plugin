---
name: sf-compound
description: Capture learnings from completed work into institutional knowledge system
arguments:
  - name: scope
    description: What to compound (defaults to recent work)
    required: false
---

# /sf-compound

You are capturing learnings from completed work into the institutional knowledge system. Every solution documented makes the next iteration smarter.

## Goal

Analyze recent work and capture learnings: `$ARGUMENTS.scope`

If no scope specified, analyze recent commits and changes.

---

## The Compound Loop

```
Brainstorm (10%) → Plan (30%) → Work (20%) → Review (20%) → Compound (20%) → Repeat
                                                                  │
                                                                  └── YOU ARE HERE
```

---

## Step 1: Analyze Recent Work

Review what was built:
```bash
# Recent commits
git log --oneline -20

# Changed files
git diff HEAD~5 --name-only

# Recent solutions
ls docs/solutions/ -R
```

---

## Step 2: Search Existing Knowledge First

Before writing new entries, check what already exists:

- Task sf-learnings-researcher(work_description)

Avoid duplicating existing documentation. Update existing entries if the new work adds context.

---

## Step 3: Classify Learnings

For each insight from the work, classify into a category:

| Category | Directory | Examples |
|---|---|---|
| Governor Limits | `docs/solutions/governor-limit-issues/` | SOQL 101, DML 150, CPU timeout |
| Deployment | `docs/solutions/deployment-issues/` | Deploy failures, metadata conflicts |
| Test Failures | `docs/solutions/test-failures/` | Flaky tests, coverage gaps |
| Security | `docs/solutions/security-issues/` | CRUD/FLS, injection, sharing |
| Integration | `docs/solutions/integration-issues/` | Callout failures, auth issues |
| Flow | `docs/solutions/flow-issues/` | Flow errors, recursion, limits |
| LWC | `docs/solutions/lwc-issues/` | Rendering, wire, events |
| Data Model | `docs/solutions/data-model-issues/` | Relationships, indexes, skew |
| Best Practice | `docs/solutions/best-practices/` | Proven patterns, approaches |
| Pattern | `docs/solutions/patterns/` | Reusable design patterns |

---

## Step 4: Write Solution Documents

For each learning, create a solution document with YAML frontmatter:

```markdown
---
title: "{Short descriptive title}"
date: {YYYY-MM-DD}
category: {category from schema.yaml}
severity: {critical|high|medium|low}
tags: ["{tag1}", "{tag2}", "{tag3}"]
---

## Symptoms
{What went wrong or what was the challenge}

## Root Cause
{Why it happened — technical explanation}

## Resolution
{How it was fixed — specific code/config changes}

## Prevention
{How to avoid this in the future}

## Related Files
- {file_path}:{line_number}
```

Save to: `docs/solutions/{category}/{YYYY-MM-DD}-{slug}.md`

Validate frontmatter against `schema.yaml`.

---

## Step 5: Update Plugin Resources

Route updates via index files:
- Read `agents/index.md` to identify agent files for new checks
- Read `skills/index.md` to identify skill files for new patterns
- Update only files relevant to the work classification
- Avoid cross-contamination across domains

### What to update:
- **Agent files**: Add new review checks discovered during the work
- **Skill files**: Add new patterns or gotchas
- **CLAUDE.md**: Update project context, conventions, tips

---

## Step 6: Compound Report

Save a report to `docs/solutions/` summarizing all changes.

---

## Output

```
Compound complete.

Knowledge updates:
- Solutions documented: {count} new entries in docs/solutions/
- Skills updated: {list of skills modified}
- Agents updated: {list of agents modified}
- CLAUDE.md: {entries added/updated}

Categories:
- {category}: {count} entries

The next iteration starts smarter.

Next: /sf-brainstorm or /sf-plan for the next feature
```
