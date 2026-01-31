---
name: sf-plan
description: Research and design Salesforce features - creates specifications, not code
arguments:
  - name: feature
    description: Description of the feature to plan
    required: true
---

# /sf-plan

You are planning a Salesforce implementation. Your job is to research and design - **NOT write code**.

## Goal

Create a specification and technical design for: `$ARGUMENTS.feature`

---

## MANDATORY: Task Classification

**STOP. Before reading any agents or skills, you MUST classify this task.**

### Step 1: Identify Primary Component Type

Analyze the feature request and determine the PRIMARY Salesforce component:

| If Request Mentions... | Classification | Load ONLY These Resources |
|------------------------|----------------|---------------------------|
| Flow, Record-Triggered Flow, Screen Flow, Scheduled Flow, Automation, Process Builder | **AUTOMATION** | `agents/automation/*.md` + `skills/flow-patterns/` |
| Apex, Trigger, Class, Batch, Schedulable, Queueable, Service, Handler | **APEX** | `agents/apex/*.md` + `skills/apex-patterns/` |
| LWC, Lightning Web Component, Component, Aura, Frontend | **LWC** | `agents/lwc/*.md` + `skills/lwc-patterns/` |
| API, REST, Callout, Integration, External System, Platform Event, Webhook | **INTEGRATION** | `agents/integration/*.md` + `skills/integration-patterns/` |
| Object, Field, Relationship, Data Model, Sharing, Permission, OWD | **ARCHITECTURE** | `agents/architecture/*.md` + `skills/security-guide/` |

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

## Internal-First Solution Discovery (Guidance)

Before considering any external service or third-party tool, identify native Salesforce solutions first.

### Step 1: Enumerate Native Options

Consider and prefer Salesforce-native capabilities first:
- Declarative automation (Flows, Validation Rules, Approval Processes)
- Apex and platform events
- LWC, Aura, Visualforce, and standard UI patterns
- Standard objects, fields, and metadata
- Reports, dashboards, and standard security model

### Step 2: Choose the Simplest Native Approach

Select the lowest-complexity internal approach that meets requirements.
Only consider external services if native options cannot meet the requirements.

### Step 3: Justify External Dependencies (If Any)

If you recommend any external tool or service, explicitly state:
- Why native Salesforce options are insufficient
- What capability is missing internally
- Why the external option is necessary

---

## Web Research (Parallel Guidance)

If the requirement is new, unclear, or could have multiple approaches, consider running web research in parallel.

### What to Research

Run WebSearch across multiple sources to validate the internal-first approach:
- Official docs: `site:developer.salesforce.com`
- Community Q&A: `site:salesforce.stackexchange.com`
- External Salesforce authors (blogs)
- Salesforce consulting companies (implementation writeups)

### How to Search

Run parallel searches with the same core intent but different sources. Example:
- "record-triggered flow bulkification site:developer.salesforce.com"
- "record-triggered flow bulkification site:salesforce.stackexchange.com"
- "record-triggered flow bulkification blog salesforce"
- "record-triggered flow bulkification consulting implementation"

### Suggested Output

Summarize findings into:
- **Native-first confirmation** (what Salesforce supports natively)
- **Common pitfalls** (from Stack Exchange)
- **Recommended patterns** (from docs and blogs)

---

## Critical Constraint

**DO NOT WRITE CODE.** This command produces:
- Architecture decisions (which components, how they connect)
- Method signatures (names, parameters, return types)
- Configuration specifications (object names, field names, Flow structure)
- Task lists for implementation

Code implementation happens in `/sf-work`.

---

## Available Resources

Before starting, understand what resources are available:

### Agents (Expertise)
Read `.claude/agents/index.md` to find agents relevant to this task.

### Skills (Domain Knowledge)
Read `.claude/skills/index.md` to find skills relevant to this task.

### Existing Codebase
Explore the codebase to understand existing patterns, naming conventions, and architecture.

---

## Your Process

1. **Understand the request** - What Salesforce components are needed? (Flow? Apex? LWC? Integration?)

2. **Read relevant resources** - Based on what's being built, read ONLY the applicable agents and skills from the index files.

3. **Explore the codebase** - Find existing patterns to follow.

4. **Use WebSearch if needed** - When local knowledge doesn't cover the specific scenario.

5. **Design the solution** - Architecture, not code.

6. **Save the plan** - To `.specify/specs/` folder.

---

## Output Format

Create a folder: `.specify/specs/<NNN>-<feature-slug>/`

### spec.md (Business Requirements)
```markdown
# [Feature Name] - Specification

## Overview
[What this feature does and why]

## User Stories
[Who needs this, what they do, why it matters]

## Acceptance Criteria
[How we know it's done]

## Constraints
[Limits, security requirements, dependencies]
```

### plan.md (Technical Design)
```markdown
# [Feature Name] - Technical Plan

## Components
[What will be built - list of Flows, Classes, LWC, Objects, etc.]

## Architecture
[How components connect, data flow, sequence]

## Design Decisions
[Why this approach was chosen]

## Governor Limit Considerations
[Relevant limits and how they're addressed]

## Security Considerations
[CRUD/FLS, sharing, permissions needed]
```

### tasks.md (Implementation Checklist)
```markdown
# [Feature Name] - Tasks

## Implementation Tasks
- [ ] Task 1
- [ ] Task 2
...

## Testing Tasks
- [ ] Task 1
...

## Deployment Tasks
- [ ] Task 1
...
```

---

## WebSearch Guidance

Use WebSearch when:
- Skills don't cover the specific pattern
- Need latest Salesforce documentation
- Working with newer features
- Need community solutions
 - Native-first evaluation is complete and still insufficient

Search sites:
- `site:developer.salesforce.com` - Official docs
- `site:salesforce.stackexchange.com` - Community solutions

---

## Examples of Good Output

**For a Flow request:**
- Describe Flow type, trigger conditions, entry criteria
- List Flow elements (Decisions, Loops, Actions)
- Specify any Invocable Apex needed
- Do NOT include actual Flow XML or Apex code

**For an Apex request:**
- Describe classes and their responsibilities
- List method signatures with parameters and return types
- Describe relationships between classes
- Do NOT include implementation code

**For an LWC request:**
- Describe component hierarchy
- List props, events, and wire adapters
- Specify Apex controller methods needed
- Do NOT include actual JavaScript or HTML

---

## After Planning

When plan is complete, inform the user:

```
Plan created: .specify/specs/<NNN>-<feature>/

Next: /sf-work .specify/specs/<NNN>-<feature>/plan.md
```
