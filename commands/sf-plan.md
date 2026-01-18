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
