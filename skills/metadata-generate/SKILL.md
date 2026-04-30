---
name: metadata-generate
description: "Generate Salesforce metadata XML — custom objects, custom fields, custom applications, custom tabs, list views, and custom Lightning types. Single skill that takes a `--type` argument and produces the right metadata file with all required attributes, sharing-model rules, and naming conventions baked in. Use when creating any of these metadata types. Trigger phrases: 'create a custom object', 'add a field to', 'generate a Lookup field', 'create a Master-Detail relationship', 'set up a Roll-up Summary', 'add a custom application', 'create a tab for', 'create a list view filtered by', 'define a Custom Lightning Type'. Pairs with `metadata-consistency-checker` agent."
argument-hint: "--type <object|field|app|tab|listview|lightning-type> + the metadata-specific args (e.g., --object Account --field-name Industry__c --field-type Text)"
---

# <span data-proof="authored" data-by="ai:claude">/metadata-generate</span>

> **<span data-proof="authored" data-by="ai:claude">Principles enforced:</span>** <span data-proof="authored" data-by="ai:claude">1 (preserve the quality ceiling), 4 (spec is the artifact), 5 (taste over typing). See</span> <span data-proof="authored" data-by="ai:claude">`PRINCIPLES.md`.</span>

## <span data-proof="authored" data-by="ai:claude">Copy-paste-to-agent</span>

```
Generate Salesforce metadata XML for one of: CustomObject, CustomField, CustomApplication,
CustomTab, ListView, CustomLightningType. Read the type-specific section below for required
attributes, sharing-model rules, and forbidden elements. Always write to the canonical
project path (force-app/main/default/<type>/...). Always include description and
inlineHelpText for fields. After generation, dispatch `metadata-consistency-checker` for a
cross-metadata review. Hard-stop on any forbidden element — these cause silent deploy
failures.
```

## <span data-proof="authored" data-by="ai:claude">When to use</span>

<span data-proof="authored" data-by="ai:claude">This skill consolidates six metadata generators into one. Pick the right</span> <span data-proof="authored" data-by="ai:claude">`--type`</span> <span data-proof="authored" data-by="ai:claude">for the work:</span>

| <span data-proof="authored" data-by="ai:claude">`--type`</span>         | <span data-proof="authored" data-by="ai:claude">Generates</span>             | <span data-proof="authored" data-by="ai:claude">File path</span>                                             |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| <span data-proof="authored" data-by="ai:claude">`object`</span>         | <span data-proof="authored" data-by="ai:claude">`CustomObject`</span>        | <span data-proof="authored" data-by="ai:claude">`objects/<Object>/<Object>.object-meta.xml`</span>           |
| <span data-proof="authored" data-by="ai:claude">`field`</span>          | <span data-proof="authored" data-by="ai:claude">`CustomField`</span>         | <span data-proof="authored" data-by="ai:claude">`objects/<Object>/fields/<Field>.field-meta.xml`</span>      |
| <span data-proof="authored" data-by="ai:claude">`app`</span>            | <span data-proof="authored" data-by="ai:claude">`CustomApplication`</span>   | <span data-proof="authored" data-by="ai:claude">`applications/<App>.app-meta.xml`</span>                     |
| <span data-proof="authored" data-by="ai:claude">`tab`</span>            | <span data-proof="authored" data-by="ai:claude">`CustomTab`</span>           | <span data-proof="authored" data-by="ai:claude">`tabs/<Tab>.tab-meta.xml`</span>                             |
| <span data-proof="authored" data-by="ai:claude">`listview`</span>       | <span data-proof="authored" data-by="ai:claude">`ListView`</span>            | <span data-proof="authored" data-by="ai:claude">`objects/<Object>/listViews/<View>.listView-meta.xml`</span> |
| <span data-proof="authored" data-by="ai:claude">`lightning-type`</span> | <span data-proof="authored" data-by="ai:claude">`CustomLightningType`</span> | <span data-proof="authored" data-by="ai:claude">`lightningTypes/<Type>.lightningType-meta.xml`</span>        |

<span data-proof="authored" data-by="ai:claude">If the user is asking for an entire Lightning app (object + fields + tabs + flexipage + perm set), use</span> <span data-proof="authored" data-by="ai:claude">`/lightning-page-generate`</span> <span data-proof="authored" data-by="ai:claude">instead — it orchestrates this skill across multiple types.</span>

***

## <span data-proof="authored" data-by="ai:claude">Universal step 0: Research (Principle 7)</span>

<span data-proof="authored" data-by="ai:claude">For every type:</span>

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher("metadata generation" + type + object_name)`</span> <span data-proof="authored" data-by="ai:claude">— has someone built similar metadata?</span> **<span data-proof="authored" data-by="ai:claude">Must-read.</span>**

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-repo-research-analyst(target_object)`</span> <span data-proof="authored" data-by="ai:claude">— what fields / tabs / list views already exist? Don't duplicate.</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/security-guide/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">— sharing model implications.</span>

***

## <span data-proof="authored" data-by="ai:claude">Type:</span> <span data-proof="authored" data-by="ai:claude">`object`</span> <span data-proof="authored" data-by="ai:claude">— CustomObject</span>

### <span data-proof="authored" data-by="ai:claude">Required attributes</span>

| <span data-proof="authored" data-by="ai:claude">Element</span>              | <span data-proof="authored" data-by="ai:claude">Constraint</span>                                                                                                                                                                                                            |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`<label>`</span>            | <span data-proof="authored" data-by="ai:claude">Singular UI name</span>                                                                                                                                                                                                      |
| <span data-proof="authored" data-by="ai:claude">`<pluralLabel>`</span>      | <span data-proof="authored" data-by="ai:claude">Plural UI name</span>                                                                                                                                                                                                        |
| <span data-proof="authored" data-by="ai:claude">`<sharingModel>`</span>     | <span data-proof="authored" data-by="ai:claude">See sharing rules below</span>                                                                                                                                                                                               |
| <span data-proof="authored" data-by="ai:claude">`<deploymentStatus>`</span> | <span data-proof="authored" data-by="ai:claude">Always</span> <span data-proof="authored" data-by="ai:claude">`Deployed`</span>                                                                                                                                              |
| <span data-proof="authored" data-by="ai:claude">`<nameField>`</span>        | <span data-proof="authored" data-by="ai:claude">Primary identifier (with</span> <span data-proof="authored" data-by="ai:claude">`<label>`</span> <span data-proof="authored" data-by="ai:claude">and</span> <span data-proof="authored" data-by="ai:claude">`<type>`)</span> |
| <span data-proof="authored" data-by="ai:claude">`<visibility>`</span>       | <span data-proof="authored" data-by="ai:claude">`Public`</span>                                                                                                                                                                                                              |

### <span data-proof="authored" data-by="ai:claude">Sharing model rules (Principle 1)</span>

* **<span data-proof="authored" data-by="ai:claude">Default</span>**<span data-proof="authored" data-by="ai:claude">:</span> <span data-proof="authored" data-by="ai:claude">`<sharingModel>ReadWrite</sharingModel>`</span>

* **<span data-proof="authored" data-by="ai:claude">Exception</span>**<span data-proof="authored" data-by="ai:claude">: If the object</span> **<span data-proof="authored" data-by="ai:claude">contains a Master-Detail field</span>**<span data-proof="authored" data-by="ai:claude">, sharing MUST be</span> <span data-proof="authored" data-by="ai:claude">`<sharingModel>ControlledByParent</sharingModel>`. This is non-negotiable; otherwise the deploy fails.</span>

### <span data-proof="authored" data-by="ai:claude">File</span>

```
force-app/main/default/objects/<ObjectApiName>/<ObjectApiName>.object-meta.xml
```

<span data-proof="authored" data-by="ai:claude">The API Name is the</span> **<span data-proof="authored" data-by="ai:claude">filename</span>**<span data-proof="authored" data-by="ai:claude">, not a tag.</span> <span data-proof="authored" data-by="ai:claude">`Vehicle__c.object-meta.xml`.</span>

***

## <span data-proof="authored" data-by="ai:claude">Type:</span> <span data-proof="authored" data-by="ai:claude">`field`</span> <span data-proof="authored" data-by="ai:claude">— CustomField</span>

### <span data-proof="authored" data-by="ai:claude">Required attributes (every field)</span>

| <span data-proof="authored" data-by="ai:claude">Element</span>            | <span data-proof="authored" data-by="ai:claude">Notes</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`<fullName>`</span>       | <span data-proof="authored" data-by="ai:claude">Derive from</span> <span data-proof="authored" data-by="ai:claude">`<label>`: capitalize each word, replace spaces with</span> <span data-proof="authored" data-by="ai:claude">`_`, append</span> <span data-proof="authored" data-by="ai:claude">`__c`. E.g.,</span> <span data-proof="authored" data-by="ai:claude">`Total Contract Value`</span> <span data-proof="authored" data-by="ai:claude">→</span> <span data-proof="authored" data-by="ai:claude">`Total_Contract_Value__c`</span> |
| <span data-proof="authored" data-by="ai:claude">`<label>`</span>          | <span data-proof="authored" data-by="ai:claude">Title Case UI name</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <span data-proof="authored" data-by="ai:claude">`<description>`</span>    | **<span data-proof="authored" data-by="ai:claude">Mandatory</span>** <span data-proof="authored" data-by="ai:claude">— state the business "why"</span>                                                                                                                                                                                                                                                                                                                                                                                        |
| <span data-proof="authored" data-by="ai:claude">`<inlineHelpText>`</span> | **<span data-proof="authored" data-by="ai:claude">Mandatory</span>** <span data-proof="authored" data-by="ai:claude">— actionable guidance, not just a label restatement</span>                                                                                                                                                                                                                                                                                                                                                               |

### <span data-proof="authored" data-by="ai:claude">Type-specific gotchas (the high-failure-rate types)</span>

**<span data-proof="authored" data-by="ai:claude">Roll-up Summary</span>** <span data-proof="authored" data-by="ai:claude">— most common deploy failure:</span>

* <span data-proof="authored" data-by="ai:claude">Required:</span> <span data-proof="authored" data-by="ai:claude">`<summaryOperation>`</span> <span data-proof="authored" data-by="ai:claude">(`count`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`sum`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`min`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`max`),</span> <span data-proof="authored" data-by="ai:claude">`<summarizedField>`</span> <span data-proof="authored" data-by="ai:claude">(the field on the child being summarized),</span> <span data-proof="authored" data-by="ai:claude">`<summaryForeignKey>`</span> <span data-proof="authored" data-by="ai:claude">(the Master-Detail relationship field on the child).</span>

* <span data-proof="authored" data-by="ai:claude">The relationship MUST be Master-Detail, not Lookup.</span>

* <span data-proof="authored" data-by="ai:claude">For</span> <span data-proof="authored" data-by="ai:claude">`count`, omit</span> <span data-proof="authored" data-by="ai:claude">`<summarizedField>`.</span>

**<span data-proof="authored" data-by="ai:claude">Master-Detail</span>** <span data-proof="authored" data-by="ai:claude">— restricted attributes:</span>

* <span data-proof="authored" data-by="ai:claude">Required:</span> <span data-proof="authored" data-by="ai:claude">`<referenceTo>`,</span> <span data-proof="authored" data-by="ai:claude">`<relationshipName>`,</span> <span data-proof="authored" data-by="ai:claude">`<relationshipLabel>`.</span>

* <span data-proof="authored" data-by="ai:claude">Forbidden:</span> <span data-proof="authored" data-by="ai:claude">`<defaultValue>`,</span> <span data-proof="authored" data-by="ai:claude">`<required>true</required>`</span> <span data-proof="authored" data-by="ai:claude">(the relationship is required by definition).</span>

* <span data-proof="authored" data-by="ai:claude">Once created, cannot be converted to Lookup without data migration.</span>

**<span data-proof="authored" data-by="ai:claude">Lookup with filter</span>** <span data-proof="authored" data-by="ai:claude">— restrictions:</span>

* <span data-proof="authored" data-by="ai:claude">Lookup filter formulas must reference fields on the source or related object only.</span>

* <span data-proof="authored" data-by="ai:claude">Cross-object references in filter formulas fail deploy.</span>

### <span data-proof="authored" data-by="ai:claude">External ID</span>

<span data-proof="authored" data-by="ai:claude">If the user mentions "integration", "importing data", "external system ID", or "unique key from</span> <span data-proof="authored" data-by="ai:claude"><System>", set</span> <span data-proof="authored" data-by="ai:claude">`<externalId>true</externalId>`. Applicable to Text, Number, Email types.</span>

### <span data-proof="authored" data-by="ai:claude">File</span>

```
force-app/main/default/objects/<ObjectApiName>/fields/<FieldApiName>.field-meta.xml
```

***

## <span data-proof="authored" data-by="ai:claude">Type:</span> <span data-proof="authored" data-by="ai:claude">`app`</span> <span data-proof="authored" data-by="ai:claude">— CustomApplication (Lightning App)</span>

### <span data-proof="authored" data-by="ai:claude">Required attributes</span>

| <span data-proof="authored" data-by="ai:claude">Element</span>         | <span data-proof="authored" data-by="ai:claude">Notes</span>                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`<fullName>`</span>    | <span data-proof="authored" data-by="ai:claude">API name</span>                                                                                                                                                                                                                                               |
| <span data-proof="authored" data-by="ai:claude">`<label>`</span>       | <span data-proof="authored" data-by="ai:claude">Display name</span>                                                                                                                                                                                                                                           |
| <span data-proof="authored" data-by="ai:claude">`<uiType>`</span>      | <span data-proof="authored" data-by="ai:claude">Always</span> <span data-proof="authored" data-by="ai:claude">`Lightning`</span>                                                                                                                                                                              |
| <span data-proof="authored" data-by="ai:claude">`<navType>`</span>     | <span data-proof="authored" data-by="ai:claude">`Standard`</span> <span data-proof="authored" data-by="ai:claude">(default) or</span> <span data-proof="authored" data-by="ai:claude">`Console`</span> <span data-proof="authored" data-by="ai:claude">(multi-record workflows like service / support)</span> |
| <span data-proof="authored" data-by="ai:claude">`<formFactors>`</span> | <span data-proof="authored" data-by="ai:claude">`["LARGE"]`</span> <span data-proof="authored" data-by="ai:claude">desktop,</span> <span data-proof="authored" data-by="ai:claude">`["SMALL"]`</span> <span data-proof="authored" data-by="ai:claude">mobile, or both</span>                                  |

### <span data-proof="authored" data-by="ai:claude">Highly recommended</span>

* <span data-proof="authored" data-by="ai:claude">`<brand>`</span> <span data-proof="authored" data-by="ai:claude">block — header color, footer color, override-org-theme flag. Without branding, the app looks generic.</span>

* <span data-proof="authored" data-by="ai:claude">`<actionOverrides>`</span> <span data-proof="authored" data-by="ai:claude">— required when custom record pages exist. List the action override entries.</span>

* <span data-proof="authored" data-by="ai:claude">`<utilityBar>`</span> <span data-proof="authored" data-by="ai:claude">— reference a</span> <span data-proof="authored" data-by="ai:claude">`UtilityBar`</span> <span data-proof="authored" data-by="ai:claude">config if the app needs one.</span>

### <span data-proof="authored" data-by="ai:claude">Decision: Standard vs Console nav</span>

* **<span data-proof="authored" data-by="ai:claude">Standard</span>** <span data-proof="authored" data-by="ai:claude">— default. General sales / marketing / operations apps.</span>

* **<span data-proof="authored" data-by="ai:claude">Console</span>** <span data-proof="authored" data-by="ai:claude">— only for support / service / call center workflows that need multi-record split-view workspaces. Don't use Console for ordinary apps; it confuses end users.</span>

### <span data-proof="authored" data-by="ai:claude">File</span>

```
force-app/main/default/applications/<AppApiName>.app-meta.xml
```

***

## <span data-proof="authored" data-by="ai:claude">Type:</span> <span data-proof="authored" data-by="ai:claude">`tab`</span> <span data-proof="authored" data-by="ai:claude">— CustomTab</span>

### <span data-proof="authored" data-by="ai:claude">Strict element allowlist (Principle 1 — anything else fails deploy)</span>

<span data-proof="authored" data-by="ai:claude">The root element MUST be</span> <span data-proof="authored" data-by="ai:claude">`<CustomTab>`</span> <span data-proof="authored" data-by="ai:claude">(NOT</span> <span data-proof="authored" data-by="ai:claude">`<Tab>`). Namespace:</span> <span data-proof="authored" data-by="ai:claude">`xmlns="http://soap.sforce.com/2006/04/metadata"`.</span>

| <span data-proof="authored" data-by="ai:claude">Tab type</span>             | <span data-proof="authored" data-by="ai:claude">ONLY these elements (nothing else)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **<span data-proof="authored" data-by="ai:claude">Object tabs</span>**      | <span data-proof="authored" data-by="ai:claude">`<customObject>true</customObject>`,</span> <span data-proof="authored" data-by="ai:claude">`<motif>`</span> <span data-proof="authored" data-by="ai:claude">(required),</span> <span data-proof="authored" data-by="ai:claude">`<description>`</span> <span data-proof="authored" data-by="ai:claude">(optional)</span>                                                                                                                                                                                                                                                                                                             |
| **<span data-proof="authored" data-by="ai:claude">Web tabs</span>**         | <span data-proof="authored" data-by="ai:claude">`<customObject>false</customObject>`,</span> <span data-proof="authored" data-by="ai:claude">`<label>`,</span> <span data-proof="authored" data-by="ai:claude">`<motif>`,</span> <span data-proof="authored" data-by="ai:claude">`<url>`,</span> <span data-proof="authored" data-by="ai:claude">`<urlEncodingKey>UTF-8</urlEncodingKey>`,</span> <span data-proof="authored" data-by="ai:claude">`<description>`</span> <span data-proof="authored" data-by="ai:claude">(optional),</span> <span data-proof="authored" data-by="ai:claude">`<frameHeight>`</span> <span data-proof="authored" data-by="ai:claude">(optional)</span> |
| **<span data-proof="authored" data-by="ai:claude">Visualforce tabs</span>** | <span data-proof="authored" data-by="ai:claude">`<customObject>false</customObject>`,</span> <span data-proof="authored" data-by="ai:claude">`<label>`,</span> <span data-proof="authored" data-by="ai:claude">`<motif>`,</span> <span data-proof="authored" data-by="ai:claude">`<page>`,</span> <span data-proof="authored" data-by="ai:claude">`<description>`</span> <span data-proof="authored" data-by="ai:claude">(optional)</span>                                                                                                                                                                                                                                           |

### <span data-proof="authored" data-by="ai:claude">Forbidden elements (every one fails deploy)</span>

<span data-proof="authored" data-by="ai:claude">`<sobjectName>`,</span> <span data-proof="authored" data-by="ai:claude">`<name>`,</span> <span data-proof="authored" data-by="ai:claude">`<fullName>`,</span> <span data-proof="authored" data-by="ai:claude">`<apiVersion>`,</span> <span data-proof="authored" data-by="ai:claude">`<isHidden>`,</span> <span data-proof="authored" data-by="ai:claude">`<tabVisibility>`,</span> <span data-proof="authored" data-by="ai:claude">`<type>`,</span> <span data-proof="authored" data-by="ai:claude">`<mobileReady>`,</span> <span data-proof="authored" data-by="ai:claude">`<urlFrameHeight>`,</span> <span data-proof="authored" data-by="ai:claude">`<urlType>`,</span> <span data-proof="authored" data-by="ai:claude">`<urlRedirect>`,</span> <span data-proof="authored" data-by="ai:claude">`<encodingKey>`,</span> <span data-proof="authored" data-by="ai:claude">`<height>`,</span> <span data-proof="authored" data-by="ai:claude">`<auraComponent>`.</span>

### <span data-proof="authored" data-by="ai:claude">Motif selection (Principle 5 — taste)</span>

<span data-proof="authored" data-by="ai:claude">`<motif>`</span> <span data-proof="authored" data-by="ai:claude">is the icon style. Pick one that</span> **<span data-proof="authored" data-by="ai:claude">semantically matches</span>** <span data-proof="authored" data-by="ai:claude">the tab's purpose. Don't reuse the same motif for every tab — that's a clear "AI slop" signal.</span>

### <span data-proof="authored" data-by="ai:claude">File</span>

```
force-app/main/default/tabs/<TabApiName>.tab-meta.xml
```

***

## <span data-proof="authored" data-by="ai:claude">Type:</span> <span data-proof="authored" data-by="ai:claude">`listview`</span> <span data-proof="authored" data-by="ai:claude">— ListView</span>

### <span data-proof="authored" data-by="ai:claude">Key elements</span>

| <span data-proof="authored" data-by="ai:claude">Element</span>                | <span data-proof="authored" data-by="ai:claude">Notes</span>                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`<fullName>`</span>           | <span data-proof="authored" data-by="ai:claude">API name (also the filename)</span>                                                                                                                                                                                                                                                          |
| <span data-proof="authored" data-by="ai:claude">`<label>`</span>              | <span data-proof="authored" data-by="ai:claude">UI name (under 40 characters)</span>                                                                                                                                                                                                                                                         |
| <span data-proof="authored" data-by="ai:claude">`<filterScope>`</span>        | <span data-proof="authored" data-by="ai:claude">`Everything`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`Mine`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`Queue`</span>                           |
| <span data-proof="authored" data-by="ai:claude">`<filters>`</span>            | <span data-proof="authored" data-by="ai:claude">Array of</span> <span data-proof="authored" data-by="ai:claude">`<columnName>`,</span> <span data-proof="authored" data-by="ai:claude">`<operation>`,</span> <span data-proof="authored" data-by="ai:claude">`<value>`</span> <span data-proof="authored" data-by="ai:claude">triples</span> |
| <span data-proof="authored" data-by="ai:claude">`<booleanFilterLogic>`</span> | <span data-proof="authored" data-by="ai:claude">Optional combinator:</span> <span data-proof="authored" data-by="ai:claude">`"1 AND (2 OR 3)"`</span>                                                                                                                                                                                        |
| <span data-proof="authored" data-by="ai:claude">`<columns>`</span>            | <span data-proof="authored" data-by="ai:claude">Ordered list of field API names</span>                                                                                                                                                                                                                                                       |

### <span data-proof="authored" data-by="ai:claude">Visibility decision</span>

* **<span data-proof="authored" data-by="ai:claude">Visible to all users</span>** <span data-proof="authored" data-by="ai:claude">— when the view is broadly useful and should be source-controlled.</span>

* **<span data-proof="authored" data-by="ai:claude">Visible to certain groups / queues</span>** <span data-proof="authored" data-by="ai:claude">— when restricted by team / role / permission.</span>

* **<span data-proof="authored" data-by="ai:claude">Visible only to me</span>** <span data-proof="authored" data-by="ai:claude">— never; personal views don't belong in source control.</span>

### <span data-proof="authored" data-by="ai:claude">File</span>

```
force-app/main/default/objects/<ObjectApiName>/listViews/<fullName>.listView-meta.xml
```

<span data-proof="authored" data-by="ai:claude">Inline list views inside</span> <span data-proof="authored" data-by="ai:claude">`<ObjectApiName>.object-meta.xml`</span> <span data-proof="authored" data-by="ai:claude">are allowed but discouraged — keep them as separate files for clean diffs.</span>

***

## <span data-proof="authored" data-by="ai:claude">Type:</span> <span data-proof="authored" data-by="ai:claude">`lightning-type`</span> <span data-proof="authored" data-by="ai:claude">— CustomLightningType (CLT)</span>

<span data-proof="authored" data-by="ai:claude">CLTs are JSON-Schema-based type definitions for Einstein Agent actions and structured I/O.</span>

### <span data-proof="authored" data-by="ai:claude">Critical rules (Principle 1 — non-negotiable)</span>

**<span data-proof="authored" data-by="ai:claude">Root object schemas MUST include:</span>**

* <span data-proof="authored" data-by="ai:claude">`"type": "object"`</span>

* <span data-proof="authored" data-by="ai:claude">`"title"`</span> <span data-proof="authored" data-by="ai:claude">(the human-readable title)</span>

* <span data-proof="authored" data-by="ai:claude">`"lightning:type": "lightning__objectType"`</span>

* <span data-proof="authored" data-by="ai:claude">`"unevaluatedProperties": false`</span>

**<span data-proof="authored" data-by="ai:claude">Root object schemas MUST NOT include:</span>**

* <span data-proof="authored" data-by="ai:claude">`"examples"`</span> <span data-proof="authored" data-by="ai:claude">when</span> <span data-proof="authored" data-by="ai:claude">`"unevaluatedProperties": false`</span> <span data-proof="authored" data-by="ai:claude">is set (they conflict)</span>

**<span data-proof="authored" data-by="ai:claude">Nested objects (inside</span>** **<span data-proof="authored" data-by="ai:claude">`properties`) MUST NOT set:</span>**

* <span data-proof="authored" data-by="ai:claude">`"lightning:type": "lightning__objectType"`</span> <span data-proof="authored" data-by="ai:claude">(it's only allowed at the root)</span>

### <span data-proof="authored" data-by="ai:claude">Reference vs inline</span>

<span data-proof="authored" data-by="ai:claude">For nested objects:</span>

* **<span data-proof="authored" data-by="ai:claude">Referenced CLT</span>** <span data-proof="authored" data-by="ai:claude">(reusable / separately deployed):</span> <span data-proof="authored" data-by="ai:claude">`"lightning:type": "c__<CLTName>"`</span> <span data-proof="authored" data-by="ai:claude">— note this is the FQN, not the JSON-Schema title.</span>

* **<span data-proof="authored" data-by="ai:claude">Standard Lightning types</span>** <span data-proof="authored" data-by="ai:claude">when the structure is simple (primitives only).</span>

* **<span data-proof="authored" data-by="ai:claude">Apex class types</span>** <span data-proof="authored" data-by="ai:claude">(`@apexClassType/...`) when the structure already lives server-side.</span>

### <span data-proof="authored" data-by="ai:claude">Lists / arrays — heavily restricted</span>

<span data-proof="authored" data-by="ai:claude">The CLT metaschema rejects the</span> <span data-proof="authored" data-by="ai:claude">`items`</span> <span data-proof="authored" data-by="ai:claude">keyword by default. Treat</span> <span data-proof="authored" data-by="ai:claude">`items`</span> <span data-proof="authored" data-by="ai:claude">as</span> **<span data-proof="authored" data-by="ai:claude">disallowed</span>**<span data-proof="authored" data-by="ai:claude">.</span>

* **<span data-proof="authored" data-by="ai:claude">Root-level arrays</span>**<span data-proof="authored" data-by="ai:claude">: include</span> <span data-proof="authored" data-by="ai:claude">`"lightning:type": "lightning__listType"`, MUST NOT include</span> <span data-proof="authored" data-by="ai:claude">`"items"`. Optional</span> <span data-proof="authored" data-by="ai:claude">`"type": "array"`.</span>

* **<span data-proof="authored" data-by="ai:claude">Nested arrays</span>**<span data-proof="authored" data-by="ai:claude">: include</span> <span data-proof="authored" data-by="ai:claude">`"type": "array"`, MUST NOT include</span> <span data-proof="authored" data-by="ai:claude">`"lightning:type": "lightning__listType"`</span> <span data-proof="authored" data-by="ai:claude">or</span> <span data-proof="authored" data-by="ai:claude">`"items"`.</span>

### <span data-proof="authored" data-by="ai:claude">File</span>

```
force-app/main/default/lightningTypes/<TypeApiName>.lightningType-meta.xml
```

***

## <span data-proof="authored" data-by="ai:claude">Universal post-generation validation (every type, Principle 2)</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTgsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
sf code-analyzer run --target <generated-file-path> --json
```

<span data-proof="authored" data-by="ai:claude">Then dispatch in parallel:</span>

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`metadata-consistency-checker(file_path)`</span> <span data-proof="authored" data-by="ai:claude">— cross-metadata coherence (e.g., the field references an object that exists; the tab references an object that exists)</span>

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`pattern-recognition-specialist(file_path)`</span> <span data-proof="authored" data-by="ai:claude">— naming conventions, taste</span>

<span data-proof="authored" data-by="ai:claude">Remediate sev0/sev1/sev2. Don't declare done until both review agents return clean.</span>

***

## <span data-proof="authored" data-by="ai:claude">Output report</span>

```
Generated:
- Type: {object|field|app|tab|listview|lightning-type}
- File: <full path>
- API name: <fullName>

Type-specific:
- {sharingModel|relationshipName|navType|motif|filterScope|lightning:type}: <value>

Analyzer:    {sev0=0, sev1=0, sev2=0}
Reviews:
- metadata-consistency-checker:    {findings count}
- pattern-recognition-specialist:  {findings count}

Cross-references verified: {object exists | parent field exists | utility bar exists | ...}
```

***

## <span data-proof="authored" data-by="ai:claude">Inspiration</span>

<span data-proof="authored" data-by="ai:claude">This skill consolidates six upstream skills from</span> <span data-proof="authored" data-by="ai:claude">`forcedotcom/afv-library`</span> <span data-proof="authored" data-by="ai:claude">(Apache-2.0):</span>

* [<span data-proof="authored" data-by="ai:claude">`generating-custom-object`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-custom-object)

* [<span data-proof="authored" data-by="ai:claude">`generating-custom-field`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-custom-field)

* [<span data-proof="authored" data-by="ai:claude">`generating-custom-application`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-custom-application)

* [<span data-proof="authored" data-by="ai:claude">`generating-custom-tab`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-custom-tab)

* [<span data-proof="authored" data-by="ai:claude">`generating-list-view`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-list-view)

* [<span data-proof="authored" data-by="ai:claude">`generating-custom-lightning-type`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-custom-lightning-type)

<span data-proof="authored" data-by="ai:claude">The upstream split is one-skill-per-metadata-type — useful for narrow, surgical work, but high friction when a feature needs multiple metadata types together (which is most features). This plugin's adaptation collapses the six into one</span> <span data-proof="authored" data-by="ai:claude">`--type`-dispatched skill, citing each upstream for the deep tables (Roll-up Summary edge cases, CLT metaschema validation rules, action override patterns). When upstream is a better reference for a specific edge case, link out from this skill rather than vendoring.</span>