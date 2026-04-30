---
name: validation-rule-generate
description: "Generate Salesforce Validation Rule metadata (.validationRule-meta.xml) with correct formula syntax, CDATA-wrapped XML when required, and user-friendly error messages. Use when creating validation rules, enforcing data quality, blocking invalid records at save, or troubleshooting validation deployment errors. Trigger phrases: 'create a validation rule', 'add field validation for', 'block records when', 'enforce that <field> must be', 'add a data quality rule', 'prevent saving when'. Pairs with `validation-rule-reviewer` agent."
argument-hint: "[object name + condition + error message, e.g. 'Account: prevent save when Industry blank and AnnualRevenue > 1M']"
---

# <span data-proof="authored" data-by="ai:claude">/validation-rule-generate</span>

> **<span data-proof="authored" data-by="ai:claude">Principles enforced:</span>** <span data-proof="authored" data-by="ai:claude">1 (preserve the quality ceiling), 5 (taste over typing). See</span> <span data-proof="authored" data-by="ai:claude">`PRINCIPLES.md`.</span>

## <span data-proof="authored" data-by="ai:claude">Copy-paste-to-agent</span>

```
Generate a Salesforce Validation Rule (.validationRule-meta.xml) with: a fullName under
40 characters, an active=true flag, an errorConditionFormula that returns TRUE to BLOCK
the save, an errorMessage under 255 characters, and CDATA-wrapped formula if the formula
contains XML special characters. Place under
force-app/main/default/objects/<Object>/validationRules/<fullName>.validationRule-meta.xml.
After generation, dispatch `validation-rule-reviewer` for a formula-quality review.
```

## <span data-proof="authored" data-by="ai:claude">When to use</span>

* <span data-proof="authored" data-by="ai:claude">Block invalid records at the data layer (preferred over Apex / Flow when the rule is purely declarative)</span>

* <span data-proof="authored" data-by="ai:claude">Enforce business rules with user-friendly error messages</span>

* <span data-proof="authored" data-by="ai:claude">Cross-field validation, picklist consistency, date sanity checks</span>

* <span data-proof="authored" data-by="ai:claude">Generate the matching</span> <span data-proof="authored" data-by="ai:claude">`.validationRule-meta.xml`</span> <span data-proof="authored" data-by="ai:claude">file</span>

<span data-proof="authored" data-by="ai:claude">If the validation needs to</span> *<span data-proof="authored" data-by="ai:claude">modify</span>* <span data-proof="authored" data-by="ai:claude">a record (not just block it), this is the wrong skill — use</span> <span data-proof="authored" data-by="ai:claude">`flow-generate`</span> <span data-proof="authored" data-by="ai:claude">(before-save flow) or</span> <span data-proof="authored" data-by="ai:claude">`apex-generate`</span> <span data-proof="authored" data-by="ai:claude">(before-update trigger).</span>

***

## <span data-proof="authored" data-by="ai:claude">Required properties</span>

<span data-proof="authored" data-by="ai:claude">Every validation rule needs all four:</span>

| <span data-proof="authored" data-by="ai:claude">Property</span>                  | <span data-proof="authored" data-by="ai:claude">Constraint</span>                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`<fullName>`</span>              | <span data-proof="authored" data-by="ai:claude">Unique API name. Starts with a letter, no consecutive underscores, no trailing underscore,</span> **<span data-proof="authored" data-by="ai:claude">max 40 characters</span>**                                                                                                                              |
| <span data-proof="authored" data-by="ai:claude">`<active>`</span>                | <span data-proof="authored" data-by="ai:claude">`true`</span> <span data-proof="authored" data-by="ai:claude">to enforce,</span> <span data-proof="authored" data-by="ai:claude">`false`</span> <span data-proof="authored" data-by="ai:claude">to disable</span>                                                                                           |
| <span data-proof="authored" data-by="ai:claude">`<errorConditionFormula>`</span> | <span data-proof="authored" data-by="ai:claude">Logical formula returning</span> <span data-proof="authored" data-by="ai:claude">`TRUE`</span> <span data-proof="authored" data-by="ai:claude">to BLOCK the save (yes —</span> <span data-proof="authored" data-by="ai:claude">`TRUE`</span> <span data-proof="authored" data-by="ai:claude">blocks)</span> |
| <span data-proof="authored" data-by="ai:claude">`<errorMessage>`</span>          | <span data-proof="authored" data-by="ai:claude">User-facing message,</span> **<span data-proof="authored" data-by="ai:claude">max 255 characters</span>**<span data-proof="authored" data-by="ai:claude">. Speak to the user, not the developer</span>                                                                                                      |

***

## <span data-proof="authored" data-by="ai:claude">Hard constraints</span>

<span data-proof="authored" data-by="ai:claude">These are the most-common deployment failures. Treat each as a non-negotiable gate.</span>

### <span data-proof="authored" data-by="ai:claude">1. CDATA-wrap the formula when it contains XML special characters</span>

<span data-proof="authored" data-by="ai:claude">If</span> <span data-proof="authored" data-by="ai:claude">`errorConditionFormula`</span> <span data-proof="authored" data-by="ai:claude">contains</span> <span data-proof="authored" data-by="ai:claude">`<`,</span> <span data-proof="authored" data-by="ai:claude">`>`,</span> <span data-proof="authored" data-by="ai:claude">`&`, or</span> <span data-proof="authored" data-by="ai:claude">`"`, wrap it:</span>

```xml proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTI1LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
<errorConditionFormula><![CDATA[
  AND(
    ISBLANK(Industry__c),
    AnnualRevenue > 1000000
  )
]]></errorConditionFormula>
```

<span data-proof="authored" data-by="ai:claude">If the formula has no special characters, plain text works.</span> **<span data-proof="authored" data-by="ai:claude">When in doubt, CDATA-wrap</span>** <span data-proof="authored" data-by="ai:claude">— it's never wrong.</span>

### <span data-proof="authored" data-by="ai:claude">2. Function correctness (the high-frequency formula errors)</span>

| <span data-proof="authored" data-by="ai:claude">Function</span>      | <span data-proof="authored" data-by="ai:claude">Rule</span>                                                                                                                                                                                                                                                       | <span data-proof="authored" data-by="ai:claude">Common mistake</span>                                                                                                                                                                                                       |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`TEXT()`</span>      | <span data-proof="authored" data-by="ai:claude">Not on Text fields. Use only on numbers, dates, picklists</span>                                                                                                                                                                                                  | <span data-proof="authored" data-by="ai:claude">`TEXT(Name)`</span> <span data-proof="authored" data-by="ai:claude">— drop the</span> <span data-proof="authored" data-by="ai:claude">`TEXT()`</span>                                                                       |
| <span data-proof="authored" data-by="ai:claude">`CASE()`</span>      | <span data-proof="authored" data-by="ai:claude">Last argument is the</span> **<span data-proof="authored" data-by="ai:claude">default value</span>** <span data-proof="authored" data-by="ai:claude">— always required. Total args must be</span> **<span data-proof="authored" data-by="ai:claude">even</span>** | <span data-proof="authored" data-by="ai:claude">Missing default → deploy fail</span>                                                                                                                                                                                        |
| <span data-proof="authored" data-by="ai:claude">`VALUE()`</span>     | <span data-proof="authored" data-by="ai:claude">Only on Text fields parsed to number. Don't wrap a number</span>                                                                                                                                                                                                  | <span data-proof="authored" data-by="ai:claude">`VALUE(Amount)`</span> <span data-proof="authored" data-by="ai:claude">when</span> <span data-proof="authored" data-by="ai:claude">`Amount`</span> <span data-proof="authored" data-by="ai:claude">is already Number</span> |
| <span data-proof="authored" data-by="ai:claude">`DAY()`</span>       | <span data-proof="authored" data-by="ai:claude">Only on</span> **<span data-proof="authored" data-by="ai:claude">Date</span>** <span data-proof="authored" data-by="ai:claude">fields. Convert Datetime first</span>                                                                                              | <span data-proof="authored" data-by="ai:claude">`DAY(CreatedDate)`</span> <span data-proof="authored" data-by="ai:claude">— wrap with</span> <span data-proof="authored" data-by="ai:claude">`DATEVALUE(CreatedDate)`</span>                                                |
| <span data-proof="authored" data-by="ai:claude">`MONTH()`</span>     | <span data-proof="authored" data-by="ai:claude">Only on</span> **<span data-proof="authored" data-by="ai:claude">Date</span>** <span data-proof="authored" data-by="ai:claude">fields. Same Datetime fix</span>                                                                                                   | <span data-proof="authored" data-by="ai:claude">Same as</span> <span data-proof="authored" data-by="ai:claude">`DAY()`</span>                                                                                                                                               |
| <span data-proof="authored" data-by="ai:claude">`DATEVALUE()`</span> | <span data-proof="authored" data-by="ai:claude">Only on</span> **<span data-proof="authored" data-by="ai:claude">Datetime</span>** <span data-proof="authored" data-by="ai:claude">fields. Don't wrap a Date</span>                                                                                               | <span data-proof="authored" data-by="ai:claude">`DATEVALUE(CloseDate)`</span> <span data-proof="authored" data-by="ai:claude">— drop it</span>                                                                                                                              |
| <span data-proof="authored" data-by="ai:claude">`ISPICKVAL()`</span> | **<span data-proof="authored" data-by="ai:claude">Required</span>** <span data-proof="authored" data-by="ai:claude">for picklist equality. Plain</span> <span data-proof="authored" data-by="ai:claude">`=`</span> <span data-proof="authored" data-by="ai:claude">does not work</span>                           | <span data-proof="authored" data-by="ai:claude">`Status = 'Open'`</span> <span data-proof="authored" data-by="ai:claude">→</span> <span data-proof="authored" data-by="ai:claude">`ISPICKVAL(Status, 'Open')`</span>                                                        |
| <span data-proof="authored" data-by="ai:claude">`ISCHANGED()`</span> | <span data-proof="authored" data-by="ai:claude">Use to detect field-value change between old and new</span>                                                                                                                                                                                                       | <br />                                                                                                                                                                                                                                                                      |

### <span data-proof="authored" data-by="ai:claude">3. Update-vs-replace semantics (Principle 5 — taste)</span>

<span data-proof="authored" data-by="ai:claude">When a user says "update the formula":</span>

* **<span data-proof="authored" data-by="ai:claude">"Update the formula to</span>** **<span data-proof="authored" data-by="ai:claude"><X>"</span>** <span data-proof="authored" data-by="ai:claude">→ completely replace the existing formula logic with</span> <span data-proof="authored" data-by="ai:claude">`<X>`.</span>

* **<span data-proof="authored" data-by="ai:claude">"Update the formula to also</span>** **<span data-proof="authored" data-by="ai:claude"><X>"</span>** <span data-proof="authored" data-by="ai:claude">→ keep existing logic, append with</span> <span data-proof="authored" data-by="ai:claude">`AND(<existing>, <X>)`</span> <span data-proof="authored" data-by="ai:claude">or</span> <span data-proof="authored" data-by="ai:claude">`OR(<existing>, <X>)`</span> <span data-proof="authored" data-by="ai:claude">— read carefully which one the user means.</span>

<span data-proof="authored" data-by="ai:claude">Never silently rewrite. Echo your interpretation in the report.</span>

### <span data-proof="authored" data-by="ai:claude">4. File path and extension</span>

```
force-app/main/default/objects/<ObjectApiName>/validationRules/<fullName>.validationRule-meta.xml
```

<span data-proof="authored" data-by="ai:claude">The</span> <span data-proof="authored" data-by="ai:claude">`.validationRule-meta.xml`</span> <span data-proof="authored" data-by="ai:claude">extension is mandatory. Anything else fails deploy.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 0: Research (Principle 7)</span>

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher("validation rule" + object_name)`</span> <span data-proof="authored" data-by="ai:claude">— does a similar rule already exist?</span> **<span data-proof="authored" data-by="ai:claude">Must-read.</span>**

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-repo-research-analyst(object_name)`</span> <span data-proof="authored" data-by="ai:claude">— list existing validation rules on this object to avoid duplication or conflict.</span>

***

## <span data-proof="authored" data-by="ai:claude">Workflow</span>

1. **<span data-proof="authored" data-by="ai:claude">Gather inputs.</span>** <span data-proof="authored" data-by="ai:claude">Object, intent, blocking condition, error message text. Ask clarifying questions only if the condition is genuinely ambiguous.</span>
2. **<span data-proof="authored" data-by="ai:claude">Verify field availability.</span>** <span data-proof="authored" data-by="ai:claude">Confirm every field referenced exists on the object. Hint: read the object metadata file.</span>
3. **<span data-proof="authored" data-by="ai:claude">Author the formula.</span>** <span data-proof="authored" data-by="ai:claude">Apply the function-correctness rules above.</span>
4. **<span data-proof="authored" data-by="ai:claude">Choose CDATA wrap if needed.</span>**
5. **<span data-proof="authored" data-by="ai:claude">Write the file.</span>** <span data-proof="authored" data-by="ai:claude">Path + extension as above.</span>
6. **<span data-proof="authored" data-by="ai:claude">Validate</span>** <span data-proof="authored" data-by="ai:claude">with</span> <span data-proof="authored" data-by="ai:claude">`sf code-analyzer run --target <path>`</span> <span data-proof="authored" data-by="ai:claude">and remediate findings.</span>
7. **<span data-proof="authored" data-by="ai:claude">Dispatch review</span>** <span data-proof="authored" data-by="ai:claude">—</span> <span data-proof="authored" data-by="ai:claude">`validation-rule-reviewer`</span> <span data-proof="authored" data-by="ai:claude">agent for formula quality, message UX, edge cases.</span>
8. **<span data-proof="authored" data-by="ai:claude">Report.</span>**

***

## <span data-proof="authored" data-by="ai:claude">Output report</span>

```
Generated:
- force-app/main/default/objects/<Object>/validationRules/<fullName>.validationRule-meta.xml

Formula:
- {one-line summary of the blocking condition}
- CDATA wrap: {yes|no}

Error message:
- "{full message under 255 chars}"

Analyzer:    {sev0=0, sev1=0, sev2=0}     or "unavailable: <reason>"
Review:      {validation-rule-reviewer findings count}

Update semantics: {replace|append}     ← only when modifying an existing rule
```

***

## <span data-proof="authored" data-by="ai:claude">Inspiration</span>

<span data-proof="authored" data-by="ai:claude">Adapted from</span> [<span data-proof="authored" data-by="ai:claude">`forcedotcom/afv-library/skills/generating-validation-rule`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-validation-rule) <span data-proof="authored" data-by="ai:claude">(Apache-2.0). The upstream skill is compact (72 lines) and focused on the high-failure-rate constraints (CDATA, function correctness, update-vs-replace). This plugin's adaptation adds the parallel-dispatch review and Principle 5 framing for the update-vs-replace semantic.</span>