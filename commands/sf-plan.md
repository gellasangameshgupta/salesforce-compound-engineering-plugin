---
name: sf-plan
description: Research and design Salesforce features using parallel research agents
arguments:
  - name: feature
    description: Description of the feature to plan
    required: true
---

# <span data-proof="authored" data-by="ai:claude">/sf-plan</span>

<span data-proof="authored" data-by="ai:claude">You are planning a Salesforce implementation using parallel research agents. Your job is to research and design —</span> **<span data-proof="authored" data-by="ai:claude">NOT write code</span>**<span data-proof="authored" data-by="ai:claude">.</span>

## <span data-proof="authored" data-by="ai:claude">Goal</span>

<span data-proof="authored" data-by="ai:claude">Create a specification and technical design for:</span> <span data-proof="authored" data-by="ai:claude">`$ARGUMENTS.feature`</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 0: Check for Brainstorm</span>

<span data-proof="authored" data-by="ai:claude">Before starting, check if a relevant brainstorm exists:</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTEsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
ls -la docs/brainstorms/*.md 2>/dev/null | head -10
```

<span data-proof="authored" data-by="ai:claude">If a recent brainstorm matches this feature:</span>

1. <span data-proof="authored" data-by="ai:claude">Read it and extract key decisions.</span>
2. <span data-proof="authored" data-by="ai:claude">Skip idea refinement — use brainstorm decisions as input.</span>
3. <span data-proof="authored" data-by="ai:claude">Announce: "Found brainstorm from {date}: {topic}. Using as context."</span>

<span data-proof="authored" data-by="ai:claude">If no brainstorm found, proceed with research.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 1: Parallel Research (dispatch simultaneously)</span>

<span data-proof="authored" data-by="ai:claude">Launch these research agents</span> **<span data-proof="authored" data-by="ai:claude">in parallel</span>** <span data-proof="authored" data-by="ai:claude">using the Agent tool:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-learnings-researcher(feature_description) — Check institutional knowledge</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-repo-research-analyst(feature_description) — Understand project patterns</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-best-practices-researcher(feature_description) — Research best practices</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-framework-docs-researcher(feature_description) — Platform documentation</span>

### <span data-proof="authored" data-by="ai:claude">Conditional agents:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-git-history-analyzer(feature_description) — If modifying existing code</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 2: Consolidate Research</span>

<span data-proof="authored" data-by="ai:claude">After all research agents return:</span>

1. <span data-proof="authored" data-by="ai:claude">Document relevant file paths from repo research.</span>
2. <span data-proof="authored" data-by="ai:claude">Include institutional learnings from</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`.</span>
3. <span data-proof="authored" data-by="ai:claude">Note external documentation URLs and best practices.</span>
4. <span data-proof="authored" data-by="ai:claude">Capture CLAUDE.md conventions.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 3: Internal-First Discovery</span>

<span data-proof="authored" data-by="ai:claude">Prefer Salesforce-native capabilities:</span>

* <span data-proof="authored" data-by="ai:claude">Declarative automation (Flows, Validation Rules, Approval Processes)</span>

* <span data-proof="authored" data-by="ai:claude">Apex and platform events</span>

* <span data-proof="authored" data-by="ai:claude">LWC, standard UI patterns</span>

* <span data-proof="authored" data-by="ai:claude">Standard objects, fields, and metadata</span>

* <span data-proof="authored" data-by="ai:claude">Standard security model</span>

<span data-proof="authored" data-by="ai:claude">If external services are proposed, justify why native options are insufficient.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 4: Spec Flow Analysis</span>

<span data-proof="authored" data-by="ai:claude">Dispatch the spec flow analyzer to validate the design:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-spec-flow-analyzer(feature_spec, research_findings)</span>

<span data-proof="authored" data-by="ai:claude">Review the permutation matrix and address any gaps identified.</span>

***

## <span data-proof="authored" data-by="ai:claude">Critical Constraint</span>

**<span data-proof="authored" data-by="ai:claude">DO NOT WRITE CODE.</span>** <span data-proof="authored" data-by="ai:claude">This command produces:</span>

* <span data-proof="authored" data-by="ai:claude">Architecture decisions (which components, how they connect)</span>

* <span data-proof="authored" data-by="ai:claude">Method signatures (names, parameters, return types)</span>

* <span data-proof="authored" data-by="ai:claude">Configuration specifications (object names, field names, Flow structure)</span>

* <span data-proof="authored" data-by="ai:claude">Task lists for implementation</span>

<span data-proof="authored" data-by="ai:claude">Code implementation happens in</span> <span data-proof="authored" data-by="ai:claude">`/sf-work`.</span>

***

## <span data-proof="authored" data-by="ai:claude">Available Resources</span>

### <span data-proof="authored" data-by="ai:claude">Agents (Expertise)</span>

<span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`agents/index.md`</span> <span data-proof="authored" data-by="ai:claude">to route to relevant review agents.</span>

### <span data-proof="authored" data-by="ai:claude">Skills (Domain Knowledge)</span>

<span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/index.md`</span> <span data-proof="authored" data-by="ai:claude">to route to relevant skills.</span>

### <span data-proof="authored" data-by="ai:claude">Existing Codebase</span>

<span data-proof="authored" data-by="ai:claude">Explore the codebase to understand existing patterns.</span>

***

## <span data-proof="authored" data-by="ai:claude">Output</span>

<span data-proof="authored" data-by="ai:claude">Save plan under</span> <span data-proof="authored" data-by="ai:claude">`docs/plans/`</span> <span data-proof="authored" data-by="ai:claude">with format:
`docs/plans/YYYY-MM-DD-<type>-<feature-slug>-plan.md`</span>

<span data-proof="authored" data-by="ai:claude">Include:</span>

* <span data-proof="authored" data-by="ai:claude">`spec.md`</span> <span data-proof="authored" data-by="ai:claude">section (business requirements, acceptance criteria, constraints)</span>

* <span data-proof="authored" data-by="ai:claude">`plan.md`</span> <span data-proof="authored" data-by="ai:claude">section (components, architecture, design decisions, limits, security)</span>

* <span data-proof="authored" data-by="ai:claude">`tasks.md`</span> <span data-proof="authored" data-by="ai:claude">section (implementation, testing, deployment checklist)</span>

***

## <span data-proof="authored" data-by="ai:claude">After Planning</span>

<span data-proof="authored" data-by="ai:claude">When plan is complete:</span>

```
Plan created: docs/plans/YYYY-MM-DD-<type>-<feature>-plan.md

Research agents dispatched: {count}
Institutional learnings applied: {count}
Spec flow gaps identified: {count}

Next steps:
- /sf-deepen docs/plans/<plan>.md — Enhance with deeper research
- /sf-work docs/plans/<plan>.md — Begin implementation
```