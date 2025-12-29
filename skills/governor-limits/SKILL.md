---
name: governor-limits
description: Complete Salesforce governor limits reference with strategies to avoid and handle limit exceptions
---

# Salesforce Governor Limits Reference

This skill provides comprehensive governor limit information and strategies for writing limit-safe code.

## Quick Reference Table

### Synchronous Limits

| Limit | Value | Per |
|-------|-------|-----|
| Total SOQL queries | 100 | Transaction |
| Total SOQL rows retrieved | 50,000 | Transaction |
| Total SOSL queries | 20 | Transaction |
| Total DML statements | 150 | Transaction |
| Total DML rows | 10,000 | Transaction |
| Total CPU time | 10,000 ms | Transaction |
| Total heap size | 6 MB | Transaction |
| Total callouts | 100 | Transaction |
| Total callout time | 120 seconds | Transaction |
| Total email invocations | 10 | Transaction |
| Total push notifications | 10 | Transaction |
| Total sendEmail methods | 10 | Transaction |
| Total future calls | 50 | Transaction |
| Total queueable jobs | 50 | Transaction |
| Total event publishes | 150 | Transaction |
| Maximum query rows in batch | 50,000,000 | Batch |

### Asynchronous Limits (Future, Queueable, Batch)

| Limit | Value | Per |
|-------|-------|-----|
| Total SOQL queries | 200 | Transaction |
| Total CPU time | 60,000 ms | Transaction |
| Total heap size | 12 MB | Transaction |
| Queueable jobs from queueable | 1 | Execution |
| Batch executions per 24 hours | 250,000 | Org |

### Static Limits (Cannot Be Changed)

| Limit | Value |
|-------|-------|
| Characters in class | 1,000,000 |
| Characters in trigger | 1,000,000 |
| SOQL query length | 100,000 |
| SOSL query length | 20,000 |
| SOQL offset | 2,000 |
| Subqueries in SOQL | 20 |
| Fields in SOQL | 200 |
| Child relationships in SOQL | 200 |
| Records in Database.insert/update/delete | 10,000 |

## Limit Check Methods

```apex
// Query current usage
System.debug('SOQL Queries: ' + Limits.getQueries() + '/' + Limits.getLimitQueries());
System.debug('DML Statements: ' + Limits.getDmlStatements() + '/' + Limits.getLimitDmlStatements());
System.debug('CPU Time: ' + Limits.getCpuTime() + '/' + Limits.getLimitCpuTime());
System.debug('Heap Size: ' + Limits.getHeapSize() + '/' + Limits.getLimitHeapSize());

// All limit checks
System.debug('SOQL Rows: ' + Limits.getQueryRows() + '/' + Limits.getLimitQueryRows());
System.debug('DML Rows: ' + Limits.getDmlRows() + '/' + Limits.getLimitDmlRows());
System.debug('Callouts: ' + Limits.getCallouts() + '/' + Limits.getLimitCallouts());
System.debug('Future Calls: ' + Limits.getFutureCalls() + '/' + Limits.getLimitFutureCalls());
System.debug('Queueable Jobs: ' + Limits.getQueueableJobs() + '/' + Limits.getLimitQueueableJobs());
```

## Common Limit Exceptions and Solutions

### 1. Too Many SOQL Queries (101)

**Exception**: `System.LimitException: Too many SOQL queries: 101`

**Common Causes**:
- SOQL inside a loop
- Queries in constructor/getter called multiple times
- Recursive triggers without proper guards

**Solutions**:

```apex
// BAD: Query in loop
for (Account acc : accounts) {
    List<Contact> contacts = [SELECT Id FROM Contact WHERE AccountId = :acc.Id];
}

// GOOD: Bulkified query
Map<Id, List<Contact>> contactsByAccount = new Map<Id, List<Contact>>();
for (Contact c : [SELECT Id, AccountId FROM Contact WHERE AccountId IN :accountIds]) {
    if (!contactsByAccount.containsKey(c.AccountId)) {
        contactsByAccount.put(c.AccountId, new List<Contact>());
    }
    contactsByAccount.get(c.AccountId).add(c);
}
```

### 2. Too Many DML Statements (151)

**Exception**: `System.LimitException: Too many DML statements: 151`

**Common Causes**:
- DML inside a loop
- Multiple update calls for same records
- Inefficient trigger recursion

**Solutions**:

```apex
// BAD: DML in loop
for (Account acc : accounts) {
    acc.Status__c = 'Active';
    update acc;
}

// GOOD: Collect and single DML
List<Account> toUpdate = new List<Account>();
for (Account acc : accounts) {
    acc.Status__c = 'Active';
    toUpdate.add(acc);
}
update toUpdate;
```

### 3. Too Many Query Rows (50,001)

**Exception**: `System.LimitException: Too many query rows: 50001`

**Common Causes**:
- Querying large tables without filters
- Aggregate queries on large data sets
- Non-selective queries

**Solutions**:

```apex
// BAD: Unbounded query
List<Contact> allContacts = [SELECT Id FROM Contact];

// GOOD: Paginated query with LIMIT and OFFSET
Integer batchSize = 10000;
Integer offset = 0;
List<Contact> batch = [SELECT Id FROM Contact LIMIT :batchSize OFFSET :offset];

// BETTER: Use Batch Apex for large data sets
global class ProcessContactsBatch implements Database.Batchable<SObject> {
    global Database.QueryLocator start(Database.BatchableContext bc) {
        return Database.getQueryLocator('SELECT Id FROM Contact');
    }
    // ...
}
```

### 4. CPU Time Limit Exceeded

**Exception**: `System.LimitException: Apex CPU time limit exceeded`

**Common Causes**:
- Complex string operations
- Nested loops
- Regex in loops
- Expensive calculations repeated

**Solutions**:

```apex
// BAD: String concatenation in loop
String result = '';
for (Account acc : accounts) {
    result += acc.Name + ', ';
}

// GOOD: Use StringBuilder pattern
List<String> names = new List<String>();
for (Account acc : accounts) {
    names.add(acc.Name);
}
String result = String.join(names, ', ');

// Move heavy processing to async
if (Limits.getCpuTime() > 8000) {  // 80% threshold
    // Queue remaining work
    System.enqueueJob(new ProcessRemainingJob(remainingRecords));
    return;
}
```

### 5. Heap Size Limit Exceeded

**Exception**: `System.LimitException: Apex heap size too large`

**Common Causes**:
- Large collections in memory
- Storing query results that aren't needed
- Large string operations
- Not releasing references

**Solutions**:

```apex
// BAD: Loading all records into memory
List<Contact> allContacts = [SELECT Id, Name, Email, ... 50 fields 
                              FROM Contact];

// GOOD: Query only needed fields
List<Contact> contacts = [SELECT Id, Name FROM Contact];

// BETTER: Process in chunks
for (List<Contact> batch : [SELECT Id, Name FROM Contact]) {
    processBatch(batch);
    // Batch is eligible for GC after this
}

// Clear large collections when done
hugeList.clear();
hugeList = null;
```

### 6. Too Many Future Calls (51)

**Exception**: `System.LimitException: Too many future calls: 51`

**Solutions**:

```apex
// BAD: Future call in loop
for (Account acc : accounts) {
    MyClass.processFuture(acc.Id);
}

// GOOD: Pass collection to single future
@future
public static void processAccounts(Set<Id> accountIds) {
    // Process all accounts
}

// BETTER: Use Queueable with chaining
public class ProcessAccountsJob implements Queueable {
    private List<Id> accountIds;
    private Integer startIndex;
    
    public void execute(QueueableContext ctx) {
        // Process batch
        // Chain next job if more records
        if (startIndex + batchSize < accountIds.size()) {
            System.enqueueJob(new ProcessAccountsJob(accountIds, startIndex + batchSize));
        }
    }
}
```

## Limit-Safe Patterns

### Pattern 1: Governor Limit Monitor

```apex
public class LimitMonitor {
    
    private Integer queryThreshold = 80;   // 80% of limit
    private Integer dmlThreshold = 120;     // 80% of limit
    private Integer cpuThreshold = 8000;    // 80% of limit
    
    public Boolean isApproachingLimits() {
        return Limits.getQueries() >= queryThreshold ||
               Limits.getDmlStatements() >= dmlThreshold ||
               Limits.getCpuTime() >= cpuThreshold;
    }
    
    public void checkAndQueue(List<SObject> remaining, Type jobType) {
        if (isApproachingLimits() && !remaining.isEmpty()) {
            System.enqueueJob((Queueable)jobType.newInstance());
        }
    }
    
    public static String getLimitSummary() {
        return String.format(
            'SOQL: {0}/{1}, DML: {2}/{3}, CPU: {4}/{5}ms, Heap: {6}/{7}',
            new List<Object>{
                Limits.getQueries(), Limits.getLimitQueries(),
                Limits.getDmlStatements(), Limits.getLimitDmlStatements(),
                Limits.getCpuTime(), Limits.getLimitCpuTime(),
                Limits.getHeapSize(), Limits.getLimitHeapSize()
            }
        );
    }
}
```

### Pattern 2: Lazy Loading

```apex
public class AccountService {
    
    // Cache to prevent redundant queries
    private static Map<Id, Account> accountCache = new Map<Id, Account>();
    
    public static Account getAccount(Id accountId) {
        if (!accountCache.containsKey(accountId)) {
            accountCache.put(accountId, 
                [SELECT Id, Name, Industry FROM Account WHERE Id = :accountId]);
        }
        return accountCache.get(accountId);
    }
    
    // Bulk load for multiple IDs
    public static Map<Id, Account> getAccounts(Set<Id> accountIds) {
        Set<Id> uncached = new Set<Id>();
        for (Id accId : accountIds) {
            if (!accountCache.containsKey(accId)) {
                uncached.add(accId);
            }
        }
        
        if (!uncached.isEmpty()) {
            for (Account acc : [SELECT Id, Name, Industry 
                                FROM Account WHERE Id IN :uncached]) {
                accountCache.put(acc.Id, acc);
            }
        }
        
        Map<Id, Account> result = new Map<Id, Account>();
        for (Id accId : accountIds) {
            result.put(accId, accountCache.get(accId));
        }
        return result;
    }
    
    @TestVisible
    private static void clearCache() {
        accountCache.clear();
    }
}
```

### Pattern 3: Query Selector Pattern

```apex
public class AccountSelector {
    
    // Centralized query methods with consistent field sets
    public static final Set<String> DEFAULT_FIELDS = new Set<String>{
        'Id', 'Name', 'Industry', 'AnnualRevenue', 'OwnerId'
    };
    
    public List<Account> selectById(Set<Id> ids) {
        return selectById(ids, DEFAULT_FIELDS);
    }
    
    public List<Account> selectById(Set<Id> ids, Set<String> fields) {
        String query = 'SELECT ' + String.join(new List<String>(fields), ', ') +
                      ' FROM Account WHERE Id IN :ids';
        return Database.query(query);
    }
    
    public List<Account> selectByIdWithContacts(Set<Id> ids) {
        return [
            SELECT Id, Name, Industry,
                   (SELECT Id, Name, Email FROM Contacts)
            FROM Account
            WHERE Id IN :ids
        ];
    }
    
    // Selective query for large tables
    public List<Account> selectActiveByIndustry(String industry) {
        return [
            SELECT Id, Name 
            FROM Account 
            WHERE Industry = :industry 
              AND IsActive__c = true
            LIMIT 10000
        ];
    }
}
```

## Limit Budgeting Strategy

When designing features, budget your limits:

| Component | SOQL | DML | CPU (ms) |
|-----------|------|-----|----------|
| Trigger validation | 5 | 0 | 500 |
| Field updates | 2 | 1 | 200 |
| Related record creation | 5 | 2 | 1000 |
| External callout | 1 | 1 | 2000 |
| Notification flow | 3 | 1 | 500 |
| **Total** | **16** | **5** | **4200** |
| **Budget (80%)** | **80** | **120** | **8000** |
| **Remaining** | **64** | **115** | **3800** |

This ensures headroom for:
- Unexpected trigger recursion
- Platform automation (flows, validation rules)
- Future feature additions
