---
name: sf:triage
description: Present review findings one-by-one and convert approved items to actionable todos
arguments:
  - name: report
    description: Path to review report file
    required: false
---

# Salesforce Triage Command

Interactively review findings from `/sf:review` and convert approved items into actionable todos.

## Workflow

### Step 1: Load Review Findings

```bash
# Load from most recent review or specified file
REPORT=${1:-".sf-compound/latest-review.json"}
```

### Step 2: Interactive Triage

For each finding, present:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Finding 1 of 15 | CRITICAL | apex-security-sentinel
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 Location: AccountController.cls:45
🏷️ Category: Security - SOQL Injection

Issue:
User input directly concatenated into SOQL query.

Current Code:
┌────────────────────────────────────────────────┐
│ String query = 'SELECT Id FROM Account ' +    │
│                'WHERE Name = \'' + name + '\'';│
│ return Database.query(query);                  │
└────────────────────────────────────────────────┘

Recommended Fix:
┌────────────────────────────────────────────────┐
│ return [SELECT Id FROM Account                 │
│         WHERE Name = :name];                   │
└────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Actions:
  [a] Accept → Create todo
  [s] Skip → Mark as won't fix
  [d] Defer → Add to backlog
  [e] Edit → Modify finding
  [?] More info → Show details
  [q] Quit → Save progress and exit

Choice: _
```

### Step 3: Generate Todos

For accepted findings, create structured todos:

```markdown
## Triage Results

### Accepted (Create Todos)
- [ ] TODO-001: Fix SOQL injection in AccountController.cls:45 [CRITICAL]
- [ ] TODO-002: Add CRUD check in OpportunityService.cls:78 [HIGH]
- [ ] TODO-003: Bulkify DML in LeadHandler.cls:120 [HIGH]

### Skipped (Won't Fix)
- Finding #4: Naming convention - Existing pattern in codebase
- Finding #8: Minor optimization - Low impact

### Deferred (Backlog)
- Finding #5: Refactor to service pattern - Requires larger effort
- Finding #12: Add unit tests - Schedule for next sprint
```

### Step 4: Create Work Items

```bash
# Option 1: Save as markdown todo list
cat > .sf-compound/todos.md << EOF
# Review Todos - $(date +%Y-%m-%d)

## Critical
- [ ] Fix SOQL injection in AccountController.cls

## High
- [ ] Add CRUD check in OpportunityService.cls
- [ ] Bulkify DML in LeadHandler.cls
EOF

# Option 2: Create Linear/Jira issues
# (If integration configured)
```

## Triage Categories

### Accept
- Issue is valid
- Should be fixed in current work
- Creates actionable todo

### Skip
- False positive
- Existing pattern/decision
- Not applicable
- Adds to skip list with reason

### Defer
- Valid but not urgent
- Requires larger effort
- Out of scope for current work
- Adds to backlog

## Batch Actions

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Batch Actions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [1] Accept all CRITICAL findings (3 items)
  [2] Accept all from apex-security-sentinel (5 items)
  [3] Skip all LOW severity (8 items)
  [4] Continue one-by-one

Choice: _
```

## Progress Tracking

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Progress: 10/15 findings reviewed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Accepted:  6
⏭️ Skipped:   3
📋 Deferred:  1
⏳ Remaining: 5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Output Files

```
.sf-compound/
├── latest-review.json     # Review findings
├── triage-session.json    # Triage decisions
├── todos.md               # Accepted todos
└── backlog.md             # Deferred items
```
