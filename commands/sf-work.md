---
name: sf-work
description: Execute Salesforce implementation plans using parallel implementation subagents
arguments:
  - name: plan_file
    description: Path to the plan markdown file
    required: true
---

# Salesforce Work Execution Command

Executes implementation plans created by `/sf-plan` using **parallel subagents** for different types of work - Apex, LWC, Tests, and Configuration.

## Subagent Architecture

```
/sf-work .specify/specs/001-lead-scoring/plan.md
         │
         ├── [SETUP PHASE]
         │   └── Main Agent: Parse plan, create branch, setup environment
         │
         ├── [PARALLEL IMPLEMENTATION PHASE]
         │   ├── Apex Subagent: Triggers, Handlers, Services, Selectors
         │   ├── LWC Subagent: Components, Controllers, Tests
         │   ├── Config Subagent: Objects, Fields, Flows, Permissions
         │   └── Test Subagent: Test Classes, Test Data Factory
         │
         ├── [VALIDATION PHASE]
         │   ├── Deploy Validation Subagent
         │   └── Test Execution Subagent
         │
         └── [COMPLETION PHASE]
             └── Main Agent: Create PR, update tasks
```

---

## Workflow

When the user runs `/sf-work [plan file]`, execute the following:

### Step 1: Load and Parse Plan

```bash
# Read the plan and related files
cat .specify/specs/<feature>/plan.md   # Technical design
cat .specify/specs/<feature>/spec.md   # Requirements
cat .specify/specs/<feature>/tasks.md  # Task checklist
```

Extract:
- Components to build (Apex classes, LWC, Flows)
- Dependencies between components
- Test requirements
- Deployment sequence

### Step 2: Setup Environment

```bash
# Create feature branch
git checkout -b feature/$(basename $PLAN_DIR)

# Verify org connection
sf org display --target-org $DEFAULT_ORG

# Pull latest metadata
sf project retrieve start
```

### Step 3: Deploy Implementation Subagents (PARALLEL)

**CRITICAL**: Based on the plan, spawn the appropriate subagents IN PARALLEL:

```
Use the Task tool to spawn these subagents concurrently:

1. APEX IMPLEMENTATION SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Implement Apex components for: [FEATURE]

     Plan file: [PLAN_PATH]

     Read and follow patterns from:
     - .claude/skills/apex-patterns/
     - .claude/skills/governor-limits/
     - .claude/skills/security-guide/

     Components to create:
     [LIST FROM PLAN]

     For each class:
     1. Follow existing trigger handler pattern
     2. Implement CRUD/FLS checks
     3. Bulkify all operations
     4. Add proper error handling
     5. Include ApexDoc comments

     Return: List of files created with paths

2. LWC IMPLEMENTATION SUBAGENT (if UI in plan)
   subagent_type: "general-purpose"
   prompt: |
     Implement LWC components for: [FEATURE]

     Plan file: [PLAN_PATH]

     Read and follow patterns from:
     - .claude/skills/lwc-patterns/
     - .claude/skills/security-guide/

     Components to create:
     [LIST FROM PLAN]

     For each component:
     1. Use wire adapters for cacheable data
     2. Implement proper error handling
     3. Add loading states
     4. Follow accessibility guidelines
     5. Create Apex controller if needed

     Return: List of files created with paths

3. CONFIG IMPLEMENTATION SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Implement configuration/metadata for: [FEATURE]

     Plan file: [PLAN_PATH]

     Components to create:
     [LIST FROM PLAN - objects, fields, flows, permissions]

     For each:
     1. Create custom objects/fields via SFDX
     2. Setup validation rules
     3. Configure Flows
     4. Create permission sets

     Commands to use:
     - sf sobject create field
     - sf flow create

     Return: List of metadata created

4. TEST IMPLEMENTATION SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Create test classes for: [FEATURE]

     Plan file: [PLAN_PATH]

     Read patterns from:
     - .claude/skills/test-factory/

     Classes needing tests:
     [LIST FROM PLAN]

     For each test class:
     1. Create test data factory methods
     2. Test positive scenarios
     3. Test negative scenarios
     4. Test bulk (200+ records)
     5. Test as different users/profiles
     6. Target 90%+ coverage

     Return: List of test files created with coverage estimates
```

### Step 4: Coordinate Dependencies

Some components have dependencies. Handle sequentially:

```
IF Trigger depends on Handler:
  1. Wait for Apex Subagent to create Handler
  2. Then create Trigger

IF LWC depends on Apex Controller:
  1. Wait for Apex Subagent to create Controller
  2. Then allow LWC Subagent to complete component
```

### Step 5: Deploy Validation Subagents (PARALLEL)

After implementation, validate:

```
Use the Task tool to spawn these subagents concurrently:

1. DEPLOYMENT VALIDATION SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Validate deployment for: [FEATURE]

     Run commands:
     - sf project deploy validate --target-org scratch-org
     - sf scanner run --target force-app/

     Check:
     - All metadata deploys successfully
     - No PMD critical/high violations
     - No dependency errors

     Return: Deployment validation report

2. TEST EXECUTION SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Execute all tests for: [FEATURE]

     Run commands:
     - sf apex run test --class-names [TEST_CLASSES] --code-coverage

     Verify:
     - All tests pass
     - Coverage >= 90% for new classes
     - No governor limit issues in tests

     Return: Test execution report with coverage
```

### Step 6: Present Progress

During work, display real-time progress:

```
🚀 Executing: Lead Scoring Automation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Plan loaded: 16 tasks across 5 phases

🔧 Subagents Deployed:
  [████████░░] Apex Subagent: 4/6 classes
  [██████████] LWC Subagent: Complete (2 components)
  [████░░░░░░] Config Subagent: 2/5 fields
  [░░░░░░░░░░] Test Subagent: Waiting for Apex

✅ Completed:
  • LeadScoringHandler.cls
  • LeadScoringService.cls
  • leadScoreCard.js
  • leadScoreCard.html

⏳ In Progress:
  • LeadScoringSelector.cls (Apex Subagent)
  • Lead.Score__c (Config Subagent)

📊 Status:
  Files created: 8
  Deployed: 6
  Tests passing: 4/4
  Coverage: 87%
```

### Step 7: Complete and Create PR

When all subagents complete:

```bash
# Final validation
sf project deploy validate --target-org $SANDBOX_ORG --test-level RunLocalTests

# Commit all changes
git add .
git commit -m "feat: [FEATURE] - Implementation complete

Components:
- [LIST OF CREATED COMPONENTS]

Coverage: XX%"

# Push and create PR
git push -u origin feature/$(basename $PLAN_DIR)

gh pr create \
  --title "Feature: [FEATURE NAME]" \
  --body "$(cat .specify/specs/<feature>/plan.md)" \
  --base main
```

---

## Subagent Coordination Patterns

### Pattern 1: Independent Work (Parallel)
```
Config Subagent ─┬─> Creates fields
Apex Subagent   ─┼─> Creates service classes (no field dependency)
LWC Subagent    ─┴─> Creates components (no Apex dependency)
```

### Pattern 2: Sequential Dependency
```
Apex Subagent creates Handler
         │
         ▼
Apex Subagent creates Trigger (depends on Handler)
         │
         ▼
Test Subagent creates tests (depends on all Apex)
```

### Pattern 3: Cross-Subagent Dependency
```
Apex Subagent creates Controller
         │
         ├──────────────────────────┐
         ▼                          ▼
LWC Subagent imports Controller    Test Subagent tests Controller
```

---

## Error Handling

### Subagent Failure

```
❌ Apex Subagent Failed

Error: LeadScoringHandler.cls
  Line 45: Variable 'score' does not exist

Options:
  1. [Auto-fix] Let subagent retry with error context
  2. [Manual] Review and fix manually
  3. [Skip] Continue with other subagents

Choice [1/2/3]: 1

🔄 Retrying Apex Subagent with error context...
```

### Dependency Blocked

```
⚠️ Test Subagent Blocked

Waiting for:
  - LeadScoringHandler.cls (Apex Subagent: In Progress)
  - LeadScoringService.cls (Apex Subagent: In Progress)

Auto-resuming when dependencies complete...
```

### Deployment Failure

```
❌ Deployment Validation Failed

Errors:
  1. LeadTrigger.trigger: Dependent class 'LeadScoringHandler' not found

Resolution:
  Apex Subagent will deploy Handler first, then retry Trigger

🔄 Reordering deployment sequence...
```

---

## Session Management

### Pause Work
```bash
/sf-work --pause

💾 Session saved: .sf-compound/work-session.json
   Completed: 8/16 tasks
   Subagent states preserved
   Resume with: /sf-work --resume
```

### Resume Work
```bash
/sf-work --resume

📋 Resuming: Lead Scoring Automation
   Restoring 4 subagent states...

   ✓ Apex Subagent: Resuming from LeadScoringSelector
   ✓ Config Subagent: Resuming from validation rules
   ✓ LWC Subagent: Complete
   ✓ Test Subagent: Ready to start
```

---

## Example Execution

### Input
```bash
/sf-work .specify/specs/001-lead-scoring/plan.md
```

### Output (Progressive)
```
🚀 Starting: Lead Scoring Automation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Plan Analysis:
   Apex Classes: 4 (Handler, Service, Selector, Trigger)
   LWC Components: 2 (scoreCard, scoreHistory)
   Custom Fields: 3 (Score__c, Last_Score_Date__c, Score_History__c)
   Test Classes: 3

🌿 Branch created: feature/001-lead-scoring
🔗 Org connected: MyDevOrg

🤖 Deploying 4 subagents...

[00:00] Apex Subagent: Starting...
[00:00] LWC Subagent: Starting...
[00:00] Config Subagent: Starting...
[00:02] Config Subagent: ✓ Created Lead.Score__c
[00:03] Apex Subagent: ✓ Created LeadScoringHandler.cls
[00:05] Config Subagent: ✓ Created Lead.Last_Score_Date__c
[00:06] Apex Subagent: ✓ Created LeadScoringService.cls
[00:08] LWC Subagent: ✓ Created leadScoreCard component
[00:10] Apex Subagent: ✓ Created LeadScoringSelector.cls
[00:12] Apex Subagent: ✓ Created LeadTrigger.trigger
[00:14] LWC Subagent: ✓ Created leadScoreHistory component
[00:15] Config Subagent: Complete ✅

[00:16] Test Subagent: Starting (dependencies met)...
[00:20] Test Subagent: ✓ Created LeadScoringHandlerTest.cls
[00:24] Test Subagent: ✓ Created LeadScoringServiceTest.cls
[00:28] Test Subagent: Complete ✅

[00:30] Validation Subagent: Running deployment check...
[00:45] Validation Subagent: ✓ Deployment valid

[00:46] Test Execution Subagent: Running tests...
[01:15] Test Execution Subagent: ✓ All tests pass (12/12)
[01:15] Test Execution Subagent: ✓ Coverage: 94%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Implementation Complete!

Files Created: 12
Tests Passing: 12/12
Coverage: 94%

Next Steps:
  1. Review changes: git diff main
  2. Run review: /sf-review
  3. Create PR: /sf-deploy pr
```

---

## Integration with Other Commands

```bash
# After work completes
/sf-review                    # Multi-agent code review
/sf-test --coverage           # Run full test suite
/sf-deploy sandbox            # Deploy to sandbox
/sf-compound                  # Document learnings
```
