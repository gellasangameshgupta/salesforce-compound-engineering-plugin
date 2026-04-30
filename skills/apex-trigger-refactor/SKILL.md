---
name: apex-trigger-refactor
description: "Modernize legacy Salesforce triggers — move SOQL/DML out of loops, separate concerns into a Trigger Handler / Trigger Actions Framework class, generate matching test coverage, and re-deploy. Use when you find a trigger with inline business logic, DML inside loops, no recursion guard, or no handler class. Trigger phrases: 'refactor this trigger', 'modernize this legacy trigger', 'fix this trigger to be bulk-safe', 'add a handler for', 'this trigger has DML in a loop', 'split this trigger into a handler', 'move logic out of trigger body'. Pairs with `apex-trigger-architect` agent."
argument-hint: "[trigger name or path, e.g. OpportunityTrigger or force-app/main/default/triggers/OpportunityTrigger.trigger]"
---

# <span data-proof="authored" data-by="ai:claude">/apex-trigger-refactor</span>

> **<span data-proof="authored" data-by="ai:claude">Principles enforced:</span>** <span data-proof="authored" data-by="ai:claude">1 (preserve the quality ceiling), 2 (verifiability), 3 (jagged intelligence — recursion / context edges), 5 (taste). See</span> <span data-proof="authored" data-by="ai:claude">`PRINCIPLES.md`.</span>

## <span data-proof="authored" data-by="ai:claude">Copy-paste-to-agent</span>

```
Refactor a legacy Salesforce trigger into a Trigger Handler (or Trigger Actions Framework)
pattern. Move all SOQL and DML out of loops. Separate concerns by trigger context. Add
recursion guard. Generate matching tests with 251+ records that cross the trigger batch
boundary. Validate with sf code-analyzer. Run sf apex run test before declaring done.
Capture the before/after diff in the report — Principle 5 demands taste, not just correctness.
```

## <span data-proof="authored" data-by="ai:claude">When to use</span>

<span data-proof="authored" data-by="ai:claude">Run this skill when any of the following are true:</span>

* <span data-proof="authored" data-by="ai:claude">The trigger contains SOQL or DML inside a</span> <span data-proof="authored" data-by="ai:claude">`for`</span> <span data-proof="authored" data-by="ai:claude">loop</span>

* <span data-proof="authored" data-by="ai:claude">The trigger has business logic in the trigger body (not delegated to a handler)</span>

* <span data-proof="authored" data-by="ai:claude">The trigger has no recursion guard</span>

* <span data-proof="authored" data-by="ai:claude">The trigger mixes multiple contexts (`isInsert`,</span> <span data-proof="authored" data-by="ai:claude">`isUpdate`,</span> <span data-proof="authored" data-by="ai:claude">`isAfter`,</span> <span data-proof="authored" data-by="ai:claude">`isBefore`) without separation</span>

* <span data-proof="authored" data-by="ai:claude">Test coverage is below 90% on the trigger or its handler</span>

* <span data-proof="authored" data-by="ai:claude">A code review flagged a</span> <span data-proof="authored" data-by="ai:claude">`apex-trigger-architect`</span> <span data-proof="authored" data-by="ai:claude">finding</span>

<span data-proof="authored" data-by="ai:claude">If the trigger is already well-architected, do not refactor for taste alone — Principle 5 says taste matters, but Principle 1 + the YAGNI rule say don't refactor what works without a real defect.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 0: Research (Principle 7)</span>

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher("trigger refactor" + object_name)`</span> <span data-proof="authored" data-by="ai:claude">— has someone refactored this object's triggers before?</span> **<span data-proof="authored" data-by="ai:claude">Must-read.</span>**

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-repo-research-analyst(trigger_name)`</span> <span data-proof="authored" data-by="ai:claude">— does the project use a trigger framework (TAF, fflib, or custom)? Match the existing convention; don't invent a new one.</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/apex-patterns/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">— Trigger Handler section is the reference for the target shape.</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/governor-limits/SKILL.md`.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 1: Analyze the trigger</span>

<span data-proof="authored" data-by="ai:claude">Read the trigger file and identify:</span>

| <span data-proof="authored" data-by="ai:claude">Anti-pattern</span>                                                                                       | <span data-proof="authored" data-by="ai:claude">Detection</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | <span data-proof="authored" data-by="ai:claude">Fix location</span>                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **<span data-proof="authored" data-by="ai:claude">DML in loops</span>**                                                                                   | <span data-proof="authored" data-by="ai:claude">`insert`,</span> <span data-proof="authored" data-by="ai:claude">`update`,</span> <span data-proof="authored" data-by="ai:claude">`delete`,</span> <span data-proof="authored" data-by="ai:claude">`upsert`,</span> <span data-proof="authored" data-by="ai:claude">`Database.*`</span> <span data-proof="authored" data-by="ai:claude">inside a</span> <span data-proof="authored" data-by="ai:claude">`for`</span> <span data-proof="authored" data-by="ai:claude">block</span> | <span data-proof="authored" data-by="ai:claude">Aggregate into a</span> <span data-proof="authored" data-by="ai:claude">`List<SObject>`</span> <span data-proof="authored" data-by="ai:claude">outside the loop, single bulk DML at end</span>            |
| **<span data-proof="authored" data-by="ai:claude">SOQL in loops</span>**                                                                                  | <span data-proof="authored" data-by="ai:claude">`[SELECT ...]`</span> <span data-proof="authored" data-by="ai:claude">or</span> <span data-proof="authored" data-by="ai:claude">`Database.query(...)`</span> <span data-proof="authored" data-by="ai:claude">inside a</span> <span data-proof="authored" data-by="ai:claude">`for`</span> <span data-proof="authored" data-by="ai:claude">block</span>                                                                                                                            | <span data-proof="authored" data-by="ai:claude">Pre-fetch into a</span> <span data-proof="authored" data-by="ai:claude">`Map<Id, SObject>`</span> <span data-proof="authored" data-by="ai:claude">keyed by lookup; access from map inside the loop</span> |
| **<span data-proof="authored" data-by="ai:claude">Mixed contexts in one block</span>**                                                                    | <span data-proof="authored" data-by="ai:claude">`if (Trigger.isInsert) { ... if (Trigger.isUpdate) { ... } }`</span> <span data-proof="authored" data-by="ai:claude">interleaved</span>                                                                                                                                                                                                                                                                                                                                           | <span data-proof="authored" data-by="ai:claude">One handler method per context:</span> <span data-proof="authored" data-by="ai:claude">`onBeforeInsert`,</span> <span data-proof="authored" data-by="ai:claude">`onAfterUpdate`, etc.</span>              |
| **<span data-proof="authored" data-by="ai:claude">No recursion guard</span>**                                                                             | <span data-proof="authored" data-by="ai:claude">Handler can re-enter on workflow / process recursion</span>                                                                                                                                                                                                                                                                                                                                                                                                                       | <span data-proof="authored" data-by="ai:claude">Static</span> <span data-proof="authored" data-by="ai:claude">`Set<Id>`</span> <span data-proof="authored" data-by="ai:claude">guard or framework-provided guard</span>                                   |
| **<span data-proof="authored" data-by="ai:claude">Business logic in trigger body</span>**                                                                 | <span data-proof="authored" data-by="ai:claude">More than the dispatch line in the</span> <span data-proof="authored" data-by="ai:claude">`.trigger`</span> <span data-proof="authored" data-by="ai:claude">file</span>                                                                                                                                                                                                                                                                                                           | <span data-proof="authored" data-by="ai:claude">Move all logic to handler class; trigger contains only the handler instantiation + dispatch</span>                                                                                                        |
| **<span data-proof="authored" data-by="ai:claude">`without sharing`</span><span data-proof="authored" data-by="ai:claude">without justification</span>**  | <span data-proof="authored" data-by="ai:claude">Class declared</span> <span data-proof="authored" data-by="ai:claude">`without sharing`</span> <span data-proof="authored" data-by="ai:claude">with no comment explaining why</span>                                                                                                                                                                                                                                                                                              | <span data-proof="authored" data-by="ai:claude">Default to</span> <span data-proof="authored" data-by="ai:claude">`with sharing`; require comment if</span> <span data-proof="authored" data-by="ai:claude">`without`</span>                              |

<span data-proof="authored" data-by="ai:claude">Produce a written analysis listing every anti-pattern found, with line numbers. This is the spec the refactor will satisfy (Principle 4 — the spec is the artifact).</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 2: Choose the target pattern</span>

<span data-proof="authored" data-by="ai:claude">The plugin doesn't impose a framework — match the project's existing one:</span>

| <span data-proof="authored" data-by="ai:claude">Detected framework</span>                  | <span data-proof="authored" data-by="ai:claude">Target shape</span>                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **<span data-proof="authored" data-by="ai:claude">Trigger Actions Framework (TAF)</span>** | <span data-proof="authored" data-by="ai:claude">Custom Metadata-driven action classes implementing</span> <span data-proof="authored" data-by="ai:claude">`TriggerAction.*`</span> <span data-proof="authored" data-by="ai:claude">interfaces</span>                                                                                                                                          |
| **<span data-proof="authored" data-by="ai:claude">fflib</span>**                           | <span data-proof="authored" data-by="ai:claude">Domain class extending</span> <span data-proof="authored" data-by="ai:claude">`fflib_SObjectDomain`</span>                                                                                                                                                                                                                                    |
| **<span data-proof="authored" data-by="ai:claude">Custom handler</span>**                  | <span data-proof="authored" data-by="ai:claude">Class with</span> <span data-proof="authored" data-by="ai:claude">`before<Context>`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`after<Context>`</span> <span data-proof="authored" data-by="ai:claude">methods, called from a single dispatch line in the trigger</span> |
| **<span data-proof="authored" data-by="ai:claude">None</span>**                            | <span data-proof="authored" data-by="ai:claude">Default to plain Trigger Handler pattern from</span> <span data-proof="authored" data-by="ai:claude">`apex-patterns`</span> <span data-proof="authored" data-by="ai:claude">— single class, context methods, recursion guard</span>                                                                                                           |

<span data-proof="authored" data-by="ai:claude">When</span> <span data-proof="authored" data-by="ai:claude">`none`</span> <span data-proof="authored" data-by="ai:claude">is detected, propose the target pattern in the analysis report and</span> **<span data-proof="authored" data-by="ai:claude">ask the user to confirm</span>** <span data-proof="authored" data-by="ai:claude">before refactoring. Don't unilaterally pick a framework.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 3: Refactor in phases (one anti-pattern at a time)</span>

<span data-proof="authored" data-by="ai:claude">Phase the refactor so each commit is a small, testable improvement (Principle 5 — taste says one fix per commit, not a big-bang rewrite):</span>

1. **<span data-proof="authored" data-by="ai:claude">Move SOQL out of loops.</span>** <span data-proof="authored" data-by="ai:claude">Pre-fetch related records into a</span> <span data-proof="authored" data-by="ai:claude">`Map<Id, SObject>`. Verify behavior unchanged.</span>
2. **<span data-proof="authored" data-by="ai:claude">Move DML out of loops.</span>** <span data-proof="authored" data-by="ai:claude">Aggregate into a list, single DML at the end. Verify.</span>
3. **<span data-proof="authored" data-by="ai:claude">Split trigger body into handler.</span>** <span data-proof="authored" data-by="ai:claude">Trigger becomes a 1-line dispatch:</span>

```apex proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTMzLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
trigger OpportunityTrigger on Opportunity (before insert, before update, after update) {
    new OpportunityTriggerHandler().run();
}
```

1. **<span data-proof="authored" data-by="ai:claude">Separate by context.</span>** <span data-proof="authored" data-by="ai:claude">Handler dispatches</span> <span data-proof="authored" data-by="ai:claude">`onBeforeInsert`,</span> <span data-proof="authored" data-by="ai:claude">`onBeforeUpdate`,</span> <span data-proof="authored" data-by="ai:claude">`onAfterUpdate`, etc.</span>
2. **<span data-proof="authored" data-by="ai:claude">Add recursion guard.</span>** <span data-proof="authored" data-by="ai:claude">Static</span> <span data-proof="authored" data-by="ai:claude">`Set<Id>`</span> <span data-proof="authored" data-by="ai:claude">of processed IDs OR framework-provided guard.</span>
3. **<span data-proof="authored" data-by="ai:claude">Validate sharing keyword.</span>** <span data-proof="authored" data-by="ai:claude">Default</span> <span data-proof="authored" data-by="ai:claude">`with sharing`</span> <span data-proof="authored" data-by="ai:claude">unless explicitly justified.</span>

<span data-proof="authored" data-by="ai:claude">After each phase, run the test suite. If a phase breaks tests,</span> **<span data-proof="authored" data-by="ai:claude">stop and diagnose</span>** <span data-proof="authored" data-by="ai:claude">— do not press forward layering more changes on top of broken behavior (Principle 3).</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 4: Generate or update the test class (Principle 2)</span>

<span data-proof="authored" data-by="ai:claude">Tests are not optional. After refactor:</span>

* <span data-proof="authored" data-by="ai:claude">Test class targets the</span> **<span data-proof="authored" data-by="ai:claude">handler class</span>**<span data-proof="authored" data-by="ai:claude">, not the trigger directly. Triggers remain a 1-line dispatch.</span>

* **<span data-proof="authored" data-by="ai:claude">251+ records</span>** <span data-proof="authored" data-by="ai:claude">in</span> <span data-proof="authored" data-by="ai:claude">`@TestSetup`</span> <span data-proof="authored" data-by="ai:claude">to cross the 200-record trigger batch boundary.</span>

* <span data-proof="authored" data-by="ai:claude">Cover every refactored context: insert path, update path with stage change, update path without stage change, delete path, etc.</span>

* <span data-proof="authored" data-by="ai:claude">For each anti-pattern that was fixed, add a test that would have</span> **<span data-proof="authored" data-by="ai:claude">caught</span>** <span data-proof="authored" data-by="ai:claude">the original bug (e.g., a 251-record bulk insert test that would have hit the SOQL-101 limit on the legacy trigger).</span>

<span data-proof="authored" data-by="ai:claude">Use</span> <span data-proof="authored" data-by="ai:claude">`/apex-generate test for <HandlerClassName>`</span> <span data-proof="authored" data-by="ai:claude">if you need help authoring the test class.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 5: Validate (mandatory, Principle 2)</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MzY2LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
# Static analysis on every changed file
sf code-analyzer run --target force-app/main/default/triggers/<TriggerName>.trigger,force-app/main/default/classes/<HandlerClassName>.cls,force-app/main/default/classes/<HandlerClassName>Test.cls --json

# Run the tests
sf apex run test --tests <HandlerClassName>Test --code-coverage --result-format human --synchronous --json
```

<span data-proof="authored" data-by="ai:claude">Remediate every sev0/sev1/sev2. Coverage target:</span> **<span data-proof="authored" data-by="ai:claude">90%+</span>** <span data-proof="authored" data-by="ai:claude">on the handler class.</span>

<span data-proof="authored" data-by="ai:claude">Dispatch</span> <span data-proof="authored" data-by="ai:claude">`apex-trigger-architect`</span> <span data-proof="authored" data-by="ai:claude">review agent for a pattern review.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 6: Report</span>

```
Refactor: <TriggerName>

Anti-patterns identified (Step 1):
- {n} DML-in-loop occurrences (lines …)
- {n} SOQL-in-loop occurrences (lines …)
- {n} mixed-context blocks
- recursion guard: {present|missing}
- handler delegation: {present|missing}

Phases applied:
1. SOQL hoist:        OK
2. DML hoist:         OK
3. Handler extract:   OK (created <HandlerClassName>)
4. Context split:     OK (onBeforeInsert, onAfterUpdate, ...)
5. Recursion guard:   OK
6. Sharing audit:     OK ({with|without} sharing — {justified|default})

Files changed:
- triggers/<TriggerName>.trigger    (legacy logic removed; now 1-line dispatch)
- classes/<HandlerClassName>.cls    (new)
- classes/<HandlerClassName>.cls-meta.xml (new)
- classes/<HandlerClassName>Test.cls (new or extended)

Analyzer: {sev0=0, sev1=0, sev2=0}
Testing:  {pass=N, fail=0, coverage=NN%}
Review:   apex-trigger-architect — {findings count}

Before/After diff: {one paragraph summary of the most important behavioral guarantees preserved}
```

***

## <span data-proof="authored" data-by="ai:claude">Hand off</span>

<span data-proof="authored" data-by="ai:claude">If the refactor surfaced a recursion-prevention pattern, an order-of-execution gotcha, or a sharing-model edge case worth remembering — run</span> <span data-proof="authored" data-by="ai:claude">`/sf-compound`</span> <span data-proof="authored" data-by="ai:claude">to capture under</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`. Trigger refactors are exactly the kind of jagged-edge knowledge that pays back compounded (Principle 7).</span>

***

## <span data-proof="authored" data-by="ai:claude">Inspiration</span>

<span data-proof="authored" data-by="ai:claude">Adapted from</span> [<span data-proof="authored" data-by="ai:claude">`forcedotcom/afv-library/skills/trigger-refactor-pipeline`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/trigger-refactor-pipeline) <span data-proof="authored" data-by="ai:claude">(Apache-2.0). The upstream skill ships a Python-based static analyzer (`scripts/analyze_trigger.py`), a handler-patterns reference, and a baseline anti-pattern trigger to practice on. For the analyzer script and the full handler pattern catalog, consult the upstream. This plugin's adaptation is opinionated about one-fix-per-commit phasing and integrates with the principles framework +</span> <span data-proof="authored" data-by="ai:claude">`apex-trigger-architect`</span> <span data-proof="authored" data-by="ai:claude">review agent.</span>