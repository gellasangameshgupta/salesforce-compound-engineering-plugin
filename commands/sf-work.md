---
name: sf-work
description: Implement Salesforce features following a plan
arguments:
  - name: plan
    description: Path to plan file or feature description
    required: true
---

# /sf-work

You are implementing a Salesforce feature. Your job is to write production-quality code.

## Goal

Implement the feature described in: `$ARGUMENTS.plan`

If a plan file path is provided, read it first. If a description is provided, implement directly.

---

## MANDATORY: Task Classification

**STOP. Before reading any agents or skills, you MUST classify this task.**

### Step 1: Identify Primary Component Type

Analyze the implementation request and determine the PRIMARY Salesforce component:

| If Building... | Classification | Load ONLY These Resources |
|----------------|----------------|---------------------------|
| Flow, Record-Triggered Flow, Screen Flow, Scheduled Flow, Automation | **AUTOMATION** | `agents/automation/*.md` + `skills/flow-patterns/` |
| Apex Class, Trigger, Batch, Schedulable, Queueable, Service, Handler | **APEX** | `agents/apex/*.md` + `skills/apex-patterns/` |
| LWC, Lightning Web Component, Aura Component | **LWC** | `agents/lwc/*.md` + `skills/lwc-patterns/` |
| REST API, Callout, Integration, Platform Event | **INTEGRATION** | `agents/integration/*.md` + `skills/integration-patterns/` |
| Custom Object, Fields, Relationships, Sharing Rules | **ARCHITECTURE** | `agents/architecture/*.md` + `skills/security-guide/` |

### Step 2: Output Your Classification

**You MUST explicitly state:** `Task Classification: [AUTOMATION|APEX|LWC|INTEGRATION|ARCHITECTURE]`

### Step 3: Load Resources for ONLY That Classification

- Read the agents listed for your classification
- Read the skills listed for your classification
- Read `skills/governor-limits/` (applies to all classifications)

### Step 4: DO NOT Cross-Load

**CRITICAL ROUTING RULES:**
- If classification is AUTOMATION → DO NOT read `agents/apex/*.md` or `skills/apex-patterns/`
- If classification is APEX → DO NOT read `agents/automation/*.md` or `skills/flow-patterns/`
- If classification is LWC → DO NOT read `agents/apex/*.md` (unless Apex controller is needed)
- Mixing patterns from wrong domains causes incorrect recommendations

---

## Internal-First Implementation (Guidance)

Before using any external service or third-party tool, prefer Salesforce-native capabilities first.

### Step 1: Prefer Native Salesforce Features

Use built-in platform features wherever possible:
- Flows, Validation Rules, Approval Processes
- Apex, Platform Events, and standard metadata
- LWC, Aura, Visualforce for UI
- Standard security model (CRUD/FLS, sharing)

### Step 2: Only Use External Dependencies if Required

If external services are needed, justify them explicitly by documenting:
- The exact platform gap
- Why a native approach cannot satisfy requirements
- The minimal external dependency needed

---

## Web Research (Parallel Guidance)

If implementation details are uncertain or platform behavior is version-sensitive, consider running web research in parallel.

### What to Research

Use multiple sources to validate the chosen approach:
- Official docs: `site:developer.salesforce.com`
- Community Q&A: `site:salesforce.stackexchange.com`
- External Salesforce authors (blogs)
- Salesforce consulting companies (implementation writeups)

### How to Search

Run parallel searches with consistent intent and different sources. Example:
- "platform event publish limits site:developer.salesforce.com"
- "platform event publish limits site:salesforce.stackexchange.com"
- "platform event publish limits blog salesforce"
- "platform event publish limits consulting implementation"

### Suggested Output

Summarize findings into:
- **Native-first confirmation** (what the platform supports)
- **Edge cases** (from community and blogs)
- **Implementation guardrails** (limits, pitfalls, best practices)

---

## Available Resources

### Agents (Expertise)
Read `.claude/agents/index.md` to find agents relevant to implementation.

### Skills (Domain Knowledge)
Read `.claude/skills/index.md` to find patterns and best practices.

### Existing Codebase
Follow existing patterns, naming conventions, and architecture in the project.

---

## Implementation Standards

### Apex Code
- Follow existing trigger handler pattern in codebase
- Bulkify all operations (handle 200+ records)
- CRUD/FLS enforcement on all database operations
- Proper exception handling
- Meaningful method and variable names

### Flows
- Clear element naming (e.g., `Get_Account_Details`, `Decision_Check_Status`)
- Entry conditions to prevent unnecessary execution
- Bulkified operations (no DML/SOQL in loops)
- Fault handling for error scenarios

### LWC
- Component naming follows existing conventions
- Proper error handling and loading states
- Accessible markup (ARIA, keyboard navigation)
- Efficient wire/imperative Apex calls

### Test Classes
- Minimum 90% code coverage target
- Bulk tests (200+ records)
- Positive and negative scenarios
- Test as different user contexts when relevant

---

## Your Process

1. **Read the plan** - Understand what needs to be built

2. **Read relevant skills** - Get patterns for the component type being built

3. **Explore existing code** - Find patterns to follow in the codebase

4. **Implement** - Write the code following standards above

5. **Create tests** - Write test classes for Apex code

6. **Validate** - Ensure code compiles and tests pass

---

## WebSearch Guidance

Use WebSearch when:
- Need syntax for a specific Salesforce API
- Implementing a feature not covered in skills
- Need latest best practices
- Troubleshooting errors
 - Native-first evaluation is complete and still insufficient

---

## Output

Create the necessary files in the appropriate directories:
- Apex classes: `force-app/main/default/classes/`
- Apex triggers: `force-app/main/default/triggers/`
- LWC: `force-app/main/default/lwc/`
- Flows: `force-app/main/default/flows/`

---

## After Implementation

When implementation is complete:

```
Implementation complete.

Files created:
- [list of files]

Next: /sf-review
```
