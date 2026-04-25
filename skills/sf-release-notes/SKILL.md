---
name: sf-release-notes
description: "Generate release notes for a Salesforce package or plugin from PRs, commits, and changelog entries. Use when shipping a managed package version, an unlocked package, or a plugin release. Trigger phrases: 'write release notes', 'generate the changelog'."
argument-hint: "[optional: from-tag or commit range]"
---

# sf-release-notes

Produce structured release notes (Added / Changed / Fixed / BREAKING) from git history.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Salesforce package version names follow `<major>.<minor>.<patch>-<build>` for managed packages.
- Surface BREAKING for: removed fields, removed picklist values, changed Apex method signatures, changed `@RestResource` URL bindings.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-release-notes`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-release-notes/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-release-notes` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
