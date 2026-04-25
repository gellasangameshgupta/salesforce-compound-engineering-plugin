---
name: sf-resolve-pr-feedback
description: "Resolve PR review feedback on a Salesforce PR by evaluating validity and fixing issues in parallel. Use when the user says 'resolve PR feedback', 'address review comments', 'fix the review threads'. Salesforce-aware: distinguishes Apex-style reviewer suggestions from valid governor-limit/security/sharing concerns."
argument-hint: "[PR URL or number]"
---

# sf-resolve-pr-feedback

Dispatch sub-agents to evaluate each review thread, classify validity, implement the fix, and respond. Each thread is processed in parallel with metadata-diff awareness.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Distinguish style-preference comments from governor-limit / FLS / sharing correctness comments.
- When fix touches metadata (object, field, profile, permset), include the metadata XML diff in the resolution and re-run the affected Apex tests via `sf apex run test`.
- When fix touches a trigger or handler, verify the bulk test still passes against 200+ records.
- When fix involves a callout, confirm Named Credential and `Test.setMock` coverage remain aligned.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-resolve-pr-feedback`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-resolve-pr-feedback/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-resolve-pr-feedback` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
