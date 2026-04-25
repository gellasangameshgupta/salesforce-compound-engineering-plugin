---
name: sf-doc-review
description: "Review Salesforce planning documents (plans, requirements, brainstorms) using parallel persona agents that surface role-specific issues. Use when a Salesforce plan or requirements doc exists and the user wants to improve it. Trigger phrases: 'review this plan', 'doc-review this spec', 'persona review', 'find gaps in this Salesforce plan'."
argument-hint: "[path to a plan or requirements document under docs/plans/ or docs/brainstorms/]"
---

# sf-doc-review

Dispatch sf-feasibility-reviewer, sf-coherence-reviewer, sf-product-lens-reviewer, sf-scope-guardian-reviewer, sf-security-lens-reviewer, sf-design-lens-reviewer, and sf-adversarial-document-reviewer in parallel against a Salesforce planning document. Merge findings, dedupe, and present them with confidence scores.

<feature_description>
#$ARGUMENTS
</feature_description>

## Salesforce Angle

- **Feasibility persona** flags governor-limit risks at plan time (e.g., 'this batch design is unbounded by record count').
- **Security lens** flags missing CRUD/FLS handling, sharing-rule changes that affect the data model, or external API auth gaps.
- **Scope guardian** challenges premature trigger-handler abstractions or fflib introduction when a simpler pattern fits.
- **Adversarial document reviewer** constructs Salesforce-specific failure scenarios (Bulk API + UI concurrent saves, Process Builder fanning into trigger, packaging-time consequences).

## Interaction Method

When asking the user a question, use the platform's blocking question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex, `ask_user` in Gemini). Fall back to numbered options in chat when no blocking tool is available. Ask one question at a time. Prefer concise single-select choices when natural options exist.

## Procedure

This skill ports EveryInc's V3 [`ce-doc-review`](~/.claude/plugins/cache/every-marketplace/compound-engineering/3.0.6/skills/ce-doc-review/SKILL.md) procedure to Salesforce. The full step-by-step procedure (phases, decision points, sub-references) lives in the V3 source. This Salesforce variant inherits that procedure and applies the **Salesforce Angle** notes above wherever the V3 procedure mentions inputs, examples, or outputs.

When implementing this skill at execution time, read the V3 procedure for structure, then substitute Salesforce contexts, file paths (`force-app/main/default/...`), test commands (`sf apex run test`), and deploy commands (`sf project deploy validate` / `sf project deploy start`) for the V3 examples.

## Reference

- V3 source skill: `ce-doc-review` in [EveryInc compound-engineering-plugin v3.x](https://github.com/EveryInc/compound-engineering-plugin)
- Salesforce knowledge: `docs/solutions/` (search via `sf-learnings-researcher` agent)
- Migration plan: `docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md` (U6 unit)
