---
name: sf-plan
description: Create comprehensive Salesforce implementation plans using parallel research subagents
arguments:
  - name: feature_description
    description: Description of the feature to plan
    required: true
---

# Salesforce Feature Planning Command

Create detailed, actionable implementation plans for Salesforce features. This command **deploys parallel subagents** for research, design validation, and architecture analysis - just like compound engineering.

## Subagent Architecture

```
/sf-plan "Lead Scoring Automation"
         │
         ├── [PARALLEL RESEARCH PHASE - 40% of work]
         │   ├── Research Subagent 1: Codebase Patterns
         │   ├── Research Subagent 2: Salesforce Best Practices
         │   ├── Research Subagent 3: Governor Limit Analysis
         │   └── Research Subagent 4: Security Requirements
         │
         ├── [PARALLEL DESIGN PHASE]
         │   ├── Design Subagent 1: Data Model Architect
         │   ├── Design Subagent 2: Apex Architecture
         │   ├── Design Subagent 3: LWC Architecture
         │   └── Design Subagent 4: Integration Architecture
         │
         └── [SYNTHESIS PHASE]
             └── Main Agent: Synthesize all findings into plan
```

---

## Workflow

When the user runs `/sf-plan [feature description]`, execute the following:

### Step 1: Parse the Feature Request

Extract key information:
- **Feature name**: Short identifier
- **Objects involved**: Standard/custom objects
- **Automation type**: Trigger, Flow, Apex, LWC, Integration
- **Data volume**: Expected record counts
- **User context**: Who will use this

### Step 2: Deploy Research Subagents (PARALLEL)

**CRITICAL**: Spawn these 4 subagents IN PARALLEL using the Task tool:

```
Use the Task tool to spawn these subagents concurrently:

1. CODEBASE RESEARCH SUBAGENT
   subagent_type: "Explore"
   prompt: |
     Research the existing codebase patterns for: [FEATURE]

     Find and analyze:
     - Existing trigger patterns (handler framework? standalone?)
     - Service layer patterns (if any)
     - Naming conventions used
     - Similar features already implemented
     - Test patterns and factory classes

     Search commands to run:
     - find . -name "*Trigger*" -type f
     - find . -name "*Handler*" -o -name "*Service*"
     - grep -r "TriggerHandler" --include="*.cls"

     Return: Summary of patterns found and recommendations

2. SALESFORCE BEST PRACTICES SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Research Salesforce best practices for: [FEATURE]

     Consult skills files:
     - Read .claude/skills/apex-patterns/ for service layer patterns
     - Read .claude/skills/lwc-patterns/ for LWC architecture
     - Read .claude/skills/integration-patterns/ if integration needed

     Return: Recommended patterns with code examples

3. GOVERNOR LIMIT ANALYSIS SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Analyze governor limit implications for: [FEATURE]

     Read .claude/skills/governor-limits/ and calculate:
     - Expected SOQL queries per transaction
     - Expected DML statements per transaction
     - CPU time estimates
     - Heap size considerations
     - Bulk operation impact (200+ records)

     Return: Governor limit budget table and risk assessment

4. SECURITY REQUIREMENTS SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Analyze security requirements for: [FEATURE]

     Read .claude/skills/security-guide/ and determine:
     - CRUD/FLS requirements
     - Sharing rule implications
     - Data sensitivity classification
     - Required permission sets
     - Platform security considerations

     Return: Security checklist and requirements
```

### Step 3: Deploy Design Subagents (PARALLEL)

**After research completes**, spawn design subagents IN PARALLEL:

```
Use the Task tool to spawn these subagents concurrently:

1. DATA MODEL ARCHITECT SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Design the data model for: [FEATURE]

     Read .claude/agents/architecture/data-model-architect.md

     Provide:
     - Custom objects needed
     - Custom fields on existing objects
     - Relationships (lookup, master-detail)
     - Record types if needed
     - Validation rules

     Return: Data model diagram and field specifications

2. APEX ARCHITECTURE SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Design Apex architecture for: [FEATURE]

     Read agents:
     - .claude/agents/apex/apex-trigger-architect.md
     - .claude/agents/apex/apex-governor-guardian.md

     Read skills:
     - .claude/skills/apex-patterns/

     Provide:
     - Trigger handler design
     - Service class design
     - Selector class design (if complex queries)
     - Utility classes needed

     Return: Class diagrams and method signatures

3. LWC ARCHITECTURE SUBAGENT (if UI needed)
   subagent_type: "general-purpose"
   prompt: |
     Design LWC components for: [FEATURE]

     Read agents:
     - .claude/agents/lwc/lwc-architecture-strategist.md
     - .claude/agents/lwc/lwc-performance-oracle.md

     Read skills:
     - .claude/skills/lwc-patterns/

     Provide:
     - Component hierarchy
     - Wire vs imperative decisions
     - Event communication design
     - Apex controller requirements

     Return: Component tree and communication diagram

4. INTEGRATION ARCHITECTURE SUBAGENT (if integration needed)
   subagent_type: "general-purpose"
   prompt: |
     Design integration architecture for: [FEATURE]

     Read agents:
     - .claude/agents/integration/rest-api-architect.md
     - .claude/agents/integration/callout-pattern-reviewer.md

     Read skills:
     - .claude/skills/integration-patterns/

     Provide:
     - API design (inbound/outbound)
     - Named credential setup
     - Error handling strategy
     - Retry/circuit breaker patterns

     Return: Integration diagram and API specifications
```

### Step 4: Synthesize Findings

After all subagents return, synthesize their findings:

```markdown
# Implementation Plan: [Feature Name]

## Research Summary
[Compiled from Research Subagents]

### Existing Patterns Found
[From Codebase Research Subagent]

### Best Practices Applied
[From Salesforce Best Practices Subagent]

### Governor Limit Budget
[From Governor Limit Analysis Subagent]

| Limit | Budget | This Feature | Remaining | Risk |
|-------|--------|--------------|-----------|------|
| SOQL Queries | 100 | X | 100-X | ✅/⚠️/🔴 |
| DML Statements | 150 | Y | 150-Y | ✅/⚠️/🔴 |
| CPU Time (ms) | 10,000 | Z | 10,000-Z | ✅/⚠️/🔴 |

### Security Requirements
[From Security Requirements Subagent]

---

## Technical Design

### Data Model
[From Data Model Architect Subagent]

### Apex Architecture
[From Apex Architecture Subagent]

### LWC Architecture
[From LWC Architecture Subagent - if applicable]

### Integration Architecture
[From Integration Architecture Subagent - if applicable]

---

## Implementation Tasks

### Phase 1: Data Model
- [ ] Task 1.1: [description]
- [ ] Task 1.2: [description]

### Phase 2: Backend Logic
- [ ] Task 2.1: [description]
- [ ] Task 2.2: [description]

### Phase 3: Tests
- [ ] Task 3.1: [description]
- [ ] Task 3.2: [description]

### Phase 4: UI Components
- [ ] Task 4.1: [description]
- [ ] Task 4.2: [description]

### Phase 5: Deployment
- [ ] Task 5.1: [description]
- [ ] Task 5.2: [description]

---

## Test Plan
[From Test Requirements analysis]

## Deployment Plan
[Sequenced based on dependencies]

## Risk Assessment
[Compiled from all subagents]
```

### Step 5: Save to .specify/specs/

```bash
# Generate feature directory
FEATURE_SLUG=$(echo "$FEATURE" | tr ' ' '-' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]//g')
NEXT_NUM=$(ls -d .specify/specs/*/ 2>/dev/null | wc -l | xargs printf "%03d")
FEATURE_DIR=".specify/specs/${NEXT_NUM}-${FEATURE_SLUG}"
mkdir -p "$FEATURE_DIR"
```

Save three files:
1. **`spec.md`** - Business requirements
2. **`plan.md`** - Technical plan (synthesized from subagents)
3. **`tasks.md`** - Implementation checklist

### Step 6: Present Results

```
✅ Plan created using 8 parallel subagents

Research Phase (4 subagents):
  ✓ Codebase patterns analyzed
  ✓ Best practices compiled
  ✓ Governor limits budgeted
  ✓ Security requirements defined

Design Phase (4 subagents):
  ✓ Data model designed
  ✓ Apex architecture designed
  ✓ LWC components designed
  ✓ Integration patterns defined

📁 Files created: .specify/specs/001-lead-scoring/
  • spec.md   - 5 user stories
  • plan.md   - Full technical plan
  • tasks.md  - 16 implementation tasks

Next: /sf-work .specify/specs/001-lead-scoring/plan.md
```

---

## Example Subagent Invocation

Here's the actual Task tool syntax to use:

```
<task_invocations>
<!-- Research Phase - All 4 run in PARALLEL -->
<task>
  description: "Research codebase patterns"
  subagent_type: "Explore"
  prompt: "Research existing patterns for [FEATURE]. Find triggers, handlers, services, naming conventions. Return pattern summary."
</task>

<task>
  description: "Research SF best practices"
  subagent_type: "general-purpose"
  prompt: "Read .claude/skills/apex-patterns/, lwc-patterns/, integration-patterns/. Return recommended patterns for [FEATURE]."
</task>

<task>
  description: "Analyze governor limits"
  subagent_type: "general-purpose"
  prompt: "Read .claude/skills/governor-limits/. Calculate SOQL, DML, CPU budget for [FEATURE]. Return limit table."
</task>

<task>
  description: "Analyze security requirements"
  subagent_type: "general-purpose"
  prompt: "Read .claude/skills/security-guide/. Determine CRUD/FLS, sharing, permissions for [FEATURE]. Return security checklist."
</task>
</task_invocations>
```

---

## Quality Checklist

Before presenting the plan, verify subagents covered:

- [ ] Existing codebase patterns researched
- [ ] Salesforce best practices applied
- [ ] Governor limits calculated for bulk (200+)
- [ ] Security requirements documented
- [ ] Data model designed with relationships
- [ ] Apex architecture follows org patterns
- [ ] LWC design uses wire adapters appropriately
- [ ] Integration uses Named Credentials
- [ ] Test plan covers bulk and permission scenarios
- [ ] Deployment sequence respects dependencies
