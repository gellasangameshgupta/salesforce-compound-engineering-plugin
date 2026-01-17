---
name: sf-compound
description: Capture learnings to make future Salesforce development easier
arguments:
  - name: scope
    description: What to compound (feature, review, bug, pattern)
    required: false
---

# Salesforce Compound Command

The **final 20% of compound engineering** - captures learnings from completed work to make future development easier. This is what makes each unit of work compound into future productivity.

## The Compound Loop

```
Plan (40%) → Work (20%) → Review (20%) → Compound (20%) → Repeat
                                              │
                                              ▼
                                    ┌─────────────────────┐
                                    │  CAPTURED LEARNINGS │
                                    ├─────────────────────┤
                                    │ • New patterns      │
                                    │ • Updated skills    │
                                    │ • Enhanced agents   │
                                    │ • CLAUDE.md updates │
                                    │ • Test fixtures     │
                                    └─────────────────────┘
                                              │
                                              ▼
                              Next iteration starts smarter
```

---

## Subagent Architecture

```
/sf-compound [scope]
    │
    ├── [ANALYSIS PHASE - PARALLEL]
    │   ├── Change Analysis Subagent: What was built
    │   ├── Pattern Discovery Subagent: Reusable patterns found
    │   ├── Issue Analysis Subagent: Problems encountered
    │   └── Learning Extraction Subagent: Key insights
    │
    ├── [SYNTHESIS PHASE]
    │   └── Knowledge Synthesis Subagent: Organize findings
    │
    └── [INTEGRATION PHASE - PARALLEL]
        ├── Skill Update Subagent: Update skills with patterns
        ├── Agent Enhancement Subagent: Add new checks to agents
        ├── CLAUDE.md Update Subagent: Update project context
        └── Test Fixture Subagent: Save test patterns
```

---

## Workflow

When the user runs `/sf-compound [scope]`, execute the following:

### Step 1: Determine Scope

```
IF scope is empty:
    Analyze latest completed feature
ELSE IF scope is "feature":
    Analyze specific feature work
ELSE IF scope is "review":
    Analyze code review findings
ELSE IF scope is "bug":
    Analyze bug fix for prevention
ELSE IF scope is "pattern":
    Extract and document a pattern
```

### Step 2: Deploy Analysis Subagents (PARALLEL)

**Deploy these 4 subagents IN PARALLEL:**

```
1. CHANGE ANALYSIS SUBAGENT
   subagent_type: "Explore"
   prompt: |
     Analyze recent changes in the codebase.

     Find:
     - New files created (git diff --name-status main)
     - Modified files
     - New patterns introduced
     - Architecture decisions made

     Return: Summary of what was built

2. PATTERN DISCOVERY SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Identify reusable patterns in recent work.

     Look for:
     - New Apex patterns (services, handlers, selectors)
     - LWC component patterns
     - Integration patterns
     - Test patterns
     - Error handling approaches

     Compare with existing skills:
     - .claude/skills/apex-patterns/
     - .claude/skills/lwc-patterns/
     - .claude/skills/integration-patterns/
     - .claude/skills/test-factory/

     Return: New patterns to document

3. ISSUE ANALYSIS SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Analyze issues encountered during development.

     Review:
     - Git commit messages for fixes
     - Review comments and resolutions
     - Test failures and fixes
     - Deployment issues

     Categorize:
     - Governor limit issues
     - Security issues
     - Bulkification problems
     - Integration failures

     Return: Issues that could be prevented in future

4. LEARNING EXTRACTION SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Extract key learnings from the development cycle.

     Identify:
     - What worked well
     - What was harder than expected
     - Surprises or gotchas
     - Time-saving discoveries
     - Tools or techniques that helped

     Return: Key insights and recommendations
```

### Step 3: Synthesize Knowledge

```
KNOWLEDGE SYNTHESIS SUBAGENT
subagent_type: "general-purpose"
prompt: |
  Synthesize findings from analysis subagents.

  Organize into:
  1. Patterns to add to skills
  2. Checks to add to agents
  3. Context to add to CLAUDE.md
  4. Test fixtures to save
  5. Documentation to create

  Return: Organized knowledge structure
```

### Step 4: Deploy Integration Subagents (PARALLEL)

**Update the system with learnings:**

```
1. SKILL UPDATE SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Update skill files with new patterns.

     Files to potentially update:
     - .claude/skills/apex-patterns/index.md
     - .claude/skills/lwc-patterns/index.md
     - .claude/skills/integration-patterns/index.md
     - .claude/skills/test-factory/index.md
     - .claude/skills/governor-limits/index.md

     Add:
     - New code patterns with examples
     - Best practices discovered
     - Common pitfalls to avoid

     Return: List of skill files updated

2. AGENT ENHANCEMENT SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Enhance agent checklists with new checks.

     Files to potentially update:
     - .claude/agents/apex/*.md
     - .claude/agents/lwc/*.md
     - .claude/agents/automation/*.md
     - .claude/agents/integration/*.md
     - .claude/agents/architecture/*.md

     Add:
     - New checklist items based on issues found
     - New anti-patterns to detect
     - Updated severity ratings

     Return: List of agents updated

3. CLAUDE.MD UPDATE SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Update CLAUDE.md with project-specific context.

     Add:
     - New naming conventions discovered
     - Architecture decisions documented
     - Integration endpoints
     - Common workflows

     Return: CLAUDE.md changes

4. TEST FIXTURE SUBAGENT
   subagent_type: "general-purpose"
   prompt: |
     Save reusable test patterns.

     Update .claude/skills/test-factory/:
     - New TestDataFactory methods
     - Mock implementations
     - Test helper utilities
     - Common assertion patterns

     Return: Test fixtures saved
```

### Step 5: Generate Compound Report

```markdown
# Compound Engineering Report

## Summary
Feature: [Feature Name]
Duration: [Development Time]
Files Changed: [Count]
Learnings Captured: [Count]

---

## Patterns Discovered

### New Apex Pattern: Batch Processor with Retry
**Added to**: .claude/skills/apex-patterns/

```apex
public class RetryableBatchProcessor implements Database.Batchable<SObject> {
    private Integer maxRetries = 3;
    // Pattern implementation...
}
```

**When to use**: Processing large data sets with external dependencies

---

### New LWC Pattern: Debounced Search
**Added to**: .claude/skills/lwc-patterns/

```javascript
// Debounce search input
handleSearchChange(event) {
    window.clearTimeout(this.delayTimeout);
    this.delayTimeout = setTimeout(() => {
        this.searchTerm = event.target.value;
        this.handleSearch();
    }, 300);
}
```

**When to use**: Search inputs with API calls

---

## Agent Enhancements

### apex-governor-guardian.md
Added new checklist item:
- [ ] Check for SOQL in scheduled job execute()

### apex-security-sentinel.md
Added new anti-pattern:
- Storing API keys in Custom Settings (use Named Credentials)

---

## Issues Prevented (Future)

| Issue Type | Prevention Added | Location |
|------------|-----------------|----------|
| Governor limit in batch | New checklist item | apex-governor-guardian.md |
| CRUD bypass | Updated pattern | security-guide skill |
| Test data isolation | New factory method | test-factory skill |

---

## CLAUDE.md Updates

Added:
- Naming convention: Batch jobs use `*BatchProcessor` suffix
- Architecture: External APIs use retry pattern with exponential backoff
- Integration: Marketing Cloud uses Named Credential `Marketing_Cloud_API`

---

## Test Fixtures Created

| Fixture | Purpose | Location |
|---------|---------|----------|
| createMarketingCloudMock() | Mock MC API responses | test-factory |
| createBulkLeads(count) | Generate bulk test leads | test-factory |

---

## Metrics

| Metric | Value |
|--------|-------|
| Skills Updated | 3 |
| Agents Enhanced | 2 |
| Patterns Documented | 4 |
| Test Fixtures Added | 2 |

---

## Compound Impact

This work will make future development easier by:

1. **Faster Planning**: New patterns documented for similar features
2. **Better Reviews**: Agents now check for issues encountered
3. **Easier Testing**: New test fixtures available
4. **Reduced Bugs**: Anti-patterns documented and auto-detected

Next feature benefiting from this: Similar integrations, batch processing
```

### Step 6: Present Results

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  COMPOUND ENGINEERING COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Learnings captured from: Lead Scoring Feature

📚 Knowledge Updates:
  ┌────────────────────────┬───────┐
  │ Skills Updated         │     3 │
  │ Agents Enhanced        │     2 │
  │ Patterns Documented    │     4 │
  │ Test Fixtures Added    │     2 │
  │ CLAUDE.md Entries      │     3 │
  └────────────────────────┴───────┘

✅ New Patterns Added:
  • Batch Processor with Retry → apex-patterns
  • Debounced Search → lwc-patterns
  • Platform Event Error Handler → integration-patterns
  • Bulk Test with Assertions → test-factory

🛡️ Future Issues Prevented:
  • Governor limit in batch jobs (new agent check)
  • CRUD bypass in services (updated pattern)
  • Test data pollution (new factory method)

📄 Report saved: .specify/compounds/2024-01-15-lead-scoring.md

💡 Compound Impact:
   Future similar features will be 40% faster to implement
   due to documented patterns and enhanced agents.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The next iteration of work starts smarter.
```

---

## Compound Categories

### /sf-compound feature
Captures learnings from completed feature work.

### /sf-compound review
Captures learnings from code review (what issues were found and how to prevent them).

### /sf-compound bug
Analyzes a bug fix to prevent similar bugs:
```
/sf-compound bug "Fixed SOQL injection in AccountSearch"
```

### /sf-compound pattern
Documents a specific pattern discovered:
```
/sf-compound pattern "Retry pattern for external callouts"
```

---

## Where Learnings Are Stored

```
.claude/
├── skills/
│   ├── apex-patterns/index.md      ← New Apex patterns
│   ├── lwc-patterns/index.md       ← New LWC patterns
│   ├── integration-patterns/       ← Integration learnings
│   ├── test-factory/               ← Test fixtures
│   └── governor-limits/            ← Limit optimizations
├── agents/
│   └── */*.md                      ← Enhanced checklists
├── CLAUDE.md                       ← Project context

.specify/
└── compounds/                      ← Compound reports
    ├── 2024-01-15-lead-scoring.md
    ├── 2024-01-20-integration-fix.md
    └── ...
```

---

## Compound Loop Integration

```bash
# Full compound engineering workflow

# 1. Plan (40%)
/sf-plan "Lead scoring automation"

# 2. Work (20%)
/sf-work .specify/specs/001-lead-scoring/plan.md

# 3. Review (20%)
/sf-review

# 4. Compound (20%) ← THIS COMMAND
/sf-compound

# Next iteration benefits from captured learnings
/sf-plan "Contact scoring automation"  # Uses patterns from lead scoring
```

---

## Configuration

```json
// .sf-compound/config.json
{
  "compound": {
    "autoCompound": true,           // Auto-run after PR merge
    "updateSkills": true,           // Update skill files
    "updateAgents": true,           // Update agent checklists
    "updateClaudeMd": true,         // Update CLAUDE.md
    "saveTestFixtures": true,       // Save test patterns
    "reportDirectory": ".specify/compounds/"
  }
}
```
