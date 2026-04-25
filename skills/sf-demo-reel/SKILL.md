---
name: sf-demo-reel
description: "Capture a visual demo (GIF, screenshot, terminal recording) for a Salesforce PR. Use when shipping UI changes (LWC, Flow Screen), CLI operations (`sf` commands), or any work with observable Salesforce behavior that benefits from visual proof. Trigger phrases: 'capture a demo', 'record this Flow', 'screenshot this LWC'."
argument-hint: "[optional: scope or screen to capture]"
---

# sf-demo-reel

Capture visual evidence for PR descriptions of Salesforce-visible changes.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Common targets: LWC component in Lightning App Builder, Flow Builder canvas, Setup tree changes, `sf` CLI deploy output.
- Avoid recording sensitive org data — sanitize Account/Contact/Opportunity records before recording.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-demo-reel`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-demo-reel/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-demo-reel` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
