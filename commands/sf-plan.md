---
name: sf-plan
description: Create comprehensive Salesforce implementation plans using parallel research subagents
arguments:
  - name: feature
    description: Description of the feature to plan
    required: true
---

# /sf-plan

Turn feature ideas into detailed Salesforce implementation plans using parallel subagents for research and design.

## Instructions

When this command is invoked, you MUST follow these steps exactly:

### Step 1: Parse the Feature Request

Extract from `$ARGUMENTS.feature`:
- Feature name (short identifier)
- Objects involved (Account, Lead, Custom__c, etc.)
- Components needed (Apex, LWC, Flow, Integration)
- Estimated complexity

Announce: "Starting /sf-plan for: [feature name]"

### Step 2: Deploy Research Subagents (PARALLEL)

**IMMEDIATELY spawn these 4 subagents in parallel using the Task tool:**

<subagent_deployment>
You MUST call the Task tool 4 times in a SINGLE message to run these in parallel:

1. Task tool call:
   - description: "Research codebase patterns"
   - subagent_type: "Explore"
   - prompt: "Research the existing Salesforce codebase for: [FEATURE]. Find: 1) Existing trigger patterns (look for *Trigger.trigger, *Handler.cls), 2) Service layer patterns (*Service.cls), 3) Test patterns (*Test.cls, TestDataFactory), 4) Naming conventions used. Return a summary of patterns found."

2. Task tool call:
   - description: "Research SF best practices"
   - subagent_type: "general-purpose"
   - prompt: |
     Research Salesforce best practices for building: [FEATURE]

     STEP 1 - Read local skills:
     - Read file: .claude/skills/apex-patterns/index.md
     - Read file: .claude/skills/lwc-patterns/index.md

     STEP 2 - Use WebSearch tool to find additional patterns:
     - Search: "Salesforce [FEATURE] best practices site:developer.salesforce.com"
     - Search: "Salesforce [FEATURE] implementation site:salesforce.stackexchange.com"
     - Search: "Salesforce [FEATURE] apex pattern"

     STEP 3 - Synthesize findings from BOTH local skills AND web search.

     Return: Recommended patterns with code examples, citing sources.

3. Task tool call:
   - description: "Analyze governor limits"
   - subagent_type: "general-purpose"
   - prompt: |
     Analyze governor limit implications for: [FEATURE]

     STEP 1 - Read local skill:
     - Read file: .claude/skills/governor-limits/index.md

     STEP 2 - Use WebSearch for latest limits and optimizations:
     - Search: "Salesforce governor limits site:developer.salesforce.com"
     - Search: "Salesforce [FEATURE] governor limit optimization site:salesforce.stackexchange.com"

     STEP 3 - Calculate budget:
     - Expected SOQL queries per transaction
     - Expected DML operations
     - CPU time considerations
     - Heap size for bulk operations (200+ records)

     Return: Governor limit budget table with any relevant citations.

4. Task tool call:
   - description: "Analyze security requirements"
   - subagent_type: "general-purpose"
   - prompt: |
     Analyze security requirements for: [FEATURE]

     STEP 1 - Read local skill:
     - Read file: .claude/skills/security-guide/index.md

     STEP 2 - Use WebSearch for security best practices:
     - Search: "Salesforce security review best practices site:developer.salesforce.com"
     - Search: "Salesforce CRUD FLS enforcement site:salesforce.stackexchange.com"
     - Search: "Salesforce AppExchange security requirements"

     STEP 3 - Compile requirements:
     - CRUD/FLS requirements
     - Sharing model implications
     - Data sensitivity classification
     - Required permission sets

     Return: Security checklist with references to official docs.
</subagent_deployment>

**Wait for all 4 subagents to complete before proceeding.**

Display progress:
```
Research Phase (4 subagents):
  ├── Codebase patterns: [status]
  ├── Best practices: [status]
  ├── Governor limits: [status]
  └── Security requirements: [status]
```

### Step 3: Deploy Design Subagents (PARALLEL)

**After research completes, spawn these 3 subagents in parallel using the Task tool:**

<subagent_deployment>
You MUST call the Task tool 3 times in a SINGLE message:

1. Task tool call:
   - description: "Design Apex architecture"
   - subagent_type: "general-purpose"
   - prompt: |
     Design the Apex architecture for: [FEATURE]

     STEP 1 - Read local agent guidance:
     - Read file: .claude/agents/apex/apex-trigger-architect.md
     - Read file: .claude/skills/apex-patterns/index.md

     STEP 2 - Use WebSearch for architecture patterns:
     - Search: "Salesforce Apex trigger handler pattern site:developer.salesforce.com"
     - Search: "Salesforce service layer pattern site:salesforce.stackexchange.com"
     - Search: "Salesforce fflib apex common patterns"

     STEP 3 - Design architecture including:
     - Trigger + Handler design
     - Service class methods
     - Selector class if complex queries
     - Custom exceptions

     Return: Class diagrams and method signatures with pattern references.

2. Task tool call:
   - description: "Design LWC architecture"
   - subagent_type: "general-purpose"
   - prompt: |
     Design LWC components for: [FEATURE]

     STEP 1 - Read local agent guidance:
     - Read file: .claude/agents/lwc/lwc-architecture-strategist.md
     - Read file: .claude/skills/lwc-patterns/index.md

     STEP 2 - Use WebSearch for LWC patterns:
     - Search: "Salesforce LWC component design patterns site:developer.salesforce.com"
     - Search: "LWC wire vs imperative site:salesforce.stackexchange.com"
     - Search: "Salesforce LWC best practices 2024"

     STEP 3 - Design including:
     - Component hierarchy
     - Wire vs imperative decisions
     - Event communication
     - Apex controller requirements

     Return: Component tree and props/events with pattern references.

3. Task tool call:
   - description: "Design test architecture"
   - subagent_type: "general-purpose"
   - prompt: |
     Design test strategy for: [FEATURE]

     STEP 1 - Read local skill:
     - Read file: .claude/skills/test-factory/index.md

     STEP 2 - Use WebSearch for test patterns:
     - Search: "Salesforce Apex testing best practices site:developer.salesforce.com"
     - Search: "Salesforce TestDataFactory pattern site:salesforce.stackexchange.com"
     - Search: "Salesforce mock callout testing"

     STEP 3 - Design including:
     - Test classes needed
     - TestDataFactory methods
     - Test scenarios (positive, negative, bulk, user context)
     - Mock requirements for callouts

     Return: Test matrix targeting 90%+ coverage with pattern references.
</subagent_deployment>

**Wait for all 3 design subagents to complete.**

Display progress:
```
Design Phase (3 subagents):
  ├── Apex architecture: [status]
  ├── LWC architecture: [status]
  └── Test architecture: [status]
```

### Step 4: Synthesize into Plan

Combine all subagent outputs into a structured plan:

```markdown
# Implementation Plan: [Feature Name]

## Research Summary

### Existing Patterns
[From codebase research subagent]

### Best Practices to Apply
[From best practices subagent]

### Governor Limit Budget
| Limit | Budget | This Feature | Remaining | Risk |
|-------|--------|--------------|-----------|------|
| SOQL | 100 | X | 100-X | ✅/⚠️/🔴 |
| DML | 150 | Y | 150-Y | ✅/⚠️/🔴 |
| CPU (ms) | 10,000 | Z | 10,000-Z | ✅/⚠️/🔴 |

### Security Requirements
[From security subagent]

---

## Technical Design

### Apex Architecture
[From Apex design subagent]

### LWC Architecture
[From LWC design subagent]

### Test Strategy
[From test design subagent]

---

## Implementation Tasks

### Phase 1: Data Model
- [ ] Task 1.1
- [ ] Task 1.2

### Phase 2: Backend (Apex)
- [ ] Task 2.1
- [ ] Task 2.2

### Phase 3: Frontend (LWC)
- [ ] Task 3.1
- [ ] Task 3.2

### Phase 4: Tests
- [ ] Task 4.1
- [ ] Task 4.2

### Phase 5: Deploy
- [ ] Task 5.1
- [ ] Task 5.2

---

## Risks & Mitigations
[Identified risks from all subagents]

## Open Questions
[Questions needing stakeholder input]
```

### Step 5: Save Plan Files

Create the feature directory and save files:

```bash
# Create directory
mkdir -p .specify/specs/[NNN]-[feature-slug]/
```

Save three files:
1. `.specify/specs/[NNN]-[feature-slug]/spec.md` - Business requirements
2. `.specify/specs/[NNN]-[feature-slug]/plan.md` - Technical plan (main output)
3. `.specify/specs/[NNN]-[feature-slug]/tasks.md` - Implementation checklist

### Step 6: Present Results

```
✅ Plan created using 7 parallel subagents

Research Phase (4 subagents):
  ✓ Codebase patterns analyzed
  ✓ Best practices compiled
  ✓ Governor limits budgeted
  ✓ Security requirements defined

Design Phase (3 subagents):
  ✓ Apex architecture designed
  ✓ LWC components designed
  ✓ Test strategy created

📁 Files saved: .specify/specs/001-[feature]/
  • spec.md   - Business requirements
  • plan.md   - Technical design
  • tasks.md  - Implementation checklist (X tasks)

Next: /sf-work .specify/specs/001-[feature]/plan.md
```

## Important

- You MUST actually call the Task tool to spawn subagents
- Spawn research subagents in ONE message (parallel)
- Wait for research to complete
- Spawn design subagents in ONE message (parallel)
- Wait for design to complete
- Then synthesize results
