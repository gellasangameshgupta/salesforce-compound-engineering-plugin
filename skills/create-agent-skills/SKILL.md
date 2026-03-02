# <span data-proof="authored" data-by="ai:claude">Create Agent Skills</span>

<span data-proof="authored" data-by="ai:claude">Guide for creating new agents and skills to extend the SF Compound Engineering Plugin.</span>

## <span data-proof="authored" data-by="ai:claude">Agent Structure</span>

<span data-proof="authored" data-by="ai:claude">Agents live in</span> <span data-proof="authored" data-by="ai:claude">`agents/{category}/`</span> <span data-proof="authored" data-by="ai:claude">and follow this template:</span>

```markdown proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MzcxLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
---
name: {agent-name}
description: {One-line description of what the agent does}
model: {haiku|sonnet|opus}
scope: {APEX_ONLY|AUTOMATION_ONLY|LWC_ONLY|INTEGRATION_ONLY|UNIVERSAL}
---

# {Agent Title}

{Role description — who you are and what you do}

## Your Process

### Step 1: {First action}
{Description}

### Step 2: {Second action}
{Description}

## Output Format

```

<span data-proof="authored" data-by="ai:claude">{Expected output structure}</span>

```

## When to Use

{When this agent should be dispatched}
```

### <span data-proof="authored" data-by="ai:claude">Agent Categories</span>

| <span data-proof="authored" data-by="ai:claude">Category</span>     | <span data-proof="authored" data-by="ai:claude">Directory</span>              | <span data-proof="authored" data-by="ai:claude">For</span>                                |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">apex</span>         | <span data-proof="authored" data-by="ai:claude">`agents/apex/`</span>         | <span data-proof="authored" data-by="ai:claude">Apex code review and patterns</span>      |
| <span data-proof="authored" data-by="ai:claude">automation</span>   | <span data-proof="authored" data-by="ai:claude">`agents/automation/`</span>   | <span data-proof="authored" data-by="ai:claude">Flow and declarative automation</span>    |
| <span data-proof="authored" data-by="ai:claude">lwc</span>          | <span data-proof="authored" data-by="ai:claude">`agents/lwc/`</span>          | <span data-proof="authored" data-by="ai:claude">Lightning Web Components</span>           |
| <span data-proof="authored" data-by="ai:claude">integration</span>  | <span data-proof="authored" data-by="ai:claude">`agents/integration/`</span>  | <span data-proof="authored" data-by="ai:claude">APIs, callouts, events</span>             |
| <span data-proof="authored" data-by="ai:claude">architecture</span> | <span data-proof="authored" data-by="ai:claude">`agents/architecture/`</span> | <span data-proof="authored" data-by="ai:claude">Cross-cutting concerns</span>             |
| <span data-proof="authored" data-by="ai:claude">research</span>     | <span data-proof="authored" data-by="ai:claude">`agents/research/`</span>     | <span data-proof="authored" data-by="ai:claude">Information gathering and analysis</span> |
| <span data-proof="authored" data-by="ai:claude">workflow</span>     | <span data-proof="authored" data-by="ai:claude">`agents/workflow/`</span>     | <span data-proof="authored" data-by="ai:claude">Process automation and quality</span>     |

### <span data-proof="authored" data-by="ai:claude">Model Selection</span>

| <span data-proof="authored" data-by="ai:claude">Model</span>  | <span data-proof="authored" data-by="ai:claude">Use For</span>                                        | <span data-proof="authored" data-by="ai:claude">Speed</span>   | <span data-proof="authored" data-by="ai:claude">Depth</span>   |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">haiku</span>  | <span data-proof="authored" data-by="ai:claude">Fast searches, simple checks, pattern matching</span> | <span data-proof="authored" data-by="ai:claude">Fastest</span> | <span data-proof="authored" data-by="ai:claude">Basic</span>   |
| <span data-proof="authored" data-by="ai:claude">sonnet</span> | <span data-proof="authored" data-by="ai:claude">Deep analysis, research, complex review</span>        | <span data-proof="authored" data-by="ai:claude">Medium</span>  | <span data-proof="authored" data-by="ai:claude">Deep</span>    |
| <span data-proof="authored" data-by="ai:claude">opus</span>   | <span data-proof="authored" data-by="ai:claude">Critical decisions, architectural review</span>       | <span data-proof="authored" data-by="ai:claude">Slowest</span> | <span data-proof="authored" data-by="ai:claude">Deepest</span> |

## <span data-proof="authored" data-by="ai:claude">Skill Structure</span>

<span data-proof="authored" data-by="ai:claude">Skills live in</span> <span data-proof="authored" data-by="ai:claude">`skills/{skill-name}/`</span> <span data-proof="authored" data-by="ai:claude">with a</span> <span data-proof="authored" data-by="ai:claude">`SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">file:</span>

```markdown proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTU4LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
# {Skill Name}

{Description of what knowledge this skill provides}

## {Section 1}

{Content — patterns, reference, examples}

## {Section 2}

{More content}
```

### <span data-proof="authored" data-by="ai:claude">Skill Design Principles</span>

1. **<span data-proof="authored" data-by="ai:claude">Reference, not instructions</span>**<span data-proof="authored" data-by="ai:claude">: Skills provide knowledge, agents use that knowledge</span>
2. **<span data-proof="authored" data-by="ai:claude">Scoped</span>**<span data-proof="authored" data-by="ai:claude">: Each skill has a clear scope (APEX_ONLY, UNIVERSAL, etc.)</span>
3. **<span data-proof="authored" data-by="ai:claude">Searchable</span>**<span data-proof="authored" data-by="ai:claude">: Use clear headings and code examples</span>
4. **<span data-proof="authored" data-by="ai:claude">Concise</span>**<span data-proof="authored" data-by="ai:claude">: Include only what's needed for decision-making</span>

## <span data-proof="authored" data-by="ai:claude">After Creating</span>

1. **<span data-proof="authored" data-by="ai:claude">Update</span>** **<span data-proof="authored" data-by="ai:claude">`agents/index.md`</span>**<span data-proof="authored" data-by="ai:claude">: Add the new agent to the routing table</span>
2. **<span data-proof="authored" data-by="ai:claude">Update</span>** **<span data-proof="authored" data-by="ai:claude">`skills/index.md`</span>**<span data-proof="authored" data-by="ai:claude">: Add the new skill to the routing table</span>
3. **<span data-proof="authored" data-by="ai:claude">Update</span>** **<span data-proof="authored" data-by="ai:claude">`plugin.json`</span>**<span data-proof="authored" data-by="ai:claude">: Increment the component counts</span>
4. **<span data-proof="authored" data-by="ai:claude">Test</span>**<span data-proof="authored" data-by="ai:claude">: Verify the agent/skill is discovered and used correctly</span>

## <span data-proof="authored" data-by="ai:claude">Naming Conventions</span>

* **<span data-proof="authored" data-by="ai:claude">Agents</span>**<span data-proof="authored" data-by="ai:claude">:</span> <span data-proof="authored" data-by="ai:claude">`{domain}-{role}.md`</span> <span data-proof="authored" data-by="ai:claude">(e.g.,</span> <span data-proof="authored" data-by="ai:claude">`apex-governor-guardian.md`)</span>

* **<span data-proof="authored" data-by="ai:claude">Skills</span>**<span data-proof="authored" data-by="ai:claude">:</span> <span data-proof="authored" data-by="ai:claude">`{topic}/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">(e.g.,</span> <span data-proof="authored" data-by="ai:claude">`governor-limits/SKILL.md`)</span>

* **<span data-proof="authored" data-by="ai:claude">Commands</span>**<span data-proof="authored" data-by="ai:claude">:</span> <span data-proof="authored" data-by="ai:claude">`sf-{action}.md`</span> <span data-proof="authored" data-by="ai:claude">(e.g.,</span> <span data-proof="authored" data-by="ai:claude">`sf-brainstorm.md`)</span>

* <span data-proof="authored" data-by="ai:claude">Use kebab-case for all file and directory names</span>

* <span data-proof="authored" data-by="ai:claude">Prefix Salesforce-specific agents with</span> <span data-proof="authored" data-by="ai:claude">`sf-`</span> <span data-proof="authored" data-by="ai:claude">in the research/workflow categories</span>