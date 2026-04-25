---
name: sf-setup
description: "Set up the sf-compound-engineering-plugin environment for a new Salesforce developer. Validates Salesforce CLI, sfdx-project.json, MCP servers, and Claude Code plugin install. Use when onboarding to the plugin or troubleshooting install. Trigger phrases: 'set up the plugin', 'check plugin prerequisites', 'verify my Salesforce environment'."
argument-hint: "[no arguments]"
---

# sf-setup

Verify prerequisites, surface missing pieces, and walk the user through installing or configuring each one.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Check `sf --version` (Salesforce CLI v2+) and report install command if missing.
- Check for `sfdx-project.json` in the project root (current dir or first ancestor with one).
- Check `.mcp.json` for Context7 and `@salesforce/mcp` entries; offer to add the Salesforce DX MCP server.
- Verify Claude Code plugin install: `claude /plugin list` includes `sf-compound-engineering`.
- Optional: check `ast-grep` CLI presence (used by review agents for structural Apex/LWC analysis).

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-setup`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-setup/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-setup` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
