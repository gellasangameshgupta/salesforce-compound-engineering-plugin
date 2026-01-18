---
name: sf-compound
description: Capture learnings from completed work to improve future development
arguments:
  - name: scope
    description: What to compound (defaults to recent work)
    required: false
---

# /sf-compound

You are capturing learnings from completed work. Your job is to identify patterns and insights that will make future development faster and better.

## Goal

Analyze recent work and capture learnings to: `$ARGUMENTS.scope`

If no scope specified, analyze recent commits and changes.

---

## The Compound Loop

```
Plan (40%) → Work (20%) → Review (20%) → Compound (20%) → Repeat
                                              │
                                              └── YOU ARE HERE
```

This is what makes each iteration smarter than the last.

---

## Available Resources

### Agents (to enhance)
Read `.claude/agents/index.md` - agents can have new checks added based on issues found.

### Skills (to expand)
Read `.claude/skills/index.md` - skills can have new patterns added based on work done.

### CLAUDE.md (to update)
Project-specific context and learnings.

---

## What to Capture

### 1. Patterns
New reusable patterns discovered during implementation:
- Apex patterns (trigger handlers, services, utilities)
- Flow patterns (subflows, invocable actions)
- LWC patterns (component communication, state management)
- Test patterns (factories, mocks)

### 2. Issues Prevented
Problems encountered that could be caught earlier:
- Add new checks to relevant agent files
- Document the issue and how to detect it

### 3. Project Context
Org-specific knowledge for CLAUDE.md:
- Naming conventions discovered
- Architecture decisions made
- Integration endpoints configured
- Gotchas and tips

### 4. Test Fixtures
Reusable test data and mocks:
- TestDataFactory methods
- Mock implementations
- Test helper utilities

---

## Your Process

1. **Analyze recent work** - What was built, what decisions were made

2. **Identify new patterns** - Code patterns not yet in skills

3. **Find preventable issues** - Problems that could be caught earlier

4. **Extract project context** - Org-specific learnings

5. **Update the knowledge base**:
   - Add patterns to relevant skill files
   - Add checks to relevant agent files
   - Update CLAUDE.md with project context

6. **Create compound report** - Document what was captured

---

## Output

### Update Files

Based on what was learned, update:
- `.claude/skills/*/SKILL.md` - New patterns
- `.claude/agents/*/*.md` - New checks
- `CLAUDE.md` - Project context

### Create Compound Report

Save to `.specify/compounds/<date>-<feature>.md`:

```markdown
# Compound Report: [Feature]

## What Was Built
[Summary of components created]

## Patterns Captured
[New patterns added to skills]

## Agent Enhancements
[New checks added to agents]

## CLAUDE.md Updates
[New project context]

## Impact
[How this makes future work easier]
```

---

## After Compounding

When complete:

```
Compound complete.

Knowledge updates:
- Skills: X patterns added
- Agents: X checks added
- CLAUDE.md: X entries added

Report: .specify/compounds/<date>-<feature>.md

The next iteration starts smarter.
```
