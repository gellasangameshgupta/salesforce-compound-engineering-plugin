---
name: sf-lfg
description: Full autonomous pipeline — plan, deepen, work, review, resolve, test, deploy
arguments:
  - name: feature
    description: Feature description or plan file path to execute end-to-end
    required: true
  - name: deploy
    description: "Deploy target: scratch, sandbox, or none (default: none)"
    required: false
---

# <span data-proof="authored" data-by="ai:claude">/sf-lfg</span>

<span data-proof="authored" data-by="ai:claude">Full autonomous pipeline. Takes a feature from idea to deployment with minimal human intervention.</span>

**<span data-proof="authored" data-by="ai:claude">LFG = Let's F</span>**<span data-proof="authored" data-by="ai:claude">*ing Go.**</span>

## <span data-proof="authored" data-by="ai:claude">Goal</span>

<span data-proof="authored" data-by="ai:claude">Execute the full compound engineering loop for:</span> <span data-proof="authored" data-by="ai:claude">`$ARGUMENTS.feature`</span>

***

## <span data-proof="authored" data-by="ai:claude">Pipeline Overview</span>

```
┌─────────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌─────────┐    ┌──────────┐    ┌──────────┐
│ 1. PLAN     │───▶│ 2.DEEPEN │───▶│ 3. WORK  │───▶│ 4.REVIEW │───▶│5.RESOLVE│───▶│ 6. TEST  │───▶│ 7.DEPLOY │
│ /sf-plan    │    │/sf-deepen│    │ /sf-work  │    │/sf-review│    │  fixes  │    │  sf apex │    │ sf deploy│
└─────────────┘    └──────────┘    └──────────┘    └──────────┘    └─────────┘    └──────────┘    └──────────┘
       │                                                                                                │
       └────────────────────────────────────────────────────────────────────────────────────────────────┘
                                              /sf-compound (capture learnings)
```

***

## <span data-proof="authored" data-by="ai:claude">Stage 1: PLAN</span>

<span data-proof="authored" data-by="ai:claude">If</span> <span data-proof="authored" data-by="ai:claude">`$ARGUMENTS.feature`</span> <span data-proof="authored" data-by="ai:claude">is a file path, read it as the plan. Otherwise, create one:</span>

1. <span data-proof="authored" data-by="ai:claude">Check</span> <span data-proof="authored" data-by="ai:claude">`docs/brainstorms/`</span> <span data-proof="authored" data-by="ai:claude">for matching brainstorm.</span>
2. <span data-proof="authored" data-by="ai:claude">Dispatch parallel research agents:</span>

   * <span data-proof="authored" data-by="ai:claude">Task sf-learnings-researcher(feature)</span>

   * <span data-proof="authored" data-by="ai:claude">Task sf-repo-research-analyst(feature)</span>

   * <span data-proof="authored" data-by="ai:claude">Task sf-best-practices-researcher(feature)</span>

   * <span data-proof="authored" data-by="ai:claude">Task sf-framework-docs-researcher(feature)</span>
3. <span data-proof="authored" data-by="ai:claude">Design architecture (no code).</span>
4. <span data-proof="authored" data-by="ai:claude">Run spec flow analysis:</span>

   * <span data-proof="authored" data-by="ai:claude">Task sf-spec-flow-analyzer(plan)</span>
5. <span data-proof="authored" data-by="ai:claude">Save to</span> <span data-proof="authored" data-by="ai:claude">`docs/plans/YYYY-MM-DD-feat-{slug}-plan.md`.</span>

**<span data-proof="authored" data-by="ai:claude">Gate:</span>** <span data-proof="authored" data-by="ai:claude">Plan must have acceptance criteria and task list before proceeding.</span>

***

## <span data-proof="authored" data-by="ai:claude">Stage 2: DEEPEN</span>

<span data-proof="authored" data-by="ai:claude">Enhance the plan with parallel research per section:</span>

1. <span data-proof="authored" data-by="ai:claude">Parse plan sections.</span>
2. <span data-proof="authored" data-by="ai:claude">Dispatch research agents per section (governor limits, sharing, security, performance).</span>
3. <span data-proof="authored" data-by="ai:claude">Merge findings into plan.</span>
4. <span data-proof="authored" data-by="ai:claude">Add Salesforce-specific depth (order of execution, API versions, known issues).</span>

**<span data-proof="authored" data-by="ai:claude">Gate:</span>** <span data-proof="authored" data-by="ai:claude">Plan sections must have research notes before proceeding.</span>

***

## <span data-proof="authored" data-by="ai:claude">Stage 3: WORK</span>

<span data-proof="authored" data-by="ai:claude">Implement the plan:</span>

1. <span data-proof="authored" data-by="ai:claude">Pre-implementation research (parallel):</span>

   * <span data-proof="authored" data-by="ai:claude">Task sf-learnings-researcher(plan)</span>

   * <span data-proof="authored" data-by="ai:claude">Task sf-repo-research-analyst(plan)</span>
2. <span data-proof="authored" data-by="ai:claude">Route via indexes for applicable agents/skills.</span>
3. <span data-proof="authored" data-by="ai:claude">Implement with native-first approach.</span>
4. <span data-proof="authored" data-by="ai:claude">Write tests alongside code.</span>
5. <span data-proof="authored" data-by="ai:claude">Run System-Wide Test Check (5 questions):</span>

   * <span data-proof="authored" data-by="ai:claude">Trigger fire check</span>

   * <span data-proof="authored" data-by="ai:claude">Bulk test check (200+ records)</span>

   * <span data-proof="authored" data-by="ai:claude">Governor limit test</span>

   * <span data-proof="authored" data-by="ai:claude">Sharing scenario check</span>

   * <span data-proof="authored" data-by="ai:claude">Integration mock check</span>
6. <span data-proof="authored" data-by="ai:claude">Make incremental commits.</span>

**<span data-proof="authored" data-by="ai:claude">Gate:</span>** <span data-proof="authored" data-by="ai:claude">All 5 test check questions must pass before proceeding.</span>

***

## <span data-proof="authored" data-by="ai:claude">Stage 4: REVIEW</span>

<span data-proof="authored" data-by="ai:claude">Review with parallel agent dispatch:</span>

1. <span data-proof="authored" data-by="ai:claude">Classify changed files.</span>
2. <span data-proof="authored" data-by="ai:claude">Dispatch all applicable review agents in parallel (comprehensive depth):</span>

   * <span data-proof="authored" data-by="ai:claude">Stack-specific agents (Apex, LWC, Flow, Integration)</span>

   * <span data-proof="authored" data-by="ai:claude">Architecture agents (pattern recognition, metadata consistency)</span>

   * <span data-proof="authored" data-by="ai:claude">Workflow agents (code simplicity, deployment verification)</span>

   * <span data-proof="authored" data-by="ai:claude">Research agents (best practices validation)</span>
3. <span data-proof="authored" data-by="ai:claude">Consolidate findings by severity.</span>

**<span data-proof="authored" data-by="ai:claude">Gate:</span>** <span data-proof="authored" data-by="ai:claude">No Critical or High findings remaining before proceeding.</span>

***

## <span data-proof="authored" data-by="ai:claude">Stage 5: RESOLVE</span>

<span data-proof="authored" data-by="ai:claude">Fix any review findings:</span>

1. <span data-proof="authored" data-by="ai:claude">Address Critical findings first, then High, then Medium.</span>
2. <span data-proof="authored" data-by="ai:claude">For each fix:</span>

   * <span data-proof="authored" data-by="ai:claude">Make the code change</span>

   * <span data-proof="authored" data-by="ai:claude">Verify the fix doesn't introduce new issues</span>

   * <span data-proof="authored" data-by="ai:claude">Commit with descriptive message</span>
3. <span data-proof="authored" data-by="ai:claude">Re-run review on changed files only (fast depth).</span>

**<span data-proof="authored" data-by="ai:claude">Gate:</span>** <span data-proof="authored" data-by="ai:claude">Re-review returns no Critical or High findings.</span>

***

## <span data-proof="authored" data-by="ai:claude">Stage 6: TEST</span>

<span data-proof="authored" data-by="ai:claude">Run comprehensive tests:</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTA5LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
# Run all local tests with coverage
sf apex run test --test-level RunLocalTests --code-coverage --synchronous
```

1. <span data-proof="authored" data-by="ai:claude">Verify all tests pass.</span>
2. <span data-proof="authored" data-by="ai:claude">Verify code coverage ≥ 75% org-wide, ≥ 90% per class.</span>
3. <span data-proof="authored" data-by="ai:claude">Check for any test failures or coverage gaps.</span>

**<span data-proof="authored" data-by="ai:claude">Gate:</span>** <span data-proof="authored" data-by="ai:claude">All tests pass with required coverage. If tests fail, return to Stage 5.</span>

***

## <span data-proof="authored" data-by="ai:claude">Stage 7: DEPLOY (conditional)</span>

<span data-proof="authored" data-by="ai:claude">Based on</span> <span data-proof="authored" data-by="ai:claude">`$ARGUMENTS.deploy`:</span>

### <span data-proof="authored" data-by="ai:claude">deploy=none (default)</span>

<span data-proof="authored" data-by="ai:claude">Skip deployment. Report readiness.</span>

### <span data-proof="authored" data-by="ai:claude">deploy=scratch</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTYxLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
sf org create scratch --definition-file config/project-scratch-def.json --alias lfg-test
sf project deploy start --target-org lfg-test --test-level RunLocalTests
```

### <span data-proof="authored" data-by="ai:claude">deploy=sandbox</span>

1. <span data-proof="authored" data-by="ai:claude">Dispatch deployment verification:</span>

   * <span data-proof="authored" data-by="ai:claude">Task sf-deployment-verification-agent(changed_files)</span>
2. <span data-proof="authored" data-by="ai:claude">Validate deployment:</span>

   ```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NjAsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
   sf project deploy start --dry-run --test-level RunLocalTests
   ```
3. <span data-proof="authored" data-by="ai:claude">If validation passes and Go decision:</span>

   ```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTAsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
   sf project deploy start --test-level RunLocalTests
   ```

**<span data-proof="authored" data-by="ai:claude">Gate:</span>** <span data-proof="authored" data-by="ai:claude">Deployment succeeds with all tests passing.</span>

***

## <span data-proof="authored" data-by="ai:claude">Stage 8: COMPOUND</span>

<span data-proof="authored" data-by="ai:claude">After pipeline completes (regardless of deploy stage):</span>

1. <span data-proof="authored" data-by="ai:claude">Analyze what was built.</span>
2. <span data-proof="authored" data-by="ai:claude">Search for existing knowledge to avoid duplicates.</span>
3. <span data-proof="authored" data-by="ai:claude">Write solution documents to</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`.</span>
4. <span data-proof="authored" data-by="ai:claude">Update relevant agents/skills with new patterns.</span>
5. <span data-proof="authored" data-by="ai:claude">Update CLAUDE.md with project context.</span>

***

## <span data-proof="authored" data-by="ai:claude">Abort Conditions</span>

<span data-proof="authored" data-by="ai:claude">The pipeline aborts and asks for human input if:</span>

* <span data-proof="authored" data-by="ai:claude">Plan has no clear acceptance criteria (Stage 1)</span>

* <span data-proof="authored" data-by="ai:claude">Spec flow analysis finds Critical gaps with no obvious fix (Stage 1)</span>

* <span data-proof="authored" data-by="ai:claude">Review finds security vulnerabilities (Stage 4)</span>

* <span data-proof="authored" data-by="ai:claude">Tests fail after 2 resolve cycles (Stage 5-6 loop)</span>

* <span data-proof="authored" data-by="ai:claude">Deployment validation fails (Stage 7)</span>

***

## <span data-proof="authored" data-by="ai:claude">Output</span>

```
🚀 LFG Pipeline Complete

Feature: {feature_name}
Plan: docs/plans/{plan_file}

Pipeline Results:
├── Plan:    ✅ Created with {n} research agents
├── Deepen:  ✅ {n} sections enhanced
├── Work:    ✅ {n} files created/modified
├── Review:  ✅ {n} agents dispatched, {n} findings resolved
├── Resolve: ✅ {n} fixes applied
├── Test:    ✅ All tests passing, {n}% coverage
├── Deploy:  ✅ {deployed_to|skipped}
└── Compound:✅ {n} solutions documented

Knowledge captured:
- docs/solutions/: {n} new entries
- Skills updated: {list}
- Agents updated: {list}

Total time: {duration}
```