---
name: apex-generate
description: "Generate Apex classes and tests with bulkification, CRUD/FLS, and the project's trigger framework wired in. Covers services, selectors, domain classes, batch / queueable / schedulable, invocable methods, REST resources, and the matching test classes with TestDataFactory + 251+ record bulk tests. Trigger phrases: 'create an Apex class', 'generate a service class', 'write a queueable for', 'scaffold a batch class', 'build an @InvocableMethod', 'add a REST resource', 'generate Apex tests for', 'cover this class with tests'. Pairs with `apex-patterns` (reference) and `test-factory` (TDF reference). Do NOT trigger for triggers themselves — use `apex-trigger-refactor` for trigger work."
argument-hint: "[class type, target object, business intent, or 'test for <ClassName>']"
---

# <span data-proof="authored" data-by="ai:claude">/apex-generate</span>

> **<span data-proof="authored" data-by="ai:claude">Principles enforced:</span>** <span data-proof="authored" data-by="ai:claude">1 (preserve the quality ceiling), 2 (verifiability), 5 (taste over typing). See</span> <span data-proof="authored" data-by="ai:claude">`PRINCIPLES.md`.</span>

## <span data-proof="authored" data-by="ai:claude">Copy-paste-to-agent</span>

```
Generate production-grade Apex (class + .cls-meta.xml) AND its test class (Test.cls +
.cls-meta.xml) as one unit. Test generation is mandatory, not optional. Bulkify all SOQL
and DML out of loops. Enforce CRUD/FLS via Schema.* checks or USER_MODE. Declare an explicit
sharing keyword on every class. Test with 251+ records to cross the 200-trigger boundary.
Use TestDataFactory — never inline record creation in @TestSetup. Use Assert.* class only —
never legacy System.assertEquals. After generation, run sf code-analyzer and sf apex run
test; remediate sev0/sev1/sev2 violations and capture pass/fail + coverage in the report.
```

## <span data-proof="authored" data-by="ai:claude">Required inputs (gather or infer before authoring)</span>

* **<span data-proof="authored" data-by="ai:claude">Class type</span>** <span data-proof="authored" data-by="ai:claude">— service, selector, domain, batch, queueable, schedulable, invocable, DTO, utility, interface, abstract, exception, REST resource</span>

* **<span data-proof="authored" data-by="ai:claude">Target object(s)</span>** <span data-proof="authored" data-by="ai:claude">and the business intent</span>

* **<span data-proof="authored" data-by="ai:claude">Class name</span>** <span data-proof="authored" data-by="ai:claude">— derive from type + target (e.g.,</span> <span data-proof="authored" data-by="ai:claude">`OpportunityService`,</span> <span data-proof="authored" data-by="ai:claude">`LeadSelector`,</span> <span data-proof="authored" data-by="ai:claude">`OrderBatch`)</span>

* **<span data-proof="authored" data-by="ai:claude">Net-new vs refactor</span>** <span data-proof="authored" data-by="ai:claude">— and any API version constraints</span>

* **<span data-proof="authored" data-by="ai:claude">Verification target</span>** <span data-proof="authored" data-by="ai:claude">— coverage %, specific assertions</span>

<span data-proof="authored" data-by="ai:claude">Defaults if unspecified:</span> <span data-proof="authored" data-by="ai:claude">`with sharing`,</span> <span data-proof="authored" data-by="ai:claude">`public`, API</span> <span data-proof="authored" data-by="ai:claude">`66.0`, ApexDoc on every public method, test class</span> **<span data-proof="authored" data-by="ai:claude">mandatory</span>**<span data-proof="authored" data-by="ai:claude">.</span>

<span data-proof="authored" data-by="ai:claude">If the request is clear, generate immediately. Don't ask back-and-forth on routine choices.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 0: Pre-implementation research (parallel, Principle 7)</span>

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher(class_intent)`</span> <span data-proof="authored" data-by="ai:claude">— has anyone solved this shape?</span> **<span data-proof="authored" data-by="ai:claude">Must-read.</span>**

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-repo-research-analyst(class_intent)`</span> <span data-proof="authored" data-by="ai:claude">— what selectors / services / handlers / TDF already exist? Reuse before generating.</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/apex-patterns/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">(Selector / Service / Domain / Trigger Handler patterns)</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/governor-limits/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">(limit-bearing operations)</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/test-factory/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">(TDF patterns — required for the test class step)</span>

***

## <span data-proof="authored" data-by="ai:claude">Phase 1: Author the production class</span>

1. **<span data-proof="authored" data-by="ai:claude">Choose the smallest correct pattern</span>** <span data-proof="authored" data-by="ai:claude">— service for orchestration, selector for SOQL, domain for object behavior, batch/queueable/schedulable for async,</span> <span data-proof="authored" data-by="ai:claude">`@InvocableMethod`</span> <span data-proof="authored" data-by="ai:claude">for Flow callability.</span>
2. **<span data-proof="authored" data-by="ai:claude">Apply guardrails (every rule below is a hard stop):</span>**

| <span data-proof="authored" data-by="ai:claude">Rule</span>                                                                                                                                                      | <span data-proof="authored" data-by="ai:claude">Why</span>                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">All SOQL</span> **<span data-proof="authored" data-by="ai:claude">outside</span>** <span data-proof="authored" data-by="ai:claude">loops</span>                  | <span data-proof="authored" data-by="ai:claude">Governor limit (100 per transaction)</span>                                                                                                                                                                                                                                                                                                                                       |
| <span data-proof="authored" data-by="ai:claude">All DML</span> **<span data-proof="authored" data-by="ai:claude">outside</span>** <span data-proof="authored" data-by="ai:claude">loops</span>                   | <span data-proof="authored" data-by="ai:claude">Governor limit (150 per transaction)</span>                                                                                                                                                                                                                                                                                                                                       |
| <span data-proof="authored" data-by="ai:claude">Sharing keyword</span> **<span data-proof="authored" data-by="ai:claude">declared</span>** <span data-proof="authored" data-by="ai:claude">on every class</span> | <span data-proof="authored" data-by="ai:claude">`with sharing`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`without sharing`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`inherited sharing`</span> <span data-proof="authored" data-by="ai:claude">— never default</span>                |
| <span data-proof="authored" data-by="ai:claude">CRUD/FLS enforced on every database access</span>                                                                                                                | <span data-proof="authored" data-by="ai:claude">Use</span> <span data-proof="authored" data-by="ai:claude">`Schema.sObjectType.X.isAccessible()`</span> <span data-proof="authored" data-by="ai:claude">or</span> <span data-proof="authored" data-by="ai:claude">`WITH USER_MODE`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`AccessLevel.USER_MODE`</span> |
| <span data-proof="authored" data-by="ai:claude">Bulkify all entry points</span>                                                                                                                                  | <span data-proof="authored" data-by="ai:claude">Methods accept</span> <span data-proof="authored" data-by="ai:claude">`List<SObject>`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`Map<Id, SObject>`, not single records</span>                                                                                                                               |
| <span data-proof="authored" data-by="ai:claude">ApexDoc on every public method</span>                                                                                                                            | <span data-proof="authored" data-by="ai:claude">Includes</span> <span data-proof="authored" data-by="ai:claude">`@param`,</span> <span data-proof="authored" data-by="ai:claude">`@return`,</span> <span data-proof="authored" data-by="ai:claude">`@throws`, business rationale</span>                                                                                                                                           |
| <span data-proof="authored" data-by="ai:claude">`@AuraEnabled(cacheable=true)`</span> <span data-proof="authored" data-by="ai:claude">for read-only LWC reads</span>                                             | <span data-proof="authored" data-by="ai:claude">Cache hit + governor relief</span>                                                                                                                                                                                                                                                                                                                                                |

1. **<span data-proof="authored" data-by="ai:claude">Generate two files together:</span>**

   * <span data-proof="authored" data-by="ai:claude">`{ClassName}.cls`</span>

   * <span data-proof="authored" data-by="ai:claude">`{ClassName}.cls-meta.xml`</span> <span data-proof="authored" data-by="ai:claude">(apiVersion 66.0, status Active)</span>

***

## <span data-proof="authored" data-by="ai:claude">Phase 2: Author the test class (mandatory, Principle 2)</span>

<span data-proof="authored" data-by="ai:claude">A class without tests is not a deliverable. Generate</span> <span data-proof="authored" data-by="ai:claude">`{ClassName}Test.cls`</span> <span data-proof="authored" data-by="ai:claude">and its</span> <span data-proof="authored" data-by="ai:claude">`.cls-meta.xml`</span> <span data-proof="authored" data-by="ai:claude">immediately.</span>

<span data-proof="authored" data-by="ai:claude">Test discipline (every rule is enforced):</span>

| <span data-proof="authored" data-by="ai:claude">Rule</span>                                                                                                                                                                                                                                  | <span data-proof="authored" data-by="ai:claude">Application</span>                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **<span data-proof="authored" data-by="ai:claude">One behavior per method</span>**                                                                                                                                                                                                           | <span data-proof="authored" data-by="ai:claude">`shouldUpdateStatus_WhenValidInput`,</span> <span data-proof="authored" data-by="ai:claude">`shouldThrow_WhenNullInput`,</span> <span data-proof="authored" data-by="ai:claude">`shouldHandleBulk_When251Records`</span> <span data-proof="authored" data-by="ai:claude">— separate methods per scenario</span>           |
| **<span data-proof="authored" data-by="ai:claude">Bulkify with 251+ records</span>**                                                                                                                                                                                                         | <span data-proof="authored" data-by="ai:claude">Crosses the 200-trigger batch boundary. For batch Apex tests, set</span> <span data-proof="authored" data-by="ai:claude">`batchSize >= testRecordCount`</span>                                                                                                                                                            |
| **<span data-proof="authored" data-by="ai:claude">Isolate test data via</span>** **<span data-proof="authored" data-by="ai:claude">`TestDataFactory`</span>**                                                                                                                                | <span data-proof="authored" data-by="ai:claude">Never inline record building in</span> <span data-proof="authored" data-by="ai:claude">`@TestSetup`. If TDF doesn't exist, generate it first</span>                                                                                                                                                                       |
| **<span data-proof="authored" data-by="ai:claude">Use</span>** **<span data-proof="authored" data-by="ai:claude">`Assert`</span><span data-proof="authored" data-by="ai:claude">class only</span>**                                                                                          | <span data-proof="authored" data-by="ai:claude">`Assert.areEqual`,</span> <span data-proof="authored" data-by="ai:claude">`Assert.isTrue`,</span> <span data-proof="authored" data-by="ai:claude">`Assert.fail`</span> <span data-proof="authored" data-by="ai:claude">— never legacy</span> <span data-proof="authored" data-by="ai:claude">`System.assertEquals`</span> |
| **<span data-proof="authored" data-by="ai:claude">Wrap with</span>** **<span data-proof="authored" data-by="ai:claude">`Test.startTest()`</span>** **<span data-proof="authored" data-by="ai:claude">/</span>** **<span data-proof="authored" data-by="ai:claude">`Test.stopTest()`</span>** | <span data-proof="authored" data-by="ai:claude">Resets governor limits, fires async synchronously</span>                                                                                                                                                                                                                                                                  |
| **<span data-proof="authored" data-by="ai:claude">Mock external boundaries</span>**                                                                                                                                                                                                          | <span data-proof="authored" data-by="ai:claude">`HttpCalloutMock`</span> <span data-proof="authored" data-by="ai:claude">for callouts,</span> <span data-proof="authored" data-by="ai:claude">`Test.setFixedSearchResults`</span> <span data-proof="authored" data-by="ai:claude">for SOSL, DML mocks via dependency injection</span>                                     |
| **<span data-proof="authored" data-by="ai:claude">Test negative paths</span>**                                                                                                                                                                                                               | <span data-proof="authored" data-by="ai:claude">Validate exceptions and error handling, not just happy paths</span>                                                                                                                                                                                                                                                       |
| **<span data-proof="authored" data-by="ai:claude">No</span>** **<span data-proof="authored" data-by="ai:claude">`SeeAllData=true`</span>**                                                                                                                                                   | <span data-proof="authored" data-by="ai:claude">Org data dependency = flaky tests</span>                                                                                                                                                                                                                                                                                  |
| **<span data-proof="authored" data-by="ai:claude">No magic numbers in assertions</span>**                                                                                                                                                                                                    | <span data-proof="authored" data-by="ai:claude">Derive expected values from setup constants</span>                                                                                                                                                                                                                                                                        |

<span data-proof="authored" data-by="ai:claude">Given/When/Then structure inside every test method:</span>

```apex proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6Mzc1LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
@isTest
static void shouldUpdateStatus_WhenValidInput() {
    // Given
    List<Account> accounts = [SELECT Id FROM Account];

    // When
    Test.startTest();
    MyService.processAccounts(accounts);
    Test.stopTest();

    // Then
    Assert.areEqual(251, [SELECT COUNT() FROM Account WHERE Status__c = 'Processed'],
        'All accounts should be marked Processed');
}
```

<span data-proof="authored" data-by="ai:claude">Coverage targets:</span> **<span data-proof="authored" data-by="ai:claude">75% minimum to deploy, 90%+ recommended</span>** <span data-proof="authored" data-by="ai:claude">per class.</span>

***

## <span data-proof="authored" data-by="ai:claude">Phase 3: Validate (mandatory before reporting, Principle 2)</span>

<span data-proof="authored" data-by="ai:claude">Writing files is the midpoint. The deliverable isn't done until both checks pass.</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6Mjc0LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
# Static analysis
sf code-analyzer run --target force-app/main/default/classes/{ClassName}.cls --json
# Or via MCP: run_code_analyzer on the generated files

# Test execution
sf apex run test --tests {ClassName}Test --code-coverage --result-format human --synchronous --json
```

<span data-proof="authored" data-by="ai:claude">Remediate every sev0/sev1/sev2 violation and re-run. If tests fail, fix and re-run — don't paper over with</span> <span data-proof="authored" data-by="ai:claude">`try/catch`.</span>

***

## <span data-proof="authored" data-by="ai:claude">Phase 4: Report</span>

```
Generated:
- {ClassName}.cls + .cls-meta.xml
- {ClassName}Test.cls + .cls-meta.xml
- TestDataFactory.cls + .cls-meta.xml      (if not previously present)

Analyzer:    {sev0=0, sev1=0, sev2=0, sev3=N}    or "unavailable: <reason>"
Testing:     {pass=N, fail=0, coverage=NN%}      or "unavailable: <reason>"
Patterns:    {layer=Service|Selector|Domain|Async|Invocable|REST}
Sharing:     {with|without|inherited} sharing
Bulkification: PASS — no SOQL/DML in loops
CRUD/FLS:    {Schema.* checks | USER_MODE | both}
```

<span data-proof="authored" data-by="ai:claude">A report missing analyzer or testing lines is incomplete. Always invoke the tools before claiming</span> <span data-proof="authored" data-by="ai:claude">`unavailable`.</span>

***

## <span data-proof="authored" data-by="ai:claude">Test-only mode (`apex-generate test for <ClassName>`)</span>

<span data-proof="authored" data-by="ai:claude">If invoked with</span> <span data-proof="authored" data-by="ai:claude">`test for <ClassName>`, skip Phase 1 and treat the existing</span> <span data-proof="authored" data-by="ai:claude">`.cls`</span> <span data-proof="authored" data-by="ai:claude">as input. Read it, identify untested branches, generate or extend the test class, run Phase 3 validation. Same discipline applies.</span>

***

## <span data-proof="authored" data-by="ai:claude">Hand off to /sf-compound</span>

<span data-proof="authored" data-by="ai:claude">After successful generation, if the work surfaced a non-obvious pattern (e.g., a TDF helper that handles a duplicate-rule edge case, a mock pattern for a third-party callout), run</span> <span data-proof="authored" data-by="ai:claude">`/sf-compound`</span> <span data-proof="authored" data-by="ai:claude">to capture it under</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`</span> <span data-proof="authored" data-by="ai:claude">(Principle 7).</span>

***

## <span data-proof="authored" data-by="ai:claude">Inspiration</span>

<span data-proof="authored" data-by="ai:claude">Adapted from</span> [<span data-proof="authored" data-by="ai:claude">`forcedotcom/afv-library/skills/generating-apex`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-apex) <span data-proof="authored" data-by="ai:claude">and</span> [<span data-proof="authored" data-by="ai:claude">`generating-apex-test`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-apex-test) <span data-proof="authored" data-by="ai:claude">(Apache-2.0). Upstream ships separate skills with extensive</span> <span data-proof="authored" data-by="ai:claude">`assets/`</span> <span data-proof="authored" data-by="ai:claude">template files and</span> <span data-proof="authored" data-by="ai:claude">`references/`</span> <span data-proof="authored" data-by="ai:claude">for async-testing, mocking-patterns, assertion-patterns, and TDF. This plugin merges them into one because production-class + test-class is one transaction, not two. For the full template files and edge-case tables (duplicate rules, multi-org test data isolation, governor-limit reset semantics under</span> <span data-proof="authored" data-by="ai:claude">`Test.stopTest()`), consult the upstream references.</span>