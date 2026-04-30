---
name: lightning-page-generate
description: "Generate Salesforce Lightning pages — FlexiPages (RecordPage / AppPage / HomePage) and entire Lightning apps that orchestrate object + fields + tabs + flexipage + permission set. Use when creating Lightning record pages, app home pages, or building a complete LEX app from a description. Trigger phrases: 'create a Lightning record page', 'build a Lightning page', 'add a flexipage', 'generate a record page for', 'build a Lightning app', 'create a complete LEX app', 'I need a project management app', 'generate a flexipage with', 'add components to the record page'. Pairs with `metadata-consistency-checker`."
argument-hint: "[--type page|app + page intent OR app intent, e.g. '--type page record-page for Account' or '--type app project-management app with Tasks Resources Supplies']"
---

# /lightning-page-generate

> **Principles enforced:** 1 (preserve the quality ceiling), 4 (spec is the artifact), 7 (institutional memory). See `PRINCIPLES.md`.

## Copy-paste-to-agent

```
Generate a Lightning page (FlexiPage) OR a complete Lightning app. Two modes:
(--type page) — single FlexiPage. ALWAYS bootstrap with `sf template generate flexipage`
first; never write FlexiPage XML from scratch (region IDs and component configs are too
fragile to hand-author). Then add components.
(--type app) — full LEX app. Orchestrate metadata in dependency order: object → fields →
tab → flexipage → custom application → list view → validation rule → permission set.
Dispatch /metadata-generate for each piece. End with /permission-set-generate to grant
access. Always include a Verification Strategy: how does a user actually exercise this app.
```

## When to use

Two distinct modes:

| Mode | Use when |
|---|---|
| `--type page` | Adding ONE Lightning page (record page, app page, or home page) to an existing object |
| `--type app` | Building a COMPLETE Lightning app from a natural-language description (multiple objects + supporting metadata) |

If the user wants just an object (no UI), use `/metadata-generate --type object`. If they want just a tab (no flexipage), use `/metadata-generate --type tab`.

---

## Mode: `--type page` — single FlexiPage

### Step 0: Research (Principle 7)

- Task `sf-learnings-researcher("flexipage" + object_name)` — has someone built similar pages?
- Task `sf-repo-research-analyst(object_name)` — what flexipages already exist? Update existing rather than duplicate.

### Step 1: Bootstrap with the CLI (mandatory)

**Never hand-write FlexiPage XML.** Always start from the CLI template — it produces the right region IDs, component IDs, and metadata that prevents subtle deploy failures.

```bash
sf template generate flexipage \
  --name <PageName> \
  --template <RecordPage|AppPage|HomePage> \
  --sobject <SObject> \
  --primary-field <Field1> \
  --secondary-fields <Field2,Field3> \
  --detail-fields <Field4,Field5,Field6,Field7> \
  --output-dir force-app/main/default/flexipages
```

If the CLI template command fails:

1. Install the templates plugin: `sf plugins install templates`
2. Re-run.

If it still fails, **stop**. Do not fall back to hand-authored XML.

### Step 2: Add components

Edit the generated XML to add components inside `<flexiPageRegions>`. Each component has:

- `<itemType>` — usually `Component` for standard / custom LWCs, `Field` for field components
- `<componentName>` — the LWC API name (e.g., `c:myCustomComponent` for custom, `flexipage_recordHeader` for standard)
- `<componentInstanceProperties>` — props passed to the component
- `<componentVisibility>` — visibility filters (record type, field value, user permission)

### Step 3: Validate

```bash
sf code-analyzer run --target force-app/main/default/flexipages/<PageName>.flexipage-meta.xml --json
```

Dispatch `metadata-consistency-checker` — verifies referenced components exist, fields exist on the SObject, etc.

### Output

```
Generated:
- force-app/main/default/flexipages/<PageName>.flexipage-meta.xml

Template:    {RecordPage|AppPage|HomePage}
SObject:     <name>
Components:  {count}
Visibility filters: {count}

Analyzer:    {sev0=0, sev1=0, sev2=0}
Review:      metadata-consistency-checker — {findings count}
```

---

## Mode: `--type app` — complete Lightning app

This mode orchestrates multiple metadata types in dependency order. Treat it as a mini-pipeline — each step produces an artifact the next consumes.

### Step 0: Spec the app (Principle 4 — spec is the artifact)

Before any generation, write a spec that names:

- **App name and label**
- **Custom objects needed** (each with API name, sharing model, master-detail relationships)
- **Custom fields per object** (type, label, required/optional, external ID flag)
- **Tabs** (one per object, plus any web/Visualforce tabs)
- **FlexiPages** (one record page per object minimum; optional app/home pages)
- **List views** (per-object curated views)
- **Validation rules** (data quality enforcement)
- **Permission set** (grants access to the new metadata)
- **Verification Strategy** — what does an end user actually do to exercise this app?

Save the spec to `docs/plans/YYYY-MM-DD-feat-<app-slug>-spec.md`. Present to the user. **Do not proceed without explicit approval** — the spec is the contract (Principle 4).

### Step 1: Generate in dependency order

Order matters — each metadata type depends on previous ones:

```
1. CustomObject(s)          via /metadata-generate --type object
2. CustomField(s)           via /metadata-generate --type field   (per object, after object exists)
3. CustomTab(s)             via /metadata-generate --type tab     (after object + fields)
4. FlexiPage(s)             via /lightning-page-generate --type page (after tab)
5. CustomApplication        via /metadata-generate --type app     (after tabs + flexipages)
6. ListView(s)              via /metadata-generate --type listview
7. ValidationRule(s)        via /validation-rule-generate
8. PermissionSet            via /permission-set-generate          (LAST — grants access to all the above)
```

Each step is a separate skill dispatch. Don't try to bundle into one giant XML write.

### Step 2: Deploy in the same order

```bash
# Deploy each artifact in dependency order
sf project deploy start --metadata CustomObject:<Object1>,CustomObject:<Object2>
sf project deploy start --metadata CustomField:<Object1>.<Field1>,...
# ... and so on through the chain
```

If any deploy fails, **stop** and diagnose before generating more (Principle 3 — jagged-edge errors compound).

### Step 3: Validate end-to-end

After all metadata is deployed:

- Dispatch `metadata-consistency-checker` — cross-metadata coherence (every field referenced exists, every tab references a real object, every flexipage references real fields, etc.)
- Run any tests that exercise the new objects.
- Manually open the app in the org and walk the Verification Strategy from Step 0.

### Step 4: Capture (Principle 7)

Run `/sf-compound` to write the app architecture to `docs/solutions/`. App architectures are exactly the kind of institutional memory that pays back on the second similar app.

### Output

```
Generated app: <AppApiName>

Metadata produced:
- {n} CustomObjects:    {list}
- {n} CustomFields:     {list (object.field)}
- {n} CustomTabs:       {list}
- {n} FlexiPages:       {list}
- 1 CustomApplication:  {AppApiName}
- {n} ListViews:        {list}
- {n} ValidationRules:  {list}
- 1 PermissionSet:      {PermSetApiName}

Deploy:      All steps PASS
Reviews:
- metadata-consistency-checker:    {findings count}

Verification Strategy: {one paragraph — how a user exercises this app end-to-end}
```

---

## Forbidden shortcuts (Principle 1)

- **Don't write FlexiPage XML from scratch** — always start from `sf template generate flexipage`. Hand-authored FlexiPages have a high subtle-deploy-failure rate (region ID mismatches, missing component IDs).
- **Don't deploy app metadata out of dependency order** — deploys fail when a tab references an object that hasn't deployed yet.
- **Don't skip the permission set** — an app users can't reach is not deployable in any meaningful sense.
- **Don't bundle the whole app into one XML write** — separate skill dispatches per metadata type so each can be reviewed and rolled back independently.

---

## Inspiration

This skill consolidates two upstream skills from `forcedotcom/afv-library` (Apache-2.0):

- [`generating-flexipage`](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-flexipage) — the FlexiPage CLI bootstrap discipline and component configuration
- [`generating-lightning-app`](https://github.com/forcedotcom/afv-library/tree/main/skills/generating-lightning-app) — the multi-metadata orchestration in dependency order

The upstream `generating-lightning-app` ships a "metadata type registry" that explicitly says which sub-skill to load for each type and warns against bundling. This plugin's adaptation routes those sub-skill calls through `/metadata-generate`, `/validation-rule-generate`, and `/permission-set-generate` — preserving the orchestration discipline while consolidating the leaf generators. For the full per-component-type props tables and the visibility-filter syntax, consult the upstream `generating-flexipage` reference.
