---
name: sf-compound
description: Capture learnings to make future Salesforce development easier
arguments:
  - name: scope
    description: What to compound (defaults to recent work)
    required: false
---

# /sf-compound

The final 20% of compound engineering - capture learnings from completed work to make future development easier.

## The Compound Loop

```
Plan (40%) → Work (20%) → Review (20%) → Compound (20%) → Repeat
                                              │
                                              └── YOU ARE HERE
```

## Instructions

When this command is invoked, you MUST follow these steps exactly:

### Step 1: Determine Scope

```
IF $ARGUMENTS.scope is empty:
    Analyze recent git commits and changes
ELSE:
    Analyze specified scope (feature folder, PR, etc.)
```

Announce: "Starting /sf-compound - capturing learnings from: [scope]"

### Step 2: Deploy Analysis Subagents (PARALLEL)

**IMMEDIATELY spawn these 4 subagents in parallel using the Task tool:**

<subagent_deployment>
You MUST call Task tool 4 times in a SINGLE message:

1. Task tool call:
   - description: "Analyze changes made"
   - subagent_type: "Explore"
   - prompt: |
     Analyze recent changes in the codebase.

     Commands to run:
     - git log --oneline -20
     - git diff --name-status HEAD~5
     - Find new files created

     Identify:
     - What was built (components, classes, LWCs)
     - Architecture decisions made
     - Patterns introduced

     Return: Summary of what was built and key decisions

2. Task tool call:
   - description: "Discover reusable patterns"
   - subagent_type: "general-purpose"
   - prompt: |
     Identify reusable patterns from recent work.

     Read existing skills:
     - .claude/skills/apex-patterns/index.md
     - .claude/skills/lwc-patterns/index.md
     - .claude/skills/integration-patterns/index.md

     Then analyze recent code for NEW patterns not in skills:
     - Apex patterns (trigger handlers, services, utilities)
     - LWC patterns (component communication, state)
     - Integration patterns (callouts, events)
     - Test patterns (factories, mocks)

     Return: List of new patterns with code examples

3. Task tool call:
   - description: "Analyze issues encountered"
   - subagent_type: "general-purpose"
   - prompt: |
     Analyze issues encountered during development.

     Look at:
     - Git commits with "fix:" prefix
     - Review findings that were resolved
     - Test failures and their fixes
     - Deployment issues

     Categorize by:
     - Governor limit issues
     - Security issues
     - Bulkification problems
     - Integration failures

     Return: Issues that could be prevented in future (add to agents)

4. Task tool call:
   - description: "Extract key learnings"
   - subagent_type: "general-purpose"
   - prompt: |
     Extract key learnings from the development cycle.

     Identify:
     - What worked well (keep doing)
     - What was harder than expected (document)
     - Surprises or gotchas (add to agents)
     - Time-saving discoveries (add to skills)
     - Org-specific patterns (add to CLAUDE.md)

     Return: Key insights and where to document them
</subagent_deployment>

**Wait for all analysis subagents to complete.**

Display progress:
```
Analysis Phase (4 subagents):
  ├── Change analysis: [status]
  ├── Pattern discovery: [status]
  ├── Issue analysis: [status]
  └── Learning extraction: [status]
```

### Step 3: Deploy Integration Subagents (PARALLEL)

**After analysis completes, spawn integration subagents:**

<subagent_deployment>
Call Task tool 4 times in a SINGLE message:

1. Task tool call:
   - description: "Update skills"
   - subagent_type: "general-purpose"
   - prompt: |
     Update skill files with new patterns discovered.

     Patterns to add: [FROM PATTERN DISCOVERY]

     Files to update:
     - .claude/skills/apex-patterns/index.md
     - .claude/skills/lwc-patterns/index.md
     - .claude/skills/integration-patterns/index.md
     - .claude/skills/test-factory/index.md

     For each pattern:
     - Add descriptive heading
     - Include code example
     - Note when to use it

     Return: List of skill files updated

2. Task tool call:
   - description: "Enhance agents"
   - subagent_type: "general-purpose"
   - prompt: |
     Update agent checklists with new checks.

     Issues to prevent: [FROM ISSUE ANALYSIS]

     Files to update:
     - .claude/agents/apex/*.md
     - .claude/agents/lwc/*.md
     - .claude/agents/automation/*.md
     - .claude/agents/integration/*.md

     For each issue type:
     - Add new checklist item
     - Include example of what to catch
     - Set appropriate severity

     Return: List of agents updated

3. Task tool call:
   - description: "Update CLAUDE.md"
   - subagent_type: "general-purpose"
   - prompt: |
     Update CLAUDE.md with project-specific context.

     Learnings to add: [FROM LEARNING EXTRACTION]

     Add to CLAUDE.md:
     - Naming conventions discovered
     - Architecture decisions
     - Integration endpoints
     - Org-specific patterns
     - Common workflows

     Return: CLAUDE.md additions

4. Task tool call:
   - description: "Save test fixtures"
   - subagent_type: "general-purpose"
   - prompt: |
     Save reusable test patterns to test-factory skill.

     Patterns found: [FROM PATTERN DISCOVERY - test section]

     Update .claude/skills/test-factory/index.md:
     - New TestDataFactory methods
     - Mock implementations
     - Test helper utilities
     - Assertion patterns

     Return: Test fixtures saved
</subagent_deployment>

**Wait for integration to complete.**

Display progress:
```
Integration Phase (4 subagents):
  ├── Skills updated: [status]
  ├── Agents enhanced: [status]
  ├── CLAUDE.md updated: [status]
  └── Test fixtures saved: [status]
```

### Step 4: Generate Compound Report

Create a compound report in `.specify/compounds/`:

```markdown
# Compound Report: [Feature/Date]

## What Was Built
[From change analysis subagent]

## Patterns Captured

### New Apex Pattern: [Name]
**Added to**: .claude/skills/apex-patterns/

```apex
// Code example
```

### New LWC Pattern: [Name]
**Added to**: .claude/skills/lwc-patterns/

```javascript
// Code example
```

## Agents Enhanced

| Agent | New Check Added |
|-------|-----------------|
| [agent] | [new checklist item] |

## Issues Prevented (Future)

| Issue | Prevention | Added To |
|-------|------------|----------|
| [issue] | [check] | [agent] |

## CLAUDE.md Updates

- [New context added]

## Compound Impact

This work makes future development easier by:
1. [Impact 1]
2. [Impact 2]
3. [Impact 3]
```

Save to: `.specify/compounds/[date]-[feature].md`

### Step 5: Present Results

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  /sf-compound COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Learnings captured from: [scope]

📚 Knowledge Updates:
  ┌────────────────────────┬───────┐
  │ Skills Updated         │     X │
  │ Agents Enhanced        │     Y │
  │ Patterns Documented    │     Z │
  │ Test Fixtures Added    │     W │
  │ CLAUDE.md Entries      │     V │
  └────────────────────────┴───────┘

✅ New Patterns Added:
  • [Pattern 1] → apex-patterns
  • [Pattern 2] → lwc-patterns

🛡️ Future Issues Prevented:
  • [Issue 1] (new agent check)
  • [Issue 2] (new agent check)

📄 Report: .specify/compounds/[date]-[feature].md

💡 Compound Impact:
   Future similar features will be faster because:
   - Patterns are documented
   - Agents catch known issues
   - Context is preserved

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The next iteration of work starts smarter.
```

## Important

- You MUST call Task tool to spawn subagents
- Analysis subagents run in PARALLEL (one message)
- Integration subagents run in PARALLEL after analysis
- Actually UPDATE the skill and agent files
- Save compound report to .specify/compounds/
- This is what makes compound engineering work - don't skip it!

## Integration with Workflow

```bash
/sf-plan "Feature"      # 40% - Plan with research
/sf-work plan.md        # 20% - Implement
/sf-review              # 20% - Review
/sf-compound            # 20% - Capture learnings ← THIS
# Next feature is now faster!
```
