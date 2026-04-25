---
name: sf-agent-native-audit
description: "Audit a Salesforce feature for human/agent affordance parity. Use when reviewing code or specs to ensure that any action a Salesforce user can take through UI or Setup, an agent can also take through API or MCP. Trigger phrase: 'audit this for agent parity'."
argument-hint: "[feature, file path, or design doc]"
---

# sf-agent-native-audit

Verify human/agent affordance parity on a Salesforce surface; flag gaps where agents have less power than UI users.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Map each UI action to its API/CLI/MCP counterpart.
- Flag UI-only paths (e.g., setup gestures with no Metadata API equivalent) as parity gaps.
- Verify FLS/CRUD enforcement is identical across channels.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-agent-native-audit`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-agent-native-audit/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-agent-native-audit` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
