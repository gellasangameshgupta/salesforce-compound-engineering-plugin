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

This skill ports EveryInc's V3 [`ce-sessions`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-sessions/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-sessions` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
