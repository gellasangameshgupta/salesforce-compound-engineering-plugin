---
name: sf-update
description: "Check for and apply updates to the sf-compound-engineering-plugin from upstream. Use when the user says 'update the plugin', 'check for plugin updates', 'is there a newer sf-compound-engineering version'."
argument-hint: "[no arguments]"
---

# sf-update

Check the GitHub releases endpoint for sangameshgupta/sf-compound-engineering-plugin against the locally installed version, present the changelog delta, and optionally run `claude /plugin update sf-compound-engineering`.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Upstream URL is `https://github.com/sangameshgupta/sf-compound-engineering-plugin`, NOT EveryInc's repo.
- Local plugin install lives at the marketplace cache path; reference `.claude-plugin/plugin.json#version` for the installed version.
- Salesforce skill/agent updates may include changes to docs/solutions/ schema — surface schema breaks before applying.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-update`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-update/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-update` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
