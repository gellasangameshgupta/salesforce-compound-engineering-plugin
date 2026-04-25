---
name: sf-debug
description: "Systematically find root causes and fix Salesforce bugs. Use when debugging Apex test failures, trigger fires, LWC runtime errors, deploy failures, governor limit exceptions, sharing/permission errors, integration callout failures, or metadata deploy validation errors. Trigger phrases: 'debug this trigger', 'why is this Apex test failing', 'trace this LWC error', 'investigate this deploy failure', 'why did this validate fail', 'fix this governor limit error'."
argument-hint: "[issue reference, error message, test path, log file, or description of broken behavior]"
---

# sf-debug

Investigate Salesforce-specific bugs systematically — tracing the full causal chain (UI → Flow → trigger → Apex → DML → callback) before proposing a fix — and optionally implement the fix with test-first discipline.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- **Trigger context awareness**: when a bug surfaces in a trigger, identify whether it fires on `before insert`, `after update`, `after undelete`, etc., and whether the same logic must hold across all relevant contexts.
- **Governor limit framing**: `System.LimitException` or `Too many SOQL queries: 101` errors are causal-chain symptoms; the cause is usually a query inside a loop, a recursive trigger, or unbatched DML several layers up.
- **Sharing-context bugs**: failing tests in production that pass in sandbox often trace to `with sharing` / `without sharing` / `inherited sharing` mismatches; reproduce with `System.runAs(User)` for the suspect role.
- **Mixed DML / setup/non-setup**: errors of the form `MIXED_DML_OPERATION` mean a DML on a setup object (User, Group, GroupMember) and a non-setup object happen in the same transaction; the fix is to split into asynchronous contexts.
- **Deploy validation failures**: `sf project deploy validate` failures are reproducible against a sandbox; capture the validation ID and run the relevant Apex test selectively before re-validating.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-debug`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-debug/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-debug` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
