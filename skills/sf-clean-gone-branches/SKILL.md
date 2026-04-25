---
name: sf-clean-gone-branches
description: "Clean up local git branches whose remote tracking branch is gone. Use when the user says 'clean up branches', 'delete gone branches', 'prune local branches', 'clean gone'. Salesforce-aware: also offers to remove associated scratch orgs tied to the branch via `sf org delete`."
argument-hint: "[no arguments]"
---

# sf-clean-gone-branches

Prune local branches whose origin tracking branch has been deleted, plus optionally delete the matching scratch orgs.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- Checks for scratch orgs whose alias matches the branch name and offers `sf org delete --target-org <alias> --no-prompt`.
- Skips deletion of the default branch and the currently-checked-out branch.

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-clean-gone-branches`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-clean-gone-branches/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-clean-gone-branches` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
