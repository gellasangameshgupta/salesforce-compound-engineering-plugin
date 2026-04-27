---
name: sf-review
description: "Review Salesforce code for quality, governor limits, bulkification, security (CRUD/FLS/SOQL injection), sharing model, performance, and platform best practices using parallel agent dispatch. Use when the user says 'review this Apex', 'review this LWC', 'review this Flow', 'check this trigger', 'audit this SOQL', 'security review', or wants multi-persona review of a PR or local diff. Supports fast, thorough, and comprehensive depth levels."
argument-hint: "[optional: file path, directory, PR number; defaults to uncommitted changes; pass 'fast'/'thorough'/'comprehensive' for depth]"
---

# /sf-review

You are reviewing Salesforce code using parallel agent dispatch for speed and thoroughness.

## Goal

Review the code at: `$ARGUMENTS.target`

If no target specified, review uncommitted changes (`git diff`).

---

## Review Depth Levels

Select depth based on `$ARGUMENTS.depth` (default: thorough):

| Level | Agents | Use Case |
|---|---|---|
| **fast** | Stack-specific agents only | Quick checks, small changes |
| **thorough** | All applicable agents | Standard review (default) |
| **comprehensive** | All + research + deployment verification | Pre-production, risky changes |

---

## Step 1: Identify and Classify Files

1. Get files in scope (git diff, directory listing, or PR files).
2. Classify each file by type:
   - `.cls`, `.trigger` → APEX
   - `.flow-meta.xml` → AUTOMATION
   - `.js`, `.html` (in `lwc/`) → LWC
   - `.xml` (metadata) → ARCHITECTURE
   - Callout/API related → INTEGRATION

---

## Step 2: Dispatch Review Agents in Parallel

Based on file classification, dispatch applicable agents using the **Agent tool** (subagent_type matching the agent name).

### For APEX files — dispatch in parallel:
- Task apex-governor-guardian(files, code_context)
- Task apex-security-sentinel(files, code_context)
- Task apex-bulkification-reviewer(files, code_context)
- Task apex-trigger-architect(files, code_context) — if triggers present
- Task apex-exception-handler(files, code_context)
- Task apex-test-coverage-analyst(files, code_context) — if test classes present

### For AUTOMATION files — dispatch in parallel:
- Task flow-governor-monitor(files, code_context)
- Task flow-complexity-analyzer(files, code_context)
- Task process-automation-strategist(files, code_context)
- Task validation-rule-reviewer(files, code_context) — if validation rules

### For LWC files — dispatch in parallel:
- Task lwc-architecture-strategist(files, code_context)
- Task lwc-performance-oracle(files, code_context)
- Task lwc-security-reviewer(files, code_context)
- Task lwc-accessibility-guardian(files, code_context)

### For INTEGRATION files — dispatch in parallel:
- Task rest-api-architect(files, code_context)
- Task callout-pattern-reviewer(files, code_context)
- Task integration-security-sentinel(files, code_context)

### Always include (ARCHITECTURE — universal):
- Task pattern-recognition-specialist(files, code_context)
- Task metadata-consistency-checker(files, code_context)

### Additional agents for "comprehensive" depth:
- Task sf-code-simplicity-reviewer(files, code_context)
- Task sf-deployment-verification-agent(files, code_context)
- Task sf-git-history-analyzer(files, code_context)

---

## Step 3: Parallel Research (comprehensive depth only)

For comprehensive reviews, also dispatch:
- Task sf-best-practices-researcher(feature_context)
- Task sf-framework-docs-researcher(feature_context)

Validate findings against official docs:
- `site:developer.salesforce.com`
- `site:salesforce.stackexchange.com`

---

## Step 4: Consolidate Findings

Collect results from all dispatched agents and:
1. Deduplicate findings across agents.
2. Categorize by severity: Critical, High, Medium, Low.
3. Group by file for easy navigation.
4. Include fix suggestions with code references.

---

## Output Format

```
## Review: {target}
**Depth:** {fast|thorough|comprehensive}
**Agents dispatched:** {count}

### Critical ({count})
- [{file}:{line}] {issue} — {fix suggestion}

### High ({count})
- [{file}:{line}] {issue} — {fix suggestion}

### Medium ({count})
- [{file}:{line}] {issue} — {fix suggestion}

### Low ({count})
- [{file}:{line}] {issue} — {fix suggestion}

### Summary
{overall assessment}

Next: Fix issues and run /sf-review again
```
