---
name: integration-patterns
description: Salesforce integration patterns for REST, SOAP, Platform Events, and external system connectivity
---

# Salesforce Integration Patterns

Comprehensive guide for integrating Salesforce with external systems.

## REST API Patterns

### Inbound REST (Apex REST)

```apex
@RestResource(urlMapping='/api/v1/accounts/*')
global with sharing class AccountRestService {
    
    @HttpGet
    global static ResponseWrapper getAccount() {
        RestRequest req = RestContext.request;
        RestResponse res = RestContext.response;
        
        String accountId = req.requestURI.substringAfterLast('/');
        
        try {
            Account acc = [
                SELECT Id, Name, Industry, AnnualRevenue
                FROM Account 
                WHERE Id = :accountId
                WITH SECURITY_ENFORCED
            ];
            
            res.statusCode = 200;
            return new ResponseWrapper(true, acc, null);
            
        } catch (QueryException e) {
            res.statusCode = 404;
            return new ResponseWrapper(false, null, 'Account not found');
        }
    }
    
    @HttpPost
    global static ResponseWrapper createAccount() {
        RestRequest req = RestContext.request;
        RestResponse res = RestContext.response;
        
        try {
            AccountRequest accReq = (AccountRequest) JSON.deserialize(
                req.requestBody.toString(),
                AccountRequest.class
            );
            
            Account acc = new Account(
                Name = accReq.name,
                Industry = accReq.industry
            );
            
            insert acc;
            
            res.statusCode = 201;
            return new ResponseWrapper(true, acc, null);
            
        } catch (Exception e) {
            res.statusCode = 400;
            return new ResponseWrapper(false, null, e.getMessage());
        }
    }
    
    global class AccountRequest {
        public String name;
        public String industry;
    }
    
    global class ResponseWrapper {
        public Boolean success;
        public Object data;
        public String error;
        
        public ResponseWrapper(Boolean success, Object data, String error) {
            this.success = success;
            this.data = data;
            this.error = error;
        }
    }
}
```

### Outbound REST (HTTP Callout)

```apex
public class ExternalServiceClient {
    
    private static final String NAMED_CRED = 'callout:External_API';
    
    public ExternalAccount getExternalAccount(String externalId) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint(NAMED_CRED + '/accounts/' + externalId);
        req.setMethod('GET');
        req.setHeader('Accept', 'application/json');
        req.setTimeout(30000);
        
        Http http = new Http();
        HttpResponse res = http.send(req);
        
        if (res.getStatusCode() == 200) {
            return (ExternalAccount) JSON.deserialize(
                res.getBody(), 
                ExternalAccount.class
            );
        } else {
            throw new CalloutException('API Error: ' + res.getStatusCode());
        }
    }
    
    public ExternalAccount createExternalAccount(ExternalAccount acc) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint(NAMED_CRED + '/accounts');
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        req.setBody(JSON.serialize(acc));
        req.setTimeout(30000);
        
        Http http = new Http();
        HttpResponse res = http.send(req);
        
        if (res.getStatusCode() == 201) {
            return (ExternalAccount) JSON.deserialize(
                res.getBody(),
                ExternalAccount.class
            );
        } else {
            throw new CalloutException('Create failed: ' + res.getBody());
        }
    }
    
    public class ExternalAccount {
        public String id;
        public String name;
        public String industry;
    }
}
```

## Async Callout Patterns

### Queueable with Callout

```apex
public class AsyncCalloutJob implements Queueable, Database.AllowsCallouts {
    
    private List<Id> accountIds;
    
    public AsyncCalloutJob(List<Id> accountIds) {
        this.accountIds = accountIds;
    }
    
    public void execute(QueueableContext context) {
        List<Account> accounts = [
            SELECT Id, External_Id__c 
            FROM Account 
            WHERE Id IN :accountIds
        ];
        
        ExternalServiceClient client = new ExternalServiceClient();
        List<Account> toUpdate = new List<Account>();
        
        for (Account acc : accounts) {
            try {
                ExternalServiceClient.ExternalAccount extAcc = 
                    client.getExternalAccount(acc.External_Id__c);
                
                acc.External_Status__c = 'Synced';
                acc.Last_Sync_Date__c = DateTime.now();
                toUpdate.add(acc);
                
            } catch (Exception e) {
                acc.External_Status__c = 'Error';
                acc.Sync_Error__c = e.getMessage();
                toUpdate.add(acc);
            }
        }
        
        update toUpdate;
    }
}

// Usage
System.enqueueJob(new AsyncCalloutJob(accountIds));
```

### Future Method Callout

```apex
public class AccountSyncService {
    
    @future(callout=true)
    public static void syncToExternal(Set<Id> accountIds) {
        List<Account> accounts = [
            SELECT Id, Name, Industry, External_Id__c
            FROM Account
            WHERE Id IN :accountIds
        ];
        
        ExternalServiceClient client = new ExternalServiceClient();
        
        for (Account acc : accounts) {
            try {
                if (String.isBlank(acc.External_Id__c)) {
                    // Create in external system
                    ExternalServiceClient.ExternalAccount extAcc = 
                        new ExternalServiceClient.ExternalAccount();
                    extAcc.name = acc.Name;
                    extAcc.industry = acc.Industry;
                    
                    ExternalServiceClient.ExternalAccount created = 
                        client.createExternalAccount(extAcc);
                    
                    acc.External_Id__c = created.id;
                }
            } catch (Exception e) {
                System.debug('Sync failed: ' + e.getMessage());
            }
        }
        
        update accounts;
    }
}
```

## Platform Events

### Event Definition
```xml
<!-- Order_Event__e.object-meta.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <deploymentStatus>Deployed</deploymentStatus>
    <eventType>HighVolume</eventType>
    <label>Order Event</label>
    <pluralLabel>Order Events</pluralLabel>
    <publishBehavior>PublishAfterCommit</publishBehavior>
    <fields>
        <fullName>Order_Id__c</fullName>
        <label>Order Id</label>
        <type>Text</type>
        <length>18</length>
    </fields>
    <fields>
        <fullName>Action__c</fullName>
        <label>Action</label>
        <type>Text</type>
        <length>50</length>
    </fields>
</CustomObject>
```

### Publishing Events

```apex
public class OrderEventPublisher {
    
    public static void publishOrderCreated(List<Order__c> orders) {
        List<Order_Event__e> events = new List<Order_Event__e>();
        
        for (Order__c order : orders) {
            events.add(new Order_Event__e(
                Order_Id__c = order.Id,
                Action__c = 'CREATED'
            ));
        }
        
        List<Database.SaveResult> results = EventBus.publish(events);
        
        for (Database.SaveResult result : results) {
            if (!result.isSuccess()) {
                for (Database.Error error : result.getErrors()) {
                    System.debug('Publish error: ' + error.getMessage());
                }
            }
        }
    }
}
```

### Subscribing to Events

```apex
trigger OrderEventTrigger on Order_Event__e (after insert) {
    for (Order_Event__e event : Trigger.new) {
        switch on event.Action__c {
            when 'CREATED' {
                handleOrderCreated(event);
            }
            when 'UPDATED' {
                handleOrderUpdated(event);
            }
        }
    }
}
```

## Change Data Capture

```apex
trigger AccountChangeEventTrigger on AccountChangeEvent (after insert) {
    for (AccountChangeEvent event : Trigger.new) {
        EventBus.ChangeEventHeader header = event.ChangeEventHeader;
        
        String changeType = header.getChangeType();
        List<String> changedFields = header.getChangedFields();
        
        switch on changeType {
            when 'CREATE' {
                handleCreate(event);
            }
            when 'UPDATE' {
                handleUpdate(event, changedFields);
            }
            when 'DELETE' {
                handleDelete(event);
            }
        }
    }
}
```

## Webhook Pattern (Outbound)

```apex
public class WebhookService {
    
    @future(callout=true)
    public static void sendWebhook(String payload, String webhookUrl) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint(webhookUrl);
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        req.setBody(payload);
        req.setTimeout(10000);
        
        try {
            Http http = new Http();
            HttpResponse res = http.send(req);
            
            if (res.getStatusCode() >= 200 && res.getStatusCode() < 300) {
                System.debug('Webhook sent successfully');
            } else {
                System.debug('Webhook failed: ' + res.getStatusCode());
            }
        } catch (Exception e) {
            System.debug('Webhook error: ' + e.getMessage());
        }
    }
}
```
