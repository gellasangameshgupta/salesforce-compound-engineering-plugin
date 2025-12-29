# Salesforce Compound Engineering Plugin

A Claude Code plugin that makes each unit of Salesforce engineering work easier than the last. Transform how you plan, build, and review Salesforce solutions using AI-powered tools that systematically improve your development workflow.

## What Is Salesforce Compound Engineering?

**Each unit of Salesforce work should make subsequent units of work easier—not harder.**

Traditional Salesforce development accumulates technical debt:
- Triggers without proper handler patterns
- Flows that bypass governor limits understanding
- LWC components with duplicated logic
- Hardcoded IDs and magic numbers
- Missing test coverage for edge cases

Compounding engineering inverts this. Each feature you build:
- Documents patterns for the next feature
- Creates reusable components that accelerate future work
- Establishes conventions that reduce decision fatigue
- Codifies Salesforce-specific knowledge that compounds across the team

## The Compound Engineering Loop

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Plan (40%)  →  Work (20%)  →  Review (20%)  →  Compound  │
│       ↑                                            (20%)    │
│       └────────────────────────────────────────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

80% of compound engineering is in **planning and review**. 20% is in **execution**.

## Quick Start

### Installation

```bash
# Add the marketplace
/plugin marketplace add https://github.com/YourOrg/sf-compound-engineering-plugin

# Install the plugin
/plugin install sf-compound-engineering
```

### One-Command Installation

```bash
npx claude-plugins install @YourOrg/sf-compound-engineering-plugin/sf-compound-engineering
```

## Core Commands

### `/sf:plan [feature description]`

Creates detailed implementation plans from feature descriptions with Salesforce-specific research.

```bash
# Example
claude /sf:plan "Add opportunity approval process with multi-level hierarchy and email notifications"
```

**What it does:**
- Researches your org's existing patterns (triggers, flows, classes)
- Analyzes governor limit implications
- Creates acceptance criteria with bulkification requirements
- Generates code examples following your existing patterns
- Identifies security considerations (CRUD/FLS, sharing rules)

### `/sf:work [plan file]`

Executes plans systematically with Salesforce-aware validation.

```bash
claude /sf:work plans/opportunity-approval.md
```

**What it does:**
- Creates feature branch with proper naming
- Breaks down into trackable todos
- Runs Apex tests after each change
- Validates metadata with `sf project deploy validate`
- Creates pull request when complete

### `/sf:review [PR number or metadata path]`

Performs exhaustive multi-agent code reviews with Salesforce expertise.

```bash
# Review latest PR
claude /sf:review

# Review specific PR
claude /sf:review 123

# Review local changes
claude /sf:review force-app/main/default/classes/
```

**What it does:**
- Runs 15+ specialized Salesforce review agents in parallel
- Checks governor limits, bulkification, security
- Validates trigger patterns and handler architecture
- Reviews LWC for performance and accessibility
- Analyzes Flow complexity and error handling

### `/sf:deploy [environment]`

Creates comprehensive deployment checklists and validates deployments.

```bash
claude /sf:deploy production
```

### `/sf:health`

Analyzes org health and technical debt.

```bash
claude /sf:health
```

## All Commands

| Command | Purpose |
|---------|---------|
| `/sf:plan` | Create detailed Salesforce implementation plans |
| `/sf:work` | Execute plans with systematic validation |
| `/sf:review` | Multi-agent code review for Salesforce |
| `/sf:deploy` | Deployment checklists and validation |
| `/sf:health` | Org health and technical debt analysis |
| `/sf:triage` | Triage review findings into todos |
| `/sf:resolve` | Resolve todos in parallel |
| `/sf:generate` | Generate new commands from descriptions |
| `/sf:document` | Auto-generate documentation |
| `/sf:test` | Comprehensive test analysis and generation |
| `/sf:refactor` | Safe refactoring with dependency analysis |
| `/sf:integrate` | Integration pattern planning (REST/SOAP) |
| `/sf:migrate` | Data migration planning and validation |

## Specialized Agents (24 Total)

### Apex Review Specialists

| Agent | Focus |
|-------|-------|
| `apex-governor-guardian` | Governor limits, SOQL optimization, heap management |
| `apex-bulkification-reviewer` | Bulk patterns, collection handling, trigger context |
| `apex-security-sentinel` | CRUD/FLS, injection prevention, sharing rules |
| `apex-trigger-architect` | One-trigger pattern, handler design, recursion control |
| `apex-test-coverage-analyst` | Test patterns, assertions, edge cases, data factory |
| `apex-exception-handler` | Error handling, logging, graceful degradation |

### Lightning (LWC/Aura) Specialists

| Agent | Focus |
|-------|-------|
| `lwc-performance-oracle` | Wire adapters, caching, rendering optimization |
| `lwc-security-reviewer` | Lightning Locker, CSP, XSS prevention |
| `lwc-accessibility-guardian` | WCAG compliance, ARIA, keyboard navigation |
| `aura-migration-advisor` | Aura to LWC migration patterns |
| `lwc-architecture-strategist` | Component composition, data flow, event handling |

### Automation Specialists

| Agent | Focus |
|-------|-------|
| `flow-complexity-analyzer` | Flow loops, bulkification, error handling |
| `flow-governor-monitor` | DML/SOQL in flows, recursive flows |
| `process-automation-strategist` | Flow vs Trigger vs Apex decisions |
| `validation-rule-reviewer` | Rule logic, bypass patterns, error messages |

### Integration Specialists

| Agent | Focus |
|-------|-------|
| `rest-api-architect` | API design, versioning, error responses |
| `callout-pattern-reviewer` | Async patterns, retry logic, timeout handling |
| `integration-security-sentinel` | OAuth, named credentials, certificate handling |
| `platform-event-strategist` | Event design, replay, high-volume patterns |

### Data & Architecture

| Agent | Focus |
|-------|-------|
| `data-model-architect` | Schema design, relationships, field usage |
| `sharing-security-analyst` | OWD, sharing rules, manual shares, territories |
| `package-dependency-guardian` | Namespace conflicts, version management |
| `metadata-consistency-checker` | Profile/permission set alignment, field-level security |

### Research & Documentation

| Agent | Focus |
|-------|-------|
| `salesforce-release-researcher` | New features, deprecations, release notes |
| `pattern-recognition-specialist` | Codebase patterns, anti-patterns, best practices |

## Skills (12 Total)

### Core Skills

| Skill | Purpose |
|-------|---------|
| `apex-patterns` | Common Apex patterns (selector, domain, service) |
| `lwc-patterns` | LWC component patterns and state management |
| `governor-limits` | Complete governor limit reference and strategies |
| `security-guide` | Salesforce security best practices |
| `test-factory` | Test data factory patterns |
| `integration-patterns` | Integration pattern library |

### Workflow Skills

| Skill | Purpose |
|-------|---------|
| `deployment-checklist` | Pre/post deployment validation |
| `code-review-checklist` | Comprehensive review checklist |
| `troubleshooting-guide` | Common issue resolution |
| `documentation-templates` | Technical documentation templates |
| `migration-playbook` | Data and metadata migration guides |
| `release-management` | Release process and rollback procedures |

## Example Workflows

### Planning a New Feature

```bash
claude /sf:plan "Create a lead scoring automation that:
- Calculates score based on engagement activities
- Updates lead rating based on thresholds  
- Triggers assignment rules for high-score leads
- Logs scoring history for analytics"
```

**Output:** A comprehensive plan including:
- Data model changes (custom fields, objects)
- Trigger architecture with handler pattern
- Flow vs Apex decision rationale
- Test scenarios with bulkification tests
- Deployment sequence
- Rollback plan

### Reviewing Code Before PR

```bash
claude /sf:review force-app/main/default/classes/LeadScoringHandler.cls
```

**Output:** Multi-agent analysis covering:
- Governor limit compliance
- Bulkification verification
- Security review (CRUD/FLS)
- Test coverage gaps
- Code quality suggestions
- Documentation requirements

### Deploying to Production

```bash
claude /sf:deploy production
```

**Output:** Pre-deployment checklist:
- Validation results
- Test execution summary
- Destructive changes warnings
- User impact analysis
- Rollback procedures
- Post-deployment verification steps

## Salesforce-Specific Principles

### 1. Governor Limits First
Every code review starts with governor limit analysis. The `apex-governor-guardian` agent validates SOQL queries, DML operations, and heap usage.

### 2. Bulkification by Default
The `apex-bulkification-reviewer` ensures all trigger handlers, batch jobs, and integrations handle collections properly.

### 3. Security in Depth
The security agents validate:
- CRUD/FLS enforcement
- Sharing rule compliance
- Input sanitization
- Lightning Locker compliance

### 4. Test-Driven Development
The `apex-test-coverage-analyst` ensures:
- Positive and negative test cases
- Bulk data tests (200+ records)
- User context tests (different profiles)
- Integration test patterns

### 5. Documentation as Code
Every component gets documented:
- Inline ApexDoc comments
- README files for complex features
- Architecture decision records
- Runbook for operations

## Configuration

### `.sf-compound/config.json`

```json
{
  "org": {
    "defaultOrg": "MyDevOrg",
    "scratchOrgDefinition": "config/project-scratch-def.json"
  },
  "review": {
    "agents": ["all"],
    "excludeAgents": [],
    "severityThreshold": "warning"
  },
  "deployment": {
    "runAllTests": true,
    "testLevel": "RunLocalTests",
    "checkOnly": false
  },
  "patterns": {
    "triggerHandlerPattern": "TriggerHandler",
    "selectorPattern": "Selector",
    "servicePattern": "Service"
  }
}
```

## Integration with Salesforce CLI

The plugin integrates seamlessly with Salesforce CLI commands:

```bash
# Validate before review
sf project deploy validate --target-org MyOrg

# Deploy after approval
sf project deploy start --target-org MyOrg

# Run tests
sf apex run test --target-org MyOrg --code-coverage
```

## Philosophy

### Prefer Explicit Over Magic
Salesforce has enough "magic" (automatic field updates, formula recalculations). Our code should be explicit and readable.

### Fail Fast, Fail Loud
Governor limit exceptions are better than silent data corruption. Design for visibility.

### Test Like Production
200+ record tests aren't optional—they're the minimum. Test with realistic data volumes.

### Security is Not Optional
CRUD/FLS checks, sharing rules, and input validation are requirements, not nice-to-haves.

### Document the Why
Comments should explain business logic, not what the code does. Let the code speak for itself.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new agents
- Creating skills
- Submitting improvements

## Learn More

- [Compound Engineering Philosophy](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it)
- [Salesforce Development Best Practices](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_dev_guide.htm)
- [Lightning Web Components Guide](https://developer.salesforce.com/docs/component-library/documentation/en/lwc)

## About

Created by Sangamesh | [Sanga Musings Newsletter](https://sangamusings.substack.com)

Built with the Compound Engineering philosophy for Salesforce developers who want each deployment to make the next one easier.

---

## 🔄 Updating the Plugin

### Check Current Version
The version is defined in `plugins/sf-compound-engineering/.claude-plugin/plugin.json`

### Update Methods

**If installed from GitHub:**
```bash
/plugin update sf-compound-engineering
```

**If installed from local path:**
```bash
# Pull latest changes
cd /path/to/sf-compound-engineering-plugin
git pull origin main

# Reinstall (if needed)
/plugin uninstall sf-compound-engineering
/plugin install /path/to/sf-compound-engineering-plugin
```

### Changelog
See [CHANGELOG.md](./CHANGELOG.md) for version history.
