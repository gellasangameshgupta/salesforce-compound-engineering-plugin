---
name: sf-slack-research
description: "Search Slack for organizational context relevant to a Salesforce task — past decisions, constraints, deploy history, incident postmortems. Use when the user explicitly asks to search Slack during planning, brainstorming, or debugging. Trigger phrases: 'search slack for this', 'what did we decide about this Apex'."
argument-hint: "[query or topic to search]"
---

# sf-slack-research

Synthesized Slack research about a Salesforce topic, returning a digest rather than raw messages.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Recognize Salesforce-specific channels: `#deploys`, `#admin`, `#release-management`, `#salesforce-platform`.
- Surface deploy IDs, scratch-org URLs, and ticket references found in messages.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-slack-research`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-slack-research/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-slack-research` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
