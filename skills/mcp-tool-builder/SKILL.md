---
name: mcp-tool-builder
description: Building custom MCP server tools — Apex InvocableMethod, Flow tools, prompt templates (with real-world gotchas), dual architecture patterns, and testing
scope: HOSTED_MCP
---

# MCP Tool Builder

**SCOPE: HOSTED_MCP** - This skill applies to building custom tools for Salesforce Hosted MCP Servers.
**Use when:** Creating Apex `@InvocableMethod` actions, Flow-based tools, Named Query APIs, or prompt templates for MCP exposure.

---

Custom MCP servers expose backend logic as tools that AI clients (Claude, ChatGPT, Cursor) can invoke.

**CRITICAL WARNING:** MCP and Agentforce use fundamentally different orchestration models. Code designed for Agentforce will break on MCP unless adapted. See "MCP vs Agentforce Architecture" section.

---

## Tool Types

| Tool Type | Backend | Best For |
|-----------|---------|----------|
| **Apex Invocable Action** | `global` `@InvocableMethod` | Complex logic, orchestration, external callouts |
| **AuraEnabled Method** | `@AuraEnabled` methods | Reusing existing LWC controllers |
| **Apex REST Endpoint** | `@RestResource` classes | Reusing existing custom REST APIs |
| **Flow Action** | Autolaunched Flow | Declarative, admin-maintainable logic |
| **Named Query API** | Admin-defined SOQL | Controlled read-only data access |
| **API Catalog Endpoint** | Cataloged REST APIs | Connect APIs (Billing, CPQ, Field Service, Health Cloud) |

### Decision Guide

```
Is the logic read-only SOQL?
  → Yes → Named Query API
  → No → Does it need code (callouts, complex logic, multi-step)?
    → Yes → Do you have an existing @AuraEnabled or @RestResource class?
      → Yes → Reuse it as an MCP tool
      → No → New Apex @InvocableMethod (global)
    → No → Flow Action (autolaunched only)
```

---

## Apex Invocable Action Tools

### Requirements — ALL of These Are Mandatory

- **Class** must be `global` (not `public`) — `public` classes are invisible to MCP
- **Method** must be `global` with `@InvocableMethod`
- **All inner classes** (Request/Result) must be `global`
- **All fields** in inner classes must be `global`
- Use `with sharing` for user-context enforcement
- Use `WITH SECURITY_ENFORCED` in all SOQL

> **Real-world issue:** `public` classes deploy fine but silently don't appear as MCP tools. There is no error — the tool just doesn't show up. Always use `global`.

### Basic Scaffold

```apex
global with sharing class AccountReviewTool {

    @InvocableMethod(
        label='Review Account'
        description='Retrieves a comprehensive account summary including open opportunities, recent cases, and key contacts for AI-assisted account review'
    )
    global static List<AccountReview> reviewAccount(List<AccountReviewRequest> requests) {
        List<AccountReview> results = new List<AccountReview>();

        Set<Id> accountIds = new Set<Id>();
        for (AccountReviewRequest req : requests) {
            accountIds.add(req.accountId);
        }

        Map<Id, Account> accounts = new Map<Id, Account>([
            SELECT Id, Name, Industry, AnnualRevenue,
                (SELECT Id, Name, Amount, StageName, CloseDate FROM Opportunities WHERE IsClosed = false),
                (SELECT Id, Subject, Status, Priority FROM Cases WHERE IsClosed = false ORDER BY CreatedDate DESC LIMIT 5),
                (SELECT Id, Name, Title, Email FROM Contacts ORDER BY CreatedDate DESC LIMIT 5)
            FROM Account
            WHERE Id IN :accountIds
            WITH SECURITY_ENFORCED
        ]);

        for (AccountReviewRequest req : requests) {
            Account acc = accounts.get(req.accountId);
            AccountReview review = new AccountReview();

            if (acc != null) {
                review.accountName = acc.Name;
                review.industry = acc.Industry;
                review.annualRevenue = acc.AnnualRevenue;
                review.openOpportunityCount = acc.Opportunities.size();
                review.openCaseCount = acc.Cases.size();
                review.contactCount = acc.Contacts.size();
                review.success = true;
            } else {
                review.success = false;
                review.errorMessage = 'Account not found: ' + req.accountId;
            }

            results.add(review);
        }

        return results;
    }

    global class AccountReviewRequest {
        @InvocableVariable(required=true description='The Salesforce Account record ID to review')
        global String accountId;
    }

    global class AccountReview {
        @InvocableVariable(description='Whether the review was successful')
        global Boolean success;

        @InvocableVariable(description='Account name')
        global String accountName;

        @InvocableVariable(description='Industry classification')
        global String industry;

        @InvocableVariable(description='Annual revenue in org currency')
        global Decimal annualRevenue;

        @InvocableVariable(description='Number of open (unclosed) opportunities')
        global Integer openOpportunityCount;

        @InvocableVariable(description='Number of open (unclosed) support cases')
        global Integer openCaseCount;

        @InvocableVariable(description='Total number of contacts on the account')
        global Integer contactCount;

        @InvocableVariable(description='Error message if the review failed')
        global String errorMessage;
    }
}
```

### Accept Both IDs and Human-Readable Identifiers

> **Real-world issue:** AI clients pass Case Numbers like `00001024`, not Salesforce IDs. Tools that only accept 18-char IDs break.

```apex
@InvocableVariable(required=true
    description='Case ID (18-char Salesforce record ID) or Case Number (e.g. 00001024). Accepts either format.')
global String caseId;

// Helper to detect format
private static Boolean isSalesforceId(String input) {
    if (input == null || (input.length() != 15 && input.length() != 18)) {
        return false;
    }
    try {
        Id.valueOf(input);
        return true;
    } catch (StringException e) {
        return false;
    }
}

// Usage:
if (isSalesforceId(req.caseId)) {
    cases = [SELECT Id FROM Case WHERE Id = :req.caseId WITH SECURITY_ENFORCED];
} else {
    cases = [SELECT Id FROM Case WHERE CaseNumber = :req.caseId WITH SECURITY_ENFORCED];
}
```

### Return Formatted Text, Not Raw JSON

> **Real-world issue:** Claude does not auto-apply prompt template formatting. Pre-format output server-side.

```apex
// BAD: Raw data — AI formats unpredictably
result.data = JSON.serialize(caseList);

// GOOD: Pre-formatted — AI presents directly
result.formattedOutput = '## Resolution Briefing\n\n' +
    '**Root Cause:** ' + rootCause + '\n\n' +
    '**Recommended Resolution:**\n' + resolution + '\n\n' +
    '**Similar Cases:** ' + similarCasesFormatted;
```

---

## MCP vs Agentforce Architecture

**This is the most important section.** These use fundamentally different orchestration:

### Agentforce (Inside Salesforce)

```
User → Agentforce Agent → Topic/Action → @InvocableMethod
                       → Prompt Template → Flow data provider → Apex → LLM
```

- Platform orchestrates everything server-side
- Flow data providers work (platform executes them)
- Prompt templates control output format (platform applies them)
- `public` access modifier is sufficient
- SObject inputs are fine (platform constructs them)

### MCP (External AI Clients)

```
User → Claude/Cursor → MCP Server → @InvocableMethod (tool call)
                     → Prompt Template (passive resource — may be ignored)
```

- AI client orchestrates — decides which tools to call and when
- **Flow data providers DON'T work** (MCP can't execute Flows)
- **Prompt templates are passive** — NOT enforced
- `global` access modifier required
- Human-readable inputs preferred (Names, Numbers, not just IDs)

### Dual Architecture Pattern

Design for both paths from the start:

```
                    ┌── Agentforce Path ──┐
                    │  Prompt Template     │
                    │  → Flow             │
                    │  → ContextProvider   │
                    │  → SearchService     │
                    └─────────────────────┘
                              │
Shared: SearchService ←───────┤
(core SOSL + SOQL logic)      │
                              │
                    ┌── MCP Path ─────────┐
                    │  SearchTool (global) │
                    │  → SearchService     │
                    │  → Returns formatted │
                    │    text, not JSON    │
                    └─────────────────────┘
```

| Aspect | MCP Tool | Agentforce Tool |
|--------|----------|-----------------|
| Access modifier | `global` | `public` is fine |
| Output format | Pre-formatted text | Raw data (template formats it) |
| Input types | String IDs + human-readable | SObject records |
| Flow dependencies | None | Flow data providers work |
| Template role | Passive (best-effort) | Enforced by platform |

---

## Flow-Based MCP Tools

Autolaunched Flows can be exposed as MCP tools. **Screen flows and scheduled flows are NOT supported.**

### Design Rules

- Flow type: **Autolaunched** (no screen elements)
- Input variables: Mark "Available for Input" — become MCP tool parameters
- Output variables: Mark "Available for Output" — become tool response
- Variable API names should be descriptive — AI clients see them
- Variable descriptions should be written for AI consumption

> **Important distinction:** Flows exposed as their own MCP server tools (via the Flows server) work fine. What does NOT work is using `flow://` references in `templateDataProviders` within prompt templates.

---

## Named Query API Tools

Admin-defined SOQL queries exposed as read-only MCP tools. Simplest tool type.

```sql
-- Good: Parameterized with clear purpose
SELECT Id, Name, Amount, StageName, CloseDate
FROM Opportunity
WHERE AccountId = :accountId AND IsClosed = false
ORDER BY CloseDate ASC
```

Security: Named Queries inherit the authenticated user's CRUD/FLS/sharing automatically.

---

## Prompt Templates for MCP

### Critical Gotchas (From Real-World Testing)

#### 1. Template Type Values — DO NOT Trust Documentation

The `<type>` field must use exact API picklist values. **Documentation says `FlexTemplate` but the API rejects it.**

| UI Label | Correct API Value | Custom Allowed? | MCP Compatible? |
|----------|-------------------|-----------------|-----------------|
| Global | `einstein_gpt__global` | Yes | **Yes — use this for MCP** |
| Flex | `einstein_gpt__flex` | Yes | Yes (but `global` matches standard pattern) |
| Record Summary | `einstein_gpt__recordSummary` | Yes | Copilot sidebar only |
| Field Generation | `einstein_gpt__fieldCompletion` | Yes | No |
| Sales Email | `einstein_gpt__salesEmail` | Yes | No |
| Global Standard | `einstein_gpt__globalStandard` | **No — Salesforce-managed only** | N/A |

**For MCP: use `einstein_gpt__global`**
**For Agentforce: use `einstein_gpt__flex`**

#### 2. Metadata Fields — API 66.0 Changes

- **`activeVersion`** — **REMOVED in API 66.0.** Do not include.
- **`versionIdentifier`** — **Omit.** Let the platform auto-generate.
- **`FlexTemplate`** — **INVALID.** Use `einstein_gpt__flex` or `einstein_gpt__global`.

#### 3. Input Definitions — Undocumented Syntax

| Input Type | Definition Value | Example |
|------------|-----------------|---------|
| **Free text string** | `primitive://String` | Company name, case number, search query |
| **SObject record** | `SOBJECT://Case` | Case record, Account record |

> **`primitive://String`** is not documented. It was discovered by retrieving the standard `einstein_gpt__accountReviewBriefing` template via REST API.

**To discover valid values from standard templates:**
```bash
sf api request rest "/services/data/v66.0/einstein/prompt-templates/<template_developer_name>" --target-org <org> --method GET
```

#### 4. Flow Data Providers DO NOT Work in MCP

> **Real-world error:** "Failed to attach prompt" in Claude Desktop, or `{"code": -32602, "message": "Unknown tool: invalid_tool_name"}` when MCP tries to resolve `flow://` references.

**Never use `templateDataProviders` with `flow://` in MCP templates.** Instead, instruct the AI to call tools in the template content.

If you need both MCP and Agentforce:
- **Agentforce template:** `einstein_gpt__flex` with Flow data provider
- **MCP template:** `einstein_gpt__global` without data providers — instructions tell AI which tools to call

#### 5. Claude Does NOT Enforce Prompt Template Format

> **Real-world issue:** Template specifies a 5-section output format. Claude ignores it and formats its own way.

**Solutions:**
1. **Pre-format output server-side** (recommended) — Apex tool returns formatted text
2. **Embed format in tool description** — less reliable but helps
3. **Include EXAMPLE OUTPUT in template** — single most effective control

#### 6. ChatGPT Does NOT Support MCP Prompts

Only Claude and Cursor support MCP prompt templates. ChatGPT does not.

### Working Template — String Input (API 66.0)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<GenAiPromptTemplate xmlns="http://soap.sforce.com/2006/04/metadata">
    <!-- NO activeVersion -->
    <developerName>Case_Resolution_MCP</developerName>
    <masterLabel>Case Resolution Briefing</masterLabel>
    <!-- NO relatedEntity for global templates with string inputs -->
    <templateVersions>
        <content>You are a senior support engineer creating a resolution briefing.

STEP 1: Use the "Search Similar Resolved Cases" tool
- Pass {!$Input:caseNumber} as the caseId parameter
- Review the returned resolution data

STEP 2: Create Resolution Briefing

**Root Cause Analysis**
- Primary root cause identified from similar cases
- Contributing factors

**Recommended Resolution**
- Step-by-step resolution procedure
- Expected resolution time

**Similar Resolved Cases**
- List matching cases with resolution summaries

**Confidence Assessment**
- High/Medium/Low based on match quality

EXAMPLE OUTPUT:
"## Root Cause Analysis
The SSL certificate expired on the integration endpoint...

## Recommended Resolution
1. Renew the SSL certificate via...
2. Update the Named Credential...

## Similar Resolved Cases
- Case #00001020 (95% match): Same SSL expiry pattern...

## Confidence: High
3 similar cases found with identical root cause."

Keep the tone professional and actionable.</content>
        <inputs>
            <apiName>caseNumber</apiName>
            <definition>primitive://String</definition>
            <referenceName>Input:caseNumber</referenceName>
            <required>true</required>
        </inputs>
        <primaryModel>sfdc_ai__DefaultGPT4Omni</primaryModel>
        <status>Published</status>
        <!-- NO versionIdentifier -->
    </templateVersions>
    <type>einstein_gpt__global</type>
    <visibility>Global</visibility>
</GenAiPromptTemplate>
```

### Working Template — SObject Input

```xml
<?xml version="1.0" encoding="UTF-8"?>
<GenAiPromptTemplate xmlns="http://soap.sforce.com/2006/04/metadata">
    <developerName>Account_Review_Custom</developerName>
    <masterLabel>Account Review</masterLabel>
    <relatedEntity>Account</relatedEntity>
    <templateVersions>
        <content>Analyze this account:
- Name: {!$Input:Account.Name}
- Industry: {!$Input:Account.Industry}
- Revenue: {!$Input:Account.AnnualRevenue}

Provide a health assessment with risks and next actions.</content>
        <inputs>
            <apiName>myAccount</apiName>
            <definition>SOBJECT://Account</definition>
            <referenceName>Input:Account</referenceName>
            <required>true</required>
        </inputs>
        <primaryModel>sfdc_ai__DefaultGPT4Omni</primaryModel>
        <status>Published</status>
    </templateVersions>
    <type>einstein_gpt__flex</type>
    <visibility>Global</visibility>
</GenAiPromptTemplate>
```

### Template with Apex Data Provider

```xml
<templateDataProviders>
    <definition>apex://CaseResolutionContextProvider</definition>
    <description>Searches similar resolved cases</description>
    <label>Case Resolution Context</label>
    <parameters>
        <definition>primitive://String</definition>
        <isRequired>true</isRequired>
        <parameterName>caseId</parameterName>
        <valueExpression>{!$Input:caseNumber}</valueExpression>
    </parameters>
    <referenceName>Apex:CaseResolutionContextProvider</referenceName>
</templateDataProviders>
```

> **Merge field placement rule:** NEVER put `{!$Apex:...}` merge fields inside instruction sentences. Always put data in a dedicated section BEFORE instructions.

```
## Retrieved Data (merge fields here)
{!$Apex:CaseResolutionContextProvider.resolutionContext}

## Your Task (instructions here — reference "data above")
Using the data above, create a resolution briefing...
```

### MCP Prompt Template Design Pattern ("Executive Briefing")

1. **Role assignment** — "You are a senior support engineer"
2. **Step-by-step tool instructions** — STEP 1, STEP 2 with exact tool names and parameters
3. **Detailed output sections** — Each section with bullet points
4. **Example output** — Complete realistic example (single most effective format control)
5. **Tone instruction** — "Write as if briefing a colleague"

---

## Custom Server Registration

### Step 1: Create Custom Server

Setup > Integration > Salesforce MCP Servers > New Custom MCP Server

### Step 2: Add Tools

Select backing type: Apex Action, Flow, AuraEnabled, Apex REST, Named Query, or API Catalog endpoint.

**Tool names and descriptions are critical** — AI clients use them to decide which tool to invoke.

### Step 3: Publish and Activate

Wait up to 2 minutes for propagation.

### ISV Note

Managed packages cannot directly include MCP server configurations. ISVs expose capabilities through annotated Apex classes or Autolaunched Flows for subscribers to configure.

---

## Testing MCP Tools

### Unit Testing

```apex
@IsTest
private class AccountReviewToolTest {

    @TestSetup
    static void setupTestData() {
        Account testAccount = new Account(Name = 'Test Corp', Industry = 'Technology');
        insert testAccount;

        insert new Opportunity(
            Name = 'Test Opp', AccountId = testAccount.Id,
            StageName = 'Prospecting', CloseDate = Date.today().addDays(30), Amount = 100000
        );
    }

    @IsTest
    static void testReviewAccount_success() {
        Account acc = [SELECT Id FROM Account LIMIT 1];

        AccountReviewTool.AccountReviewRequest req = new AccountReviewTool.AccountReviewRequest();
        req.accountId = acc.Id;

        System.Test.startTest();
        List<AccountReviewTool.AccountReview> results = AccountReviewTool.reviewAccount(
            new List<AccountReviewTool.AccountReviewRequest>{ req }
        );
        System.Test.stopTest();

        System.assertEquals(1, results.size());
        System.assert(results[0].success);
        System.assertEquals('Test Corp', results[0].accountName);
    }
}
```

> **Use `System.Test`** not `Test` — orgs with a custom `Test` class shadow the system class.

### Postman Testing (Raw JSON)

```json
{"method": "tools/call", "params": {"name": "Review Account", "arguments": {"accountId": "001xx000003DGbYAAW"}}}
```

### Integration Testing with AI Clients

After Postman validation:
1. Connect Claude/Cursor to the custom MCP server
2. Ask natural language questions that should trigger each tool
3. Verify AI correctly selects and invokes tools
4. Check that responses are useful and well-structured

---

## Tool Description Best Practices

### Good Descriptions

```apex
@InvocableMethod(
    label='Search Similar Resolved Cases'
    description='Searches for previously resolved cases similar to the given case using subject and description matching. Returns resolution steps, knowledge articles, and confidence scores.'
)

@InvocableVariable(required=true
    description='Case ID (18-char Salesforce record ID) or Case Number (e.g. 00001024). Accepts either format.')
global String caseId;
```

### Bad Descriptions

```apex
// Too vague — AI doesn't know when to use it
description='Processes case data'

// Missing format info — AI doesn't know what to pass
description='The case identifier'
```

### Rules

1. **Describe what, not how** — "Searches similar resolved cases" not "Runs SOSL query"
2. **Document accepted input formats** — "Case ID or Case Number (e.g. 00001024)"
3. **Explain side effects** — "will be added as an internal comment"
4. **Use action verbs** — "Searches", "Retrieves", "Escalates", "Creates"
5. **Describe output** — "Returns resolution steps, knowledge articles, and confidence scores"
