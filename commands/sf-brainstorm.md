---
name: sf-brainstorm
description: Explore ideas and approaches before planning Salesforce features
arguments:
  - name: idea
    description: The idea or problem to brainstorm
    required: true
---

# /sf-brainstorm

You are facilitating a brainstorm session to explore an idea before planning. Your job is to help think through approaches, trade-offs, and Salesforce-specific considerations.

## Goal

Explore and refine: `$ARGUMENTS.idea`

---

## Phase 0: Assess Clarity

Rate the idea's clarity:
- **Clear**: User knows what they want, specific requirements → Move fast through Phase 1
- **Exploratory**: User has a general direction but needs options → Spend time in Phase 2
- **Vague**: User has a problem but no direction → Start deep in Phase 1

---

## Phase 1: Understand (One Question at a Time)

Ask focused questions using the AskUserQuestion tool. One question per round:

1. **What problem does this solve?** — Understand the pain point
2. **Who uses this?** — Admin, developer, end user, integration
3. **What exists today?** — Current workaround or manual process
4. **What's the scale?** — Records, users, frequency
5. **What are the constraints?** — Timeline, org limits, existing architecture

Stop asking when the idea is clear enough to explore approaches. Don't over-question.

---

## Phase 2: Explore Approaches

For each viable approach, evaluate Salesforce-specific trade-offs:

### Declarative vs Code Decision Matrix

| Factor | Declarative (Flow) | Code (Apex) | Hybrid |
|---|---|---|---|
| Maintainability | Admin-friendly | Developer-required | Mixed |
| Governor Limits | Flow-specific limits | Full Apex limits | Best of both |
| Complexity ceiling | Medium | High | High |
| Testing | Limited | Full test framework | Full |
| Deployment | Change sets, metadata | Same + CI/CD | Same |

### For each approach, assess:
- **Feasibility**: Can Salesforce do this natively?
- **Scalability**: Will it work at the expected data volume?
- **Security**: Sharing model implications?
- **Maintenance**: Who will maintain this long-term?
- **Governor Limits**: What limits are at risk?

### Optional: Parallel Research

If approaches are unclear, dispatch research agents:
- Task sf-best-practices-researcher(idea_context)
- Task sf-framework-docs-researcher(idea_context)

---

## Phase 3: Capture

Save the brainstorm to `docs/brainstorms/YYYY-MM-DD-{topic-slug}.md`:

```markdown
---
title: "{topic}"
date: YYYY-MM-DD
status: complete
participants: [user, claude]
---

# Brainstorm: {topic}

## Problem Statement
{What problem are we solving}

## Key Requirements
- {requirement 1}
- {requirement 2}

## Approaches Considered

### Approach A: {name}
- **How**: {description}
- **Pros**: {list}
- **Cons**: {list}
- **SF Considerations**: {governor limits, sharing, etc.}

### Approach B: {name}
- **How**: {description}
- **Pros**: {list}
- **Cons**: {list}
- **SF Considerations**: {governor limits, sharing, etc.}

## Chosen Approach
{which approach and why}

## Open Questions
- {question 1}
- {question 2}

## Next Steps
- /sf-plan {feature description}
```

---

## Phase 4: Handoff

When brainstorm is complete:

```
Brainstorm captured: docs/brainstorms/YYYY-MM-DD-{topic}.md

Approaches explored: {count}
Chosen approach: {name}
Open questions: {count}

Next: /sf-plan {feature description based on chosen approach}
```
