---
name: sf-review
description: Review Salesforce code for quality, security, and best practices
arguments:
  - name: target
    description: File path, directory, or PR number to review (defaults to uncommitted changes)
    required: false
---

# /sf-review

You are reviewing Salesforce code. Your job is to identify issues and suggest improvements.

## Goal

Review the code at: `$ARGUMENTS.target`

If no target specified, review uncommitted changes (`git diff`).

---

## MANDATORY: Task Classification

**STOP. Before reading any agents or skills, you MUST classify the files being reviewed.**

### Step 1: Identify File Types Being Reviewed

Analyze the files and determine their PRIMARY Salesforce component type:

| If Reviewing... | Classification | Load ONLY These Agents |
|-----------------|----------------|------------------------|
| `.flow-meta.xml`, Flow metadata | **AUTOMATION** | `agents/automation/*.md` |
| `.cls`, `.trigger`, Apex files | **APEX** | `agents/apex/*.md` |
| `.js`, `.html`, `.css` in `/lwc/` folder | **LWC** | `agents/lwc/*.md` |
| Callout classes, Named Credentials, Platform Events | **INTEGRATION** | `agents/integration/*.md` |
| `.object-meta.xml`, `.field-meta.xml`, sharing rules | **ARCHITECTURE** | `agents/architecture/*.md` |

### Step 2: Output Your Classification

**You MUST explicitly state:** `Files Classification: [AUTOMATION|APEX|LWC|INTEGRATION|ARCHITECTURE]`

For mixed file types, state: `Files Classification: [TYPE1], [TYPE2]`

### Step 3: Load Agents for ONLY Those Classifications

- Read the agents listed for your classification(s)
- DO NOT load agents for file types not being reviewed

### Step 4: DO NOT Cross-Apply

**CRITICAL ROUTING RULES:**
- If reviewing Flows → DO NOT apply Apex review checklists
- If reviewing Apex → DO NOT apply Flow review checklists
- If reviewing LWC → Apply LWC agents; only apply Apex agents if reviewing Apex controllers
- Each agent type has specific checklists for specific file types

---

## Web Research (Parallel Guidance)

If review criteria are unclear or the feature uses newer platform capabilities, consider running web research in parallel.

### What to Research

Validate review criteria against multiple sources:
- Official docs: `site:developer.salesforce.com`
- Community Q&A: `site:salesforce.stackexchange.com`
- External Salesforce authors (blogs)
- Salesforce consulting companies (implementation writeups)

### Suggested Output

Summarize any research-backed review criteria and cite common pitfalls.

---

## Available Resources

### Agents (Review Expertise)
Read `.claude/agents/index.md` to find agents relevant to the files being reviewed.

### Skills (Domain Knowledge)
Read `.claude/skills/index.md` to understand what constitutes good Salesforce code.

---

## Review Focus Areas

### For Apex Code
- **Governor Limits**: SOQL/DML in loops, CPU-intensive operations
- **Security**: CRUD/FLS enforcement, SOQL injection, hardcoded credentials
- **Bulkification**: Handles 200+ records, uses collections properly
- **Error Handling**: Try-catch blocks, meaningful error messages
- **Test Quality**: Assertions, bulk tests, negative scenarios

### For Flows
- **Governor Limits**: DML/SOQL in loops, bulkification
- **Complexity**: Too many elements, deeply nested decisions
- **Error Handling**: Fault paths, user-friendly errors
- **Recursion**: Entry conditions, prevention mechanisms

### For LWC
- **Performance**: Wire vs imperative, unnecessary re-renders
- **Security**: XSS prevention, secure data handling
- **Accessibility**: ARIA attributes, keyboard navigation
- **Architecture**: Component hierarchy, event communication

### For Configuration
- **Data Model**: Relationships, field naming, indexes
- **Sharing**: OWD implications, sharing rules
- **Naming**: Conventions, API versions

---

## Your Process

1. **Identify files to review** - Get list of changed files or specified target

2. **Classify files** - Apex, LWC, Flow, Configuration

3. **Read relevant agents** - Based on file types, read applicable agent files for review criteria

4. **Review each file** - Apply the checklists from the agent files

5. **Categorize findings** - By severity (Critical, High, Medium, Low)

6. **Report findings** - With file, line, issue, and fix suggestion

---

## Severity Levels

| Severity | Meaning | Action |
|----------|---------|--------|
| Critical | Security vulnerability, data loss risk, will fail in production | Must fix |
| High | Governor limit risk, significant bug, poor practice | Should fix |
| Medium | Code quality issue, maintainability concern | Consider fixing |
| Low | Style issue, minor improvement | Nice to have |

---

## Output Format

```
Review: [target]

Files reviewed:
- [list of files]

Findings:

CRITICAL (X)
1. [File:Line] - [Issue]
   Fix: [How to fix]

HIGH (X)
1. [File:Line] - [Issue]
   Fix: [How to fix]

MEDIUM (X)
...

LOW (X)
...

Positive Observations:
- [Good patterns found]

Summary:
- Critical: X (must fix)
- High: X (should fix)
- Medium: X
- Low: X
```

---

## After Review

When review is complete:

```
Review complete.

[Summary of findings]

Next: Fix issues and run /sf-review again
```
