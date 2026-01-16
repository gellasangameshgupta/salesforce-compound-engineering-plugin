---
name: sf-test
description: Comprehensive Apex test analysis, execution, and coverage reporting
arguments:
  - name: scope
    description: Test scope (all, local, class:ClassName, changed)
    required: false
---

# Salesforce Test Command

Runs Apex tests with comprehensive reporting, coverage analysis, and recommendations. Can also generate new tests following best practices.

## Required: Load Test Agents and Skills

**IMPORTANT**: Before running or generating tests, load these files:

### Agent to Load
```
.claude/agents/apex/apex-test-coverage-analyst.md  # Test quality standards, coverage analysis
```

### Skill to Load
```
.claude/skills/test-factory/  # Test data factory patterns, mocking, assertions
```

### How to Apply

1. **Read the agent** to understand test quality standards
2. **Read the skill** for test data factory and mocking patterns
3. **When generating tests**: Use patterns from test-factory skill
4. **When analyzing tests**: Apply checklist from test-coverage-analyst agent
5. **Ensure bulk testing**: All tests should handle 200+ records

---

## Workflow

### Step 1: Determine Test Scope

```bash
# Based on argument:
# all       → Run all tests in org
# local     → Run local tests only (excludes managed packages)
# class:X   → Run specific test class
# changed   → Run tests for changed classes (smart detection)
```

### Step 2: Execute Tests

```bash
# Run local tests with coverage
sf apex run test \
  --test-level RunLocalTests \
  --code-coverage \
  --result-format human \
  --output-dir test-results \
  --wait 30
```

### Step 3: Analyze Results

```markdown
## Test Execution Report

### Summary
| Metric | Value |
|--------|-------|
| Total Tests | 150 |
| Passed | 148 |
| Failed | 2 |
| Skipped | 0 |
| Duration | 45.2s |

### Code Coverage
| Class | Coverage | Status |
|-------|----------|--------|
| AccountService | 95% | ✅ |
| AccountTriggerHandler | 88% | ✅ |
| OpportunityHelper | 72% | ⚠️ |
| LeadProcessor | 45% | ❌ |

**Overall Coverage: 82%**

### Failed Tests
1. **AccountServiceTest.testBulkInsert**
   - Error: System.AssertException: Expected 100, Actual 99
   - Line: 45

2. **OpportunityTriggerTest.testValidation**
   - Error: System.DmlException: Required field missing
   - Line: 78
```

### Step 4: Recommendations

```markdown
## Recommendations

### Coverage Improvements Needed
1. **LeadProcessor.cls** (45%)
   - Missing tests for: processLead(), validateLead()
   - Add bulk test scenario

2. **OpportunityHelper.cls** (72%)
   - Missing negative test cases
   - Add exception handling tests

### Test Quality Issues
1. **AccountServiceTest**
   - Uses hardcoded IDs (line 23)
   - No bulk test (recommend 200+ records)

2. **ContactTriggerTest**
   - Missing System.runAs() for sharing tests
```

## Test Execution Options

### Run All Tests
```bash
sf apex run test --test-level RunAllTestsInOrg --code-coverage
```

### Run Local Tests Only
```bash
sf apex run test --test-level RunLocalTests --code-coverage
```

### Run Specific Class
```bash
sf apex run test --class-names MyTestClass --code-coverage
```

### Run Specific Methods
```bash
sf apex run test --tests MyTestClass.testMethod1,MyTestClass.testMethod2
```

### Run Tests for Changed Files
```bash
# Detect changed Apex classes
CHANGED=$(git diff --name-only main | grep "\.cls$" | xargs -I {} basename {} .cls)

# Find corresponding test classes
for CLASS in $CHANGED; do
  TEST_CLASS="${CLASS}Test"
  if [ -f "force-app/main/default/classes/${TEST_CLASS}.cls" ]; then
    echo $TEST_CLASS
  fi
done
```

## Coverage Analysis

### Per-Class Coverage
```bash
sf apex run test \
  --test-level RunLocalTests \
  --code-coverage \
  --result-format json > coverage.json

# Parse coverage
jq '.result.coverage.coverage[] | {name: .name, coverage: .coveredPercent}' coverage.json
```

### Lines Not Covered
```bash
# Get uncovered lines for specific class
sf apex run test \
  --class-names AccountServiceTest \
  --code-coverage \
  --result-format json | \
  jq '.result.coverage.coverage[] | select(.name=="AccountService") | .uncoveredLines'
```

## Test Data Factory Integration

```apex
// Recommended test pattern
@isTest
private class AccountServiceTest {
    
    @TestSetup
    static void setup() {
        // Create shared test data
        List<Account> accounts = TestDataFactory.createAccounts(200);
        insert accounts;
    }
    
    @isTest
    static void testBulkOperation() {
        List<Account> accounts = [SELECT Id FROM Account];
        
        Test.startTest();
        AccountService.processAccounts(accounts);
        Test.stopTest();
        
        // Assertions
    }
}
```
