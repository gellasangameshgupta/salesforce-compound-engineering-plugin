---
name: sf-deepen
description: "Deepen an existing Salesforce plan by dispatching parallel research agents per section, adding governor-limit analysis, sharing-model implications, security review, and platform-specific implementation details. Use when the user says 'deepen this plan', 'add depth to this plan', 'research more for this plan', 'strengthen the plan', or wants a second-pass enhancement on an existing Salesforce plan."
argument-hint: "[plan file path under docs/plans/]"
---

# /sf-deepen

> **Persona dispatch (V3.1, agentless).** Where this skill says "dispatch research agents", they are *personas* — prompt assets under `references/personas/<name>.md` (research personas referenced from `../sf-plan/references/personas/`), not registered agents. Run each as an **isolated subagent** (Task tool, general-purpose subagent, persona file contents as instructions): parallel on Claude Code, inline-in-sequence on harnesses without subagents.

> **Principles enforced:** 4 (spec is the artifact), 2 (verifiability). See `PRINCIPLES.md`.

## Copy-paste-to-agent

```
Tighten an existing Salesforce plan into a load-bearing spec. This is NOT a research dump
— it is a spec-tightening pass. For each major plan section, dispatch the appropriate
research agent in parallel, then merge findings into the plan AS spec constraints (governor
caps, sharing-model implications, order-of-execution placement, API-version dependencies),
not as appended prose. If the plan's Verification Strategy from /sf-plan is incomplete or
hand-waved, fill the five fields concretely before returning.
```

## Relationship to /sf-plan

<span data-proof="authored" data-by="ai:claude">`/sf-plan`</span> <span data-proof="authored" data-by="ai:claude">produces the spec.</span> <span data-proof="authored" data-by="ai:claude">`/sf-deepen`</span> <span data-proof="authored" data-by="ai:claude">tightens it. The split is:</span>

* **<span data-proof="authored" data-by="ai:claude">`/sf-plan`</span>** <span data-proof="authored" data-by="ai:claude">— runs once, produces the initial spec/plan/verification/tasks artifacts via parallel research.</span>

* **<span data-proof="authored" data-by="ai:claude">`/sf-deepen`</span>** <span data-proof="authored" data-by="ai:claude">— runs against an existing plan file, adds Salesforce-specific depth (governor analysis, sharing impact, order-of-execution placement, known issues) and concretes any vague verification fields.</span>

<span data-proof="authored" data-by="ai:claude">If you just created a plan with</span> <span data-proof="authored" data-by="ai:claude">`/sf-plan`</span> <span data-proof="authored" data-by="ai:claude">and want it deeper, run</span> <span data-proof="authored" data-by="ai:claude">`/sf-deepen <plan_path>`. Don't run</span> <span data-proof="authored" data-by="ai:claude">`/sf-plan`</span> <span data-proof="authored" data-by="ai:claude">twice on the same feature.</span>

<span data-proof="authored" data-by="ai:claude"><feature_description>
#$ARGUMENTS
</feature_description></span>

## <span data-proof="authored" data-by="ai:claude">Interaction Method</span>

<span data-proof="authored" data-by="ai:claude">When asking the user a question, use the platform's blocking question tool:</span> <span data-proof="authored" data-by="ai:claude">`AskUserQuestion`</span> <span data-proof="authored" data-by="ai:claude">in Claude Code (call</span> <span data-proof="authored" data-by="ai:claude">`ToolSearch`</span> <span data-proof="authored" data-by="ai:claude">with</span> <span data-proof="authored" data-by="ai:claude">`select:AskUserQuestion`</span> <span data-proof="authored" data-by="ai:claude">first if its schema isn't loaded),</span> <span data-proof="authored" data-by="ai:claude">`request_user_input`</span> <span data-proof="authored" data-by="ai:claude">in Codex,</span> <span data-proof="authored" data-by="ai:claude">`ask_user`</span> <span data-proof="authored" data-by="ai:claude">in Gemini. Fall back to numbered options in chat only when no blocking tool exists in the harness or the call errors. Never silently skip the question.</span>

<span data-proof="authored" data-by="ai:claude">Ask one question at a time. Prefer a concise single-select choice when natural options exist.</span>

<span data-proof="authored" data-by="ai:claude">You enhance an existing plan by dispatching parallel research personas for each section, adding depth, best practices, and Salesforce-specific implementation details.</span>

## <span data-proof="authored" data-by="ai:claude">Goal</span>

<span data-proof="authored" data-by="ai:claude">Deepen the plan at:</span> <span data-proof="authored" data-by="ai:claude">`$ARGUMENTS.plan_path`</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 1: Parse Plan Sections</span>

<span data-proof="authored" data-by="ai:claude">Read the plan file and identify all major sections that can benefit from deeper research:</span>

* <span data-proof="authored" data-by="ai:claude">Architecture decisions</span>

* <span data-proof="authored" data-by="ai:claude">Implementation phases</span>

* <span data-proof="authored" data-by="ai:claude">Technical approach</span>

* <span data-proof="authored" data-by="ai:claude">Security considerations</span>

* <span data-proof="authored" data-by="ai:claude">Governor limit implications</span>

* <span data-proof="authored" data-by="ai:claude">Testing strategy</span>

* <span data-proof="authored" data-by="ai:claude">Deployment plan</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 2: Dispatch Parallel Research Per Section</span>

<span data-proof="authored" data-by="ai:claude">For each section, launch the appropriate research agent</span> **<span data-proof="authored" data-by="ai:claude">in parallel</span>**<span data-proof="authored" data-by="ai:claude">:</span>

### <span data-proof="authored" data-by="ai:claude">Architecture sections:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-best-practices-researcher(architecture_context)</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-framework-docs-researcher(architecture_context)</span>

### <span data-proof="authored" data-by="ai:claude">Governor Limit sections:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-learnings-researcher("governor limits" + feature_context)</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-framework-docs-researcher("governor limits" + specific_operations)</span>

### <span data-proof="authored" data-by="ai:claude">Security sections:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-best-practices-researcher("salesforce security" + feature_context)</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-learnings-researcher("security" + feature_context)</span>

### <span data-proof="authored" data-by="ai:claude">Integration sections:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-framework-docs-researcher(integration_apis)</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-best-practices-researcher(integration_pattern)</span>

### <span data-proof="authored" data-by="ai:claude">Testing sections:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-best-practices-researcher("salesforce testing" + feature_context)</span>

### <span data-proof="authored" data-by="ai:claude">Deployment sections:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-best-practices-researcher("salesforce deployment" + component_types)</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 3: Merge Results</span>

<span data-proof="authored" data-by="ai:claude">For each section:</span>

1. <span data-proof="authored" data-by="ai:claude">Read the research agent's findings.</span>
2. <span data-proof="authored" data-by="ai:claude">Integrate relevant best practices into the plan.</span>
3. <span data-proof="authored" data-by="ai:claude">Add specific code examples or configuration details where helpful.</span>
4. <span data-proof="authored" data-by="ai:claude">Flag any conflicts between the plan and best practices.</span>
5. <span data-proof="authored" data-by="ai:claude">Add source references (URLs, documentation links).</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 4: Add Salesforce-Specific Depth</span>

<span data-proof="authored" data-by="ai:claude">Enhance the plan with:</span>

* **<span data-proof="authored" data-by="ai:claude">Governor Limit Analysis</span>**<span data-proof="authored" data-by="ai:claude">: Specific limit calculations for the proposed design</span>

* **<span data-proof="authored" data-by="ai:claude">Sharing Model Impact</span>**<span data-proof="authored" data-by="ai:claude">: How the feature interacts with OWD and sharing rules</span>

* **<span data-proof="authored" data-by="ai:claude">Order of Execution</span>**<span data-proof="authored" data-by="ai:claude">: Where the feature sits in Salesforce's order of execution</span>

* **<span data-proof="authored" data-by="ai:claude">API Version Considerations</span>**<span data-proof="authored" data-by="ai:claude">: Features that depend on specific API versions</span>

* **<span data-proof="authored" data-by="ai:claude">Known Issues</span>**<span data-proof="authored" data-by="ai:claude">: Any relevant Salesforce known issues</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 5: Update Plan File</span>

<span data-proof="authored" data-by="ai:claude">Write the enhanced plan back to the same file path, preserving the original structure but adding:</span>

* <span data-proof="authored" data-by="ai:claude">`### Deep Research Notes`</span> <span data-proof="authored" data-by="ai:claude">subsections under each major section</span>

* <span data-proof="authored" data-by="ai:claude">Updated acceptance criteria based on research findings</span>

* <span data-proof="authored" data-by="ai:claude">New risk items discovered during research</span>

* <span data-proof="authored" data-by="ai:claude">Source references at the bottom</span>

***

## <span data-proof="authored" data-by="ai:claude">Output</span>

```
Plan deepened: {plan_path}

Research personas dispatched: {count}
Sections enhanced: {count}
New risks identified: {count}
Best practices added: {count}
Sources referenced: {count}

Next:
- /sf-work {plan_path} — Begin implementation
- /sf-review — Review the enhanced plan
```