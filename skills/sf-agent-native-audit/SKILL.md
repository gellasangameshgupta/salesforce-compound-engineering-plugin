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

This skill follows the standard sf-compound-engineering execution discipline:

1. **Understand the input** — read the `<feature_description>` block above and any referenced files, plans, or issues.
2. **Plan a small set of phases** — break the work into 2-5 ordered steps that an implementer (or another skill) can verify.
3. **Apply the Salesforce Angle notes above** — these encode the platform-specific considerations (governor limits, sharing context, deploy ordering, FLS, metadata semantics) that distinguish this skill from generic counterparts.
4. **Use Salesforce-aware contexts and commands** — file paths under `force-app/main/default/...`, test commands like `sf apex run test`, deploy commands like `sf project deploy validate` and `sf project deploy start`, query the org with `sf data query` when state inspection is needed.
5. **Surface decisions back to the user** — when a step requires a choice that materially affects scope or risk, ask using the platform's blocking question tool rather than guessing.

## Related

- Salesforce knowledge: `docs/solutions/` (search via the `sf-learnings-researcher` agent).
- Plugin conventions: see `CLAUDE.md` for frontmatter, naming, and protected-artifact rules.
