---
name: sf-commit
description: "Create a git commit for Salesforce work with a clear, value-communicating message in conventional-commit format with Salesforce scope taxonomy. Use when the user says 'commit', 'commit this', 'save my Apex changes', 'create a commit'. Scopes: `apex`, `lwc`, `flow`, `metadata`, `integration`, `data`, `permset`, `profile`, `docs`, `chore`."
argument-hint: "[optional: scope hint or message override]"
---

# sf-commit

Produce well-structured commit messages following Salesforce-flavored conventional commit format.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Type/scope examples: `feat(apex):`, `fix(lwc):`, `feat(flow):`, `chore(metadata):`, `feat(integration):`, `fix(data):`, `chore(permset):`, `chore(profile):`.
- Don't include attribution footers in incremental commits — only on the final ship commit (per V3 ce-commit convention).
- Stage only files relevant to this logical Salesforce unit (avoid `git add -A` to prevent picking up unrelated metadata).

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-commit`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-commit/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-commit` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
