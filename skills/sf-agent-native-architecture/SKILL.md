---
name: sf-agent-native-architecture
description: "Build Salesforce systems where any user action through Setup, the IDE, or `sf` CLI is also accessible to a Salesforce-aware agent. Use when designing automation, MCP tools, hosted MCP servers, or features that should be operable by both humans and agents. Trigger phrases: 'design this for an agent', 'agent-native this Salesforce feature'."
argument-hint: "[feature description or design context]"
---

# sf-agent-native-architecture

Apply agent-native design principles to Salesforce features: every human-affordance has an agent-affordance.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Setup actions → Metadata API + Tooling API + sf CLI equivalents.
- UI buttons → Flow `Action` or Apex `@InvocableMethod` exposed via Hosted MCP server.
- Custom field changes → Tooling API CustomField operations.
- Reports → Reports REST API.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-agent-native-architecture`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-agent-native-architecture/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-agent-native-architecture` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
