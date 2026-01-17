---
name: sf-review
description: Multi-agent code review with 23 parallel Salesforce specialist subagents
arguments:
  - name: target
    description: PR number, file path, or directory to review
    required: false
---

# Salesforce Code Review Command

Performs comprehensive, multi-agent code review using **23 parallel subagents** - each checking from a different Salesforce specialist perspective. This is the "20% review phase" of compound engineering.

## Subagent Architecture

```
/sf-review
    │
    ├── [FILE CLASSIFICATION]
    │   └── Main Agent: Classify files, determine which agents to deploy
    │
    ├── [PARALLEL REVIEW - 23 SUBAGENTS]
    │   │
    │   ├── APEX REVIEW SUBAGENTS (6)
    │   │   ├── Governor Guardian
    │   │   ├── Security Sentinel
    │   │   ├── Bulkification Reviewer
    │   │   ├── Trigger Architect
    │   │   ├── Test Coverage Analyst
    │   │   └── Exception Handler
    │   │
    │   ├── LWC REVIEW SUBAGENTS (5)
    │   │   ├── Performance Oracle
    │   │   ├── Security Reviewer
    │   │   ├── Accessibility Guardian
    │   │   ├── Architecture Strategist
    │   │   └── Aura Migration Advisor
    │   │
    │   ├── AUTOMATION REVIEW SUBAGENTS (4)
    │   │   ├── Flow Complexity Analyzer
    │   │   ├── Flow Governor Monitor
    │   │   ├── Process Automation Strategist
    │   │   └── Validation Rule Reviewer
    │   │
    │   ├── INTEGRATION REVIEW SUBAGENTS (4)
    │   │   ├── REST API Architect
    │   │   ├── Callout Pattern Reviewer
    │   │   ├── Platform Event Strategist
    │   │   └── Integration Security Sentinel
    │   │
    │   └── ARCHITECTURE REVIEW SUBAGENTS (4)
    │       ├── Data Model Architect
    │       ├── Sharing Security Analyst
    │       ├── Metadata Consistency Checker
    │       └── Pattern Recognition Specialist
    │
    └── [SYNTHESIS]
        └── Main Agent: Aggregate findings, prioritize, generate report
```

---

## Workflow

When the user runs `/sf-review [target]`, execute the following:

### Step 1: Determine Review Target

```
IF target is empty:
    Review latest uncommitted changes (git diff)
ELSE IF target is a number:
    Fetch PR #{target} and review
ELSE IF target is a URL:
    Parse GitHub/GitLab PR URL
ELSE IF target is a path:
    Review files at that path
```

### Step 2: Classify Files

Group files by type for targeted agent deployment:

```javascript
const classification = {
    apex: [],        // .cls, .trigger
    lwc: [],         // .js, .html, .css in lwc/
    aura: [],        // .cmp, .evt, .app in aura/
    flows: [],       // .flow-meta.xml
    objects: [],     // .object-meta.xml, .field-meta.xml
    profiles: [],    // .profile-meta.xml, .permissionset-meta.xml
    tests: []        // *Test.cls
};
```

### Step 3: Deploy Review Subagents (PARALLEL)

**CRITICAL**: Deploy ALL 23 subagents IN PARALLEL using the Task tool. Each reads its agent file and reviews the code:

```
Use the Task tool to spawn ALL these subagents concurrently:

═══════════════════════════════════════════════════════════════════
APEX REVIEW SUBAGENTS (6)
═══════════════════════════════════════════════════════════════════

1. GOVERNOR GUARDIAN SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Review code for governor limit compliance.

     Read agent: .claude/agents/apex/apex-governor-guardian.md
     Files to review: [APEX_FILES]

     Check:
     - SOQL queries inside loops
     - DML statements per transaction
     - CPU time complexity
     - Heap size usage
     - Bulk operation handling

     Return findings as JSON:
     {
       "agent": "governor-guardian",
       "severity": "critical|high|medium|low",
       "findings": [{ "file", "line", "issue", "fix" }]
     }

2. SECURITY SENTINEL SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Review code for security vulnerabilities.

     Read agent: .claude/agents/apex/apex-security-sentinel.md
     Files to review: [APEX_FILES]

     Check:
     - CRUD/FLS enforcement
     - SOQL/SOSL injection
     - XSS vulnerabilities
     - Hardcoded credentials
     - Sharing keyword usage

     Return findings as JSON...

3. BULKIFICATION REVIEWER SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Review code for bulk data handling.

     Read agent: .claude/agents/apex/apex-bulkification-reviewer.md
     Files to review: [APEX_FILES]

     Check:
     - Queries return collections (not single records)
     - DML on collections (not in loops)
     - Map/Set usage for lookups
     - Trigger.new/old handling

     Return findings as JSON...

4. TRIGGER ARCHITECT SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Review trigger implementation patterns.

     Read agent: .claude/agents/apex/apex-trigger-architect.md
     Files to review: [TRIGGER_FILES]

     Check:
     - One trigger per object
     - Handler pattern usage
     - Recursion prevention
     - Context variable usage
     - Order of execution

     Return findings as JSON...

5. TEST COVERAGE ANALYST SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Review test class quality.

     Read agent: .claude/agents/apex/apex-test-coverage-analyst.md
     Files to review: [TEST_FILES]

     Check:
     - Positive/negative scenarios
     - Bulk testing (200+ records)
     - User context testing
     - Assertion quality
     - Test data creation

     Return findings as JSON...

6. EXCEPTION HANDLER SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Review error handling patterns.

     Read agent: .claude/agents/apex/apex-exception-handler.md
     Files to review: [APEX_FILES]

     Check:
     - Try-catch blocks
     - Custom exception classes
     - Error logging
     - User-friendly messages
     - DML error handling

     Return findings as JSON...

═══════════════════════════════════════════════════════════════════
LWC REVIEW SUBAGENTS (5)
═══════════════════════════════════════════════════════════════════

7. LWC PERFORMANCE ORACLE SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Review LWC performance patterns.

     Read agent: .claude/agents/lwc/lwc-performance-oracle.md
     Files to review: [LWC_FILES]

     Check:
     - Wire vs imperative calls
     - Unnecessary re-renders
     - Large DOM operations
     - Event handling efficiency
     - Caching strategies

     Return findings as JSON...

8. LWC SECURITY REVIEWER SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Review LWC security.

     Read agent: .claude/agents/lwc/lwc-security-reviewer.md
     Files to review: [LWC_FILES]

     Check:
     - innerHTML usage (XSS)
     - CSP compliance
     - Secure data handling
     - Third-party library risks

     Return findings as JSON...

9. LWC ACCESSIBILITY GUARDIAN SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Review LWC accessibility.

     Read agent: .claude/agents/lwc/lwc-accessibility-guardian.md
     Files to review: [LWC_FILES]

     Check:
     - ARIA attributes
     - Keyboard navigation
     - Screen reader support
     - Color contrast
     - Focus management

     Return findings as JSON...

10. LWC ARCHITECTURE STRATEGIST SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review LWC architecture.

      Read agent: .claude/agents/lwc/lwc-architecture-strategist.md
      Files to review: [LWC_FILES]

      Check:
      - Component hierarchy
      - Event communication
      - State management
      - Reusability patterns

      Return findings as JSON...

11. AURA MIGRATION ADVISOR SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review Aura components for migration.

      Read agent: .claude/agents/lwc/aura-migration-advisor.md
      Files to review: [AURA_FILES]

      Check:
      - LWC migration candidates
      - Deprecated patterns
      - Performance issues
      - Modern alternatives

      Return findings as JSON...

═══════════════════════════════════════════════════════════════════
AUTOMATION REVIEW SUBAGENTS (4)
═══════════════════════════════════════════════════════════════════

12. FLOW COMPLEXITY ANALYZER SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review Flow complexity.

      Read agent: .claude/agents/automation/flow-complexity-analyzer.md
      Files to review: [FLOW_FILES]

      Check:
      - Loop complexity
      - Decision branch depth
      - Subflow usage
      - Variable naming
      - Documentation

      Return findings as JSON...

13. FLOW GOVERNOR MONITOR SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review Flow governor limits.

      Read agent: .claude/agents/automation/flow-governor-monitor.md
      Files to review: [FLOW_FILES]

      Check:
      - DML in loops
      - SOQL in loops
      - Batch size handling
      - Bulkification

      Return findings as JSON...

14. PROCESS AUTOMATION STRATEGIST SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review automation strategy.

      Read agent: .claude/agents/automation/process-automation-strategist.md
      Files to review: [FLOW_FILES, TRIGGER_FILES]

      Check:
      - Flow vs Apex decisions
      - Automation conflicts
      - Order of execution
      - Maintainability

      Return findings as JSON...

15. VALIDATION RULE REVIEWER SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review validation rules.

      Read agent: .claude/agents/automation/validation-rule-reviewer.md
      Files to review: [OBJECT_FILES]

      Check:
      - Rule complexity
      - Error messages
      - Bypass patterns
      - Performance impact

      Return findings as JSON...

═══════════════════════════════════════════════════════════════════
INTEGRATION REVIEW SUBAGENTS (4)
═══════════════════════════════════════════════════════════════════

16. REST API ARCHITECT SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review REST API implementations.

      Read agent: .claude/agents/integration/rest-api-architect.md
      Files to review: [APEX_FILES with @RestResource]

      Check:
      - Endpoint design
      - Versioning strategy
      - Error responses
      - Rate limiting

      Return findings as JSON...

17. CALLOUT PATTERN REVIEWER SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review HTTP callout patterns.

      Read agent: .claude/agents/integration/callout-pattern-reviewer.md
      Files to review: [APEX_FILES with HttpRequest]

      Check:
      - Named Credentials usage
      - Timeout handling
      - Retry logic
      - Error handling

      Return findings as JSON...

18. PLATFORM EVENT STRATEGIST SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review Platform Event usage.

      Read agent: .claude/agents/integration/platform-event-strategist.md
      Files to review: [FILES with Platform Events]

      Check:
      - Event design
      - Subscriber patterns
      - Error handling
      - Replay ID handling

      Return findings as JSON...

19. INTEGRATION SECURITY SENTINEL SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review integration security.

      Read agent: .claude/agents/integration/integration-security-sentinel.md
      Files to review: [INTEGRATION_FILES]

      Check:
      - Credential storage
      - Data in transit
      - Authentication methods
      - Sensitive data handling

      Return findings as JSON...

═══════════════════════════════════════════════════════════════════
ARCHITECTURE REVIEW SUBAGENTS (4)
═══════════════════════════════════════════════════════════════════

20. DATA MODEL ARCHITECT SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review data model design.

      Read agent: .claude/agents/architecture/data-model-architect.md
      Files to review: [OBJECT_FILES]

      Check:
      - Relationship design
      - Field naming
      - Index candidates
      - Data volume considerations

      Return findings as JSON...

21. SHARING SECURITY ANALYST SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review sharing model.

      Read agent: .claude/agents/architecture/sharing-security-analyst.md
      Files to review: [OBJECT_FILES, SHARING_FILES]

      Check:
      - OWD settings
      - Sharing rules
      - Apex sharing
      - Visibility patterns

      Return findings as JSON...

22. METADATA CONSISTENCY CHECKER SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Review metadata consistency.

      Read agent: .claude/agents/architecture/metadata-consistency-checker.md
      Files to review: [ALL_METADATA]

      Check:
      - Naming conventions
      - API version consistency
      - Profile/permission alignment
      - Package organization

      Return findings as JSON...

23. PATTERN RECOGNITION SPECIALIST SUBAGENT
    subagent_type: "general-purpose"
    prompt: |
      Identify anti-patterns and code smells.

      Read agent: .claude/agents/architecture/pattern-recognition-specialist.md
      Files to review: [ALL_FILES]

      Check:
      - God classes
      - Duplicate code
      - Hardcoded values
      - Dead code
      - Complexity metrics

      Return findings as JSON...
```

### Step 4: Collect and Synthesize Findings

After all 23 subagents return, aggregate:

```javascript
const allFindings = {
    critical: [],  // 🔴 Must fix before merge
    high: [],      // 🟠 Should fix before merge
    medium: [],    // 🟡 Consider fixing
    low: [],       // 🔵 Nice to have
    info: []       // ℹ️ Informational
};

// Merge findings from all subagents
subagentResults.forEach(result => {
    result.findings.forEach(finding => {
        allFindings[finding.severity].push({
            ...finding,
            agent: result.agent
        });
    });
});
```

### Step 5: Generate Review Report

```markdown
# Salesforce Code Review Report

## Review Summary

| Metric | Value |
|--------|-------|
| Files Reviewed | X |
| Subagents Deployed | 23 |
| Review Duration | Y seconds |

### Findings by Severity

| Severity | Count | Status |
|----------|-------|--------|
| 🔴 Critical | X | Must fix before merge |
| 🟠 High | Y | Should fix before merge |
| 🟡 Medium | Z | Consider fixing |
| 🔵 Low | W | Nice to have |
| ℹ️ Info | V | Informational |

### Findings by Agent Category

| Category | Agents | Findings |
|----------|--------|----------|
| Apex | 6 | X |
| LWC | 5 | Y |
| Automation | 4 | Z |
| Integration | 4 | W |
| Architecture | 4 | V |

---

## 🔴 Critical Issues (Must Fix)

### CR-001: SOQL Injection Vulnerability
**Agent**: Security Sentinel
**File**: `AccountController.cls:45`
**Category**: Security

**Issue**:
User input directly concatenated into SOQL query without sanitization.

**Current Code**:
```apex
String query = 'SELECT Id FROM Account WHERE Name = \'' + userInput + '\'';
```

**Recommended Fix**:
```apex
String query = 'SELECT Id FROM Account WHERE Name = :userInput';
```

**Why This Matters**:
Allows attackers to extract or modify data through malicious input.

---

### CR-002: [Next Critical Issue]
...

---

## 🟠 High Priority Issues

### HI-001: [Issue Title]
...

---

## 🟡 Medium Priority Issues

### MI-001: [Issue Title]
...

---

## 🔵 Low Priority / Suggestions

### LO-001: [Issue Title]
...

---

## ✅ Positive Observations

- Good use of trigger handler pattern (Trigger Architect)
- CRUD checks present in service layer (Security Sentinel)
- Test coverage at 92% (Test Coverage Analyst)
- LWC uses wire adapters efficiently (Performance Oracle)

---

## Agent-Specific Reports

### Apex Agents (6)
- Governor Guardian: 2 findings
- Security Sentinel: 3 findings
- Bulkification Reviewer: 1 finding
- Trigger Architect: 0 findings ✅
- Test Coverage Analyst: 2 findings
- Exception Handler: 1 finding

### LWC Agents (5)
...

### Automation Agents (4)
...

### Integration Agents (4)
...

### Architecture Agents (4)
...

---

## Recommended Actions

1. **Before Merge**: Fix all 🔴 Critical and 🟠 High issues
2. **In This PR**: Address 🟡 Medium issues if time permits
3. **Follow-up**: Track 🔵 Low issues as tech debt

---

## Next Steps

```bash
# Auto-fix applicable issues
/sf-resolve

# Run tests after fixes
/sf-test

# Re-review after fixes
/sf-review
```
```

### Step 6: Present Results

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SALESFORCE CODE REVIEW COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 23 Subagents deployed in parallel
⏱️  Review completed in 45 seconds

┌─────────────┬───────┬────────────────────────┐
│ Severity    │ Count │ Action Required        │
├─────────────┼───────┼────────────────────────┤
│ 🔴 Critical │   2   │ Must fix before merge  │
│ 🟠 High     │   3   │ Should fix             │
│ 🟡 Medium   │   5   │ Consider fixing        │
│ 🔵 Low      │   4   │ Nice to have           │
└─────────────┴───────┴────────────────────────┘

📁 Full report: review-report-2024-01-15.md

Next Steps:
  • Fix critical: /sf-resolve --critical
  • View details: cat review-report-2024-01-15.md
  • Re-review: /sf-review
```

---

## Agent Deployment Matrix

| File Type | Agents Deployed |
|-----------|-----------------|
| *.cls | Governor, Security, Bulk, Exception (4) |
| *Trigger.trigger | + Trigger Architect (5) |
| *Test.cls | + Test Coverage Analyst (5) |
| *.js (lwc) | LWC Performance, Security, A11y, Arch (4) |
| *.html (lwc) | LWC A11y, Arch (2) |
| *.cmp (aura) | Aura Migration Advisor (1) |
| *.flow-meta.xml | Flow Complexity, Governor, Strategy (3) |
| *.object-meta.xml | Data Model, Sharing, Metadata (3) |
| All files | Pattern Recognition (always) |

---

## Configuration

```json
// .sf-compound/config.json
{
  "review": {
    "parallelAgents": true,
    "agentTimeout": 60000,
    "excludeAgents": ["aura-migration-advisor"],
    "severityThreshold": "low",
    "excludePaths": ["force-app/main/default/staticresources/"]
  }
}
```
