---
name: slds2-uplift
description: "Migrate Lightning Web Components and Aura components from SLDS 1 to SLDS 2 by running the SLDS linter and fixing every violation type — hardcoded values, deprecated tokens, LWC-token-to-SLDS-hook conversions, and slds class overrides. Use when uplifting components to SLDS 2, fixing linter violations, replacing hardcoded CSS values with SLDS hooks, or migrating LWC tokens. Trigger phrases: 'uplift to SLDS 2', 'migrate to SLDS 2', 'run the SLDS linter', 'fix SLDS violations', 'replace hardcoded CSS with SLDS hooks', 'convert lwc tokens to SLDS hooks', 'no-hardcoded-values', 'no-slds-class-overrides', 'lwc-token-to-slds-hook', 'no-deprecated-tokens-slds1'. Pairs with `lwc-patterns`."
argument-hint: "[component path or directory; defaults to current LWC under force-app/main/default/lwc]"
---

# <span data-proof="authored" data-by="ai:claude">/slds2-uplift</span>

> **<span data-proof="authored" data-by="ai:claude">Principles enforced:</span>** <span data-proof="authored" data-by="ai:claude">1 (preserve the quality ceiling), 5 (taste over typing). See</span> <span data-proof="authored" data-by="ai:claude">`PRINCIPLES.md`.</span>

## <span data-proof="authored" data-by="ai:claude">Copy-paste-to-agent</span>

```
Migrate LWC and Aura components from SLDS 1 to SLDS 2 using @salesforce-ux/slds-linter.
Run with --fix first to auto-fix simple violations. For remaining violations, fix by rule
type with the table below. Always use a fallback value: var(--slds-g-hook, originalValue).
For class overrides, change BOTH .css AND .html (or .cmp) — the markup change is the
commonly-missed step. Skip layout values (100%, auto, 0, inherit, none). Re-run the linter
after fixes; do not declare done until zero errors.
```

## <span data-proof="authored" data-by="ai:claude">When to use</span>

* <span data-proof="authored" data-by="ai:claude">Migrating LWC or Aura components from SLDS 1 to SLDS 2</span>

* <span data-proof="authored" data-by="ai:claude">Fixing SLDS linter violations on existing components</span>

* <span data-proof="authored" data-by="ai:claude">Replacing hardcoded CSS values with SLDS 2 hooks</span>

* <span data-proof="authored" data-by="ai:claude">Converting</span> <span data-proof="authored" data-by="ai:claude">`--lwc-*`</span> <span data-proof="authored" data-by="ai:claude">tokens to</span> <span data-proof="authored" data-by="ai:claude">`--slds-g-*`</span> <span data-proof="authored" data-by="ai:claude">hooks</span>

* <span data-proof="authored" data-by="ai:claude">Resolving</span> <span data-proof="authored" data-by="ai:claude">`t(...)`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`token(...)`</span> <span data-proof="authored" data-by="ai:claude">legacy syntax</span>

<span data-proof="authored" data-by="ai:claude">If a component is brand-new and not yet built, write it in SLDS 2 from the start (cite this skill in the implementation, but no migration is needed).</span>

***

## <span data-proof="authored" data-by="ai:claude">SLDS 2 hook categories (the namespace)</span>

| <span data-proof="authored" data-by="ai:claude">Category</span>   | <span data-proof="authored" data-by="ai:claude">Hook prefix</span>                | <span data-proof="authored" data-by="ai:claude">What it replaces</span>                                                                                                                                      |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <span data-proof="authored" data-by="ai:claude">Color</span>      | <span data-proof="authored" data-by="ai:claude">`--slds-g-color-*`</span>         | <span data-proof="authored" data-by="ai:claude">Hardcoded colors,</span> <span data-proof="authored" data-by="ai:claude">`--lwc-color*`</span> <span data-proof="authored" data-by="ai:claude">tokens</span> |
| <span data-proof="authored" data-by="ai:claude">Spacing</span>    | <span data-proof="authored" data-by="ai:claude">`--slds-g-spacing-*`</span>       | <span data-proof="authored" data-by="ai:claude">Hardcoded margins, padding, gaps</span>                                                                                                                      |
| <span data-proof="authored" data-by="ai:claude">Sizing</span>     | <span data-proof="authored" data-by="ai:claude">`--slds-g-sizing-*`</span>        | <span data-proof="authored" data-by="ai:claude">Hardcoded widths, heights, dimensions</span>                                                                                                                 |
| <span data-proof="authored" data-by="ai:claude">Typography</span> | <span data-proof="authored" data-by="ai:claude">`--slds-g-font-*`</span>          | <span data-proof="authored" data-by="ai:claude">Hardcoded font sizes, weights, line heights</span>                                                                                                           |
| <span data-proof="authored" data-by="ai:claude">Border</span>     | <span data-proof="authored" data-by="ai:claude">`--slds-g-sizing-border-*`</span> | <span data-proof="authored" data-by="ai:claude">Hardcoded border widths</span>                                                                                                                               |
| <span data-proof="authored" data-by="ai:claude">Radius</span>     | <span data-proof="authored" data-by="ai:claude">`--slds-g-radius-border-*`</span> | <span data-proof="authored" data-by="ai:claude">Hardcoded border-radius</span>                                                                                                                               |
| <span data-proof="authored" data-by="ai:claude">Shadow</span>     | <span data-proof="authored" data-by="ai:claude">`--slds-g-shadow-*`</span>        | <span data-proof="authored" data-by="ai:claude">Hardcoded</span> <span data-proof="authored" data-by="ai:claude">`box-shadow`</span> <span data-proof="authored" data-by="ai:claude">values</span>           |

**<span data-proof="authored" data-by="ai:claude">Color hooks require judgment</span>** <span data-proof="authored" data-by="ai:claude">(context-dependent — you have to read the markup to choose between surface, accent, on-accent variants). Non-color hooks are mostly numbered scales with straightforward mappings.</span>

***

## <span data-proof="authored" data-by="ai:claude">Workflow</span>

### <span data-proof="authored" data-by="ai:claude">Step 0: Research (Principle 7)</span>

* <span data-proof="authored" data-by="ai:claude">Task</span> <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher("SLDS 2 uplift")`</span> <span data-proof="authored" data-by="ai:claude">— has someone migrated similar components?</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/lwc-patterns/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">for the project's LWC conventions.</span>

### <span data-proof="authored" data-by="ai:claude">Step 1: Run the linter with auto-fix</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTAsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
npx @salesforce-ux/slds-linter@latest lint --fix .
```

<span data-proof="authored" data-by="ai:claude">The linter analyzes</span> <span data-proof="authored" data-by="ai:claude">`.css`,</span> <span data-proof="authored" data-by="ai:claude">`.html`</span> <span data-proof="authored" data-by="ai:claude">(LWC), and</span> <span data-proof="authored" data-by="ai:claude">`.cmp`</span> <span data-proof="authored" data-by="ai:claude">(Aura), auto-fixes simple cases, and reports remaining violations.</span>

### <span data-proof="authored" data-by="ai:claude">Step 2: Read the linter output</span>

<span data-proof="authored" data-by="ai:claude">Linter output format:</span>

```
componentName.css
  15:3   warning   Overriding slds-button isn't supported.            slds/no-slds-class-overrides
  23:5   error     The '--lwc-colorBackground' design token is deprecated. ...
                   1. --slds-g-color-surface-2
                   2. --slds-g-color-surface-container-2              slds/lwc-token-to-slds-hook
  30:8   warning   Consider replacing the #ffffff static value ...    slds/no-hardcoded-values-slds2
  31:15  error     Consider removing t(fontSizeMedium) ...            slds/no-deprecated-tokens-slds1
```

<span data-proof="authored" data-by="ai:claude">Four violation types. Each has a different fix strategy.</span>

### <span data-proof="authored" data-by="ai:claude">Step 3: Fix by violation type</span>

| <span data-proof="authored" data-by="ai:claude">Rule</span>                              | <span data-proof="authored" data-by="ai:claude">Fix</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`slds/no-hardcoded-values-slds2`</span>  | <span data-proof="authored" data-by="ai:claude">Replace the hardcoded value with an SLDS hook + the original as fallback:</span> <span data-proof="authored" data-by="ai:claude">`var(--slds-g-color-surface-1, #ffffff)`</span>                                                                                                                                                                                                                                                                                                                                                                                |
| <span data-proof="authored" data-by="ai:claude">`slds/lwc-token-to-slds-hook`</span>     | <span data-proof="authored" data-by="ai:claude">Replace</span> <span data-proof="authored" data-by="ai:claude">`--lwc-*`</span> <span data-proof="authored" data-by="ai:claude">with the recommended SLDS hook, keeping the LWC token as fallback:</span> <span data-proof="authored" data-by="ai:claude">`var(--slds-g-color-surface-2, var(--lwc-colorBackground, #fff))`</span>                                                                                                                                                                                                                              |
| <span data-proof="authored" data-by="ai:claude">`slds/no-slds-class-overrides`</span>    | <span data-proof="authored" data-by="ai:claude">Create a component-prefixed CSS class (e.g.,</span> <span data-proof="authored" data-by="ai:claude">`.myapp-button`), add it to the markup</span> **<span data-proof="authored" data-by="ai:claude">alongside</span>** <span data-proof="authored" data-by="ai:claude">the SLDS class. Both</span> <span data-proof="authored" data-by="ai:claude">`.css`</span> <span data-proof="authored" data-by="ai:claude">AND</span> <span data-proof="authored" data-by="ai:claude">`.html`/`.cmp`</span> <span data-proof="authored" data-by="ai:claude">change</span> |
| <span data-proof="authored" data-by="ai:claude">`slds/no-deprecated-tokens-slds1`</span> | <span data-proof="authored" data-by="ai:claude">Replace</span> <span data-proof="authored" data-by="ai:claude">`t(fontSizeMedium)`</span> <span data-proof="authored" data-by="ai:claude">with</span> <span data-proof="authored" data-by="ai:claude">`var(--slds-g-font-size-base, var(--lwc-fontSizeMedium, 0.8125rem))`</span> <span data-proof="authored" data-by="ai:claude">— chain SLDS → LWC → literal</span>                                                                                                                                                                                           |

### <span data-proof="authored" data-by="ai:claude">Step 4: Skip layout values (don't fix what isn't broken)</span>

<span data-proof="authored" data-by="ai:claude">The linter flags</span> **<span data-proof="authored" data-by="ai:claude">all</span>** <span data-proof="authored" data-by="ai:claude">hardcoded values, including layout. Skip these — they have no SLDS hook equivalent:</span>

| <span data-proof="authored" data-by="ai:claude">Value</span>                                                                                                                                   | <span data-proof="authored" data-by="ai:claude">Why skipped</span>                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`100%`,</span> <span data-proof="authored" data-by="ai:claude">`50%`</span> <span data-proof="authored" data-by="ai:claude">etc.</span>        | <span data-proof="authored" data-by="ai:claude">Layout percentages</span>             |
| <span data-proof="authored" data-by="ai:claude">`auto`,</span> <span data-proof="authored" data-by="ai:claude">`inherit`,</span> <span data-proof="authored" data-by="ai:claude">`none`</span> | <span data-proof="authored" data-by="ai:claude">Layout keywords</span>                |
| <span data-proof="authored" data-by="ai:claude">`0`</span>                                                                                                                                     | <span data-proof="authored" data-by="ai:claude">Zero baseline (no hook needed)</span> |

<span data-proof="authored" data-by="ai:claude">Never replace layout values with arbitrary hooks — that's making the warning go away by introducing a bug.</span>

### <span data-proof="authored" data-by="ai:claude">Step 5: Always include a fallback</span>

<span data-proof="authored" data-by="ai:claude">Every replacement uses</span> <span data-proof="authored" data-by="ai:claude">`var(--slds-g-hook, originalValue)`. The fallback</span> **<span data-proof="authored" data-by="ai:claude">must be the exact original value</span>** <span data-proof="authored" data-by="ai:claude">from the source CSS — not a guess, not a different fallback.</span>

```css proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTA5LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
/* WRONG */
color: var(--slds-g-color-surface-1);

/* RIGHT */
color: var(--slds-g-color-surface-1, #ffffff);
```

<span data-proof="authored" data-by="ai:claude">This preserves rendering on legacy contexts that don't resolve SLDS 2 hooks.</span>

### <span data-proof="authored" data-by="ai:claude">Step 6: Class override pattern (the high-frequency miss)</span>

<span data-proof="authored" data-by="ai:claude">Class overrides are the rule devs forget the markup change for. Both files change:</span>

**<span data-proof="authored" data-by="ai:claude">CSS</span>** <span data-proof="authored" data-by="ai:claude">— rename</span> <span data-proof="authored" data-by="ai:claude">`.slds-*`</span> <span data-proof="authored" data-by="ai:claude">selector to</span> <span data-proof="authored" data-by="ai:claude">`{componentName}-{element}`</span> <span data-proof="authored" data-by="ai:claude">(camelCase):</span>

```css proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTMwLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
/* before */
.slds-button {
  background: blue;
}

/* after */
.myapp-button {
  background: var(--slds-g-color-accent-1, blue);
}
```

**<span data-proof="authored" data-by="ai:claude">Markup (`.html`</span>** **<span data-proof="authored" data-by="ai:claude">or</span>** **<span data-proof="authored" data-by="ai:claude">`.cmp`)</span>** <span data-proof="authored" data-by="ai:claude">— add the new class alongside the existing SLDS class:</span>

```html proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTAyLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
<!-- before -->
<button class="slds-button">

<!-- after -->
<button class="slds-button myapp-button">
```

<span data-proof="authored" data-by="ai:claude">Forgetting the markup change leaves the component looking unstyled. This is the #1 SLDS-2 uplift bug.</span>

### <span data-proof="authored" data-by="ai:claude">Step 7: Validate (Principle 2)</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6ODYsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
# Re-run linter — must return zero errors
npx @salesforce-ux/slds-linter@latest lint .
```

<span data-proof="authored" data-by="ai:claude">Then run any existing Jest tests to confirm rendering didn't regress visually:</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NDQsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
npm test --prefix force-app/main/default/lwc
```

***

## <span data-proof="authored" data-by="ai:claude">Output report</span>

```
SLDS 2 uplift: <component or directory>

Linter pre-fix:    {warnings} warnings, {errors} errors
After --fix:       {warnings} warnings, {errors} errors  (auto-fixed: {count})

Manual fixes by rule:
- slds/no-hardcoded-values-slds2:  {count}
- slds/lwc-token-to-slds-hook:      {count}
- slds/no-slds-class-overrides:     {count} (CSS+markup pairs)
- slds/no-deprecated-tokens-slds1:  {count}

Skipped (layout values): {count}

Linter final:      0 errors

Files changed:
- .css files: {list}
- .html / .cmp files: {list}

Tests:             {pass=N, fail=0}
```

<span data-proof="authored" data-by="ai:claude">Zero errors is the gate (Principle 1). If errors remain after fixes, do not declare done.</span>

***

## <span data-proof="authored" data-by="ai:claude">Hand off</span>

<span data-proof="authored" data-by="ai:claude">If the uplift surfaced a non-obvious hook choice (e.g., picking</span> <span data-proof="authored" data-by="ai:claude">`--slds-g-color-accent-3`</span> <span data-proof="authored" data-by="ai:claude">over</span> <span data-proof="authored" data-by="ai:claude">`surface-2`</span> <span data-proof="authored" data-by="ai:claude">because of a hover-state context), capture via</span> <span data-proof="authored" data-by="ai:claude">`/sf-compound`. SLDS 2 hook selection is exactly the kind of taste judgment Principle 5 demands future-you can re-derive (Principle 7).</span>

***

## <span data-proof="authored" data-by="ai:claude">Inspiration</span>

<span data-proof="authored" data-by="ai:claude">Adapted from</span> [<span data-proof="authored" data-by="ai:claude">`forcedotcom/afv-library/skills/uplifting-components-to-slds2`</span>](https://github.com/forcedotcom/afv-library/tree/main/skills/uplifting-components-to-slds2) <span data-proof="authored" data-by="ai:claude">(Apache-2.0). The upstream skill ships dedicated reference files per rule (`rule-no-hardcoded-values.md`,</span> <span data-proof="authored" data-by="ai:claude">`rule-lwc-token-to-slds-hook.md`,</span> <span data-proof="authored" data-by="ai:claude">`rule-no-slds-class-overrides.md`,</span> <span data-proof="authored" data-by="ai:claude">`rule-no-deprecated-tokens-slds1.md`) with exhaustive fix-vs-skip triage tables and decision trees for color hook selection. For the full color-context decision tree (when to choose surface vs accent vs on-accent vs container), consult the upstream references. This plugin's adaptation tightens around the principles framework.</span>