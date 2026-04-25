# <span data-proof="authored" data-by="ai:claude">Salesforce Agents Index</span>

<span data-proof="authored" data-by="ai:claude">Use this index to find agents by topical concern. After the V3 migration, all agents live in a flat</span> <span data-proof="authored" data-by="ai:claude">`agents/`</span> <span data-proof="authored" data-by="ai:claude">directory and are named</span> <span data-proof="authored" data-by="ai:claude">`sf-<name>.agent.md`. The topical groupings below are documentation aids — they do not correspond to filesystem paths.</span>

<span data-proof="authored" data-by="ai:claude">The Task tool can dispatch any of these agents in parallel. Each agent's</span> <span data-proof="authored" data-by="ai:claude">`description`</span> <span data-proof="authored" data-by="ai:claude">frontmatter carries its own auto-routing trigger phrases.</span>

***

## <span data-proof="authored" data-by="ai:claude">Routing Map</span>

| <span data-proof="authored" data-by="ai:claude">Classification</span> | <span data-proof="authored" data-by="ai:claude">Read Section</span>              | <span data-proof="authored" data-by="ai:claude">Avoid</span>                                             |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">AUTOMATION</span>     | <span data-proof="authored" data-by="ai:claude">Flow & Automation</span>         | <span data-proof="authored" data-by="ai:claude">Apex Development, LWC</span>                             |
| <span data-proof="authored" data-by="ai:claude">APEX</span>           | <span data-proof="authored" data-by="ai:claude">Apex Development</span>          | <span data-proof="authored" data-by="ai:claude">Flow & Automation</span>                                 |
| <span data-proof="authored" data-by="ai:claude">LWC</span>            | <span data-proof="authored" data-by="ai:claude">Lightning Web Components</span>  | <span data-proof="authored" data-by="ai:claude">Flow & Automation (unless Apex controller needed)</span> |
| <span data-proof="authored" data-by="ai:claude">INTEGRATION</span>    | <span data-proof="authored" data-by="ai:claude">Integration</span>               | <span data-proof="authored" data-by="ai:claude">Flow & Automation</span>                                 |
| <span data-proof="authored" data-by="ai:claude">ARCHITECTURE</span>   | <span data-proof="authored" data-by="ai:claude">Architecture & Data Model</span> | <span data-proof="authored" data-by="ai:claude">N/A (applies broadly)</span>                             |
| <span data-proof="authored" data-by="ai:claude">RESEARCH</span>       | <span data-proof="authored" data-by="ai:claude">Research</span>                  | <span data-proof="authored" data-by="ai:claude">N/A (dispatch for any task)</span>                       |
| <span data-proof="authored" data-by="ai:claude">WORKFLOW</span>       | <span data-proof="authored" data-by="ai:claude">Workflow</span>                  | <span data-proof="authored" data-by="ai:claude">N/A (dispatch as needed)</span>                          |

***

## <span data-proof="authored" data-by="ai:claude">Usage Guidance</span>

1. <span data-proof="authored" data-by="ai:claude">Confirm classification from the skill or task at hand.</span>
2. <span data-proof="authored" data-by="ai:claude">Locate the relevant agent in the topical section below.</span>
3. <span data-proof="authored" data-by="ai:claude">Use the Task tool to dispatch agents in parallel; the</span> <span data-proof="authored" data-by="ai:claude">`sf-review`</span> <span data-proof="authored" data-by="ai:claude">and</span> <span data-proof="authored" data-by="ai:claude">`sf-doc-review`</span> <span data-proof="authored" data-by="ai:claude">skills do this automatically.</span>
4. <span data-proof="authored" data-by="ai:claude">For mixed work, dispatch each applicable agent against the matching files.</span>

***

## <span data-proof="authored" data-by="ai:claude">Apex Development</span>

<span data-proof="authored" data-by="ai:claude">Apex classes, triggers, batch jobs, queueable, schedulable, services.</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                       | <span data-proof="authored" data-by="ai:claude">File</span>                                      | <span data-proof="authored" data-by="ai:claude">Use When</span>                                   |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Apex Trigger Architect</span>      | <span data-proof="authored" data-by="ai:claude">`sf-apex-trigger-architect.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">Designing trigger logic, handler patterns</span>  |
| <span data-proof="authored" data-by="ai:claude">Apex Governor Guardian</span>      | <span data-proof="authored" data-by="ai:claude">`sf-apex-governor-guardian.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">Checking SOQL/DML usage, limit compliance</span>  |
| <span data-proof="authored" data-by="ai:claude">Apex Bulkification Reviewer</span> | <span data-proof="authored" data-by="ai:claude">`sf-apex-bulkification-reviewer.agent.md`</span> | <span data-proof="authored" data-by="ai:claude">Ensuring code handles 200+ records</span>         |
| <span data-proof="authored" data-by="ai:claude">Apex Security Sentinel</span>      | <span data-proof="authored" data-by="ai:claude">`sf-apex-security-sentinel.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">CRUD/FLS checks, SOQL injection prevention</span> |
| <span data-proof="authored" data-by="ai:claude">Apex Exception Handler</span>      | <span data-proof="authored" data-by="ai:claude">`sf-apex-exception-handler.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">Error handling patterns, custom exceptions</span> |
| <span data-proof="authored" data-by="ai:claude">Apex Test Coverage Analyst</span>  | <span data-proof="authored" data-by="ai:claude">`sf-apex-test-coverage-analyst.agent.md`</span>  | <span data-proof="authored" data-by="ai:claude">Test class design, coverage strategy</span>       |

***

## <span data-proof="authored" data-by="ai:claude">Flow & Automation</span>

<span data-proof="authored" data-by="ai:claude">Flows and declarative automation.</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                         | <span data-proof="authored" data-by="ai:claude">File</span>                                        | <span data-proof="authored" data-by="ai:claude">Use When</span>                                     |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Flow Governor Monitor</span>         | <span data-proof="authored" data-by="ai:claude">`sf-flow-governor-monitor.agent.md`</span>         | <span data-proof="authored" data-by="ai:claude">Checking Flow limits, DML/SOQL in Flows</span>      |
| <span data-proof="authored" data-by="ai:claude">Flow Complexity Analyzer</span>      | <span data-proof="authored" data-by="ai:claude">`sf-flow-complexity-analyzer.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">Evaluating Flow maintainability, refactoring</span> |
| <span data-proof="authored" data-by="ai:claude">Process Automation Strategist</span> | <span data-proof="authored" data-by="ai:claude">`sf-process-automation-strategist.agent.md`</span> | <span data-proof="authored" data-by="ai:claude">Choosing between Flow, Apex, or triggers</span>     |
| <span data-proof="authored" data-by="ai:claude">Validation Rule Reviewer</span>      | <span data-proof="authored" data-by="ai:claude">`sf-validation-rule-reviewer.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">Validation rule logic, error messages</span>        |

***

## <span data-proof="authored" data-by="ai:claude">Lightning Web Components (LWC)</span>

<span data-proof="authored" data-by="ai:claude">LWC components and Aura migrations. Use Apex agents only if reviewing the Apex controller.</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                       | <span data-proof="authored" data-by="ai:claude">File</span>                                      | <span data-proof="authored" data-by="ai:claude">Use When</span>                                   |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">LWC Architecture Strategist</span> | <span data-proof="authored" data-by="ai:claude">`sf-lwc-architecture-strategist.agent.md`</span> | <span data-proof="authored" data-by="ai:claude">Component hierarchy, state management</span>      |
| <span data-proof="authored" data-by="ai:claude">LWC Performance Oracle</span>      | <span data-proof="authored" data-by="ai:claude">`sf-lwc-performance-oracle.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">Wire vs imperative, rendering optimization</span> |
| <span data-proof="authored" data-by="ai:claude">LWC Security Reviewer</span>       | <span data-proof="authored" data-by="ai:claude">`sf-lwc-security-reviewer.agent.md`</span>       | <span data-proof="authored" data-by="ai:claude">XSS prevention, secure data handling</span>       |
| <span data-proof="authored" data-by="ai:claude">LWC Accessibility Guardian</span>  | <span data-proof="authored" data-by="ai:claude">`sf-lwc-accessibility-guardian.agent.md`</span>  | <span data-proof="authored" data-by="ai:claude">ARIA, keyboard navigation, screen readers</span>  |
| <span data-proof="authored" data-by="ai:claude">Aura Migration Advisor</span>      | <span data-proof="authored" data-by="ai:claude">`sf-aura-migration-advisor.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">Converting Aura components to LWC</span>          |

***

## <span data-proof="authored" data-by="ai:claude">Integration</span>

<span data-proof="authored" data-by="ai:claude">APIs, callouts, events, external systems, MCP tools.</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                             | <span data-proof="authored" data-by="ai:claude">File</span>                                            | <span data-proof="authored" data-by="ai:claude">Use When</span>                                                                                            |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Callout Pattern Reviewer</span>          | <span data-proof="authored" data-by="ai:claude">`sf-callout-pattern-reviewer.agent.md`</span>          | <span data-proof="authored" data-by="ai:claude">HTTP callouts, Named Credentials, retry logic</span>                                                       |
| <span data-proof="authored" data-by="ai:claude">REST API Architect</span>                | <span data-proof="authored" data-by="ai:claude">`sf-rest-api-architect.agent.md`</span>                | <span data-proof="authored" data-by="ai:claude">REST API design, versioning,</span> <span data-proof="authored" data-by="ai:claude">`@RestResource`</span> |
| <span data-proof="authored" data-by="ai:claude">Integration Security Sentinel</span>     | <span data-proof="authored" data-by="ai:claude">`sf-integration-security-sentinel.agent.md`</span>     | <span data-proof="authored" data-by="ai:claude">OAuth, Named Credentials, secure data exchange</span>                                                      |
| <span data-proof="authored" data-by="ai:claude">Platform Event Strategist</span>         | <span data-proof="authored" data-by="ai:claude">`sf-platform-event-strategist.agent.md`</span>         | <span data-proof="authored" data-by="ai:claude">Platform Events, high-volume patterns, EDA</span>                                                          |
| <span data-proof="authored" data-by="ai:claude">MCP Server Configuration Reviewer</span> | <span data-proof="authored" data-by="ai:claude">`sf-mcp-server-configuration-reviewer.agent.md`</span> | <span data-proof="authored" data-by="ai:claude">Hosted MCP server setup, ECA, template wiring</span>                                                       |
| <span data-proof="authored" data-by="ai:claude">MCP Tool Builder</span>                  | <span data-proof="authored" data-by="ai:claude">`sf-mcp-tool-builder-agent.agent.md`</span>            | <span data-proof="authored" data-by="ai:claude">Building custom MCP tools — InvocableMethod, Flow, Named Queries</span>                                    |

***

## <span data-proof="authored" data-by="ai:claude">Architecture & Data Model</span>

<span data-proof="authored" data-by="ai:claude">Schema, sharing, metadata, design patterns. Applies broadly across classifications.</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                          | <span data-proof="authored" data-by="ai:claude">File</span>                                         | <span data-proof="authored" data-by="ai:claude">Use When</span>                                                |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Data Model Architect</span>           | <span data-proof="authored" data-by="ai:claude">`sf-data-model-architect.agent.md`</span>           | <span data-proof="authored" data-by="ai:claude">Schema design, relationships, indexing</span>                  |
| <span data-proof="authored" data-by="ai:claude">Sharing Security Analyst</span>       | <span data-proof="authored" data-by="ai:claude">`sf-sharing-security-analyst.agent.md`</span>       | <span data-proof="authored" data-by="ai:claude">OWD, sharing rules, record access</span>                       |
| <span data-proof="authored" data-by="ai:claude">Metadata Consistency Checker</span>   | <span data-proof="authored" data-by="ai:claude">`sf-metadata-consistency-checker.agent.md`</span>   | <span data-proof="authored" data-by="ai:claude">Profile/permission alignment, deployment consistency</span>    |
| <span data-proof="authored" data-by="ai:claude">Pattern Recognition Specialist</span> | <span data-proof="authored" data-by="ai:claude">`sf-pattern-recognition-specialist.agent.md`</span> | <span data-proof="authored" data-by="ai:claude">Identifying anti-patterns and improvement opportunities</span> |

***

## <span data-proof="authored" data-by="ai:claude">Research</span>

<span data-proof="authored" data-by="ai:claude">Fast-dispatch research agents.</span> <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher`</span> <span data-proof="authored" data-by="ai:claude">runs on</span> <span data-proof="authored" data-by="ai:claude">`model: haiku`</span> <span data-proof="authored" data-by="ai:claude">for speed; others use</span> <span data-proof="authored" data-by="ai:claude">`model: inherit`.</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                     | <span data-proof="authored" data-by="ai:claude">File</span>                                    | <span data-proof="authored" data-by="ai:claude">Use When</span>                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <span data-proof="authored" data-by="ai:claude">Learnings Researcher</span>      | <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">Search</span> <span data-proof="authored" data-by="ai:claude">`docs/solutions/`</span> <span data-proof="authored" data-by="ai:claude">for relevant past Salesforce learnings</span>                                                       |
| <span data-proof="authored" data-by="ai:claude">Best Practices Researcher</span> | <span data-proof="authored" data-by="ai:claude">`sf-best-practices-researcher.agent.md`</span> | <span data-proof="authored" data-by="ai:claude">External best-practice search (Context7, docs, community)</span>                                                                                                                                                                           |
| <span data-proof="authored" data-by="ai:claude">Git History Analyzer</span>      | <span data-proof="authored" data-by="ai:claude">`sf-git-history-analyzer.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">Trace metadata + Apex evolution via</span> <span data-proof="authored" data-by="ai:claude">`git log -S`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`git blame`</span> |
| <span data-proof="authored" data-by="ai:claude">Repo Research Analyst</span>     | <span data-proof="authored" data-by="ai:claude">`sf-repo-research-analyst.agent.md`</span>     | <span data-proof="authored" data-by="ai:claude">Understand the Salesforce project structure and conventions</span>                                                                                                                                                                         |
| <span data-proof="authored" data-by="ai:claude">Framework Docs Researcher</span> | <span data-proof="authored" data-by="ai:claude">`sf-framework-docs-researcher.agent.md`</span> | <span data-proof="authored" data-by="ai:claude">Salesforce platform docs (Apex, LWC, Flow, Metadata API, Tooling API)</span>                                                                                                                                                               |

***

## <span data-proof="authored" data-by="ai:claude">Workflow</span>

<span data-proof="authored" data-by="ai:claude">Cross-cutting workflow agents dispatched by</span> <span data-proof="authored" data-by="ai:claude">`sf-review`,</span> <span data-proof="authored" data-by="ai:claude">`sf-work`,</span> <span data-proof="authored" data-by="ai:claude">`sf-debug`, and other orchestration skills.</span>

| <span data-proof="authored" data-by="ai:claude">Agent</span>                         | <span data-proof="authored" data-by="ai:claude">File</span>                                        | <span data-proof="authored" data-by="ai:claude">Use When</span>                                                          |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| <span data-proof="authored" data-by="ai:claude">Spec Flow Analyzer</span>            | <span data-proof="authored" data-by="ai:claude">`sf-spec-flow-analyzer.agent.md`</span>            | <span data-proof="authored" data-by="ai:claude">Permutation analysis, gap identification in plans/specs</span>           |
| <span data-proof="authored" data-by="ai:claude">Bug Reproduction Validator</span>    | <span data-proof="authored" data-by="ai:claude">`sf-bug-reproduction-validator.agent.md`</span>    | <span data-proof="authored" data-by="ai:claude">Systematic 6-step Salesforce bug reproduction</span>                     |
| <span data-proof="authored" data-by="ai:claude">PR Comment Resolver</span>           | <span data-proof="authored" data-by="ai:claude">`sf-pr-comment-resolver.agent.md`</span>           | <span data-proof="authored" data-by="ai:claude">Parallel resolution of PR review threads</span>                          |
| <span data-proof="authored" data-by="ai:claude">Code Simplicity Reviewer</span>      | <span data-proof="authored" data-by="ai:claude">`sf-code-simplicity-reviewer.agent.md`</span>      | <span data-proof="authored" data-by="ai:claude">YAGNI enforcement, LOC reduction estimates</span>                        |
| <span data-proof="authored" data-by="ai:claude">Deployment Verification Agent</span> | <span data-proof="authored" data-by="ai:claude">`sf-deployment-verification-agent.agent.md`</span> | <span data-proof="authored" data-by="ai:claude">Go/No-Go deployment checklists for Salesforce metadata + data ops</span> |

***

## <span data-proof="authored" data-by="ai:claude">V3-Ported Review and Research Agents (planned for U7)</span>

<span data-proof="authored" data-by="ai:claude">The following agents are scheduled for porting in U7 of the V3 migration plan (`docs/plans/2026-04-25-001-feat-v3-architecture-migration-plan.md`). Until ported, the</span> <span data-proof="authored" data-by="ai:claude">`sf-review`</span> <span data-proof="authored" data-by="ai:claude">and</span> <span data-proof="authored" data-by="ai:claude">`sf-doc-review`</span> <span data-proof="authored" data-by="ai:claude">skills fall back to the agents above. After porting, this section will be promoted into regular topical groups.</span>

* <span data-proof="authored" data-by="ai:claude">`sf-correctness-reviewer.agent.md`</span> <span data-proof="authored" data-by="ai:claude">(always-on logic/state correctness)</span>

* <span data-proof="authored" data-by="ai:claude">`sf-maintainability-reviewer.agent.md`</span> <span data-proof="authored" data-by="ai:claude">(always-on premature abstraction / dead code)</span>

* <span data-proof="authored" data-by="ai:claude">`sf-testing-reviewer.agent.md`</span> <span data-proof="authored" data-by="ai:claude">(always-on coverage gaps, brittle tests)</span>

* <span data-proof="authored" data-by="ai:claude">`sf-project-standards-reviewer.agent.md`</span> <span data-proof="authored" data-by="ai:claude">(always-on CLAUDE/AGENTS.md adherence)</span>

* <span data-proof="authored" data-by="ai:claude">`sf-architecture-strategist.agent.md`</span> <span data-proof="authored" data-by="ai:claude">(architectural compliance)</span>

* <span data-proof="authored" data-by="ai:claude">`sf-performance-oracle.agent.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-performance-reviewer.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-reliability-reviewer.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-api-contract-reviewer.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-data-migrations-reviewer.agent.md`</span> <span data-proof="authored" data-by="ai:claude">(Salesforce metadata deploy safety)</span>

* <span data-proof="authored" data-by="ai:claude">`sf-data-integrity-guardian.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-feasibility-reviewer.agent.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-coherence-reviewer.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-product-lens-reviewer.agent.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-scope-guardian-reviewer.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-security-lens-reviewer.agent.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-design-lens-reviewer.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-adversarial-reviewer.agent.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-adversarial-document-reviewer.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-previous-comments-reviewer.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-issue-intelligence-analyst.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-session-historian.agent.md`</span>

* <span data-proof="authored" data-by="ai:claude">`sf-slack-researcher.agent.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-web-researcher.agent.md`</span>

***

## <span data-proof="authored" data-by="ai:claude">Notes</span>

* <span data-proof="authored" data-by="ai:claude">All agents use V3 frontmatter:</span> <span data-proof="authored" data-by="ai:claude">`name`,</span> <span data-proof="authored" data-by="ai:claude">`description`,</span> <span data-proof="authored" data-by="ai:claude">`model`,</span> <span data-proof="authored" data-by="ai:claude">`tools`,</span> <span data-proof="authored" data-by="ai:claude">`color`. The</span> <span data-proof="authored" data-by="ai:claude">`scope`</span> <span data-proof="authored" data-by="ai:claude">field has been retired.</span>

* <span data-proof="authored" data-by="ai:claude">`sf-learnings-researcher`</span> <span data-proof="authored" data-by="ai:claude">keeps</span> <span data-proof="authored" data-by="ai:claude">`model: haiku`</span> <span data-proof="authored" data-by="ai:claude">for speed;</span> <span data-proof="authored" data-by="ai:claude">`sf-spec-flow-analyzer`</span> <span data-proof="authored" data-by="ai:claude">keeps</span> <span data-proof="authored" data-by="ai:claude">`model: sonnet`</span> <span data-proof="authored" data-by="ai:claude">for depth; all other agents use</span> <span data-proof="authored" data-by="ai:claude">`model: inherit`.</span>

* <span data-proof="authored" data-by="ai:claude">Workflow agents that may write files (`sf-bug-reproduction-validator`,</span> <span data-proof="authored" data-by="ai:claude">`sf-pr-comment-resolver`,</span> <span data-proof="authored" data-by="ai:claude">`sf-deployment-verification-agent`,</span> <span data-proof="authored" data-by="ai:claude">`sf-mcp-tool-builder-agent`) get the full</span> <span data-proof="authored" data-by="ai:claude">`Read, Edit, Write, Grep, Glob, Bash`</span> <span data-proof="authored" data-by="ai:claude">tool set; review/research agents get</span> <span data-proof="authored" data-by="ai:claude">`Read, Grep, Glob, Bash`.</span>