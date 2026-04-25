---
name: sf-commit-push-pr
description: "Commit, push, and open a PR for Salesforce work with an adaptive PR description. Use when the user says 'commit and PR', 'push and open a PR for this Apex', 'ship this LWC', 'create a PR'. End-to-end from working changes to an open PR."
argument-hint: "[optional: PR title hint or scope]"
---

# sf-commit-push-pr

Atomic flow: commit (using sf-commit conventions) → push → open PR (using sf-pr-description).

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- PR description includes deploy plan, test plan, and Salesforce-specific risk callouts.
- Push refuses force-push to main/master without explicit user confirmation.
- Skips the evidence prompt when commit message and diff are sufficient — same heuristic as V3 ce-commit-push-pr.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-commit-push-pr`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-commit-push-pr/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-commit-push-pr` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
