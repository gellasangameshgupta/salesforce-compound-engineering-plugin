---
name: sf-optimize
description: "Run metric-driven iterative optimization loops on a Salesforce target. Define a measurable goal (Apex CPU time, SOQL count, query selectivity, LWC bundle size, governor-limit headroom), build measurement scaffolding, then run experiments. Use for 'optimize this query', 'reduce SOQL count', 'speed up this trigger', 'optimize this LWC render'."
argument-hint: "[target description and metric to optimize]"
---

# sf-optimize

Systematic experimentation loop: measure → propose → run experiments in parallel → keep improvements → converge.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Salesforce metrics: Apex CPU time, heap size, SOQL count, DML count, query selectivity (filterable indexes hit), LWC bundle size, p95 page load.
- Measurement scaffolding uses `Limits.getCpuTime()`, `Limits.getQueries()`, debug logs, the SOQL Query Plan tool, and the LWC Lighthouse profile.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-optimize`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-optimize/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-optimize` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
