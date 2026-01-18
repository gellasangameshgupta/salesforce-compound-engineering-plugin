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
