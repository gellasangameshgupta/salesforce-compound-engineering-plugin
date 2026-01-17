---
name: sf-resolve
description: Parallel issue resolution using specialized fix subagents
arguments:
  - name: filter
    description: Filter todos by severity (critical, high, medium, low) or specific issue ID
    required: false
---

# Salesforce Resolve Command

Resolves issues found during review using **parallel fix subagents** - each specialized in a different type of Salesforce fix.

## Subagent Architecture

```
/sf-resolve [filter]
    │
    ├── [ANALYSIS PHASE]
    │   └── Issue Classification Subagent: Categorize issues by type
    │
    ├── [PARALLEL FIX PHASE]
    │   ├── Security Fix Subagent: CRUD/FLS, injection fixes
    │   ├── Governor Fix Subagent: Limit optimization fixes
    │   ├── Bulkification Fix Subagent: Bulk pattern fixes
    │   ├── Error Handling Fix Subagent: Exception handling fixes
    │   └── Pattern Fix Subagent: Architecture/pattern fixes
    │
    ├── [VALIDATION PHASE - PARALLEL]
    │   ├── Test Execution Subagent: Run affected tests
    │   └── Deploy Validation Subagent: Validate deployment
    │
    └── [COMPLETION PHASE]
        └── Main Agent: Commit changes, update todos
```

---

## Workflow

When the user runs `/sf-resolve [filter]`, execute the following:

### Step 1: Load Pending Issues

Load issues from review findings or todo list:

```
Loading issues from .sf-compound/review-findings.json...

Found 8 issues:
┌─────┬──────────┬─────────────────────────────┬──────────────────────┐
│  ID │ Severity │ Issue                       │ File                 │
├─────┼──────────┼─────────────────────────────┼──────────────────────┤
│  1  │ CRITICAL │ SOQL Injection              │ AccountController:45 │
│  2  │ CRITICAL │ Missing CRUD check          │ LeadService:78       │
│  3  │ HIGH     │ DML in loop                 │ OpportunityHandler:120│
│  4  │ HIGH     │ Query in loop               │ ContactBatch:55      │
│  5  │ MEDIUM   │ Missing null check          │ CaseHelper:34        │
│  6  │ MEDIUM   │ No error handling           │ QuoteService:89      │
│  7  │ LOW      │ Poor variable naming        │ AccountUtils:12      │
│  8  │ LOW      │ Missing ApexDoc             │ LeadProcessor:1      │
└─────┴──────────┴─────────────────────────────┴──────────────────────┘

Filter applied: [filter]
Issues to resolve: X
```

### Step 2: Classify Issues

```
ISSUE CLASSIFICATION SUBAGENT
subagent_type: "general-purpose"
prompt: |
  Classify issues by fix type:

  Issues: [ISSUE_LIST]

  Categories:
  - SECURITY: CRUD/FLS, injection, sharing, credentials
  - GOVERNOR: Limits, loops, bulkification
  - ERROR_HANDLING: Try-catch, logging, user messages
  - PATTERN: Architecture, naming, structure

  Return: Categorized issue list with fix subagent assignment
```

### Step 3: Deploy Fix Subagents (PARALLEL)

**Deploy specialized fix subagents IN PARALLEL:**

```
1. SECURITY FIX SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Fix security issues in Salesforce code.

     Issues assigned: [SECURITY_ISSUES]

     Read agent: .claude/agents/apex/apex-security-sentinel.md
     Read skill: .claude/skills/security-guide/

     For each issue:
     1. Read the file
     2. Identify the vulnerability
     3. Apply the correct fix pattern from security-guide
     4. Verify fix using agent checklist

     Security Fix Patterns:

     SOQL INJECTION:
     ```apex
     // Before
     String query = 'SELECT Id FROM Account WHERE Name = \'' + name + '\'';
     return Database.query(query);

     // After - Use bind variables
     return [SELECT Id FROM Account WHERE Name = :name];
     ```

     CRUD/FLS:
     ```apex
     // Before
     update accounts;

     // After - Check permissions
     if (!Schema.sObjectType.Account.isUpdateable()) {
         throw new SecurityException('Insufficient privileges');
     }
     update accounts;
     ```

     Return: List of files modified with changes made

2. GOVERNOR FIX SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Fix governor limit issues.

     Issues assigned: [GOVERNOR_ISSUES]

     Read agent: .claude/agents/apex/apex-governor-guardian.md
     Read agent: .claude/agents/apex/apex-bulkification-reviewer.md
     Read skill: .claude/skills/governor-limits/

     Governor Fix Patterns:

     SOQL IN LOOP:
     ```apex
     // Before
     for (Account acc : accounts) {
         List<Contact> contacts = [SELECT Id FROM Contact WHERE AccountId = :acc.Id];
     }

     // After - Query once, use Map
     Map<Id, List<Contact>> contactsByAccount = new Map<Id, List<Contact>>();
     for (Contact c : [SELECT Id, AccountId FROM Contact WHERE AccountId IN :accountIds]) {
         if (!contactsByAccount.containsKey(c.AccountId)) {
             contactsByAccount.put(c.AccountId, new List<Contact>());
         }
         contactsByAccount.get(c.AccountId).add(c);
     }
     ```

     DML IN LOOP:
     ```apex
     // Before
     for (Lead lead : leads) {
         lead.Status = 'Working';
         update lead;
     }

     // After - Collect and update once
     for (Lead lead : leads) {
         lead.Status = 'Working';
     }
     update leads;
     ```

     Return: List of files modified with changes made

3. ERROR HANDLING FIX SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Fix error handling issues.

     Issues assigned: [ERROR_ISSUES]

     Read agent: .claude/agents/apex/apex-exception-handler.md
     Read skill: .claude/skills/apex-patterns/

     Error Handling Fix Patterns:

     ADD TRY-CATCH:
     ```apex
     // Before
     HttpResponse response = http.send(request);

     // After
     try {
         HttpResponse response = http.send(request);
         if (response.getStatusCode() != 200) {
             throw new CalloutException('API error: ' + response.getStatus());
         }
     } catch (CalloutException e) {
         Logger.error('Callout failed', e);
         throw new AuraHandledException('Unable to process request');
     }
     ```

     DML ERROR HANDLING:
     ```apex
     // Before
     insert records;

     // After
     Database.SaveResult[] results = Database.insert(records, false);
     for (Database.SaveResult sr : results) {
         if (!sr.isSuccess()) {
             for (Database.Error err : sr.getErrors()) {
                 Logger.error('Insert failed: ' + err.getMessage());
             }
         }
     }
     ```

     Return: List of files modified with changes made

4. PATTERN FIX SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Fix pattern and architecture issues.

     Issues assigned: [PATTERN_ISSUES]

     Read agent: .claude/agents/architecture/pattern-recognition-specialist.md
     Read skill: .claude/skills/apex-patterns/

     Pattern Fix Examples:

     VARIABLE NAMING:
     ```apex
     // Before
     List<Account> a = [SELECT Id FROM Account];

     // After
     List<Account> accounts = [SELECT Id FROM Account];
     ```

     ADD APEXDOC:
     ```apex
     // Before
     public static void processAccounts(List<Account> accounts) {

     // After
     /**
      * @description Processes accounts for scoring calculation
      * @param accounts List of accounts to process
      * @throws AccountServiceException if processing fails
      */
     public static void processAccounts(List<Account> accounts) {
     ```

     Return: List of files modified with changes made
```

### Step 4: Deploy Validation Subagents (PARALLEL)

**After fixes, validate in parallel:**

```
1. TEST EXECUTION SUBAGENT
   subagent_type: "Bash"
   prompt: |
     Run tests for modified files.

     Modified files: [FILE_LIST]

     Commands:
     - Identify test classes for modified files
     - sf apex run test --class-names [TEST_CLASSES] --code-coverage

     Return: Test results summary

2. DEPLOY VALIDATION SUBAGENT
   subagent_type: "Bash"
   prompt: |
     Validate deployment of fixed files.

     Modified files: [FILE_LIST]

     Commands:
     - sf project deploy validate --source-dir [FILES]
     - sf scanner run --target [FILES]

     Return: Deployment validation result
```

### Step 5: Present Results

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ISSUE RESOLUTION COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Resolution Summary

┌──────────────────┬───────┬───────┬─────────┐
│ Category         │ Found │ Fixed │ Skipped │
├──────────────────┼───────┼───────┼─────────┤
│ Security         │     2 │     2 │       0 │
│ Governor Limits  │     2 │     2 │       0 │
│ Error Handling   │     1 │     1 │       0 │
│ Patterns         │     2 │     2 │       0 │
├──────────────────┼───────┼───────┼─────────┤
│ TOTAL            │     9 │     9 │       0 │
└──────────────────┴───────┴───────┴─────────┘

✅ Files Modified:
  • AccountController.cls (security fix)
  • LeadService.cls (security fix)
  • OpportunityHandler.cls (governor fix)
  • ContactBatch.cls (governor fix)
  • CaseHelper.cls (error handling)
  • QuoteService.cls (error handling)
  • AccountUtils.cls (pattern fix)
  • LeadProcessor.cls (pattern fix)

🧪 Validation Results:
  • Tests: 24/24 passing ✅
  • Coverage: 89% (was 85%)
  • Deployment: Valid ✅
  • PMD: No violations ✅

📝 Commit created:
   "fix: Resolve 9 code review issues

   Security:
   - Fix SOQL injection in AccountController
   - Add CRUD checks in LeadService

   Performance:
   - Bulkify DML in OpportunityHandler
   - Remove SOQL from loop in ContactBatch

   Quality:
   - Add error handling to CaseHelper and QuoteService
   - Improve naming and docs in AccountUtils, LeadProcessor"

Next Steps:
  • Push changes: git push
  • Create PR: /sf-deploy pr
  • Re-review: /sf-review
```

---

## Resolution Options

### Resolve All Critical Issues
```bash
/sf-resolve critical
```

### Resolve Specific Issue
```bash
/sf-resolve 1
# Resolves issue #1 only
```

### Resolve by Category
```bash
/sf-resolve security
/sf-resolve governor
/sf-resolve pattern
```

### Interactive Mode
```bash
/sf-resolve
# Shows all issues, prompts for selection
```

---

## Auto-Fix Capabilities

| Issue Type | Auto-Fixable | Notes |
|------------|--------------|-------|
| SOQL Injection | ✅ Yes | Convert to bind variables |
| Missing CRUD | ✅ Yes | Add Schema checks |
| DML in Loop | ✅ Yes | Move outside loop |
| Query in Loop | ✅ Yes | Use Map pattern |
| Null Check | ✅ Yes | Add null guard |
| Error Handling | ⚠️ Partial | May need custom logic |
| Architecture | ❌ No | Requires human decision |

---

## Integration with Workflow

```bash
# After review finds issues
/sf-review              # Finds 9 issues
/sf-resolve critical    # Fix 2 critical issues
/sf-resolve high        # Fix 3 high issues
/sf-test               # Verify fixes
/sf-review             # Re-review (should be clean)
/sf-deploy pr          # Create PR
```
