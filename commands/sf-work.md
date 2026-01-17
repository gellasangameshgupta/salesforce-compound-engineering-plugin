---
name: sf-work
description: Execute Salesforce implementation plans using parallel subagents
arguments:
  - name: plan
    description: Path to the plan.md file
    required: true
---

# /sf-work

Execute implementation plans using parallel subagents for Apex, LWC, Config, and Tests.

## Instructions

When this command is invoked, you MUST follow these steps exactly:

### Step 1: Load the Plan

Read the plan file from `$ARGUMENTS.plan`:

```bash
# Read the plan
cat $ARGUMENTS.plan

# Also read related files
cat $(dirname $ARGUMENTS.plan)/spec.md
cat $(dirname $ARGUMENTS.plan)/tasks.md
```

Extract:
- Components to build (Apex, LWC, Flows, Objects)
- Dependencies between components
- Test requirements

Announce: "Starting /sf-work for: [feature name from plan]"

### Step 2: Setup Environment

```bash
# Create feature branch
git checkout -b feature/[feature-slug]

# Verify org connection
sf org display
```

Display:
```
Environment Setup:
  • Branch: feature/[name]
  • Org: [org alias]
  • Plan: [X] components to build
```

### Step 3: Deploy Implementation Subagents (PARALLEL)

**IMMEDIATELY spawn these subagents in parallel using the Task tool:**

<subagent_deployment>
You MUST call Task tool multiple times in a SINGLE message:

1. Task tool call:
   - description: "Implement Apex classes"
   - subagent_type: "general-purpose"
   - prompt: |
     Implement the Apex components for this feature.

     Plan: [PASTE RELEVANT APEX SECTION FROM PLAN]

     Read these skills first:
     - .claude/skills/apex-patterns/index.md (for patterns)
     - .claude/skills/security-guide/index.md (for CRUD/FLS)
     - .claude/skills/governor-limits/index.md (for limits)

     Create these files:
     [LIST APEX CLASSES FROM PLAN]

     Requirements:
     - Follow trigger handler pattern
     - Implement CRUD/FLS checks
     - Bulkify all operations
     - Add ApexDoc comments
     - Create in force-app/main/default/classes/

     Return: List of files created with paths

2. Task tool call:
   - description: "Implement LWC components"
   - subagent_type: "general-purpose"
   - prompt: |
     Implement the LWC components for this feature.

     Plan: [PASTE RELEVANT LWC SECTION FROM PLAN]

     Read these skills first:
     - .claude/skills/lwc-patterns/index.md
     - .claude/skills/security-guide/index.md

     Create these components:
     [LIST LWC COMPONENTS FROM PLAN]

     Requirements:
     - Use wire adapters for cacheable data
     - Implement error handling with toast
     - Add loading states
     - Follow accessibility guidelines
     - Create in force-app/main/default/lwc/

     Return: List of files created with paths

3. Task tool call:
   - description: "Create configuration"
   - subagent_type: "general-purpose"
   - prompt: |
     Create the configuration/metadata for this feature.

     Plan: [PASTE RELEVANT CONFIG SECTION FROM PLAN]

     Create:
     [LIST OBJECTS, FIELDS, FLOWS FROM PLAN]

     Use SFDX commands:
     - sf sobject create for objects
     - Manual XML for fields
     - Flow XML or sf flow create

     Create in force-app/main/default/objects/ and flows/

     Return: List of metadata created

4. Task tool call:
   - description: "Implement test classes"
   - subagent_type: "general-purpose"
   - prompt: |
     Create comprehensive test classes for this feature.

     Plan: [PASTE RELEVANT TEST SECTION FROM PLAN]

     Read this skill first:
     - .claude/skills/test-factory/index.md

     Create test classes for:
     [LIST CLASSES NEEDING TESTS]

     Requirements:
     - @TestSetup with TestDataFactory
     - Positive tests for each method
     - Negative tests (invalid inputs)
     - Bulk tests (200+ records)
     - System.runAs() for user context
     - Target 90%+ coverage

     Create in force-app/main/default/classes/

     Return: List of test files created
</subagent_deployment>

**Wait for all implementation subagents to complete.**

Display progress:
```
Implementation Phase (4 subagents):
  ├── Apex classes: [status]
  ├── LWC components: [status]
  ├── Configuration: [status]
  └── Test classes: [status]
```

### Step 4: Deploy Validation Subagents (PARALLEL)

**After implementation completes, spawn validation subagents:**

<subagent_deployment>
Call Task tool 2 times in a SINGLE message:

1. Task tool call:
   - description: "Validate deployment"
   - subagent_type: "Bash"
   - prompt: |
     Validate the deployment of all created files.

     Run these commands:
     1. sf project deploy validate --source-dir force-app/main/default/
     2. sf scanner run --target force-app/main/default/ --format table

     Check:
     - All metadata deploys successfully
     - No PMD critical/high violations
     - No dependency errors

     Return: Validation results

2. Task tool call:
   - description: "Run tests"
   - subagent_type: "Bash"
   - prompt: |
     Run all tests for the new code.

     Commands:
     sf apex run test --class-names [TEST_CLASSES] --code-coverage --result-format human

     Verify:
     - All tests pass
     - Coverage >= 90%

     Return: Test results with coverage
</subagent_deployment>

**Wait for validation to complete.**

Display progress:
```
Validation Phase (2 subagents):
  ├── Deployment validation: [status]
  └── Test execution: [status]
```

### Step 5: Handle Errors

If any subagent fails:

```
❌ [Subagent] Failed

Error: [error message]

Options:
1. [Resume] Retry with error context
2. [Skip] Continue with other subagents
3. [Abort] Stop /sf-work

Choice:
```

For resume, spawn a new Task with error context included in prompt.

### Step 6: Complete and Report

When all subagents complete successfully:

```bash
# Commit all changes
git add .
git commit -m "feat: [Feature Name]

Components:
- [List of components created]

Coverage: XX%"
```

Present results:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  /sf-work COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 6 subagents deployed

Implementation Phase:
  ✓ Apex classes: X files created
  ✓ LWC components: Y components created
  ✓ Configuration: Z metadata items
  ✓ Test classes: W test files

Validation Phase:
  ✓ Deployment: Valid
  ✓ Tests: XX/XX passing
  ✓ Coverage: XX%

📁 Files created: [total count]
📝 Commit: [commit hash]

Next Steps:
  • Review code: /sf-review
  • Push changes: git push -u origin feature/[name]
  • Create PR: /sf-deploy pr
```

## Important

- You MUST call Task tool to spawn subagents
- Implementation subagents run in PARALLEL (one message)
- Validation subagents run in PARALLEL after implementation
- Each subagent MUST read skill files for patterns
- Handle errors gracefully with retry options
