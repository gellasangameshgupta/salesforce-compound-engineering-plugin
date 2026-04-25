---
name: sf-ideate
description: "Generate and critically evaluate grounded ideas about a Salesforce topic. Use when asking what to improve, requesting Salesforce idea generation, exploring surprising directions before brainstorming one in depth. Trigger phrases: 'what should I improve in this org', 'give me ideas for this Apex codebase', 'ideate on this LWC', 'surprise me with Salesforce'."
argument-hint: "[topic, focus area, or 'surprise me' for AI-driven ideation]"
---

# sf-ideate

Generate 3-5 grounded ideas about a Salesforce topic with explicit warrants, then critique each.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Ideas are grounded in the current org's metadata, Apex code structure, and `docs/solutions/` learnings.
- Surprise mode pulls from cross-domain analogies (other Salesforce orgs, SF community patterns) rather than local repo signals only.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-ideate`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-ideate/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-ideate` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
