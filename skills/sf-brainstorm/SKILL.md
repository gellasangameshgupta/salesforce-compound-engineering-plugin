---
name: sf-brainstorm
description: "Explore Salesforce feature ideas and approaches through collaborative dialogue before writing requirements and planning implementation. Use for Apex/LWC/Flow/Integration feature ideas, problem framing, when the user says 'let's brainstorm', or when they want to think through Salesforce-specific options before deciding what to build. Also use when a user describes a vague Salesforce request, asks 'what should we build', 'help me think through this trigger', 'should this be a Flow or Apex', presents a problem with multiple valid Salesforce approaches, or seems unsure about scope or Salesforce-domain direction. Trigger phrases: 'brainstorm a Salesforce feature', 'should this be Flow or Apex', 'help me think through this integration', 'what approach for this LWC'."
argument-hint: "[optional: idea, problem statement, or Salesforce feature description]"
---

# /sf-brainstorm

> **Persona dispatch (V3.1, agentless).** Where this skill says "dispatch research agents", they are *personas* — prompt assets under `references/personas/<name>.md` (research personas referenced from `../sf-plan/references/personas/`), not registered agents. Run each as an **isolated subagent** (Task tool, general-purpose subagent, persona file contents as instructions): parallel on Claude Code, inline-in-sequence on harnesses without subagents.

> **Principles enforced:** 4 (spec is the artifact, in embryo). See `PRINCIPLES.md`.

**Strategy grounding:** If a `STRATEGY.md` exists at the repo root, read it first so the brainstorm stays inside the program's target problem, approach, and personas.

## Copy-paste-to-agent

```
Run a Salesforce-aware brainstorm to refine a feature idea before planning. Ask one
focused question at a time about problem, users, scale, and constraints. For each viable
approach, evaluate the declarative-vs-code trade-off (governor limits, maintenance,
testability, sharing impact). Save the result to docs/brainstorms/YYYY-MM-DD-{slug}.md as
input to /sf-plan — this is pre-spec exploration, not a spec.
```

<feature_description>
#$ARGUMENTS
</feature_description>

## Interaction Method

<span data-proof="authored" data-by="ai:claude">When asking the user a question, use the platform's blocking question tool:</span> <span data-proof="authored" data-by="ai:claude">`AskUserQuestion`</span> <span data-proof="authored" data-by="ai:claude">in Claude Code (call</span> <span data-proof="authored" data-by="ai:claude">`ToolSearch`</span> <span data-proof="authored" data-by="ai:claude">with</span> <span data-proof="authored" data-by="ai:claude">`select:AskUserQuestion`</span> <span data-proof="authored" data-by="ai:claude">first if its schema isn't loaded),</span> <span data-proof="authored" data-by="ai:claude">`request_user_input`</span> <span data-proof="authored" data-by="ai:claude">in Codex,</span> <span data-proof="authored" data-by="ai:claude">`ask_user`</span> <span data-proof="authored" data-by="ai:claude">in Gemini. Fall back to numbered options in chat only when no blocking tool exists in the harness or the call errors. Never silently skip the question.</span>

<span data-proof="authored" data-by="ai:claude">Ask one question at a time. Prefer a concise single-select choice when natural options exist.</span>

<span data-proof="authored" data-by="ai:claude">You are facilitating a brainstorm session to explore an idea before planning. Your job is to help think through approaches, trade-offs, and Salesforce-specific considerations.</span>

## <span data-proof="authored" data-by="ai:claude">Goal</span>

<span data-proof="authored" data-by="ai:claude">Explore and refine:</span> <span data-proof="authored" data-by="ai:claude">`$ARGUMENTS.idea`</span>

***

## <span data-proof="authored" data-by="ai:claude">Phase 0: Assess Clarity</span>

<span data-proof="authored" data-by="ai:claude">Rate the idea's clarity:</span>

* **<span data-proof="authored" data-by="ai:claude">Clear</span>**<span data-proof="authored" data-by="ai:claude">: User knows what they want, specific requirements → Move fast through Phase 1</span>

* **<span data-proof="authored" data-by="ai:claude">Exploratory</span>**<span data-proof="authored" data-by="ai:claude">: User has a general direction but needs options → Spend time in Phase 2</span>

* **<span data-proof="authored" data-by="ai:claude">Vague</span>**<span data-proof="authored" data-by="ai:claude">: User has a problem but no direction → Start deep in Phase 1</span>

***

## <span data-proof="authored" data-by="ai:claude">Phase 1: Understand (One Question at a Time)</span>

<span data-proof="authored" data-by="ai:claude">Ask focused questions using the AskUserQuestion tool. One question per round:</span>

1. **What problem does this solve?** — Understand the pain point
2. **Who uses this?** — Admin, developer, end user, integration
3. **What exists today?** — Current workaround or manual process
4. **What's the scale?** — Records, users, frequency
5. **What are the constraints?** — Timeline, org limits, existing architecture

Stop asking when the idea is clear enough to explore approaches. Don't over-question.

***

## Phase 2: Explore Approaches

For each viable approach, evaluate Salesforce-specific trade-offs:

### Declarative vs Code Decision Matrix

| Factor             | Declarative (Flow)    | Code (Apex)         | Hybrid       |
| ------------------ | --------------------- | ------------------- | ------------ |
| Maintainability    | Admin-friendly        | Developer-required  | Mixed        |
| Governor Limits    | Flow-specific limits  | Full Apex limits    | Best of both |
| Complexity ceiling | Medium                | High                | High         |
| Testing            | Limited               | Full test framework | Full         |
| Deployment         | Change sets, metadata | Same + CI/CD        | Same         |

### For each approach, assess:

* **Feasibility**: Can Salesforce do this natively?

* **Scalability**: Will it work at the expected data volume?

* **Security**: Sharing model implications?

* **Maintenance**: Who will maintain this long-term?

* **Governor Limits**: What limits are at risk?

### Optional: Parallel Research

If approaches are unclear, dispatch research personas:

* Task sf-best-practices-researcher(idea\_context)

* Task sf-framework-docs-researcher(idea\_context)

***

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

***

## Phase 4: Handoff

When brainstorm is complete:

```
Brainstorm captured: docs/brainstorms/YYYY-MM-DD-{topic}.md

Approaches explored: {count}
Chosen approach: {name}
Open questions: {count}

Next: /sf-plan {feature description based on chosen approach}
```