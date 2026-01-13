---
name: sf-work
description: Execute Salesforce implementation plans systematically with validation
arguments:
  - name: plan_file
    description: Path to the plan markdown file
    required: true
---

# Salesforce Work Execution Command

Executes implementation plans created by `/sf-plan` systematically, with continuous validation and Salesforce-specific checks.

## Workflow

When the user runs `/sf-work [plan file]`, execute the following:

### Step 1: Load and Parse Plan

```bash
# Read the plan file from .specify/specs/<feature>/
# Example: .specify/specs/001-lead-scoring/plan.md
cat .specify/specs/001-lead-scoring/plan.md

# Also read the spec and tasks files
cat .specify/specs/001-lead-scoring/spec.md   # Requirements
cat .specify/specs/001-lead-scoring/tasks.md  # Checklist

# Extract key sections from plan.md:
# - Data Model Changes
# - Automation Components
# - Test Requirements
# - Deployment Sequence
```

### Step 2: Setup Work Environment

```bash
# Create feature branch
git checkout -b feature/$(basename $PLAN_FILE .md)

# Verify org connection
sf org display --target-org $DEFAULT_ORG

# Create scratch org if needed (for ISV development)
sf org create scratch --definition-file config/project-scratch-def.json --alias feature-org

# Pull latest metadata
sf project retrieve start --target-org $DEFAULT_ORG
```

### Step 3: Generate Todo List

Parse the plan and create a structured todo list:

```markdown
## Work Todos for: [Feature Name]

### Phase 1: Data Model
- [ ] TODO-001: Create custom field Score__c on Lead
- [ ] TODO-002: Create custom field Last_Score_Date__c on Lead
- [ ] TODO-003: Create custom object Scoring_Rule__c

### Phase 2: Backend Logic
- [ ] TODO-004: Create LeadScoringHandler.cls
- [ ] TODO-005: Create LeadScoringService.cls
- [ ] TODO-006: Create LeadScoringSelector.cls
- [ ] TODO-007: Update LeadTrigger.trigger

### Phase 3: Tests
- [ ] TODO-008: Create LeadScoringHandlerTest.cls
- [ ] TODO-009: Create LeadScoringServiceTest.cls
- [ ] TODO-010: Achieve 90%+ coverage

### Phase 4: UI Components
- [ ] TODO-011: Create leadScoreCard LWC
- [ ] TODO-012: Create leadScoreCard.js-meta.xml
- [ ] TODO-013: Add to Lead Lightning Record Page

### Phase 5: Deployment
- [ ] TODO-014: Validate deployment to sandbox
- [ ] TODO-015: Create permission set
- [ ] TODO-016: Update package.xml
```

### Step 4: Execute Todos Systematically

For each todo:

```
1. Read the todo requirements
2. Research existing patterns (if needed)
3. Implement the change
4. Run local validation
5. Run relevant tests
6. Mark todo complete
7. Commit with meaningful message
```

#### For Apex Classes:

```bash
# After creating/modifying Apex
# Run PMD static analysis
sf scanner run --target force-app/main/default/classes/NewClass.cls

# Deploy to scratch org for validation
sf project deploy start --source-dir force-app/main/default/classes/NewClass.cls

# Run specific test class
sf apex run test --class-names NewClassTest --result-format human

# Check coverage
sf apex run test --class-names NewClassTest --code-coverage --result-format human
```

#### For LWC Components:

```bash
# After creating/modifying LWC
# Run ESLint
npx eslint force-app/main/default/lwc/componentName/

# Deploy component
sf project deploy start --source-dir force-app/main/default/lwc/componentName/

# Run Jest tests (if configured)
npm run test:unit -- --testPathPattern=componentName
```

#### For Flows:

```bash
# Validate Flow XML
sf project deploy validate --source-dir force-app/main/default/flows/FlowName.flow-meta.xml

# Deploy Flow
sf project deploy start --source-dir force-app/main/default/flows/FlowName.flow-meta.xml
```

### Step 5: Continuous Validation

After each significant change:

```bash
# Run all local tests
sf apex run test --test-level RunLocalTests --code-coverage

# Check for PMD violations
sf scanner run --target force-app/main/default/

# Validate full deployment
sf project deploy validate --target-org $DEFAULT_ORG --test-level RunLocalTests
```

### Step 6: Create Pull Request

When all todos complete:

```bash
# Final validation
sf project deploy validate --target-org $SANDBOX_ORG --test-level RunLocalTests

# Push branch
git push -u origin feature/$(basename $PLAN_FILE .md)

# Create PR (GitHub CLI)
gh pr create \
  --title "Feature: [Feature Name]" \
  --body "$(cat .specify/specs/001-feature-name/plan.md)" \
  --base main
```

## Todo Execution Patterns

### Pattern: Apex Class Creation

```
Todo: Create AccountScoringService.cls

1. Check for existing service pattern:
   find . -name "*Service.cls" -exec head -20 {} \;

2. Create class following pattern:
   - Public with sharing class
   - Static methods for stateless operations
   - Instance methods for stateful operations
   - Proper exception handling

3. Create corresponding test class:
   - Test positive scenarios
   - Test negative scenarios
   - Test bulk (200+ records)
   - Test as different users

4. Validate:
   sf apex run test --class-names AccountScoringServiceTest
   
5. Commit:
   git add force-app/main/default/classes/AccountScoringService*
   git commit -m "feat: Add AccountScoringService for score calculations"
```

### Pattern: Trigger Implementation

```
Todo: Update AccountTrigger for scoring

1. Check trigger handler pattern:
   cat force-app/main/default/triggers/AccountTrigger.trigger

2. Update trigger (keep it thin):
   trigger AccountTrigger on Account (...) {
       new AccountTriggerHandler().run();
   }

3. Update handler with new logic:
   - Add method to handler
   - Call service layer for business logic

4. Test:
   sf apex run test --class-names AccountTriggerHandlerTest

5. Validate full trigger test suite:
   sf apex run test --tests AccountTriggerHandlerTest,AccountScoringServiceTest
```

### Pattern: LWC Component Creation

```
Todo: Create accountScoreCard LWC

1. Create component structure:
   sf lightning generate component --type lwc --name accountScoreCard

2. Implement component:
   - accountScoreCard.html (template)
   - accountScoreCard.js (controller)
   - accountScoreCard.css (styles)
   - accountScoreCard.js-meta.xml (config)

3. Create Apex controller if needed:
   - AccountScoreCardController.cls
   - AccountScoreCardControllerTest.cls

4. Test:
   - Deploy to scratch org
   - Manual testing on record page
   - Jest tests if configured

5. Commit:
   git add force-app/main/default/lwc/accountScoreCard/
   git commit -m "feat: Add accountScoreCard component"
```

## Work Session Management

### Starting a Work Session

```bash
/sf-work .specify/specs/001-lead-scoring/plan.md

Output:
📋 Loaded plan: Lead Scoring Automation
📊 Generated 16 todos across 5 phases
🔧 Environment: MyDevOrg (connected)
📁 Branch: feature/lead-scoring created

Starting Phase 1: Data Model
─────────────────────────────
TODO-001: Create custom field Score__c on Lead
  Press Enter to start, 's' to skip, 'q' to quit...
```

### During Work

```
✅ TODO-001: Complete
   Created: Lead.Score__c (Number)
   Deployed to: MyDevOrg
   
Moving to TODO-002...

TODO-002: Create custom field Last_Score_Date__c on Lead
  Working...
```

### Pausing and Resuming

```bash
# Save progress
/sf-work --pause

Output:
💾 Progress saved to .sf-compound/work-session.json
   Completed: 8/16 todos
   Current phase: Phase 2 - Backend Logic
   
Resume with: /sf-work --resume
```

### Resuming Work

```bash
/sf-work --resume

Output:
📋 Resuming: Lead Scoring Automation
📊 Progress: 8/16 todos complete
📍 Continuing from: TODO-009

TODO-009: Create LeadScoringServiceTest.cls
  Press Enter to continue...
```

## Validation Checkpoints

### After Each Phase

```
Phase 1 Complete: Data Model ✅
─────────────────────────────
Created:
  ✓ Lead.Score__c
  ✓ Lead.Last_Score_Date__c
  ✓ Scoring_Rule__c (custom object)

Validation:
  ✓ All fields deployed successfully
  ✓ Field-level security set
  ✓ Page layouts updated

Proceed to Phase 2? [Y/n]
```

### Before Pull Request

```
Pre-PR Validation
─────────────────
Code Quality:
  ✓ No PMD violations (Critical/High)
  ✓ All tests passing
  ✓ Code coverage: 94% (target: 90%)

Deployment Validation:
  ✓ Validated to sandbox: SUCCESS
  ✓ All metadata accounted for
  ✓ No destructive changes

Documentation:
  ✓ Apex classes have ApexDoc
  ✓ LWC components documented
  ✓ README updated

Ready to create PR? [Y/n]
```

## Error Handling

### Deployment Failure

```
❌ Deployment Failed: TODO-007

Error: 
  LeadTrigger.trigger: Dependent class 'LeadScoringHandler' does not exist

Resolution Options:
  1. Complete TODO-004 first (creates LeadScoringHandler)
  2. Reorder todos to fix dependency
  3. Skip and come back later

Choice [1/2/3]:
```

### Test Failure

```
⚠️ Test Failed: TODO-009

Failed Tests:
  LeadScoringServiceTest.testBulkScoring
    Expected: 100 leads updated
    Actual: 50 leads updated

Options:
  1. Debug and fix
  2. View full stack trace
  3. Skip (not recommended)
  
Choice [1/2/3]:
```

## Integration with Other Commands

```bash
# After work, run review
/sf-review

# If issues found, resolve them
/sf-resolve

# Then deploy
/sf-deploy sandbox
```
