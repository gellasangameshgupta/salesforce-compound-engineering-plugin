---
name: sf:plan
description: Create comprehensive Salesforce implementation plans from feature descriptions
arguments:
  - name: feature_description
    description: Description of the feature to plan
    required: true
---

# Salesforce Feature Planning Command

Create detailed, actionable implementation plans for Salesforce features. This command researches your org's patterns, considers governor limits, and produces deployment-ready specifications.

## Workflow

When the user runs `/sf:plan [feature description]`, execute the following steps:

### Step 1: Understand the Request

Parse the feature description to identify:
- **Object(s) involved**: Standard or custom objects
- **Automation type**: Trigger, Flow, Apex, LWC, or combination
- **Integration needs**: External systems, APIs
- **Data volume**: Expected record counts
- **User context**: Who will use this feature

### Step 2: Research Existing Patterns

Search the codebase to understand current patterns:

```bash
# Find existing triggers for the object
find . -name "*Trigger*" -type f | head -20

# Find existing handlers
find . -name "*Handler*" -o -name "*Service*" | head -20

# Check for existing test patterns
find . -name "*Test*" -type f | head -10

# Look for similar features
grep -r "related_keyword" --include="*.cls" --include="*.js" | head -20
```

Ask Claude to analyze:
- What trigger patterns are used? (Handler framework, standalone?)
- What naming conventions are followed?
- How are tests structured?
- Are there service layer patterns?

### Step 3: Assess Governor Limit Impact

For each component, calculate governor limit usage:

| Component | Queries | DML | CPU | Heap |
|-----------|---------|-----|-----|------|
| Trigger Handler | X | Y | Z | W |
| Flow | X | Y | Z | W |
| LWC Apex | X | Y | Z | W |
| **Total** | **SUM** | **SUM** | **SUM** | **SUM** |

Flag any concerns:
- Approaching 80% of any limit
- Potential for bulk operations to exceed limits
- Recursive automation risks

### Step 4: Generate the Plan

Create a structured plan document:

```markdown
# Implementation Plan: [Feature Name]

## Overview
Brief description of what will be built and why.

## Business Requirements
- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3

## Technical Approach

### Data Model Changes
| Object | Field | Type | Description |
|--------|-------|------|-------------|
| | | | |

### Automation Components
1. **Trigger**: [Description]
2. **Flow**: [Description]  
3. **Apex Class**: [Description]

### User Interface
- LWC Component: [Description]
- Lightning Page: [Description]

## Detailed Design

### [Component 1 Name]
**Type**: Trigger Handler / Flow / LWC / etc.
**Purpose**: What it does

**Input**:
- Parameter 1
- Parameter 2

**Output**:
- Expected result

**Error Handling**:
- How errors are handled

**Code Example**:
```apex
// Example implementation following org patterns
```

### [Component 2 Name]
...

## Governor Limit Analysis

| Limit | Sync Budget | This Feature | Remaining |
|-------|-------------|--------------|-----------|
| SOQL Queries | 100 | X | 100-X |
| DML Statements | 150 | Y | 150-Y |
| CPU Time (ms) | 10,000 | Z | 10,000-Z |

## Security Considerations
- [ ] CRUD/FLS enforcement needed
- [ ] Sharing rule implications
- [ ] Sensitive data handling

## Test Plan

### Unit Tests
| Test Class | Test Methods | Coverage Target |
|------------|--------------|-----------------|
| | | 90%+ |

### Test Scenarios
1. **Positive Test**: [Description]
2. **Negative Test**: [Description]
3. **Bulk Test**: 200+ records
4. **Permission Test**: Different profiles

## Deployment Plan

### Pre-Deployment
- [ ] Backup existing data
- [ ] Notify stakeholders
- [ ] Schedule deployment window

### Deployment Sequence
1. Deploy metadata in order: [list]
2. Data migration (if needed)
3. Permission set assignments
4. Post-deployment validation

### Rollback Plan
- Steps to revert if issues occur
- Data restoration procedure

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Open Questions
1. Question needing stakeholder input
2. Technical decision pending

## Effort Estimate
| Component | Estimate |
|-----------|----------|
| Development | X hours |
| Testing | Y hours |
| Documentation | Z hours |
| **Total** | **SUM** |
```

### Step 5: Save and Present

Save the plan to the `plans/` directory:

```bash
# Create filename from feature
FILENAME="plans/$(echo "$FEATURE" | tr ' ' '-' | tr '[:upper:]' '[:lower:]').md"
```

Present the plan to the user with:
1. Summary of the approach
2. Key decisions and trade-offs
3. Questions needing input
4. Next steps to execute with `/sf:work`

## Example Usage

### Input
```
/sf:plan "Lead scoring automation that calculates score based on email opens, 
web visits, and form submissions. Scores should update in real-time and 
trigger assignment to sales reps when score exceeds threshold."
```

### Output
Creates a comprehensive plan covering:
- Custom fields on Lead (Score__c, Last_Score_Date__c, etc.)
- Platform Event for real-time updates
- Trigger handler for score calculation
- Flow for assignment rule trigger
- LWC for score visualization
- Batch job for nightly recalculation
- Integration considerations for marketing automation
- Test plan with bulk scenarios

## Plan Quality Checklist

Before presenting the plan, verify:

- [ ] All requirements are addressed
- [ ] Governor limits analyzed for bulk scenarios
- [ ] Security considerations documented
- [ ] Follows existing org patterns
- [ ] Test plan covers edge cases
- [ ] Deployment sequence is logical
- [ ] Rollback plan is actionable
- [ ] Estimates are realistic
