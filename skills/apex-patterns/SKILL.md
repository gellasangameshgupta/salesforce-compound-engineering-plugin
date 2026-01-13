---
name: apex-patterns
description: Common Apex design patterns including Selector, Service, Domain, and Trigger Handler patterns
---

# Apex Design Patterns

Common design patterns for scalable, maintainable Salesforce Apex development.

## Trigger Handler Pattern

### Base Handler Class
```apex
public virtual class TriggerHandler {
    
    private static Map<String, LoopCount> loopCountMap;
    private static Set<String> bypassedHandlers;
    
    static {
        loopCountMap = new Map<String, LoopCount>();
        bypassedHandlers = new Set<String>();
    }
    
    @TestVisible
    private TriggerOperation context;
    
    @TestVisible
    private Boolean isTriggerExecuting;
    
    public TriggerHandler() {
        this.setTriggerContext();
    }
    
    public void run() {
        if (!validateRun()) return;
        addToLoopCount();
        
        switch on context {
            when BEFORE_INSERT { this.beforeInsert(); }
            when BEFORE_UPDATE { this.beforeUpdate(); }
            when BEFORE_DELETE { this.beforeDelete(); }
            when AFTER_INSERT { this.afterInsert(); }
            when AFTER_UPDATE { this.afterUpdate(); }
            when AFTER_DELETE { this.afterDelete(); }
            when AFTER_UNDELETE { this.afterUndelete(); }
        }
    }
    
    // Context methods - override in concrete handlers
    protected virtual void beforeInsert() {}
    protected virtual void beforeUpdate() {}
    protected virtual void beforeDelete() {}
    protected virtual void afterInsert() {}
    protected virtual void afterUpdate() {}
    protected virtual void afterDelete() {}
    protected virtual void afterUndelete() {}
    
    // Bypass methods
    public static void bypass(String handlerName) {
        bypassedHandlers.add(handlerName);
    }
    
    public static void clearBypass(String handlerName) {
        bypassedHandlers.remove(handlerName);
    }
    
    public static Boolean isBypassed(String handlerName) {
        return bypassedHandlers.contains(handlerName);
    }
    
    public static void clearAllBypasses() {
        bypassedHandlers.clear();
    }
    
    // Loop count methods
    public void setMaxLoopCount(Integer max) {
        String handlerName = getHandlerName();
        if (!loopCountMap.containsKey(handlerName)) {
            loopCountMap.put(handlerName, new LoopCount(max));
        } else {
            loopCountMap.get(handlerName).setMax(max);
        }
    }
    
    // Private methods
    @TestVisible
    private void setTriggerContext() {
        this.isTriggerExecuting = Trigger.isExecuting;
        this.context = Trigger.operationType;
    }
    
    private Boolean validateRun() {
        if (!this.isTriggerExecuting || this.context == null) {
            throw new TriggerHandlerException('Trigger handler called outside of trigger context');
        }
        return !bypassedHandlers.contains(getHandlerName());
    }
    
    private String getHandlerName() {
        return String.valueOf(this).split(':')[0];
    }
    
    private void addToLoopCount() {
        String handlerName = getHandlerName();
        if (loopCountMap.containsKey(handlerName)) {
            Boolean exceeded = loopCountMap.get(handlerName).increment();
            if (exceeded) {
                throw new TriggerHandlerException('Maximum loop count exceeded for ' + handlerName);
            }
        }
    }
    
    // Inner classes
    @TestVisible
    private class LoopCount {
        private Integer max;
        private Integer count;
        
        public LoopCount(Integer max) {
            this.max = max;
            this.count = 0;
        }
        
        public Boolean increment() {
            this.count++;
            return this.count > this.max;
        }
        
        public void setMax(Integer max) {
            this.max = max;
        }
    }
    
    public class TriggerHandlerException extends Exception {}
}
```

### Concrete Handler Example
```apex
public class AccountTriggerHandler extends TriggerHandler {
    
    private List<Account> newAccounts;
    private List<Account> oldAccounts;
    private Map<Id, Account> newAccountMap;
    private Map<Id, Account> oldAccountMap;
    
    public AccountTriggerHandler() {
        this.newAccounts = (List<Account>) Trigger.new;
        this.oldAccounts = (List<Account>) Trigger.old;
        this.newAccountMap = (Map<Id, Account>) Trigger.newMap;
        this.oldAccountMap = (Map<Id, Account>) Trigger.oldMap;
    }
    
    protected override void beforeInsert() {
        setDefaults();
        validateAccounts();
    }
    
    protected override void afterInsert() {
        createRelatedRecords();
    }
    
    protected override void beforeUpdate() {
        validateAccounts();
    }
    
    protected override void afterUpdate() {
        syncToExternalSystem();
    }
    
    // Private methods
    private void setDefaults() {
        for (Account acc : newAccounts) {
            if (String.isBlank(acc.Industry)) {
                acc.Industry = 'Other';
            }
        }
    }
    
    private void validateAccounts() {
        for (Account acc : newAccounts) {
            if (acc.AnnualRevenue < 0) {
                acc.AnnualRevenue.addError('Revenue cannot be negative');
            }
        }
    }
    
    private void createRelatedRecords() {
        // Implementation
    }
    
    private void syncToExternalSystem() {
        // Implementation
    }
}
```

## Selector Pattern

```apex
public inherited sharing class AccountSelector {
    
    private static final Set<String> DEFAULT_FIELDS = new Set<String>{
        'Id', 'Name', 'Industry', 'AnnualRevenue', 'OwnerId', 'CreatedDate'
    };
    
    public List<Account> selectById(Set<Id> ids) {
        return selectById(ids, DEFAULT_FIELDS);
    }
    
    public List<Account> selectById(Set<Id> ids, Set<String> fields) {
        String query = buildQuery(fields) + ' WHERE Id IN :ids';
        return Database.query(query);
    }
    
    public List<Account> selectByIndustry(String industry) {
        return [
            SELECT Id, Name, Industry, AnnualRevenue
            FROM Account
            WHERE Industry = :industry
            WITH SECURITY_ENFORCED
            ORDER BY Name
        ];
    }
    
    public List<Account> selectWithContacts(Set<Id> ids) {
        return [
            SELECT Id, Name, Industry,
                   (SELECT Id, Name, Email FROM Contacts ORDER BY Name)
            FROM Account
            WHERE Id IN :ids
            WITH SECURITY_ENFORCED
        ];
    }
    
    public List<Account> selectRecentlyModified(Integer days) {
        DateTime threshold = DateTime.now().addDays(-days);
        return [
            SELECT Id, Name, Industry, LastModifiedDate
            FROM Account
            WHERE LastModifiedDate >= :threshold
            WITH SECURITY_ENFORCED
            ORDER BY LastModifiedDate DESC
        ];
    }
    
    private String buildQuery(Set<String> fields) {
        return 'SELECT ' + String.join(new List<String>(fields), ', ') + ' FROM Account';
    }
}
```

## Service Pattern

```apex
public with sharing class AccountService {
    
    private AccountSelector selector;
    
    public AccountService() {
        this.selector = new AccountSelector();
    }
    
    public void activateAccounts(Set<Id> accountIds) {
        List<Account> accounts = selector.selectById(accountIds);
        
        for (Account acc : accounts) {
            acc.Status__c = 'Active';
            acc.Activated_Date__c = Date.today();
        }
        
        SecureDML.secureUpdate(accounts);
    }
    
    public Map<Id, Decimal> calculateAccountScores(Set<Id> accountIds) {
        List<Account> accounts = selector.selectWithContacts(accountIds);
        Map<Id, Decimal> scores = new Map<Id, Decimal>();
        
        for (Account acc : accounts) {
            Decimal score = calculateScore(acc);
            scores.put(acc.Id, score);
        }
        
        return scores;
    }
    
    public void mergeAccounts(Id masterAccountId, Set<Id> duplicateIds) {
        // Business logic for merging accounts
        Account master = selector.selectById(new Set<Id>{masterAccountId})[0];
        List<Account> duplicates = selector.selectById(duplicateIds);
        
        // Merge logic
        for (Account dup : duplicates) {
            // Transfer relationships, merge data
        }
        
        delete duplicates;
    }
    
    private Decimal calculateScore(Account acc) {
        Decimal score = 0;
        
        if (acc.AnnualRevenue != null) {
            score += acc.AnnualRevenue / 10000;
        }
        
        if (acc.Contacts != null) {
            score += acc.Contacts.size() * 5;
        }
        
        return score;
    }
}
```

## Domain Pattern (fflib style)

```apex
public class Accounts extends fflib_SObjectDomain {
    
    public Accounts(List<Account> records) {
        super(records);
    }
    
    public override void onBeforeInsert() {
        setDefaults();
        validate();
    }
    
    public override void onBeforeUpdate(Map<Id, SObject> existingRecords) {
        validate();
        detectChanges((Map<Id, Account>) existingRecords);
    }
    
    public override void onAfterInsert() {
        createWelcomeTasks();
    }
    
    private void setDefaults() {
        for (Account acc : (List<Account>) Records) {
            if (acc.Rating == null) {
                acc.Rating = 'Cold';
            }
        }
    }
    
    private void validate() {
        for (Account acc : (List<Account>) Records) {
            if (acc.Name != null && acc.Name.length() > 100) {
                acc.Name.addError('Name cannot exceed 100 characters');
            }
        }
    }
    
    private void detectChanges(Map<Id, Account> oldAccounts) {
        for (Account acc : (List<Account>) Records) {
            Account oldAcc = oldAccounts.get(acc.Id);
            if (acc.OwnerId != oldAcc.OwnerId) {
                // Owner changed - do something
            }
        }
    }
    
    private void createWelcomeTasks() {
        List<Task> tasks = new List<Task>();
        for (Account acc : (List<Account>) Records) {
            tasks.add(new Task(
                WhatId = acc.Id,
                OwnerId = acc.OwnerId,
                Subject = 'Welcome call for ' + acc.Name,
                ActivityDate = Date.today().addDays(7)
            ));
        }
        insert tasks;
    }
    
    public class Constructor implements fflib_SObjectDomain.IConstructable {
        public fflib_SObjectDomain construct(List<SObject> records) {
            return new Accounts(records);
        }
    }
}
```

## Unit of Work Pattern

```apex
public class AccountUnitOfWork {
    
    private List<Account> newAccounts = new List<Account>();
    private List<Account> updatedAccounts = new List<Account>();
    private List<Contact> newContacts = new List<Contact>();
    private List<Opportunity> newOpportunities = new List<Opportunity>();
    
    public void registerNew(Account acc) {
        newAccounts.add(acc);
    }
    
    public void registerDirty(Account acc) {
        updatedAccounts.add(acc);
    }
    
    public void registerNewContact(Contact con) {
        newContacts.add(con);
    }
    
    public void registerNewOpportunity(Opportunity opp) {
        newOpportunities.add(opp);
    }
    
    public void commitWork() {
        Savepoint sp = Database.setSavepoint();
        
        try {
            if (!newAccounts.isEmpty()) {
                insert newAccounts;
            }
            
            if (!updatedAccounts.isEmpty()) {
                update updatedAccounts;
            }
            
            // Set relationships after account insert
            for (Contact con : newContacts) {
                // Assuming AccountId was set to index reference
            }
            
            if (!newContacts.isEmpty()) {
                insert newContacts;
            }
            
            if (!newOpportunities.isEmpty()) {
                insert newOpportunities;
            }
            
        } catch (Exception e) {
            Database.rollback(sp);
            throw e;
        }
    }
}
```
