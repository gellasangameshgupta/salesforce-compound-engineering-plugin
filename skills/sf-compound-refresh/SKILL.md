---
name: sf-compound-refresh
description: "Refresh stale learning and pattern docs under docs/solutions/ by reviewing them against the current Salesforce codebase, then updating, consolidating, replacing, or deprecating drifted ones. Use when the user says 'refresh learnings', 'audit docs/solutions/', 'clean up stale Salesforce learnings', or after a sf-compound run flags a related older doc as superseded."
argument-hint: "[optional: scope hint such as a category or tag]"
---

# sf-compound-refresh

Audit and refresh institutional knowledge in docs/solutions/ — protected-artifact aware (edits don't delete content).

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Respects the protected-artifact rule: edits, sets `status: deprecated`, or consolidates — never deletes.
- Common drift sources: API version bumps (e.g., 60.0 → 66.0), deprecated patterns (Process Builder → Flow), platform changes (FLS-by-default for Aura).

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-compound-refresh`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-compound-refresh/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-compound-refresh` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
