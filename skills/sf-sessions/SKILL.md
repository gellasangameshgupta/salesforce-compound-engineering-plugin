---
name: sf-sessions
description: "Search and ask questions about your Claude Code, Codex, and Cursor session history filtered for Salesforce file types (Apex .cls, LWC .js/.html, Flow metadata, etc.). Use when asking what was tried before on this Salesforce work, how a Salesforce problem was investigated across sessions, or any question about past Salesforce coding sessions."
argument-hint: "[natural-language query about past sessions, optionally with a date or file-type filter]"
---

# sf-sessions

Surface relevant past investigation context, failed approaches, and learnings from Salesforce-flavored sessions that the current session cannot see.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Filter dimensions include Apex/.cls, LWC/.js+.html+.css, .flow-meta.xml, .object-meta.xml, .field-meta.xml, .permissionset-meta.xml.
- Common past-context queries: 'how did we debug this trigger before', 'what governor limit fixes have we tried', 'has this LWC been touched in last 30 days'.

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
