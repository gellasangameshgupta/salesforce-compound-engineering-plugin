---
name: permission-set-generate
description: "Generate Salesforce Permission Set metadata (PermissionSet XML) with object permissions, field-level security (FLS), tab visibility, app visibility, and user permissions. Use when creating a new permission set, granting CRUD on objects, configuring FLS for sensitive fields, or assigning system permissions. Trigger phrases: 'create a permission set', 'grant access to', 'add CRUD permissions for', 'configure FLS for', 'permission set for the app', 'allow users to access', 'grant the View All permission'. Pairs with `metadata-consistency-checker` and `security-guide`."
argument-hint: "[permission set name + scope, e.g. 'Sales_Manager_Access for Account, Opportunity, Lead with View All']"
---

# <span data-proof="authored" data-by="ai:claude">/permission-set-generate</span>

> **<span data-proof="authored" data-by="ai:claude">Principles enforced:</span>** <span data-proof="authored" data-by="ai:claude">1 (preserve the quality ceiling — overly-broad perms are a security regression), 5 (taste — perm set names matter), 7 (institutional memory). See</span> <span data-proof="authored" data-by="ai:claude">`PRINCIPLES.md`.</span>

## <span data-proof="authored" data-by="ai:claude">Copy-paste-to-agent</span>

```
Generate a Salesforce Permission Set (PermissionSet XML) with the minimum permissions
needed to do the job. Default to least privilege: allowDelete=false, modifyAllRecords=false,
viewAllRecords=false unless the user explicitly asked for a wider grant. Always set
description with the intended audience. Always validate with metadata-consistency-checker
that referenced objects, fields, tabs, and apps actually exist. Place the file at
force-app/main/default/permissionsets/<Name>.permissionset-meta.xml.
```

## <span data-proof="authored" data-by="ai:claude">When to use</span>

* <span data-proof="authored" data-by="ai:claude">Creating a new permission set for an app or role</span>

* <span data-proof="authored" data-by="ai:claude">Granting CRUD on specific objects</span>

* <span data-proof="authored" data-by="ai:claude">Configuring FLS for sensitive or custom fields</span>

* <span data-proof="authored" data-by="ai:claude">Setting tab and application visibility</span>

* <span data-proof="authored" data-by="ai:claude">Adding system / user permissions (e.g.,</span> <span data-proof="authored" data-by="ai:claude">`ViewAllData`,</span> <span data-proof="authored" data-by="ai:claude">`ModifyAllData`)</span>

<span data-proof="authored" data-by="ai:claude">If the user is asking for</span> *<span data-proof="authored" data-by="ai:claude">modifications</span>* <span data-proof="authored" data-by="ai:claude">to an existing perm set, this skill still applies — read the existing file first and update rather than recreate.</span>

<span data-proof="authored" data-by="ai:claude">If the user wants to grant access to a brand-new app and you've just generated the app via</span> <span data-proof="authored" data-by="ai:claude">`/lightning-page-generate --type app`, this skill is the LAST step of that pipeline.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 0: Research (Principle 7)</span>

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher("permission set" + scope)`</span> <span data-proof="authored" data-by="ai:claude">— has someone built a similar perm set?</span>

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-repo-research-analyst(target_objects)`</span> <span data-proof="authored" data-by="ai:claude">— what perm sets already exist? Don't duplicate; consider extending an existing one.</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/security-guide/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">for sharing-model implications and least-privilege defaults.</span>

***

## <span data-proof="authored" data-by="ai:claude">Required structure</span>

<span data-proof="authored" data-by="ai:claude">Every permission set needs at minimum:</span>

```xml proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6Mzg3LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
<?xml version="1.0" encoding="UTF-8"?>
<PermissionSet xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>YourPermissionSetName</fullName>
    <label>Human-Friendly Display Name</label>
    <description>One sentence stating purpose AND intended audience.</description>
    <hasActivationRequired>false</hasActivationRequired>
    <license>Salesforce</license>
</PermissionSet>
```

<span data-proof="authored" data-by="ai:claude">Naming conventions:</span>

* **<span data-proof="authored" data-by="ai:claude">API name</span>** <span data-proof="authored" data-by="ai:claude">(`<fullName>`): descriptive snake-case (e.g.,</span> <span data-proof="authored" data-by="ai:claude">`Sales_Manager_Access`,</span> <span data-proof="authored" data-by="ai:claude">`Order_Mgmt_App_User`).</span>

* **<span data-proof="authored" data-by="ai:claude">Label</span>**<span data-proof="authored" data-by="ai:claude">: human-readable display name.</span>

* **<span data-proof="authored" data-by="ai:claude">Description</span>**<span data-proof="authored" data-by="ai:claude">: mandatory. Must state the</span> **<span data-proof="authored" data-by="ai:claude">intended audience</span>** <span data-proof="authored" data-by="ai:claude">— "Grants Sales Managers full CRUD on Opportunity, Account, and Lead, plus View All on related custom objects." Generic descriptions are a Principle 5 fail.</span>

***

## <span data-proof="authored" data-by="ai:claude">Section 1: Object permissions (CRUD)</span>

```xml proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MzM3LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
<objectPermissions>
    <allowCreate>true</allowCreate>
    <allowRead>true</allowRead>
    <allowEdit>true</allowEdit>
    <allowDelete>false</allowDelete>
    <modifyAllRecords>false</modifyAllRecords>
    <viewAllRecords>false</viewAllRecords>
    <viewAllFields>false</viewAllFields>
    <object>Account</object>
</objectPermissions>
```

**<span data-proof="authored" data-by="ai:claude">Default to least privilege.</span>** <span data-proof="authored" data-by="ai:claude">Start with read-only; add Create/Edit/Delete only when the user explicitly asked for them.</span>

<span data-proof="authored" data-by="ai:claude">`modifyAllRecords`</span> <span data-proof="authored" data-by="ai:claude">and</span> <span data-proof="authored" data-by="ai:claude">`viewAllRecords`</span> <span data-proof="authored" data-by="ai:claude">are</span> **<span data-proof="authored" data-by="ai:claude">dangerous broad grants</span>** <span data-proof="authored" data-by="ai:claude">— they bypass sharing rules. Default to</span> <span data-proof="authored" data-by="ai:claude">`false`</span> <span data-proof="authored" data-by="ai:claude">and require explicit user request to set</span> <span data-proof="authored" data-by="ai:claude">`true`.</span>

<span data-proof="authored" data-by="ai:claude">`viewAllFields`</span> <span data-proof="authored" data-by="ai:claude">similarly bypasses FLS. Default to</span> <span data-proof="authored" data-by="ai:claude">`false`.</span>

***

## <span data-proof="authored" data-by="ai:claude">Section 2: Field-level security (FLS)</span>

```xml proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTM0LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
<fieldPermissions>
    <readable>true</readable>
    <editable>true</editable>
    <field>Account.Industry</field>
</fieldPermissions>
```

<span data-proof="authored" data-by="ai:claude">For sensitive fields (e.g., SSN, salary, PII), set</span> <span data-proof="authored" data-by="ai:claude">`<readable>false</readable>`</span> <span data-proof="authored" data-by="ai:claude">for users who don't need them.</span>

<span data-proof="authored" data-by="ai:claude">For formula and Roll-up Summary fields, only</span> <span data-proof="authored" data-by="ai:claude">`<readable>`</span> <span data-proof="authored" data-by="ai:claude">matters (`<editable>`</span> <span data-proof="authored" data-by="ai:claude">is implicit-false because they're calculated).</span>

***

## <span data-proof="authored" data-by="ai:claude">Section 3: Tab settings</span>

```xml proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6OTcsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
<tabSettings>
    <tab>standard-Account</tab>
    <visibility>Visible</visibility>
</tabSettings>
```

<span data-proof="authored" data-by="ai:claude">Visibility values:</span>

* <span data-proof="authored" data-by="ai:claude">`Visible`</span> <span data-proof="authored" data-by="ai:claude">— tab appears in nav</span>

* <span data-proof="authored" data-by="ai:claude">`Available`</span> <span data-proof="authored" data-by="ai:claude">— tab is in the user's app picker but not pinned</span>

* <span data-proof="authored" data-by="ai:claude">`None`</span> <span data-proof="authored" data-by="ai:claude">— tab is hidden</span>

***

## <span data-proof="authored" data-by="ai:claude">Section 4: App visibility</span>

```xml proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTI5LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
<applicationVisibilities>
    <application>Sales_Manager_App</application>
    <visible>true</visible>
</applicationVisibilities>
```

<span data-proof="authored" data-by="ai:claude">Apps the perm set's audience needs access to.</span>

***

## <span data-proof="authored" data-by="ai:claude">Section 5: User permissions (system permissions)</span>

```xml proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6OTEsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
<userPermissions>
    <enabled>true</enabled>
    <name>ViewSetup</name>
</userPermissions>
```

<span data-proof="authored" data-by="ai:claude">Common ones:</span>

| <span data-proof="authored" data-by="ai:claude">`<name>`</span>                | <span data-proof="authored" data-by="ai:claude">What it grants</span>                                         |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`ViewAllData`</span>           | <span data-proof="authored" data-by="ai:claude">View all records on all objects (BROAD; use sparingly)</span> |
| <span data-proof="authored" data-by="ai:claude">`ModifyAllData`</span>         | <span data-proof="authored" data-by="ai:claude">Modify all records on all objects (DANGEROUS)</span>          |
| <span data-proof="authored" data-by="ai:claude">`ViewSetup`</span>             | <span data-proof="authored" data-by="ai:claude">Read-only access to Setup</span>                              |
| <span data-proof="authored" data-by="ai:claude">`ManageUsers`</span>           | <span data-proof="authored" data-by="ai:claude">Create / edit users</span>                                    |
| <span data-proof="authored" data-by="ai:claude">`ApiEnabled`</span>            | <span data-proof="authored" data-by="ai:claude">Use the API (most users need this)</span>                     |
| <span data-proof="authored" data-by="ai:claude">`ViewMyTeamsDashboards`</span> | <span data-proof="authored" data-by="ai:claude">Sales managers' dashboards</span>                             |

**<span data-proof="authored" data-by="ai:claude">Default to NOT granting</span>** **<span data-proof="authored" data-by="ai:claude">`ViewAllData`</span>** **<span data-proof="authored" data-by="ai:claude">or</span>** **<span data-proof="authored" data-by="ai:claude">`ModifyAllData`.</span>** <span data-proof="authored" data-by="ai:claude">These bypass the sharing model — a Principle 1 ceiling violation when granted casually.</span>

***

## <span data-proof="authored" data-by="ai:claude">Section 6: Apex class access</span>

```xml proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTAwLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
<classAccesses>
    <apexClass>OrderService</apexClass>
    <enabled>true</enabled>
</classAccesses>
```

<span data-proof="authored" data-by="ai:claude">For every Apex class invoked via UI / Aura / LWC / REST that the user needs to reach, grant access here.</span>

***

## <span data-proof="authored" data-by="ai:claude">Section 7: Page access (Visualforce)</span>

```xml proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6OTQsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
<pageAccesses>
    <apexPage>OrderEntry</apexPage>
    <enabled>true</enabled>
</pageAccesses>
```

***

## <span data-proof="authored" data-by="ai:claude">Hard constraints (Principle 1)</span>

| <span data-proof="authored" data-by="ai:claude">Rule</span>                                                                                                                                                                                                                                                    | <span data-proof="authored" data-by="ai:claude">Why</span>                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`description`</span> <span data-proof="authored" data-by="ai:claude">is</span> **<span data-proof="authored" data-by="ai:claude">mandatory</span>** <span data-proof="authored" data-by="ai:claude">and must name the audience</span>                          | <span data-proof="authored" data-by="ai:claude">Future maintainers must be able to tell who this perm set is for</span>                                                                                                                                          |
| <span data-proof="authored" data-by="ai:claude">Default to least privilege on every CRUD flag</span>                                                                                                                                                                                                           | <span data-proof="authored" data-by="ai:claude">`allowDelete=true`</span> <span data-proof="authored" data-by="ai:claude">is a destructive grant — make it intentional</span>                                                                                    |
| <span data-proof="authored" data-by="ai:claude">Default to</span> <span data-proof="authored" data-by="ai:claude">`modifyAllRecords=false`,</span> <span data-proof="authored" data-by="ai:claude">`viewAllRecords=false`,</span> <span data-proof="authored" data-by="ai:claude">`viewAllFields=false`</span> | <span data-proof="authored" data-by="ai:claude">These bypass sharing/FLS — the user must explicitly ask</span>                                                                                                                                                   |
| <span data-proof="authored" data-by="ai:claude">Default to NO</span> <span data-proof="authored" data-by="ai:claude">`ViewAllData`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`ModifyAllData`</span>                                      | <span data-proof="authored" data-by="ai:claude">These bypass everything; reserve for admin/integration users</span>                                                                                                                                              |
| <span data-proof="authored" data-by="ai:claude">Reference only metadata that exists</span>                                                                                                                                                                                                                     | <span data-proof="authored" data-by="ai:claude">A perm set granting</span> <span data-proof="authored" data-by="ai:claude">`Account.NonExistentField__c`</span> <span data-proof="authored" data-by="ai:claude">deploys but corrupts the org's perm graph</span> |
| <span data-proof="authored" data-by="ai:claude">One perm set per audience, not per feature</span>                                                                                                                                                                                                              | <span data-proof="authored" data-by="ai:claude">"Sales Manager" perm set, not "Account CRUD" perm set. Audiences scale; features compose</span>                                                                                                                  |

***

## <span data-proof="authored" data-by="ai:claude">Workflow</span>

1. **<span data-proof="authored" data-by="ai:claude">Gather scope.</span>** <span data-proof="authored" data-by="ai:claude">Audience, objects, fields, tabs, apps, system perms.</span>
2. **<span data-proof="authored" data-by="ai:claude">Apply least privilege.</span>** <span data-proof="authored" data-by="ai:claude">Strip every flag that wasn't explicitly requested.</span>
3. **<span data-proof="authored" data-by="ai:claude">Verify references.</span>** <span data-proof="authored" data-by="ai:claude">Every object, field, tab, app, class, page must exist in the project.</span>
4. **<span data-proof="authored" data-by="ai:claude">Author the XML.</span>** <span data-proof="authored" data-by="ai:claude">One section at a time, top-to-bottom (object → FLS → tab → app → user perms → class → page).</span>
5. **<span data-proof="authored" data-by="ai:claude">Validate.</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`sf code-analyzer run --target <path> --json`.</span>
6. **<span data-proof="authored" data-by="ai:claude">Dispatch review.</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`metadata-consistency-checker`</span> <span data-proof="authored" data-by="ai:claude">for cross-references;</span> <span data-proof="authored" data-by="ai:claude">`security-guide`</span> <span data-proof="authored" data-by="ai:claude">should be consulted for sharing implications (this is reading, not dispatch — the skill is reference-shaped).</span>
7. **<span data-proof="authored" data-by="ai:claude">Deploy.</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`sf project deploy start --metadata PermissionSet:<Name>`.</span>
8. **<span data-proof="authored" data-by="ai:claude">Assign for testing.</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`sf org assign permset --name <Name> --target-org <alias>`.</span>

***

## <span data-proof="authored" data-by="ai:claude">Output report</span>

```
Generated:
- force-app/main/default/permissionsets/<Name>.permissionset-meta.xml

Audience:    {one sentence — who this is for}

Grants:
- Object permissions: {n} (CRUD breakdown: C=N, R=N, E=N, D=N)
- FLS:                {n} fields
- Tabs:               {n} tabs ({Visible|Available} count)
- Apps:               {n} apps
- User perms:         {list of system perms granted}
- Apex classes:       {n}
- Pages:              {n}

Broad-grant flags (audit these explicitly):
- modifyAllRecords:   {set on N objects} or "none"
- viewAllRecords:     {set on N objects} or "none"
- viewAllFields:      {set on N objects} or "none"
- ViewAllData:        {true|false}
- ModifyAllData:      {true|false}

Analyzer:    {sev0=0, sev1=0, sev2=0}
Review:      metadata-consistency-checker — {findings count}

Cross-references verified: every object, field, tab, app, class, page exists.
```

***

## <span data-proof="authored" data-by="ai:claude">Inspiration</span>

<span data-proof="authored" data-by="ai:claude">Adapted from</span> [<span data-proof="authored" data-by="ai:claude">`forcedotcom/afv-library/skills/generating-permission-set`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-permission-set) <span data-proof="authored" data-by="ai:claude">(Apache-2.0). The upstream skill is compact and structured around the seven permission-set sections. This plugin's adaptation tightens around least-privilege defaults (a Principle 1 application) and the audience-not-feature naming convention (Principle 5). For the full enumeration of system permission names and their security implications, consult the upstream and the Salesforce Metadata API reference.</span>