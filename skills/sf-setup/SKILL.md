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

This skill follows the standard sf-compound-engineering execution discipline:

1. **Understand the input** — read the `<feature_description>` block above and any referenced files, plans, or issues.
2. **Plan a small set of phases** — break the work into 2-5 ordered steps that an implementer (or another skill) can verify.
3. **Apply the Salesforce Angle notes above** — these encode the platform-specific considerations (governor limits, sharing context, deploy ordering, FLS, metadata semantics) that distinguish this skill from generic counterparts.
4. **Use Salesforce-aware contexts and commands** — file paths under `force-app/main/default/...`, test commands like `sf apex run test`, deploy commands like `sf project deploy validate` and `sf project deploy start`, query the org with `sf data query` when state inspection is needed.
5. **Surface decisions back to the user** — when a step requires a choice that materially affects scope or risk, ask using the platform's blocking question tool rather than guessing.

## Related

- Salesforce knowledge: `docs/solutions/` (search via the `sf-learnings-researcher` agent).
- Plugin conventions: see `CLAUDE.md` for frontmatter, naming, and protected-artifact rules.
