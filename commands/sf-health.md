---
name: sf-health
description: Analyze Salesforce org health, technical debt, and provide improvement recommendations
arguments:
  - name: scope
    description: Analysis scope (full, apex, lwc, automation, security)
    required: false
---

# Salesforce Health Command

Analyzes codebase and org health, identifies technical debt, and provides actionable recommendations. This is a comprehensive check before deployment.

## Required: Load ALL Agents for Health Check

**CRITICAL**: The health check runs ALL 23 agents to ensure the codebase is ready for deployment.

### Load ALL Agent Categories
```
.claude/agents/apex/           # 6 agents for Apex health
.claude/agents/lwc/            # 5 agents for LWC health
.claude/agents/automation/     # 4 agents for Flow health
.claude/agents/integration/    # 4 agents for integration health
.claude/agents/architecture/   # 4 agents for architecture health
```

### Full Agent List (23 total)
```
Apex (6):
├── apex-governor-guardian.md
├── apex-security-sentinel.md
├── apex-bulkification-reviewer.md
├── apex-trigger-architect.md
├── apex-test-coverage-analyst.md
└── apex-exception-handler.md

LWC (5):
├── lwc-performance-oracle.md
├── lwc-security-reviewer.md
├── lwc-accessibility-guardian.md
├── lwc-architecture-strategist.md
└── aura-migration-advisor.md

Automation (4):
├── flow-complexity-analyzer.md
├── flow-governor-monitor.md
├── process-automation-strategist.md
└── validation-rule-reviewer.md

Integration (4):
├── rest-api-architect.md
├── callout-pattern-reviewer.md
├── platform-event-strategist.md
└── integration-security-sentinel.md

Architecture (4):
├── data-model-architect.md
├── sharing-security-analyst.md
├── metadata-consistency-checker.md
└── pattern-recognition-specialist.md
```

### How to Apply

1. **Read ALL agent files** before running health check
2. **Apply each agent's checklist** to the entire codebase
3. **Score each category** based on checklist compliance
4. **Flag blockers**: Any CRITICAL finding = deployment blocked
5. **Generate Go/No-Go recommendation**

---

## Workflow

### Step 1: Gather Metrics

```bash
# Count components
APEX_CLASSES=$(find . -name "*.cls" ! -name "*Test*" | wc -l)
TEST_CLASSES=$(find . -name "*Test*.cls" | wc -l)
TRIGGERS=$(find . -name "*.trigger" | wc -l)
LWC_COMPONENTS=$(find . -path "*/lwc/*" -name "*.js" ! -name "*.test.js" | wc -l)
FLOWS=$(find . -name "*.flow-meta.xml" | wc -l)
```

### Step 2: Run Analysis

```markdown
## Org Health Report

### Overview
| Metric | Count | Status |
|--------|-------|--------|
| Apex Classes | 145 | - |
| Test Classes | 98 | ⚠️ (68% ratio) |
| Triggers | 12 | ✅ |
| LWC Components | 34 | - |
| Flows | 28 | - |
| Validation Rules | 45 | - |

### Code Quality Score: 72/100

#### Breakdown
- Test Coverage: 78% (target: 85%) → 15/20 points
- Code Patterns: Good → 18/20 points
- Security: Needs work → 12/20 points
- Documentation: Poor → 8/20 points
- Maintainability: Average → 19/20 points
```

### Step 3: Technical Debt Analysis

```markdown
## Technical Debt Summary

### High Priority (Fix Soon)
1. **Security Vulnerabilities** - 3 items
   - SOQL injection risks in 2 classes
   - Missing CRUD checks in 5 methods
   
2. **Governor Limit Risks** - 5 items
   - SOQL in loops: 3 occurrences
   - DML in loops: 2 occurrences

### Medium Priority (Plan to Address)
1. **Test Coverage Gaps** - 12 classes below 75%
2. **Deprecated Patterns** - 8 Process Builders to migrate
3. **Code Duplication** - 15 similar code blocks

### Low Priority (Nice to Have)
1. **Naming Conventions** - 23 non-standard names
2. **Missing Documentation** - 45 classes without ApexDoc
```

### Step 4: Recommendations

```markdown
## Recommendations

### Immediate Actions (This Sprint)
1. Fix SOQL injection in AccountController.cls
2. Add CRUD checks to OpportunityService.cls
3. Bulkify trigger handlers with DML in loops

### Short-term (Next 2-4 Weeks)
1. Increase test coverage to 85%
2. Migrate Process Builders to Flows
3. Implement trigger handler framework

### Long-term (Quarter)
1. Refactor to service layer pattern
2. Add comprehensive ApexDoc
3. Implement logging framework

## Action Plan

| Week | Focus Area | Effort |
|------|------------|--------|
| 1 | Security fixes | 8 hrs |
| 2 | Governor limit fixes | 6 hrs |
| 3-4 | Test coverage | 16 hrs |
| 5-6 | Process Builder migration | 12 hrs |
```

## Health Checks

### Apex Health
```bash
# Check for common issues
grep -r "Database.query" --include="*.cls" | wc -l  # Dynamic SOQL
grep -r "without sharing" --include="*.cls" | wc -l  # Security risk
grep -r "for.*\[SELECT" --include="*.cls" | wc -l   # SOQL in loop
```

### LWC Health
```bash
# Check for issues
grep -r "innerHTML" --include="*.js" | wc -l        # XSS risk
grep -r "eval(" --include="*.js" | wc -l            # Security risk
```

### Flow Health
```bash
# Count flow elements
grep -c "<elements>" *.flow-meta.xml | sort -t: -k2 -rn | head -10
```
