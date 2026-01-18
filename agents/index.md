# Salesforce Agents Index

This index helps you find the right agent for your task. Read only the agents relevant to what you're building.

## How to Use This Index

1. Identify what Salesforce component you're working with
2. Find the matching category below
3. Read only the agents that apply to your specific task

---

## Apex Development

Use these agents when building Apex classes, triggers, or batch jobs.

| Agent | File | Use When |
|-------|------|----------|
| Trigger Architect | `apex/apex-trigger-architect.md` | Designing trigger logic, handler patterns |
| Governor Guardian | `apex/apex-governor-guardian.md` | Checking SOQL/DML usage, limit compliance |
| Bulkification Reviewer | `apex/apex-bulkification-reviewer.md` | Ensuring code handles 200+ records |
| Security Sentinel | `apex/apex-security-sentinel.md` | CRUD/FLS checks, SOQL injection prevention |
| Exception Handler | `apex/apex-exception-handler.md` | Error handling patterns, custom exceptions |
| Test Coverage Analyst | `apex/apex-test-coverage-analyst.md` | Test class design, coverage strategy |

---

## Flow & Automation

Use these agents when building Flows, Process Builder, or declarative automation.

| Agent | File | Use When |
|-------|------|----------|
| Flow Governor Monitor | `automation/flow-governor-monitor.md` | Checking Flow limits, DML/SOQL in Flows |
| Flow Complexity Analyzer | `automation/flow-complexity-analyzer.md` | Evaluating Flow maintainability, refactoring |
| Process Automation Strategist | `automation/process-automation-strategist.md` | Choosing between Flow, Apex, or triggers |
| Validation Rule Reviewer | `automation/validation-rule-reviewer.md` | Validation rule logic, error messages |

---

## Lightning Web Components (LWC)

Use these agents when building LWC or migrating from Aura.

| Agent | File | Use When |
|-------|------|----------|
| LWC Architecture Strategist | `lwc/lwc-architecture-strategist.md` | Component hierarchy, state management |
| LWC Performance Oracle | `lwc/lwc-performance-oracle.md` | Wire vs imperative, rendering optimization |
| LWC Security Reviewer | `lwc/lwc-security-reviewer.md` | XSS prevention, secure data handling |
| LWC Accessibility Guardian | `lwc/lwc-accessibility-guardian.md` | ARIA, keyboard navigation, screen readers |
| Aura Migration Advisor | `lwc/aura-migration-advisor.md` | Converting Aura components to LWC |

---

## Integration

Use these agents when building APIs, callouts, or Platform Events.

| Agent | File | Use When |
|-------|------|----------|
| REST API Architect | `integration/rest-api-architect.md` | Building REST endpoints, API design |
| Callout Pattern Reviewer | `integration/callout-pattern-reviewer.md` | HTTP callouts, Named Credentials, mocking |
| Platform Event Strategist | `integration/platform-event-strategist.md` | Event-driven architecture, pub/sub |
| Integration Security Sentinel | `integration/integration-security-sentinel.md` | Auth, certificates, secure data transfer |

---

## Architecture & Data Model

Use these agents for org-wide design decisions.

| Agent | File | Use When |
|-------|------|----------|
| Data Model Architect | `architecture/data-model-architect.md` | Object relationships, field design |
| Sharing Security Analyst | `architecture/sharing-security-analyst.md` | OWD, sharing rules, permission sets |
| Pattern Recognition Specialist | `architecture/pattern-recognition-specialist.md` | Identifying reusable patterns in codebase |
| Metadata Consistency Checker | `architecture/metadata-consistency-checker.md` | Naming conventions, API versions |

---

## Quick Reference: Which Agents for Which Task?

| If you're building... | Use these agents |
|-----------------------|------------------|
| Apex Trigger | `apex-trigger-architect`, `apex-bulkification-reviewer`, `apex-governor-guardian` |
| Apex Service Class | `apex-governor-guardian`, `apex-security-sentinel`, `apex-exception-handler` |
| Apex Test Class | `apex-test-coverage-analyst` |
| Record-Triggered Flow | `flow-governor-monitor`, `flow-complexity-analyzer` |
| Screen Flow | `flow-complexity-analyzer`, `process-automation-strategist` |
| LWC Component | `lwc-architecture-strategist`, `lwc-performance-oracle` |
| REST API | `rest-api-architect`, `integration-security-sentinel` |
| External Callout | `callout-pattern-reviewer`, `integration-security-sentinel` |
| Platform Event | `platform-event-strategist` |
| Custom Object | `data-model-architect`, `sharing-security-analyst` |
