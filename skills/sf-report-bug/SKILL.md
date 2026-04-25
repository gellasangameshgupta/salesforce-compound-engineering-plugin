---
name: sf-report-bug
description: "Produce a structured Salesforce bug report with environment, reproduction steps, expected vs. actual behavior, governor-limit context, and org-shape details. Use when filing a bug report for Salesforce work. Trigger phrases: 'file a bug', 'report this bug', 'write up this issue'."
argument-hint: "[short bug summary or error message]"
---

# sf-report-bug

Generate a complete bug report formatted for Salesforce issue trackers (Linear/Jira/GitHub Issues).

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Environment fields include: org type (production/sandbox/scratch), API version, Apex test runner version, package versions, namespace.
- Reproduction includes the failing Apex test class, deploy ID, debug log link.
- Includes governor-limit utilization at failure point if relevant (`Limits.getQueries()`, etc.).

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-report-bug`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-report-bug/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-report-bug` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
