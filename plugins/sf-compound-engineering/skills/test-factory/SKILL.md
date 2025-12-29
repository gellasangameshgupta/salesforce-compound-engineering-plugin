---
name: test-factory
description: Test data factory patterns and utilities for Salesforce Apex testing
---

# Test Data Factory Patterns

Comprehensive test data factory for creating consistent, maintainable test data.

## Core Factory Class

```apex
@isTest
public class TestDataFactory {
    
    // ==================== ACCOUNTS ====================
    
    public static Account createAccount() {
        return createAccount(new Map<String, Object>());
    }
    
    public static Account createAccount(Map<String, Object> overrides) {
        Account acc = new Account(
            Name = 'Test Account ' + generateUniqueSuffix(),
            Industry = 'Technology',
            Type = 'Customer',
            BillingStreet = '123 Test Street',
            BillingCity = 'San Francisco',
            BillingState = 'CA',
            BillingPostalCode = '94102',
            BillingCountry = 'USA',
            Phone = '555-1234',
            Website = 'www.testaccount.com'
        );
        
        applyOverrides(acc, overrides);
        return acc;
    }
    
    public static List<Account> createAccounts(Integer count) {
        return createAccounts(count, new Map<String, Object>());
    }
    
    public static List<Account> createAccounts(Integer count, Map<String, Object> overrides) {
        List<Account> accounts = new List<Account>();
        for (Integer i = 0; i < count; i++) {
            Map<String, Object> recordOverrides = overrides.clone();
            if (!recordOverrides.containsKey('Name')) {
                recordOverrides.put('Name', 'Test Account ' + i + ' ' + generateUniqueSuffix());
            }
            accounts.add(createAccount(recordOverrides));
        }
        return accounts;
    }
    
    // ==================== CONTACTS ====================
    
    public static Contact createContact(Id accountId) {
        return createContact(accountId, new Map<String, Object>());
    }
    
    public static Contact createContact(Id accountId, Map<String, Object> overrides) {
        String suffix = generateUniqueSuffix();
        Contact con = new Contact(
            FirstName = 'Test',
            LastName = 'Contact ' + suffix,
            Email = 'test.contact.' + suffix + '@example.com',
            Phone = '555-5678',
            AccountId = accountId,
            Title = 'Test Title',
            MailingStreet = '123 Test Street',
            MailingCity = 'San Francisco',
            MailingState = 'CA',
            MailingPostalCode = '94102',
            MailingCountry = 'USA'
        );
        
        applyOverrides(con, overrides);
        return con;
    }
    
    public static List<Contact> createContacts(Id accountId, Integer count) {
        List<Contact> contacts = new List<Contact>();
        for (Integer i = 0; i < count; i++) {
            contacts.add(createContact(accountId));
        }
        return contacts;
    }
    
    // ==================== OPPORTUNITIES ====================
    
    public static Opportunity createOpportunity(Id accountId) {
        return createOpportunity(accountId, new Map<String, Object>());
    }
    
    public static Opportunity createOpportunity(Id accountId, Map<String, Object> overrides) {
        Opportunity opp = new Opportunity(
            Name = 'Test Opportunity ' + generateUniqueSuffix(),
            AccountId = accountId,
            StageName = 'Prospecting',
            CloseDate = Date.today().addDays(30),
            Amount = 10000,
            Probability = 20,
            Type = 'New Business'
        );
        
        applyOverrides(opp, overrides);
        return opp;
    }
    
    public static List<Opportunity> createOpportunities(Id accountId, Integer count) {
        List<Opportunity> opportunities = new List<Opportunity>();
        for (Integer i = 0; i < count; i++) {
            opportunities.add(createOpportunity(accountId));
        }
        return opportunities;
    }
    
    // ==================== LEADS ====================
    
    public static Lead createLead() {
        return createLead(new Map<String, Object>());
    }
    
    public static Lead createLead(Map<String, Object> overrides) {
        String suffix = generateUniqueSuffix();
        Lead ld = new Lead(
            FirstName = 'Test',
            LastName = 'Lead ' + suffix,
            Company = 'Test Company ' + suffix,
            Email = 'test.lead.' + suffix + '@example.com',
            Phone = '555-9012',
            Status = 'Open - Not Contacted',
            Industry = 'Technology',
            LeadSource = 'Web'
        );
        
        applyOverrides(ld, overrides);
        return ld;
    }
    
    public static List<Lead> createLeads(Integer count) {
        List<Lead> leads = new List<Lead>();
        for (Integer i = 0; i < count; i++) {
            leads.add(createLead());
        }
        return leads;
    }
    
    // ==================== CASES ====================
    
    public static Case createCase(Id accountId, Id contactId) {
        return createCase(accountId, contactId, new Map<String, Object>());
    }
    
    public static Case createCase(Id accountId, Id contactId, Map<String, Object> overrides) {
        Case cs = new Case(
            AccountId = accountId,
            ContactId = contactId,
            Subject = 'Test Case ' + generateUniqueSuffix(),
            Description = 'Test case description',
            Status = 'New',
            Priority = 'Medium',
            Origin = 'Web'
        );
        
        applyOverrides(cs, overrides);
        return cs;
    }
    
    // ==================== USERS ====================
    
    public static User createUser(String profileName) {
        return createUser(profileName, new Map<String, Object>());
    }
    
    public static User createUser(String profileName, Map<String, Object> overrides) {
        Profile p = [SELECT Id FROM Profile WHERE Name = :profileName LIMIT 1];
        String suffix = generateUniqueSuffix();
        
        User u = new User(
            FirstName = 'Test',
            LastName = 'User ' + suffix,
            Email = 'testuser' + suffix + '@example.com',
            Username = 'testuser' + suffix + '@example.com.test',
            Alias = suffix.left(8),
            ProfileId = p.Id,
            TimeZoneSidKey = 'America/Los_Angeles',
            LocaleSidKey = 'en_US',
            EmailEncodingKey = 'UTF-8',
            LanguageLocaleKey = 'en_US',
            IsActive = true
        );
        
        applyOverrides(u, overrides);
        return u;
    }
    
    // ==================== HELPER METHODS ====================
    
    private static String generateUniqueSuffix() {
        return String.valueOf(DateTime.now().getTime()) + 
               String.valueOf(Math.abs(Crypto.getRandomInteger())).left(4);
    }
    
    private static void applyOverrides(SObject record, Map<String, Object> overrides) {
        for (String field : overrides.keySet()) {
            record.put(field, overrides.get(field));
        }
    }
    
    // ==================== BULK INSERT HELPERS ====================
    
    public static List<Account> createAndInsertAccounts(Integer count) {
        List<Account> accounts = createAccounts(count);
        insert accounts;
        return accounts;
    }
    
    public static Map<Id, List<Contact>> createAccountsWithContacts(
        Integer accountCount, 
        Integer contactsPerAccount
    ) {
        List<Account> accounts = createAccounts(accountCount);
        insert accounts;
        
        Map<Id, List<Contact>> contactsByAccount = new Map<Id, List<Contact>>();
        List<Contact> allContacts = new List<Contact>();
        
        for (Account acc : accounts) {
            List<Contact> contacts = createContacts(acc.Id, contactsPerAccount);
            contactsByAccount.put(acc.Id, contacts);
            allContacts.addAll(contacts);
        }
        
        insert allContacts;
        return contactsByAccount;
    }
}
```

## Usage Examples

### Basic Usage
```apex
@isTest
static void testAccountCreation() {
    // Simple account
    Account acc = TestDataFactory.createAccount();
    insert acc;
    
    // Account with overrides
    Account customAcc = TestDataFactory.createAccount(new Map<String, Object>{
        'Name' => 'Custom Account Name',
        'Industry' => 'Finance',
        'AnnualRevenue' => 1000000
    });
    insert customAcc;
}
```

### Bulk Testing
```apex
@isTest
static void testBulkOperation() {
    // Create 200+ records for bulk testing
    List<Account> accounts = TestDataFactory.createAccounts(200);
    insert accounts;
    
    Test.startTest();
    // Your bulk operation here
    Test.stopTest();
}
```

### TestSetup Method
```apex
@isTest
private class AccountServiceTest {
    
    @TestSetup
    static void setup() {
        // Shared test data
        List<Account> accounts = TestDataFactory.createAccounts(5);
        insert accounts;
        
        List<Contact> allContacts = new List<Contact>();
        for (Account acc : accounts) {
            allContacts.addAll(TestDataFactory.createContacts(acc.Id, 3));
        }
        insert allContacts;
    }
    
    @isTest
    static void testMethod1() {
        List<Account> accounts = [SELECT Id FROM Account];
        // Use the test data
    }
}
```

### User Context Testing
```apex
@isTest
static void testAsStandardUser() {
    User standardUser = TestDataFactory.createUser('Standard User');
    insert standardUser;
    
    System.runAs(standardUser) {
        // Test as standard user
        Account acc = TestDataFactory.createAccount();
        insert acc;
        
        // Assertions
    }
}
```
