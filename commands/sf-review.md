---
name: sf-review
description: Multi-agent Salesforce code review with 23 parallel specialist subagents
arguments:
  - name: target
    description: File path, directory, or PR number to review (defaults to uncommitted changes)
    required: false
---

# /sf-review

Perform comprehensive code review using 23 parallel subagents - each checking from a different Salesforce specialist perspective.

## Instructions

When this command is invoked, you MUST follow these steps exactly:

### Step 1: Determine Review Target

```
IF $ARGUMENTS.target is empty:
    Run: git diff --name-only (review uncommitted changes)
ELSE IF $ARGUMENTS.target is a number:
    Fetch PR #[number] files
ELSE:
    Review files at $ARGUMENTS.target path
```

Announce: "Starting /sf-review for: [target description]"

### Step 2: Classify Files

Read the files and classify them:
- **Apex files**: *.cls, *.trigger
- **LWC files**: *.js, *.html in lwc/ folders
- **Flow files**: *.flow-meta.xml
- **Object files**: *.object-meta.xml, *.field-meta.xml
- **Test files**: *Test.cls

Display:
```
Files to Review:
  • Apex: X files
  • LWC: Y files
  • Flows: Z files
  • Tests: W files
```

### Step 3: Deploy Review Subagents (PARALLEL)

**IMMEDIATELY spawn ALL relevant subagents in parallel using the Task tool.**

Based on files found, call Task tool multiple times in a SINGLE message:

<subagent_deployment>
FOR APEX FILES - Deploy these 6 subagents:

1. Task tool call:
   - description: "Review governor limits"
   - subagent_type: "general-purpose"
   - prompt: "You are the Governor Guardian agent. Read .claude/agents/apex/apex-governor-guardian.md for your checklist. Review these Apex files for governor limit issues: [FILE_LIST]. Check for: SOQL in loops, DML in loops, CPU-intensive operations, heap issues. Return JSON: {agent: 'governor-guardian', findings: [{file, line, severity, issue, fix}]}"

2. Task tool call:
   - description: "Review security"
   - subagent_type: "general-purpose"
   - prompt: "You are the Security Sentinel agent. Read .claude/agents/apex/apex-security-sentinel.md for your checklist. Review these Apex files: [FILE_LIST]. Check for: CRUD/FLS enforcement, SOQL injection, hardcoded credentials, sharing keywords. Return JSON: {agent: 'security-sentinel', findings: [{file, line, severity, issue, fix}]}"

3. Task tool call:
   - description: "Review bulkification"
   - subagent_type: "general-purpose"
   - prompt: "You are the Bulkification Reviewer agent. Read .claude/agents/apex/apex-bulkification-reviewer.md. Review these Apex files: [FILE_LIST]. Check for: Single record operations, collections usage, Trigger.new handling. Return JSON: {agent: 'bulkification-reviewer', findings: [{file, line, severity, issue, fix}]}"

4. Task tool call:
   - description: "Review triggers"
   - subagent_type: "general-purpose"
   - prompt: "You are the Trigger Architect agent. Read .claude/agents/apex/apex-trigger-architect.md. Review these trigger files: [TRIGGER_FILES]. Check for: One trigger per object, handler pattern, recursion prevention. Return JSON: {agent: 'trigger-architect', findings: [{file, line, severity, issue, fix}]}"

5. Task tool call:
   - description: "Review test quality"
   - subagent_type: "general-purpose"
   - prompt: "You are the Test Coverage Analyst agent. Read .claude/agents/apex/apex-test-coverage-analyst.md. Review these test files: [TEST_FILES]. Check for: Bulk testing, assertions quality, System.runAs usage, test data isolation. Return JSON: {agent: 'test-coverage-analyst', findings: [{file, line, severity, issue, fix}]}"

6. Task tool call:
   - description: "Review error handling"
   - subagent_type: "general-purpose"
   - prompt: "You are the Exception Handler agent. Read .claude/agents/apex/apex-exception-handler.md. Review these Apex files: [FILE_LIST]. Check for: Try-catch blocks, custom exceptions, error logging. Return JSON: {agent: 'exception-handler', findings: [{file, line, severity, issue, fix}]}"

FOR LWC FILES - Deploy these 5 subagents:

7. Task tool call:
   - description: "Review LWC performance"
   - subagent_type: "general-purpose"
   - prompt: "You are the LWC Performance Oracle agent. Read .claude/agents/lwc/lwc-performance-oracle.md. Review these LWC files: [LWC_FILES]. Check for: Wire vs imperative, unnecessary re-renders, large DOM operations. Return JSON: {agent: 'lwc-performance-oracle', findings: [{file, line, severity, issue, fix}]}"

8. Task tool call:
   - description: "Review LWC security"
   - subagent_type: "general-purpose"
   - prompt: "You are the LWC Security Reviewer agent. Read .claude/agents/lwc/lwc-security-reviewer.md. Review these LWC files: [LWC_FILES]. Check for: innerHTML/XSS, CSP compliance, secure data handling. Return JSON: {agent: 'lwc-security-reviewer', findings: [{file, line, severity, issue, fix}]}"

9. Task tool call:
   - description: "Review LWC accessibility"
   - subagent_type: "general-purpose"
   - prompt: "You are the LWC Accessibility Guardian agent. Read .claude/agents/lwc/lwc-accessibility-guardian.md. Review these LWC files: [LWC_FILES]. Check for: ARIA attributes, keyboard navigation, focus management. Return JSON: {agent: 'lwc-accessibility-guardian', findings: [{file, line, severity, issue, fix}]}"

10. Task tool call:
    - description: "Review LWC architecture"
    - subagent_type: "general-purpose"
    - prompt: "You are the LWC Architecture Strategist agent. Read .claude/agents/lwc/lwc-architecture-strategist.md. Review these LWC files: [LWC_FILES]. Check for: Component hierarchy, event communication, state management. Return JSON: {agent: 'lwc-architecture-strategist', findings: [{file, line, severity, issue, fix}]}"

11. Task tool call:
    - description: "Check Aura migration"
    - subagent_type: "general-purpose"
    - prompt: "You are the Aura Migration Advisor agent. Read .claude/agents/lwc/aura-migration-advisor.md. Review any Aura files: [AURA_FILES]. Identify LWC migration candidates. Return JSON: {agent: 'aura-migration-advisor', findings: [{file, line, severity, issue, fix}]}"

FOR FLOW FILES - Deploy these 4 subagents:

12. Task tool call:
    - description: "Review flow complexity"
    - subagent_type: "general-purpose"
    - prompt: "You are the Flow Complexity Analyzer agent. Read .claude/agents/automation/flow-complexity-analyzer.md. Review these Flow files: [FLOW_FILES]. Check for: Loop complexity, decision depth, subflow usage. Return JSON: {agent: 'flow-complexity-analyzer', findings: [{file, line, severity, issue, fix}]}"

13. Task tool call:
    - description: "Review flow governor limits"
    - subagent_type: "general-purpose"
    - prompt: "You are the Flow Governor Monitor agent. Read .claude/agents/automation/flow-governor-monitor.md. Review these Flow files: [FLOW_FILES]. Check for: DML in loops, SOQL in loops, bulkification. Return JSON: {agent: 'flow-governor-monitor', findings: [{file, line, severity, issue, fix}]}"

14. Task tool call:
    - description: "Review automation strategy"
    - subagent_type: "general-purpose"
    - prompt: "You are the Process Automation Strategist agent. Read .claude/agents/automation/process-automation-strategist.md. Review automation: [FLOW_FILES]. Check for: Flow vs Apex decisions, automation conflicts. Return JSON: {agent: 'process-automation-strategist', findings: [{file, line, severity, issue, fix}]}"

15. Task tool call:
    - description: "Review validation rules"
    - subagent_type: "general-purpose"
    - prompt: "You are the Validation Rule Reviewer agent. Read .claude/agents/automation/validation-rule-reviewer.md. Review objects: [OBJECT_FILES]. Check for: Rule complexity, error messages, bypass patterns. Return JSON: {agent: 'validation-rule-reviewer', findings: [{file, line, severity, issue, fix}]}"

FOR INTEGRATION FILES - Deploy these 4 subagents:

16. Task tool call:
    - description: "Review REST API design"
    - subagent_type: "general-purpose"
    - prompt: "You are the REST API Architect agent. Read .claude/agents/integration/rest-api-architect.md. Review REST resources: [REST_FILES]. Check for: Endpoint design, versioning, error responses. Return JSON: {agent: 'rest-api-architect', findings: [{file, line, severity, issue, fix}]}"

17. Task tool call:
    - description: "Review callout patterns"
    - subagent_type: "general-purpose"
    - prompt: "You are the Callout Pattern Reviewer agent. Read .claude/agents/integration/callout-pattern-reviewer.md. Review callouts: [CALLOUT_FILES]. Check for: Named Credentials, timeout handling, retry logic. Return JSON: {agent: 'callout-pattern-reviewer', findings: [{file, line, severity, issue, fix}]}"

18. Task tool call:
    - description: "Review platform events"
    - subagent_type: "general-purpose"
    - prompt: "You are the Platform Event Strategist agent. Read .claude/agents/integration/platform-event-strategist.md. Review events: [EVENT_FILES]. Check for: Event design, subscriber patterns, replay handling. Return JSON: {agent: 'platform-event-strategist', findings: [{file, line, severity, issue, fix}]}"

19. Task tool call:
    - description: "Review integration security"
    - subagent_type: "general-purpose"
    - prompt: "You are the Integration Security Sentinel agent. Read .claude/agents/integration/integration-security-sentinel.md. Review integrations: [INTEGRATION_FILES]. Check for: Credential storage, data in transit. Return JSON: {agent: 'integration-security-sentinel', findings: [{file, line, severity, issue, fix}]}"

FOR ALL FILES - Deploy these 4 architecture subagents:

20. Task tool call:
    - description: "Review data model"
    - subagent_type: "general-purpose"
    - prompt: "You are the Data Model Architect agent. Read .claude/agents/architecture/data-model-architect.md. Review objects: [OBJECT_FILES]. Check for: Relationship design, field naming, indexes. Return JSON: {agent: 'data-model-architect', findings: [{file, line, severity, issue, fix}]}"

21. Task tool call:
    - description: "Review sharing model"
    - subagent_type: "general-purpose"
    - prompt: "You are the Sharing Security Analyst agent. Read .claude/agents/architecture/sharing-security-analyst.md. Review sharing: [ALL_FILES]. Check for: OWD implications, sharing rules, Apex sharing. Return JSON: {agent: 'sharing-security-analyst', findings: [{file, line, severity, issue, fix}]}"

22. Task tool call:
    - description: "Review metadata consistency"
    - subagent_type: "general-purpose"
    - prompt: "You are the Metadata Consistency Checker agent. Read .claude/agents/architecture/metadata-consistency-checker.md. Review metadata: [ALL_FILES]. Check for: Naming conventions, API versions, package organization. Return JSON: {agent: 'metadata-consistency-checker', findings: [{file, line, severity, issue, fix}]}"

23. Task tool call:
    - description: "Detect anti-patterns"
    - subagent_type: "general-purpose"
    - prompt: "You are the Pattern Recognition Specialist agent. Read .claude/agents/architecture/pattern-recognition-specialist.md. Review all code: [ALL_FILES]. Check for: God classes, duplicate code, hardcoded values, dead code. Return JSON: {agent: 'pattern-recognition-specialist', findings: [{file, line, severity, issue, fix}]}"
</subagent_deployment>

**Deploy ALL relevant subagents in ONE message for maximum parallelization.**

Display progress:
```
Deploying review subagents...
  • Apex agents (6): [deploying/complete]
  • LWC agents (5): [deploying/complete]
  • Automation agents (4): [deploying/complete]
  • Integration agents (4): [deploying/complete]
  • Architecture agents (4): [deploying/complete]
```

### Step 4: Collect and Synthesize Results

**Wait for ALL subagents to complete.**

Aggregate findings by severity:
- 🔴 **Critical**: Must fix before merge
- 🟠 **High**: Should fix before merge
- 🟡 **Medium**: Consider fixing
- 🔵 **Low**: Nice to have

### Step 5: Generate Review Report

Present findings:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SALESFORCE CODE REVIEW COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 [X] subagents deployed in parallel
⏱️  Review completed in [Y] seconds

┌─────────────┬───────┬────────────────────────┐
│ Severity    │ Count │ Action Required        │
├─────────────┼───────┼────────────────────────┤
│ 🔴 Critical │   X   │ Must fix before merge  │
│ 🟠 High     │   Y   │ Should fix             │
│ 🟡 Medium   │   Z   │ Consider fixing        │
│ 🔵 Low      │   W   │ Nice to have           │
└─────────────┴───────┴────────────────────────┘

🔴 CRITICAL ISSUES:

1. [Agent Name] - [File:Line]
   Issue: [Description]
   Fix: [Recommended fix]

🟠 HIGH ISSUES:
...

✅ POSITIVE OBSERVATIONS:
- [Good patterns found]

Next Steps:
  • Fix critical: /sf-resolve critical
  • Fix all: /sf-resolve
  • Re-review: /sf-review
```

## Important

- You MUST call Task tool to spawn subagents - don't just describe them
- Deploy ALL relevant subagents in ONE message for parallelization
- Each subagent MUST read its agent file before reviewing
- Subagents return JSON findings for easy aggregation
- Only deploy agents relevant to the file types being reviewed
