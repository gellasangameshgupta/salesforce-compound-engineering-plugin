---
name: security-guide
description: Comprehensive Salesforce security best practices and implementation patterns
---

# Salesforce Security Guide

Complete reference for implementing security best practices in Salesforce development.

## CRUD/FLS Enforcement

### Object-Level Security

```apex
// Check before query
if (!Schema.sObjectType.Account.isAccessible()) {
    throw new AuraHandledException('You do not have access to view Accounts');
}

// Check before insert
if (!Schema.sObjectType.Account.isCreateable()) {
    throw new AuraHandledException('You do not have permission to create Accounts');
}

// Check before update
if (!Schema.sObjectType.Account.isUpdateable()) {
    throw new AuraHandledException('You do not have permission to update Accounts');
}

// Check before delete
if (!Schema.sObjectType.Account.isDeletable()) {
    throw new AuraHandledException('You do not have permission to delete Accounts');
}
```

### Field-Level Security

```apex
// Check field accessibility
if (!Schema.sObjectType.Account.fields.AnnualRevenue.isAccessible()) {
    // Don't include in query or mask value
}

// Check field updateability
if (!Schema.sObjectType.Account.fields.AnnualRevenue.isUpdateable()) {
    // Don't allow field update
}

// Using WITH SECURITY_ENFORCED (Spring '19+)
List<Account> accounts = [
    SELECT Id, Name, AnnualRevenue 
    FROM Account 
    WITH SECURITY_ENFORCED
];

// Using Security.stripInaccessible (Spring '19+)
List<Account> accounts = [SELECT Id, Name, AnnualRevenue FROM Account];
SObjectAccessDecision decision = Security.stripInaccessible(
    AccessType.READABLE,
    accounts
);
List<Account> sanitizedAccounts = decision.getRecords();
```

### Bulk CRUD Check Pattern

```apex
public class SecureDML {
    
    public static void secureInsert(List<SObject> records) {
        if (records.isEmpty()) return;
        
        Schema.SObjectType objType = records[0].getSObjectType();
        if (!objType.getDescribe().isCreateable()) {
            throw new SecurityException('Cannot create ' + objType);
        }
        
        SObjectAccessDecision decision = Security.stripInaccessible(
            AccessType.CREATABLE,
            records
        );
        insert decision.getRecords();
    }
    
    public static void secureUpdate(List<SObject> records) {
        if (records.isEmpty()) return;
        
        Schema.SObjectType objType = records[0].getSObjectType();
        if (!objType.getDescribe().isUpdateable()) {
            throw new SecurityException('Cannot update ' + objType);
        }
        
        SObjectAccessDecision decision = Security.stripInaccessible(
            AccessType.UPDATABLE,
            records
        );
        update decision.getRecords();
    }
}
```

## Sharing Model

### Class Sharing Keywords

```apex
// Enforces sharing rules - USE BY DEFAULT
public with sharing class UserFacingController {
    // User can only see records they have access to
}

// Bypasses sharing rules - USE SPARINGLY
public without sharing class SystemService {
    // Only for background processes that need full access
    // Always document why this is needed
}

// Inherits from calling class
public inherited sharing class UtilityClass {
    // Flexible - uses caller's sharing context
}
```

### When to Use Each

| Keyword | Use Case |
|---------|----------|
| `with sharing` | User-facing controllers, AuraEnabled methods |
| `without sharing` | System processes, data cleanup, reports |
| `inherited sharing` | Utility classes, shared libraries |

## SOQL Injection Prevention

### Vulnerable Code
```apex
// NEVER DO THIS
String searchTerm = userInput;
String query = 'SELECT Id, Name FROM Account WHERE Name LIKE \'%' + searchTerm + '%\'';
List<Account> accounts = Database.query(query);
```

### Secure Alternatives

```apex
// Option 1: Static SOQL with bind variable (PREFERRED)
String searchTerm = '%' + userInput + '%';
List<Account> accounts = [SELECT Id, Name FROM Account WHERE Name LIKE :searchTerm];

// Option 2: Escaped dynamic SOQL (when dynamic is necessary)
String searchTerm = '%' + String.escapeSingleQuotes(userInput) + '%';
String query = 'SELECT Id, Name FROM Account WHERE Name LIKE \'' + searchTerm + '\'';
List<Account> accounts = Database.query(query);

// Option 3: SOSL for search
String searchTerm = String.escapeSingleQuotes(userInput);
List<List<SObject>> results = [FIND :searchTerm IN ALL FIELDS RETURNING Account(Id, Name)];
```

## XSS Prevention

### In Visualforce
```html
<!-- Text output - auto-escaped -->
{!account.Name}

<!-- Explicit encoding functions -->
{!HTMLENCODE(userInput)}
{!JSENCODE(userInput)}
{!JSINHTMLENCODE(userInput)}
{!URLENCODE(userInput)}
```

### In LWC
```javascript
// Safe: Template expressions are auto-escaped
// In template: {userInput}

// DANGER: Never use innerHTML with user data
element.innerHTML = userInput; // XSS VULNERABILITY!

// Safe: Use textContent
element.textContent = userInput;
```

## Sensitive Data Handling

### Never Hardcode Credentials
```apex
// WRONG
String apiKey = 'sk-12345abcdef';  // Never do this!

// RIGHT - Use Named Credentials
HttpRequest req = new HttpRequest();
req.setEndpoint('callout:My_Named_Credential/endpoint');

// RIGHT - Use Protected Custom Settings
API_Settings__c settings = API_Settings__c.getOrgDefaults();
String apiKey = settings.API_Key__c;

// RIGHT - Use Custom Metadata
API_Config__mdt config = [SELECT API_Key__c FROM API_Config__mdt WHERE DeveloperName = 'Production'];
```

### Secure Logging
```apex
// Never log sensitive data
System.debug('Processing user: ' + userId);  // OK
System.debug('Password: ' + password);        // NEVER!
System.debug('SSN: ' + ssn);                  // NEVER!
System.debug('Credit Card: ' + cardNumber);   // NEVER!

// Mask sensitive data
public static String maskSSN(String ssn) {
    if (String.isBlank(ssn) || ssn.length() < 4) return '***';
    return '***-**-' + ssn.right(4);
}
```

## Security Headers (Experience Cloud)

```apex
// In controller or filter
public PageReference setSecurityHeaders() {
    ApexPages.currentPage().getHeaders().put('X-Content-Type-Options', 'nosniff');
    ApexPages.currentPage().getHeaders().put('X-Frame-Options', 'SAMEORIGIN');
    ApexPages.currentPage().getHeaders().put('X-XSS-Protection', '1; mode=block');
    return null;
}
```

## Security Checklist

### Before Code Review
- [ ] All queries use bind variables or SECURITY_ENFORCED
- [ ] CRUD/FLS checks on all DML operations
- [ ] Classes use appropriate sharing keyword
- [ ] No hardcoded credentials or sensitive data
- [ ] User input validated and sanitized
- [ ] Sensitive data not logged
- [ ] LWC components don't use innerHTML with user data

### Before Deployment
- [ ] Security review completed
- [ ] Penetration testing (if applicable)
- [ ] Permission sets configured correctly
- [ ] Sharing rules validated
