---
name: sf:resolve
description: Resolve multiple todos in parallel with AI assistance
arguments:
  - name: filter
    description: Filter todos by severity or type
    required: false
---

# Salesforce Resolve Command

Resolves todos created from triage in parallel, applying fixes with validation.

## Workflow

### Step 1: Load Todos

```markdown
## Pending Todos

1. [CRITICAL] Fix SOQL injection - AccountController.cls:45
2. [HIGH] Add CRUD check - OpportunityService.cls:78
3. [HIGH] Bulkify DML - LeadHandler.cls:120
4. [MEDIUM] Add null check - ContactHelper.cls:34
5. [LOW] Rename variable - AccountUtils.cls:89

Select todos to resolve: [1-5, all, critical, high]
```

### Step 2: Parallel Resolution

```
Resolving 3 todos in parallel...

━━━ TODO-001: Fix SOQL injection ━━━━━━━━━━━━━━━━━
Status: ✅ Fixed
Changes:
  - AccountController.cls: Line 45 updated
  - Using bind variable instead of concatenation

━━━ TODO-002: Add CRUD check ━━━━━━━━━━━━━━━━━━━━━
Status: ✅ Fixed
Changes:
  - OpportunityService.cls: Lines 78-82 updated
  - Added Schema.sObjectType check

━━━ TODO-003: Bulkify DML ━━━━━━━━━━━━━━━━━━━━━━━━
Status: ✅ Fixed
Changes:
  - LeadHandler.cls: Lines 120-135 refactored
  - Moved DML outside loop
```

### Step 3: Validate Changes

```bash
# Run affected tests
sf apex run test --class-names AccountControllerTest,OpportunityServiceTest,LeadHandlerTest

# Validate deployment
sf project deploy validate --source-dir force-app/main/default/classes/
```

### Step 4: Commit Changes

```bash
git add -A
git commit -m "fix: Resolve security and performance issues

- Fix SOQL injection in AccountController
- Add CRUD checks in OpportunityService  
- Bulkify DML operations in LeadHandler

Resolves: TODO-001, TODO-002, TODO-003"
```

## Resolution Strategies

### SOQL Injection Fix
```apex
// Before
String query = 'SELECT Id FROM Account WHERE Name = \'' + name + '\'';
return Database.query(query);

// After
return [SELECT Id FROM Account WHERE Name = :name];
```

### CRUD Check Addition
```apex
// Before
update accounts;

// After
if (!Schema.sObjectType.Account.isUpdateable()) {
    throw new SecurityException('Insufficient privileges');
}
update accounts;
```

### DML Bulkification
```apex
// Before
for (Lead lead : leads) {
    lead.Status = 'Working';
    update lead;
}

// After
for (Lead lead : leads) {
    lead.Status = 'Working';
}
update leads;
```
