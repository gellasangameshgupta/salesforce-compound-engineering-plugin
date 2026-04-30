---
name: sf-work
description: "Execute work efficiently against a Salesforce plan or feature description while maintaining quality and finishing complete features. Use when implementing Apex classes, LWC components, Flow automation, integrations, or any planned Salesforce work. Includes a Salesforce-aware system-wide test check (trigger contexts, bulkification, governor limits, sharing scenarios, mock callouts). Trigger phrases: 'work on this plan', 'implement this Salesforce feature', 'build out this Apex', 'execute this trigger plan', 'ship this LWC'."
argument-hint: "[plan file path under docs/plans/, or feature description for bare-prompt work]"
---

# /sf-work

> **Principles enforced:** 1 (preserve the quality ceiling), 2 (verifiability), 3 (jagged intelligence). See `PRINCIPLES.md`.

## Copy-paste-to-agent

```
Implement a Salesforce feature against an existing plan. Before writing code, dispatch
sf-learnings-researcher and sf-repo-research-analyst in parallel. Then write code AND tests
together — verification is not a follow-up. Before declaring complete, answer all five
System-Wide Test Check questions: trigger contexts, bulk at 200+, governor limits, sharing,
integration mocks. If the plan has a Verification Strategy section, the implementation must
satisfy every field; do not relax it.
```

<feature_description>
#$ARGUMENTS
</feature_description>

## <span data-proof="authored" data-by="ai:claude">Interaction Method</span>

<span data-proof="authored" data-by="ai:claude">When asking the user a question, use the platform's blocking question tool:</span> <span data-proof="authored" data-by="ai:claude">`AskUserQuestion`</span> <span data-proof="authored" data-by="ai:claude">in Claude Code (call</span> <span data-proof="authored" data-by="ai:claude">`ToolSearch`</span> <span data-proof="authored" data-by="ai:claude">with</span> <span data-proof="authored" data-by="ai:claude">`select:AskUserQuestion`</span> <span data-proof="authored" data-by="ai:claude">first if its schema isn't loaded),</span> <span data-proof="authored" data-by="ai:claude">`request_user_input`</span> <span data-proof="authored" data-by="ai:claude">in Codex,</span> <span data-proof="authored" data-by="ai:claude">`ask_user`</span> <span data-proof="authored" data-by="ai:claude">in Gemini. Fall back to numbered options in chat only when no blocking tool exists in the harness or the call errors. Never silently skip the question.</span>

<span data-proof="authored" data-by="ai:claude">Ask one question at a time. Prefer a concise single-select choice when natural options exist.</span>

<span data-proof="authored" data-by="ai:claude">You are implementing a Salesforce feature with parallel agent support and built-in quality checks.</span>

## <span data-proof="authored" data-by="ai:claude">Goal</span>

<span data-proof="authored" data-by="ai:claude">Implement the feature described in:</span> <span data-proof="authored" data-by="ai:claude">`$ARGUMENTS.plan`</span>

<span data-proof="authored" data-by="ai:claude">If a plan file path is provided, read it first. If a description is provided, implement directly.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 0: Pre-Implementation Research (parallel)</span>

<span data-proof="authored" data-by="ai:claude">Before writing code, dispatch these agents</span> **<span data-proof="authored" data-by="ai:claude">in parallel</span>**<span data-proof="authored" data-by="ai:claude">:</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-learnings-researcher(feature_description) — Check for relevant past solutions</span>

* <span data-proof="authored" data-by="ai:claude">Task sf-repo-research-analyst(feature_description) — Understand existing patterns</span>

<span data-proof="authored" data-by="ai:claude">Apply findings to inform implementation approach.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 1: Route via Indexes</span>

<span data-proof="authored" data-by="ai:claude">Classify the implementation, then route:</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`agents/index.md`</span> <span data-proof="authored" data-by="ai:claude">to decide applicable agent categories</span>

* <span data-proof="authored" data-by="ai:claude">Read</span> <span data-proof="authored" data-by="ai:claude">`skills/index.md`</span> <span data-proof="authored" data-by="ai:claude">to decide applicable skills</span>

* <span data-proof="authored" data-by="ai:claude">Include</span> <span data-proof="authored" data-by="ai:claude">`skills/governor-limits/SKILL.md`</span> <span data-proof="authored" data-by="ai:claude">for limit-sensitive backend work</span>

* For metadata or code generation, dispatch the matching action-shaped skill: `/apex-generate` (Apex class + tests), `/flow-generate` (Flow XML via MCP pipeline), `/validation-rule-generate`, `/apex-trigger-refactor`, `/slds2-uplift` (LWC), `/metadata-generate` (object / field / app / tab / listview / lightning-type), `/lightning-page-generate` (FlexiPage or full LEX app), `/permission-set-generate`. Reference skills (`apex-patterns`, `flow-patterns`, `lwc-patterns`, etc.) describe the shape; generation skills produce the artifact.

***

## <span data-proof="authored" data-by="ai:claude">Step 2: Internal-First Implementation</span>

<span data-proof="authored" data-by="ai:claude">Use built-in platform features wherever possible:</span>

* <span data-proof="authored" data-by="ai:claude">Flows, Validation Rules, Approval Processes</span>

* <span data-proof="authored" data-by="ai:claude">Apex, Platform Events, and standard metadata</span>

* <span data-proof="authored" data-by="ai:claude">LWC, Aura, Visualforce for UI</span>

* <span data-proof="authored" data-by="ai:claude">Standard security model (CRUD/FLS, sharing)</span>

<span data-proof="authored" data-by="ai:claude">If external services are needed, justify explicitly.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 3: Implementation Standards</span>

### <span data-proof="authored" data-by="ai:claude">Apex Code</span>

* <span data-proof="authored" data-by="ai:claude">Follow existing trigger handler pattern in codebase</span>

* <span data-proof="authored" data-by="ai:claude">Bulkify all operations (handle 200+ records)</span>

* <span data-proof="authored" data-by="ai:claude">CRUD/FLS enforcement on all database operations</span>

* <span data-proof="authored" data-by="ai:claude">Proper exception handling</span>

* <span data-proof="authored" data-by="ai:claude">Meaningful method and variable names</span>

### <span data-proof="authored" data-by="ai:claude">Flows</span>

* <span data-proof="authored" data-by="ai:claude">Clear element naming (e.g.,</span> <span data-proof="authored" data-by="ai:claude">`Get_Account_Details`,</span> <span data-proof="authored" data-by="ai:claude">`Decision_Check_Status`)</span>

* <span data-proof="authored" data-by="ai:claude">Entry conditions to prevent unnecessary execution</span>

* <span data-proof="authored" data-by="ai:claude">Bulkified operations (no DML/SOQL in loops)</span>

* <span data-proof="authored" data-by="ai:claude">Fault handling for error scenarios</span>

### <span data-proof="authored" data-by="ai:claude">LWC</span>

* <span data-proof="authored" data-by="ai:claude">Component naming follows existing conventions</span>

* <span data-proof="authored" data-by="ai:claude">Proper error handling and loading states</span>

* <span data-proof="authored" data-by="ai:claude">Accessible markup (ARIA, keyboard navigation)</span>

* <span data-proof="authored" data-by="ai:claude">Efficient wire/imperative Apex calls</span>

### <span data-proof="authored" data-by="ai:claude">Test Classes</span>

* <span data-proof="authored" data-by="ai:claude">Minimum 90% code coverage target</span>

* <span data-proof="authored" data-by="ai:claude">Bulk tests (200+ records)</span>

* <span data-proof="authored" data-by="ai:claude">Positive and negative scenarios</span>

* <span data-proof="authored" data-by="ai:claude">Test as different user contexts when relevant</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 4: System-Wide Test Check</span>

**<span data-proof="authored" data-by="ai:claude">Before marking implementation complete, answer these 5 questions:</span>**

1. **<span data-proof="authored" data-by="ai:claude">Trigger Fire Check</span>**<span data-proof="authored" data-by="ai:claude">: What triggers fire on the affected objects? Are all contexts (insert/update/delete/undelete) handled correctly?</span>

2. **<span data-proof="authored" data-by="ai:claude">Bulk Test Check</span>**<span data-proof="authored" data-by="ai:claude">: Are bulk tests included that process 200+ records? Do they verify behavior at scale?</span>

3. **<span data-proof="authored" data-by="ai:claude">Governor Limit Test</span>**<span data-proof="authored" data-by="ai:claude">: Are governor limits tested? Specifically SOQL 101, DML 150, CPU timeout scenarios?</span>

4. **<span data-proof="authored" data-by="ai:claude">Sharing Scenario Check</span>**<span data-proof="authored" data-by="ai:claude">: Are sharing scenarios covered? Does the code work correctly under</span> <span data-proof="authored" data-by="ai:claude">`with sharing`</span> <span data-proof="authored" data-by="ai:claude">and</span> <span data-proof="authored" data-by="ai:claude">`without sharing`</span> <span data-proof="authored" data-by="ai:claude">contexts?</span>

5. **<span data-proof="authored" data-by="ai:claude">Integration Mock Check</span>**<span data-proof="authored" data-by="ai:claude">: Are all integration points (callouts, platform events) properly mocked in tests?</span>

<span data-proof="authored" data-by="ai:claude">If any answer is "no", add the missing test before proceeding.</span>

***

## <span data-proof="authored" data-by="ai:claude">Step 5: Incremental Commits</span>

<span data-proof="authored" data-by="ai:claude">Make small, focused commits as you go:</span>

* <span data-proof="authored" data-by="ai:claude">One commit per logical unit of work</span>

* <span data-proof="authored" data-by="ai:claude">Clear commit messages describing the change</span>

* <span data-proof="authored" data-by="ai:claude">Don't batch all changes into one commit</span>

***

## <span data-proof="authored" data-by="ai:claude">Output</span>

<span data-proof="authored" data-by="ai:claude">Create/modify only the required Salesforce files and list changed files in your response.</span>

***

## <span data-proof="authored" data-by="ai:claude">After Implementation</span>

<span data-proof="authored" data-by="ai:claude">When implementation is complete:</span>

```
Implementation complete.

Files created/modified:
- [list of files]

System-Wide Test Check:
✅ Trigger contexts: [handled/not applicable]
✅ Bulk tests: [included/not applicable]
✅ Governor limits: [tested/not applicable]
✅ Sharing scenarios: [covered/not applicable]
✅ Integration mocks: [mocked/not applicable]

Next: /sf-review
```