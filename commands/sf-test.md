---
name: sf-test
description: Parallel test execution and analysis with specialized subagents
arguments:
  - name: scope
    description: Test scope (all, local, class:ClassName, changed)
    required: false
---

# Salesforce Test Command

Runs Apex tests using **parallel subagents** for execution, coverage analysis, and quality recommendations.

## Subagent Architecture

```
/sf-test [scope]
    │
    ├── [PARALLEL ANALYSIS PHASE]
    │   ├── Test Discovery Subagent: Find tests to run
    │   ├── Coverage Analysis Subagent: Identify coverage gaps
    │   └── Test Quality Subagent: Assess test patterns
    │
    ├── [EXECUTION PHASE]
    │   └── Test Runner Subagent: Execute tests
    │
    └── [REPORTING PHASE]
        ├── Results Subagent: Parse and format results
        └── Recommendations Subagent: Generate improvements
```

---

## Workflow

When the user runs `/sf-test [scope]`, execute the following:

### Step 1: Determine Test Scope

```
IF scope is empty or "local":
    Run all local tests
ELSE IF scope is "all":
    Run all tests including managed packages
ELSE IF scope starts with "class:":
    Run specific test class
ELSE IF scope is "changed":
    Detect changed classes, run their tests
```

### Step 2: Deploy Analysis Subagents (PARALLEL)

**Deploy these 3 subagents IN PARALLEL using the Task tool:**

```
1. TEST DISCOVERY SUBAGENT
   subagent_type: "Explore"
   prompt: |
     Find all relevant test classes for scope: [SCOPE]

     Search for:
     - Files matching *Test.cls
     - @isTest annotated classes
     - Test methods (@isTest or testMethod)

     If scope is "changed":
     - Get changed files: git diff --name-only main
     - Find corresponding test classes

     Return: List of test classes to run

2. COVERAGE ANALYSIS SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Analyze existing test coverage for: [SCOPE]

     Read agent: .claude/agents/apex/apex-test-coverage-analyst.md

     Identify:
     - Classes with < 75% coverage
     - Classes with no tests
     - Uncovered code paths

     Return: Coverage gap report

3. TEST QUALITY SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Analyze test quality patterns.

     Read skill: .claude/skills/test-factory/

     Check tests for:
     - Bulk testing (200+ records)
     - Positive/negative scenarios
     - System.runAs() usage
     - Proper assertions
     - TestSetup methods
     - Test data isolation

     Return: Test quality assessment
```

### Step 3: Execute Tests

```
TEST RUNNER SUBAGENT
subagent_type: "Bash"
prompt: |
  Execute Apex tests:

  sf apex run test \
    --test-level [LEVEL] \
    --class-names [CLASSES] \
    --code-coverage \
    --result-format json \
    --output-dir test-results \
    --wait 30

  Return: Raw test results JSON
```

### Step 4: Deploy Reporting Subagents (PARALLEL)

**After execution, deploy these IN PARALLEL:**

```
1. RESULTS SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Parse test results from: test-results/

     Generate report:
     - Total tests: X
     - Passed: Y
     - Failed: Z
     - Duration: T seconds
     - Overall coverage: X%

     For each failed test:
     - Class and method name
     - Error message
     - Stack trace location

     For coverage:
     - Per-class coverage percentages
     - Uncovered line numbers

     Return: Formatted test report

2. RECOMMENDATIONS SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Based on test results, generate recommendations.

     Read:
     - .claude/agents/apex/apex-test-coverage-analyst.md
     - .claude/skills/test-factory/

     Provide recommendations for:
     - Failed tests: How to fix
     - Low coverage classes: What to test
     - Missing test patterns: What to add

     Return: Actionable improvement list
```

### Step 5: Present Results

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SALESFORCE TEST EXECUTION COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Test Results

┌─────────────────┬───────┐
│ Total Tests     │   150 │
│ Passed          │   148 │
│ Failed          │     2 │
│ Skipped         │     0 │
│ Duration        │ 45.2s │
└─────────────────┴───────┘

📈 Code Coverage: 82% overall

┌─────────────────────────┬──────────┬────────┐
│ Class                   │ Coverage │ Status │
├─────────────────────────┼──────────┼────────┤
│ AccountService          │      95% │ ✅     │
│ AccountTriggerHandler   │      88% │ ✅     │
│ OpportunityHelper       │      72% │ ⚠️     │
│ LeadProcessor           │      45% │ ❌     │
└─────────────────────────┴──────────┴────────┘

❌ Failed Tests:

  1. AccountServiceTest.testBulkInsert
     Error: System.AssertException: Expected 100, Actual 99
     File: AccountServiceTest.cls:45

  2. OpportunityTriggerTest.testValidation
     Error: System.DmlException: Required field missing
     File: OpportunityTriggerTest.cls:78

💡 Recommendations:

  Coverage:
  • LeadProcessor.cls (45%) - Add tests for processLead(), validateLead()
  • OpportunityHelper.cls (72%) - Add negative test cases

  Quality:
  • AccountServiceTest - Add bulk test with 200+ records
  • ContactTriggerTest - Add System.runAs() for sharing tests

Next Steps:
  • Fix failures: /sf-resolve AccountServiceTest.testBulkInsert
  • Generate tests: /sf-test generate LeadProcessor
  • Re-run: /sf-test local
```

---

## Test Generation Mode

When used with `generate` argument:

```bash
/sf-test generate AccountService
```

### Deploy Generation Subagents (PARALLEL)

```
1. CLASS ANALYSIS SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Analyze AccountService.cls for test generation.

     Identify:
     - Public methods to test
     - Code branches (if/else, switch)
     - Exception paths
     - DML operations
     - SOQL queries

     Return: Test requirements matrix

2. TEST GENERATION SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Generate comprehensive test class for AccountService.

     Read skill: .claude/skills/test-factory/

     Include:
     - @TestSetup with TestDataFactory
     - Positive tests for each method
     - Negative tests (invalid inputs)
     - Bulk tests (200+ records)
     - Exception handling tests
     - System.runAs() for sharing tests

     Follow patterns from test-factory skill.

     Return: Complete test class code

3. MOCK GENERATION SUBAGENT (if needed)
   subagent_type: "general-purpose"
   prompt: |
     Generate mocks for AccountService dependencies.

     Read skill: .claude/skills/test-factory/

     Create:
     - HttpCalloutMock implementations
     - StubProvider implementations
     - Test utility methods

     Return: Mock classes code
```

### Generated Test Output

```apex
/**
 * @description Test class for AccountService
 * @author SF Compound Engineering CLI
 * Generated: 2024-01-15
 */
@isTest
private class AccountServiceTest {

    @TestSetup
    static void setup() {
        // Create 200+ records for bulk testing
        List<Account> accounts = TestDataFactory.createAccounts(200);
        insert accounts;
    }

    /**
     * @description Test processAccounts with valid bulk data
     */
    @isTest
    static void testProcessAccounts_BulkPositive() {
        List<Account> accounts = [SELECT Id, Name FROM Account];

        Test.startTest();
        List<Account> result = AccountService.processAccounts(accounts);
        Test.stopTest();

        System.assertEquals(200, result.size(), 'Should process all accounts');
        // Additional assertions...
    }

    /**
     * @description Test processAccounts with null input
     */
    @isTest
    static void testProcessAccounts_NullInput() {
        Test.startTest();
        try {
            AccountService.processAccounts(null);
            System.assert(false, 'Should have thrown exception');
        } catch (AccountService.AccountServiceException e) {
            System.assertEquals('Input cannot be null', e.getMessage());
        }
        Test.stopTest();
    }

    /**
     * @description Test with different user profiles
     */
    @isTest
    static void testProcessAccounts_AsStandardUser() {
        User standardUser = TestDataFactory.createUser('Standard User');

        System.runAs(standardUser) {
            Test.startTest();
            // Test behavior for standard user
            Test.stopTest();
        }
    }
}
```

---

## Test Execution Options

### Run All Tests
```bash
/sf-test all
# sf apex run test --test-level RunAllTestsInOrg --code-coverage
```

### Run Local Tests Only
```bash
/sf-test local
# sf apex run test --test-level RunLocalTests --code-coverage
```

### Run Specific Class
```bash
/sf-test class:AccountServiceTest
# sf apex run test --class-names AccountServiceTest --code-coverage
```

### Run Tests for Changed Files
```bash
/sf-test changed
# Detects changed .cls files, finds corresponding tests
```

### Generate Tests
```bash
/sf-test generate AccountService
# Generates comprehensive test class
```

---

## Coverage Thresholds

| Coverage | Status | Action |
|----------|--------|--------|
| ≥ 90% | ✅ Excellent | Deploy ready |
| 75-89% | ⚠️ Acceptable | Consider improvements |
| < 75% | ❌ Insufficient | Must improve before deploy |

---

## Integration with Other Commands

```bash
# Full workflow
/sf-work plan.md           # Implement feature
/sf-test                   # Run tests
/sf-review                 # Review code
/sf-test generate NewClass # Generate missing tests
/sf-deploy sandbox         # Deploy to sandbox
```
