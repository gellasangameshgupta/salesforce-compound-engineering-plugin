# Salesforce Skills Index

This index helps you find the right skill (domain knowledge) for your task. Read only the skills relevant to what you're building.

## How to Use This Index

1. Identify what Salesforce component you're working with
2. Find the matching skill below
3. Read the skill file for patterns, limits, and best practices

---

## Available Skills

| Skill | File | Use When |
|-------|------|----------|
| Governor Limits | `governor-limits/SKILL.md` | **Always** - Any Apex, Flow, or trigger work |
| Apex Patterns | `apex-patterns/SKILL.md` | Writing Apex classes, triggers, services |
| Flow Patterns | `flow-patterns/SKILL.md` | Building any type of Flow |
| LWC Patterns | `lwc-patterns/SKILL.md` | Building Lightning Web Components |
| Security Guide | `security-guide/SKILL.md` | CRUD/FLS, sharing, permissions, AppExchange |
| Integration Patterns | `integration-patterns/SKILL.md` | Callouts, APIs, Platform Events |
| Test Factory | `test-factory/SKILL.md` | Writing test classes, test data factories |

---

## Quick Reference: Which Skills for Which Task?

| If you're building... | Read these skills |
|-----------------------|-------------------|
| Apex Trigger | `governor-limits`, `apex-patterns`, `security-guide` |
| Apex Service Class | `governor-limits`, `apex-patterns` |
| Apex Test Class | `test-factory`, `governor-limits` |
| Record-Triggered Flow | `governor-limits`, `flow-patterns` |
| Screen Flow | `flow-patterns` |
| Scheduled Flow | `governor-limits`, `flow-patterns` |
| LWC Component | `lwc-patterns`, `security-guide` |
| LWC with Apex | `lwc-patterns`, `apex-patterns`, `governor-limits` |
| REST API | `integration-patterns`, `security-guide`, `governor-limits` |
| External Callout | `integration-patterns`, `governor-limits` |
| Platform Event | `integration-patterns`, `governor-limits` |
| AppExchange Package | `security-guide`, `governor-limits` |

---

## Skill Summaries

### Governor Limits
The most critical skill. Contains all Salesforce limits (SOQL, DML, CPU, Heap) and patterns to avoid limit exceptions. **Read this for any backend work.**

### Apex Patterns
Trigger handler frameworks, service layer patterns, selector patterns, domain patterns. Use when designing Apex class structure.

### Flow Patterns
Flow design patterns, bulkification in Flows, subflows, invocable actions. Use when building declarative automation.

### LWC Patterns
Component architecture, wire vs imperative, event handling, state management. Use when building frontend components.

### Security Guide
CRUD/FLS enforcement, sharing model, permission sets, secure coding. **Required for AppExchange or any security review.**

### Integration Patterns
Named Credentials, callout patterns, retry logic, Platform Events, Change Data Capture. Use for any external system integration.

### Test Factory
TestDataFactory patterns, mock patterns, bulk test strategies. Use when writing test classes.

---

## When to Use WebSearch Instead

Use WebSearch when:
- The skill doesn't cover your specific scenario
- You need the latest Salesforce release notes
- You're working with a newer feature not in the skills
- You need community solutions from Salesforce Stack Exchange

Search these sites:
- `site:developer.salesforce.com` - Official documentation
- `site:salesforce.stackexchange.com` - Community solutions
- `site:help.salesforce.com` - Admin documentation
