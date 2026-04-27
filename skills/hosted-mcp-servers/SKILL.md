---
name: hosted-mcp-servers
description: Salesforce Hosted MCP Server setup, configuration, URL patterns, ECA management, security model, complete tool reference, and troubleshooting
scope: HOSTED_MCP
---

# Salesforce Hosted MCP Servers

**SCOPE: HOSTED_MCP** - This skill applies to setting up and configuring Salesforce Hosted MCP Servers.
**Use when:** Enabling MCP servers in an org, creating External Client Apps, connecting AI clients (Claude, Cursor, ChatGPT), or troubleshooting MCP connectivity.

---

Salesforce Hosted MCP Servers are fully managed, cloud-hosted MCP (Model Context Protocol) servers that let AI clients access Salesforce data and logic. All processing is **deterministic** — no LLM runs server-side. Intelligence is entirely on the client side.

**This is different from** the `@salesforce/mcp` CLI-based MCP server used for local development.

---

## Available Servers (Complete Reference)

### SObject Servers

| Server | API Name | Capabilities | Risk Level |
|--------|----------|-------------|------------|
| **SObject Reads** | `platform/sobject-reads` | Query, search, schema, relationships (read-only) | Lowest |
| **SObject Mutations** | `platform/sobject-mutations` | Create + update + query/search (no delete) | Medium |
| **SObject All** | `platform/sobject-all` | Full CRUD + query + search + prompt templates | Highest |
| **SObject Deletes** | `platform/sobject-deletes` | Delete + query/search for targeting | High |

### Integration & Automation Servers

| Server | Purpose |
|--------|---------|
| **API Catalog** | REST API endpoints from Salesforce's API library as tools |
| **Custom Servers** | User-defined servers with curated tool sets |
| **Data 360** | Querying unified customer data |
| **Flows** | Autolaunched Flows exposed as MCP tools |
| **Invocable Actions** | `@InvocableMethod` Apex classes as tools |
| **Prompt Builder** | Prompt Builder templates as MCP prompts |
| **Tableau Next** | Semantic model discovery, KPI querying, analytics |

### Choosing a Server

- **Start with `platform/sobject-reads`** for evaluation — zero data modification risk
- **Use `platform/sobject-mutations`** for create/update without delete capability
- **Use `platform/sobject-all`** for production — includes prompt templates
- **Build custom servers** for domain-specific tool sets (see `mcp-tool-builder` skill)

---

## Tool Reference by Server

### platform/sobject-reads Tools

| Tool | Parameters | Description |
|------|-----------|-------------|
| `getSchema` | `object-name` (optional) | No param: compact object catalog. With param: full field schema with types, required flags, picklist values |
| `soqlQuery` | `query` (required) | Execute SOQL queries. Always include WHERE and LIMIT |
| `soslSearch` | `search` (required) | Text search across multiple objects via SOSL |
| `getAuthenticatedUser` | none | User identity: ID, name, email, role, profile, manager, timezone |
| `getRecentlyViewed` | `sobject-name` (required) | Recently viewed/modified records |
| `getRelatedRecords` | `sobject-name`, `id`, `relationship-path` (all required) | Traverse relationships for child records |

### platform/sobject-all Tools (adds to reads)

| Tool | Parameters | Description |
|------|-----------|-------------|
| `createSobjectRecord` | `sobject-name`, `body` (required) | Create new records |
| `updateSobjectRecord` | `sobject-name`, `id`, `body` (required) | Update records by ID |
| `updateChildRecord` | `sobject-name`, `id`, `relationship-path`, `body` (required) | Update child via relationship |
| `deleteSobjectRecord` | `sobject-name`, `id` (required) | Delete record (15-day Recycle Bin recovery) |
| `deleteChildRecord` | `sobject-name`, `id`, `relationship-path` (required) | Delete child via relationship |

### Tableau Next Tools

| Category | Tools |
|----------|-------|
| Analytics | `analyze_data`, `list_dashboards`, `get_dashboard`, `list_visualizations`, `get_visualization` |
| Schema | `list_semantic_models`, `get_semantic_model`, `list_data_objects`, `list_relationships` |
| Metrics | `list_measures`, `list_dimensions`, `list_semantic_model_metrics`, `get_metric` |
| Navigation | `list_workspaces`, `list_workspace_assets`, `search_assets` |

**Tableau Next endpoints:**
- Production: `https://api.salesforce.com/platform/mcp/v1/analytics/tableau-next`
- Sandbox: `https://api.salesforce.com/platform/mcp/v1/sandbox/analytics/tableau-next`

---

## URL Patterns

Everything is encoded in the URL path (no query parameters or headers during discovery).

### Standard Patterns

| Org Type | URL Pattern |
|----------|------------|
| **Production** | `https://api.salesforce.com/platform/mcp/v1/{servername}` |
| **Sandbox** | `https://api.salesforce.com/platform/mcp/v1/sandbox/{servername}` |
| **Scratch Org** | `https://api.salesforce.com/platform/mcp/v1/sandbox/{servername}` |
| **Developer Edition** | `https://api.salesforce.com/platform/mcp/v1/{servername}` |

### My Domain Patterns (Recommended)

Required for orgs that disabled login from standard endpoints.

| Org Type | URL Pattern |
|----------|------------|
| **Production** | `https://api.salesforce.com/platform/mcp/v1/d/{mydomainname}/{servername}` |
| **Sandbox** | `https://api.salesforce.com/platform/mcp/v1/d/{mydomainname}--{sandboxname}/sandbox/{servername}` |
| **Scratch Org** | `https://api.salesforce.com/platform/mcp/v1/d/{mydomainname}/scratch/{servername}` |
| **Developer Edition** | `https://api.salesforce.com/platform/mcp/v1/d/{mydomainname}/develop/{servername}` |

---

## Setup Checklist

### Step 1: Verify Eligibility

- [ ] Org edition: Enterprise, Unlimited, Performance, or Developer Edition
- [ ] Admin access to Setup
- [ ] `MCPService` permission enabled (auto-enabled for eligible orgs; contact Support if missing)

### Step 2: Enable MCP Server

1. Navigate to **Setup > API Catalog > MCP Servers**
2. Toggle on the desired server (e.g., `platform/sobject-reads`)
3. Wait up to **2 minutes** for activation to propagate

> At GA, all MCP servers are **disabled by default**. Each must be individually enabled.

### Step 3: Create External Client App (ECA)

1. Navigate to **Setup > External Client App Manager**
2. Create a new External Client App
3. Enable OAuth and configure:
   - **Callback URL**: See Client Configuration section below
   - **OAuth Scopes**: `mcp_api` + `refresh_token`
4. Security settings:
   - **Enable** "Require Proof Key for Code Exchange (PKCE)"
   - **Enable** "Issue JWT-based access tokens for named users"
   - **Disable** all Flow Enablement checkboxes — deselect everything else
5. Save and note the **Consumer Key** (Client ID)

> **Important:** ECAs may take **up to 30 minutes** to propagate worldwide. Try after 1-2 minutes first.

### Step 4: Connect Client

Every MCP client needs three values:
1. **MCP Server URL** — from URL Patterns above
2. **OAuth Client ID** — Consumer Key from the ECA
3. **OAuth Client Secret** — from the ECA (if required)

### Step 5: Test with Postman First

Always test with Postman before connecting AI clients — it returns raw JSON without LLM interpretation.

---

## External Client App Configuration

### OAuth Scopes

| Scope | Purpose | Required |
|-------|---------|----------|
| `mcp_api` | Access Salesforce hosted MCP servers | Yes |
| `refresh_token` | Maintain persistent sessions | Yes |

> **Beta scopes are retired.** Do not use `api`, `sfap_api`, or `einstein_gpt_api` — these were beta-only and will cause 401 errors.

### Beta to GA Migration

| Change | Beta | GA |
|--------|------|-----|
| URL version | `v1-beta.2` | `v1` |
| Scopes | `api`, `sfap_api`, `refresh_token`, `einstein_gpt_api` | `mcp_api`, `refresh_token` |
| Activation | Org-wide toggle | Per-server in Setup (disabled by default) |
| Tokens | Beta tokens invalid | Must reauthorize |

### Callback URLs by Client

| Client | Callback URL |
|--------|-------------|
| **Claude** | `https://claude.ai/api/mcp/auth_callback` |
| **Cursor** | `cursor://anysphere.cursor-mcp/oauth/callback` |
| **Postman (Desktop)** | `https://oauth.pstmn.io/v1/callback` |
| **Postman (Web)** | `https://oauth.pstmn.io/v1/browser-callback` |
| **ChatGPT** | Copy from ChatGPT Advanced settings — **changes between releases** |

### One ECA Per Client

Create separate ECAs for each MCP client for per-client auditing and revocation.

### Production Hardening

| Setting | Purpose | When |
|---------|---------|------|
| Require Client Secret | Prevent unauthorized token requests | Web server apps (Claude, ChatGPT) |
| Permission Set Restriction | Limit to specific user groups | Production orgs |
| IP Restrictions | Restrict to known IP ranges | Fixed-IP clients |
| Token Rotation | Rotate refresh tokens on use | All production |
| Refresh Token Expiry | Expire tokens after 30 days | All production |
| Single Logout | End MCP when SF session ends | Shared workstations |

### Authentication Details

- **OAuth Authorization Code flow ONLY** — human authenticates in browser
- **No service accounts** — no machine-to-machine (M2M) flows planned
- **No Dynamic Client Registration (DCR)** — clients supporting only DCR are incompatible
- **Connected Apps are NOT supported** — must use External Client Apps
- **`.well-known` discovery**: MCP client receives 401 pointing to `.well-known` endpoint with OAuth metadata

---

## Security Model

### Core Principle

The agent inherits the **authenticated user's full security context**:

- **CRUD**: Object-level access enforced per authenticated user
- **FLS**: Field-level security — invisible fields stay invisible
- **Sharing Rules**: Record-level access follows OWD, sharing rules, manual shares
- **Audit Trail**: Authenticated user's name appears as editor

> **"If you can't do it in the Lightning UI or over the REST API, you can't do it via MCP."**

### Scope Isolation

The `mcp_api` OAuth scope is **separate** from REST API access. An MCP connection cannot access REST APIs. Full REST API access requires the `api` scope on a different ECA.

### Incremental Permission Strategies

1. **Read-Only**: `platform/sobject-reads` — zero data modification risk
2. **Named Queries**: Admin-defined SOQL — agent cannot access anything outside what admin specified
3. **Custom Tools**: Apex Invocable Actions with scoped logic — full business logic control
4. **ECA-Level**: Link ECAs to profiles/permission sets for per-client user control

### Field Labels Matter

> **"Field labels and descriptions are the primary input the LLM uses to understand your org. If your custom fields have cryptic API names and no descriptions, the agent will struggle."**

---

## Client Configuration

### Postman (Test First — Recommended)

1. Create MCP request, switch from STDIO to **HTTP**
2. Paste server URL
3. Auth tab: OAuth 2.0
   - Grant Type: **Authorization Code (With PKCE)**
   - Code Challenge Method: **SHA-256**
   - Client Authentication: **Send client credentials in body**
   - Scope: `mcp_api refresh_token`
   - Check **"Authorize using browser"**
4. Auth URLs:
   - Production Auth: `https://login.salesforce.com/services/oauth2/authorize`
   - Production Token: `https://login.salesforce.com/services/oauth2/token`
   - Sandbox Auth: `https://test.salesforce.com/services/oauth2/authorize`
   - Sandbox Token: `https://test.salesforce.com/services/oauth2/token`

**Test with JSON calls:**
```json
// Test authentication
{"method": "tools/call", "params": {"name": "getUserInfo", "arguments": {}}}

// Test SOQL
{"method": "tools/call", "params": {"name": "soqlQuery", "arguments": {"query": "SELECT Id, Name FROM Account LIMIT 5"}}}
```

### Claude

1. Left sidebar > **Customize** > Connectors > + icon
2. Enter name, optional description
3. Enter server URL
4. Advanced settings: input OAuth Client ID (consumer key)
5. Click Connect, authenticate in browser
6. Use **Configure** to manage tool permissions (enable/disable individual tools)

### Cursor

1. Settings > Cursor Settings > Tools & MCP > New MCP Server
2. Edit `mcp.json` with server URL and consumer key
3. Supports prompt templates
4. **Restart frequently** — force quit if MCP process hangs
5. Toggle server off/on with 1-2 minute wait between

### ChatGPT

1. Settings > Apps > Create App (developer mode required)
2. Enter connector name and server URL
3. Authentication: "User-defined OAuth client"
4. Input OAuth Client ID
5. **Copy callback URL from ChatGPT Advanced settings** into your ECA
6. Must explicitly select Salesforce via + button when prompting
7. **Does NOT support MCP prompt templates**

---

## Troubleshooting

### Common Issues

| Symptom | Cause | Resolution |
|---------|-------|------------|
| **404** on MCP URL | Server not activated | Enable in Setup > API Catalog > MCP Servers; wait 2 minutes |
| **401** Unauthorized | Wrong OAuth scopes | Verify ECA has `mcp_api` + `refresh_token` (not beta scopes) |
| **401** persistent | ECA not propagated | Wait up to 30 minutes after ECA creation |
| **403** Forbidden | Insufficient permissions | Check user's profile, permission sets, and sharing rules |
| Wrong data returned | Environment mismatch | Don't mix Production and Sandbox URLs |
| Connection refused | Edition requirement | Verify Enterprise+ or Developer Edition |
| "Failed to attach prompt" | Flow in templateDataProviders | Remove `templateDataProviders` with `flow://` references for MCP |
| Prompt format ignored | Claude doesn't enforce templates | Pre-format output server-side or embed format in tool description |

### Client-Specific Issues

| Client | Issue | Fix |
|--------|-------|-----|
| **Cursor** | MCP process hangs | Force quit and restart Cursor |
| **Cursor** | Server not responding | Toggle off/on with 1-2 min wait |
| **ChatGPT** | Callback URL invalid | Re-copy from ChatGPT Advanced settings (changes between releases) |
| **ChatGPT** | Salesforce not in chat | Must explicitly select via + button |
| **Claude** | Connector issues | Admin Settings > Connectors to manage |
| **Postman** | STDIO mode selected | Switch to HTTP mode |
| **Tableau Next** | Slow responses in Claude | ~1 min response time; Agentforce is 10-20x faster |

### Known Limitations

| Limitation | Detail |
|------------|--------|
| **Edition requirement** | Enterprise Edition or above (Developer Edition also qualifies) |
| **ECA propagation** | Up to 30 minutes after creation or modification |
| **Server activation** | Up to 2 minutes after toggling on/off |
| **Experience Cloud URLs** | Not supported (planned for future) |
| **API quota** | MCP tool calls consume daily API quota |
| **`mcp-remote` npm** | **Not supported** — only native OAuth/HTTP MCP clients work |
| **No DCR** | Dynamic Client Registration not supported |
| **No undelete** | Deleted records go to Recycle Bin but no MCP undelete tool |
| **Scratch Org ECAs** | Cannot create via Setup UI — must package from DevHub |
| **Connected Apps** | **Not supported** for MCP — must use External Client Apps |
| **Prompt templates** | Only Flex/Global templates. **ChatGPT does NOT support MCP prompts** |
| **ISV packaging** | Managed packages cannot include MCP server configs — expose via annotated Apex/Flows for subscribers to configure |

### Scratch Org Workaround

ECAs cannot be created directly in scratch orgs:
1. Create the ECA in a developer hub org
2. Add it to an unlocked or managed package
3. Install the package in the target scratch org

---

## MCP Gateways (Emerging)

Third-party gateways for centralized governance across multiple MCP servers:
- **MuleSoft AI Gateway**
- **Natoma**
- **Arcade.dev**
- **MCP Manager**

These provide: approved server registry, centralized access controls, advanced audit trails, compliance solutions.

---

## Hosted MCP vs Salesforce DX MCP

| Aspect | Hosted MCP Servers | Salesforce DX MCP (`@salesforce/mcp`) |
|--------|-------------------|--------------------------------------|
| **Hosting** | Cloud-managed by Salesforce | Local CLI on developer machine |
| **Audience** | End users, AI agents, production workflows | Developers during local development |
| **Transport** | Streamable HTTP via `api.salesforce.com` | STDIO via `npx` CLI |
| **Auth** | OAuth 2.0 + PKCE via External Client Apps | SF CLI authentication (`sf org login`) |
| **Tools** | SObject CRUD, prompt templates, custom actions | 60+ dev tools: deploy, retrieve, test, analyze |
| **Use Case** | AI clients querying CRM data in production | Claude Code building/deploying Salesforce code |
| **Configuration** | Per-org in Setup > API Catalog | Per-project in `.mcp.json` |

### When to Use Each

- **Hosted MCP**: AI clients need to **access Salesforce data** (query accounts, update records, run reports)
- **DX MCP**: Developers need to **build Salesforce code** (deploy metadata, run tests, analyze code)
- **Both**: An AI assistant that both builds code (DX MCP) and queries org data (Hosted MCP)

---

## Incremental Rollout Strategy

1. **Sandbox experimentation** — `platform/sobject-reads`, risk-free, use Postman alongside
2. **Early adopter group** — power users who understand data model, validate accuracy
3. **Read-write expansion** — `platform/sobject-all` or custom servers with selective writes
4. **Broader transformation** — change management, SI partner involvement
