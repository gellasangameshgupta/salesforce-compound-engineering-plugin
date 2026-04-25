---
name: sf-session-inventory
description: "Discover Claude/Codex/Cursor session files for the current Salesforce repo and extract metadata. Internal helper for sf-sessions; not usually invoked directly. Trigger phrase: 'list sessions for this repo'."
argument-hint: "[optional: repo path, defaults to current]"
---

# sf-session-inventory

Build an inventory of session files (timestamps, branches, sizes) scoped to the current Salesforce repo.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Repo identity matched by `sfdx-project.json` presence or matching project root path.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-session-inventory`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-session-inventory/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-session-inventory` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
