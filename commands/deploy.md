---
name: sf:deploy
description: Create comprehensive deployment checklists and validate deployments to Salesforce orgs
arguments:
  - name: environment
    description: Target environment (sandbox, production, scratch)
    required: true
---

# Salesforce Deployment Command

Creates deployment checklists, validates changes, and guides deployments to Salesforce orgs.

## Workflow

### Step 1: Analyze Changes

```bash
# Get list of changed files
git diff --name-only main...HEAD

# Categorize changes
- Apex Classes
- Apex Triggers
- LWC Components
- Flows
- Objects/Fields
- Profiles/Permission Sets
- Other Metadata
```

### Step 2: Generate Pre-Deployment Checklist

```markdown
## Pre-Deployment Checklist

### Code Quality
- [ ] All tests passing locally
- [ ] Code coverage > 75% (recommend 85%+)
- [ ] No PMD Critical/High violations
- [ ] Code reviewed and approved

### Validation
- [ ] Deployment validated to target org
- [ ] All Apex tests pass in target
- [ ] No destructive changes unintended

### Dependencies
- [ ] Required metadata already in target
- [ ] Custom settings/metadata populated
- [ ] Named credentials configured

### Communication
- [ ] Stakeholders notified
- [ ] Deployment window scheduled
- [ ] Rollback plan documented

### Data Considerations
- [ ] Data migration scripts ready (if needed)
- [ ] Backup completed
- [ ] Record counts verified
```

### Step 3: Validate Deployment

```bash
# Validate to sandbox
sf project deploy validate \
  --target-org $TARGET_ORG \
  --test-level RunLocalTests \
  --verbose

# For production, use:
sf project deploy validate \
  --target-org production \
  --test-level RunLocalTests \
  --verbose
```

### Step 4: Execute Deployment

```bash
# Deploy with tests
sf project deploy start \
  --target-org $TARGET_ORG \
  --test-level RunLocalTests \
  --verbose \
  --wait 30
```

### Step 5: Post-Deployment Verification

```markdown
## Post-Deployment Checklist

### Verification
- [ ] Deployment successful
- [ ] All tests passing
- [ ] Smoke tests completed
- [ ] User acceptance verified

### Cleanup
- [ ] Deployment ticket updated
- [ ] Documentation updated
- [ ] Team notified of completion
```

## Environment-Specific Guidance

### Sandbox Deployment
```bash
sf project deploy start \
  --target-org MySandbox \
  --test-level RunLocalTests
```

### Production Deployment
```bash
# Always validate first
sf project deploy validate \
  --target-org production \
  --test-level RunLocalTests

# Then deploy with the validated ID
sf project deploy quick \
  --job-id <validation-id> \
  --target-org production
```

### Scratch Org Deployment
```bash
sf project deploy start \
  --target-org MyScratchOrg
```

## Rollback Procedures

### Quick Rollback (Within 24 hours)
```bash
# Use Salesforce deployment history
# Redeploy previous version from source control
git checkout <previous-commit>
sf project deploy start --target-org $TARGET_ORG
```

### Manual Rollback
1. Identify changed components
2. Retrieve previous versions from source control
3. Deploy previous versions
4. Verify functionality restored
