---
name: sf-pr-description
description: "Write or refresh a value-first PR description for a Salesforce branch or PR. Use when the user says 'write a PR description', 'refresh the PR description', 'describe this Apex change', 'document this metadata bundle', 'rewrite this PR'. Highlights Salesforce scope: Apex/LWC/Flow/metadata included, deploy targets, Apex test coverage delta, governor-limit risks, and required post-deploy steps."
argument-hint: "[optional: PR URL or number; defaults to current branch]"
---

# sf-pr-description

Generate a Salesforce-aware pull request description that scales with change complexity: a focused trigger fix gets a short body; a metadata bundle plus Apex plus LWC plus permission changes gets sectioned with deploy plan and post-deploy verification.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- **Scope summary**: explicit list of file types touched (`force-app/main/default/classes/`, `lwc/`, `flows/`, `objects/`, `permissionsets/`, `profiles/`).
- **Deploy plan**: target environment(s), validate vs. quick-deploy, dependencies on prior deploys, package.xml or destructive changes.
- **Test plan**: Apex test classes affected, coverage delta, sharing scenarios exercised, mock callouts, manual UI verification needs.
- **Risk callouts**: governor-limit headroom changes, sharing/visibility changes, integration contract changes, permission set delta.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-pr-description`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-pr-description/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-pr-description` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
