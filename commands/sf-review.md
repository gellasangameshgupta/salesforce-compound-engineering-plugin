---
name: sf-review
description: Perform exhaustive multi-agent Salesforce code review
arguments:
  - name: target
    description: PR number, file path, or directory to review
    required: false
---

# Salesforce Code Review Command

Performs comprehensive, multi-agent code review specifically designed for Salesforce development. Runs 23 specialized agents to catch issues across Apex, LWC, Flows, and integrations.

## Required: Load ALL Review Agents

**CRITICAL**: Before reviewing any code, you MUST read and apply ALL 23 agent files. Each agent contains specific checklists and anti-patterns to check.

### Apex Agents (6)
Read and apply ALL checklists from:
```
.claude/agents/apex/
├── apex-governor-guardian.md      # Governor limits, SOQL/DML optimization
├── apex-security-sentinel.md      # CRUD/FLS, injection, security
├── apex-bulkification-reviewer.md # Bulk patterns, collection handling
├── apex-trigger-architect.md      # Trigger patterns, recursion control
├── apex-test-coverage-analyst.md  # Test quality, coverage, assertions
└── apex-exception-handler.md      # Error handling, logging patterns
```

### LWC Agents (5)
Read and apply ALL checklists from:
```
.claude/agents/lwc/
├── lwc-performance-oracle.md      # Wire vs imperative, rendering
├── lwc-security-reviewer.md       # XSS, CSP, secure coding
├── lwc-accessibility-guardian.md  # WCAG, ARIA, keyboard navigation
├── lwc-architecture-strategist.md # Component design, communication
└── aura-migration-advisor.md      # Aura to LWC migration patterns
```

### Automation Agents (4)
Read and apply ALL checklists from:
```
.claude/agents/automation/
├── flow-complexity-analyzer.md    # Flow design, loops, branches
├── flow-governor-monitor.md       # DML/SOQL in flows, limits
├── process-automation-strategist.md # Flow vs Apex decisions
└── validation-rule-reviewer.md    # Validation rule design
```

### Integration Agents (4)
Read and apply ALL checklists from:
```
.claude/agents/integration/
├── rest-api-architect.md          # API design, versioning
├── callout-pattern-reviewer.md    # Callout patterns, error handling
├── platform-event-strategist.md   # Event-driven architecture
└── integration-security-sentinel.md # Auth, credentials, data security
```

### Architecture Agents (4)
Read and apply ALL checklists from:
```
.claude/agents/architecture/
├── data-model-architect.md        # Schema design, relationships
├── sharing-security-analyst.md    # OWD, sharing rules, visibility
├── metadata-consistency-checker.md # Naming, organization, profiles
└── pattern-recognition-specialist.md # Anti-patterns, code smells
```

### How to Apply Each Agent

For EACH agent file:
1. **Read the file** to get the checklist and anti-patterns
2. **Apply each checklist item** to the code being reviewed
3. **Check for anti-patterns** listed in the agent
4. **Use the Response Format** from the agent for findings
5. **Assign severity** as defined in the agent (CRITICAL/HIGH/MEDIUM/LOW)

---

## Workflow

When the user runs `/sf-review [target]`, execute the following:

### Step 1: Determine Review Target

```
IF target is empty:
    Review latest uncommitted changes (git diff)
ELSE IF target is a number:
    Fetch PR #{target} and review its changes
ELSE IF target is a URL:
    Parse GitHub/GitLab PR URL and fetch changes
ELSE IF target is a path:
    Review files at that path
```

### Step 2: Classify Files for Review

Group changed files by type:

```javascript
const fileTypes = {
    apex: ['.cls', '.trigger'],
    lwc: ['.js', '.html', '.css'],  // in lwc/ directory
    aura: ['.cmp', '.evt', '.app', '.js'],  // in aura/ directory
    flows: ['.flow-meta.xml'],
    objects: ['.object-meta.xml', '.field-meta.xml'],
    profiles: ['.profile-meta.xml', '.permissionset-meta.xml'],
    tests: files matching '*Test.cls'
};
```

### Step 3: Dispatch Review Agents

Run appropriate agents based on file types:

#### For Apex Files (.cls, .trigger):
```
PARALLEL:
  - apex-governor-guardian (governor limits)
  - apex-bulkification-reviewer (bulk patterns)
  - apex-security-sentinel (CRUD/FLS, injection)
  - apex-trigger-architect (trigger patterns)
  - apex-test-coverage-analyst (test quality)
  - apex-exception-handler (error handling)
```

#### For LWC Files:
```
PARALLEL:
  - lwc-performance-oracle (performance)
  - lwc-security-reviewer (XSS, CSP)
  - lwc-accessibility-guardian (WCAG)
  - lwc-architecture-strategist (component design)
```

#### For Flow Files:
```
PARALLEL:
  - flow-complexity-analyzer (loops, branches)
  - flow-governor-monitor (DML/SOQL in flows)
  - process-automation-strategist (Flow vs Apex)
```

#### For All Changes:
```
PARALLEL:
  - pattern-recognition-specialist (anti-patterns)
  - metadata-consistency-checker (profiles, perms)
  - sharing-security-analyst (OWD, sharing rules)
```

### Step 4: Collect and Organize Findings

Aggregate findings from all agents:

```javascript
const findings = {
    critical: [],  // Must fix before merge
    high: [],      // Should fix before merge
    medium: [],    // Consider fixing
    low: [],       // Nice to have
    info: []       // Informational only
};
```

### Step 5: Generate Review Report

Create structured output:

```markdown
# Salesforce Code Review Report

## Summary
| Severity | Count |
|----------|-------|
| 🔴 Critical | X |
| 🟠 High | Y |
| 🟡 Medium | Z |
| 🔵 Low | W |
| ℹ️ Info | V |

## Critical Issues (Must Fix)

### CR-001: [Issue Title]
**Agent**: apex-security-sentinel
**File**: AccountController.cls:45
**Category**: Security - SOQL Injection

**Issue**: 
[Description of the problem]

**Current Code**:
```apex
String query = 'SELECT Id FROM Account WHERE Name = \'' + userInput + '\'';
```

**Recommended Fix**:
```apex
String query = 'SELECT Id FROM Account WHERE Name = :userInput';
```

**Why This Matters**:
[Business/security impact]

---

### CR-002: [Issue Title]
...

## High Priority Issues (Should Fix)

### HI-001: [Issue Title]
...

## Medium Priority Issues (Consider)

### MI-001: [Issue Title]
...

## Low Priority / Suggestions

### LO-001: [Issue Title]
...

## Positive Observations

✅ Good use of trigger handler pattern
✅ Comprehensive test coverage (92%)
✅ Proper CRUD checks in service layer

## Review Checklist

### Apex
- [x] Governor limits analyzed
- [x] Bulkification verified
- [x] CRUD/FLS enforced
- [ ] Missing: Null safety in line 78

### LWC
- [x] Wire adapters used appropriately
- [x] Event cleanup in disconnectedCallback
- [ ] Missing: Loading states for async operations

### Security
- [x] No hardcoded credentials
- [x] Using Named Credentials
- [ ] Warning: Consider adding CSP headers

## Recommended Actions

1. **Before Merge**: Fix all Critical and High issues
2. **In This PR**: Address Medium issues if time permits
3. **Follow-up PR**: Track Low issues as tech debt

## Files Reviewed
- AccountController.cls (245 lines)
- AccountTrigger.trigger (12 lines)
- accountList.js (180 lines)
- accountList.html (95 lines)
```

### Step 6: Present Findings

Display findings with actionable next steps:

```
Review complete! Found X issues across Y files.

🔴 2 Critical - Must fix before merge
🟠 3 High - Should fix before merge
🟡 5 Medium - Consider fixing

Run `/sf-triage` to review findings one by one.
Run `/sf-resolve` to auto-fix applicable issues.

View full report: review-report-2024-01-15.md
```

## Agent Dispatch Matrix

| File Type | Agents |
|-----------|--------|
| *.cls | governor, bulk, security, exception |
| *Trigger.trigger | governor, bulk, security, trigger-arch |
| *Test.cls | test-coverage, test-quality |
| *.js (lwc) | lwc-perf, lwc-security, lwc-a11y |
| *.html (lwc) | lwc-a11y, lwc-arch |
| *.flow-meta.xml | flow-complexity, flow-governor |
| *.object-meta.xml | data-model, sharing |
| *.profile-meta.xml | metadata-consistency |

## Review Configuration

Users can configure review behavior in `.sf-compound/config.json`:

```json
{
  "review": {
    "agents": ["all"],
    "excludeAgents": ["aura-migration-advisor"],
    "severityThreshold": "low",
    "autoFix": false,
    "excludePaths": ["force-app/main/default/staticresources/"],
    "customRules": {
      "requireTestsForTriggers": true,
      "minimumCoverage": 85,
      "maxCyclomaticComplexity": 10
    }
  }
}
```

## Example Scenarios

### Review Uncommitted Changes
```bash
/sf-review
# Reviews all uncommitted changes in git
```

### Review Specific PR
```bash
/sf-review 123
# Fetches and reviews PR #123
```

### Review Specific File
```bash
/sf-review force-app/main/default/classes/AccountService.cls
# Deep review of single file
```

### Review Directory
```bash
/sf-review force-app/main/default/lwc/accountList/
# Reviews all files in LWC component
```

## Integration with CI/CD

The review command can be used in CI pipelines:

```yaml
# GitHub Actions example
- name: Salesforce Code Review
  run: |
    claude /sf-review --ci --severity-threshold high
    
# Exit code:
# 0 = No critical/high issues
# 1 = Critical issues found
# 2 = High issues found
```
