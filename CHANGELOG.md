# <span data-proof="authored" data-by="ai:claude">Changelog</span>

<span data-proof="authored" data-by="ai:claude">All notable changes to the</span> <span data-proof="authored" data-by="ai:claude">`sf-compound-engineering-plugin`</span> <span data-proof="authored" data-by="ai:claude">will be documented in this file.</span>

<span data-proof="authored" data-by="ai:claude">The format is based on</span> [<span data-proof="authored" data-by="ai:claude">Keep a Changelog</span>](https://keepachangelog.com/en/1.1.0/) <span data-proof="authored" data-by="ai:claude">and this project adheres to</span> [<span data-proof="authored" data-by="ai:claude">Semantic Versioning</span>](https://semver.org/spec/v2.0.0.html)<span data-proof="authored" data-by="ai:claude">.</span>

## <span data-proof="authored" data-by="ai:claude">[3.0.0-beta.1] - 2026-04-25</span>

<span data-proof="authored" data-by="ai:claude">V3 capability ports: 22 V3 skills and 24 V3 review/research agents added as Salesforce-aware sf-* counterparts.</span>

### <span data-proof="authored" data-by="ai:claude">Added</span>

* ****                           

* ****   

  * <span data-proof="authored" data-by="ai:claude">Always-on review (4):</span> <span data-proof="authored" data-by="ai:claude">`sf-correctness-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-maintainability-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-testing-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-project-standards-reviewer`.</span>

  * <span data-proof="authored" data-by="ai:claude">Conditional review (7):</span> <span data-proof="authored" data-by="ai:claude">`sf-architecture-strategist`,</span> <span data-proof="authored" data-by="ai:claude">`sf-performance-oracle`,</span> <span data-proof="authored" data-by="ai:claude">`sf-performance-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-reliability-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-api-contract-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-data-migrations-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-data-integrity-guardian`.</span>

  * <span data-proof="authored" data-by="ai:claude">Doc-review lenses (6):</span> <span data-proof="authored" data-by="ai:claude">`sf-feasibility-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-coherence-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-product-lens-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-scope-guardian-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-security-lens-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-design-lens-reviewer`.</span>

  * <span data-proof="authored" data-by="ai:claude">Adversarial (2):</span> <span data-proof="authored" data-by="ai:claude">`sf-adversarial-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-adversarial-document-reviewer`.</span>

  * <span data-proof="authored" data-by="ai:claude">Workflow / research (5):</span> <span data-proof="authored" data-by="ai:claude">`sf-previous-comments-reviewer`,</span> <span data-proof="authored" data-by="ai:claude">`sf-issue-intelligence-analyst`,</span> <span data-proof="authored" data-by="ai:claude">`sf-session-historian`,</span> <span data-proof="authored" data-by="ai:claude">`sf-slack-researcher`,</span> <span data-proof="authored" data-by="ai:claude">`sf-web-researcher`.</span>

### <span data-proof="authored" data-by="ai:claude">Changed</span>

* <span data-proof="authored" data-by="ai:claude">Plugin version bumped to</span> <span data-proof="authored" data-by="ai:claude">`3.0.0-beta.1`</span> <span data-proof="authored" data-by="ai:claude">across all four manifests (`.claude-plugin/plugin.json`,</span> <span data-proof="authored" data-by="ai:claude">`.claude-plugin/marketplace.json`,</span> <span data-proof="authored" data-by="ai:claude">`.cursor-plugin/plugin.json`,</span> <span data-proof="authored" data-by="ai:claude">`.codex-plugin/plugin.json`).</span>

* <span data-proof="authored" data-by="ai:claude">Total agent count: 35 → 59. Total skill count: 23 → 45.</span>

### <span data-proof="authored" data-by="ai:claude">Not Ported (out of scope)</span>

* <span data-proof="authored" data-by="ai:claude">Personality reviewer agents tied to non-Salesforce stacks (Rails, frontend race conditions, Ruby gem READMEs, Swift / iOS).</span>

*       

*  

*     

## <span data-proof="authored" data-by="ai:claude">[3.0.0-alpha.1] - 2026-04-25</span>

**<span data-proof="authored" data-by="ai:claude">BREAKING.</span>** <span data-proof="authored" data-by="ai:claude">V3 architecture migration — skills replace commands, agents flatten with</span> <span data-proof="authored" data-by="ai:claude">`<name>.agent.md`</span> <span data-proof="authored" data-by="ai:claude">naming, multi-platform manifests added.</span>

### <span data-proof="authored" data-by="ai:claude">BREAKING CHANGES</span>

* ****           

* **<span data-proof="authored" data-by="ai:claude">All 35 agents flattened.</span>** <span data-proof="authored" data-by="ai:claude">Files moved from</span> <span data-proof="authored" data-by="ai:claude">`agents/{apex,architecture,automation,integration,lwc,research,workflow}/<name>.md`</span> <span data-proof="authored" data-by="ai:claude">to</span> <span data-proof="authored" data-by="ai:claude">`agents/sf-<name>.agent.md`</span> <span data-proof="authored" data-by="ai:claude">(flat layout,</span> <span data-proof="authored" data-by="ai:claude">`.agent.md`</span> <span data-proof="authored" data-by="ai:claude">suffix). Category folders are removed; topical groupings remain in</span> <span data-proof="authored" data-by="ai:claude">`agents/index.md`</span> <span data-proof="authored" data-by="ai:claude">as documentation aids only.</span>

* **<span data-proof="authored" data-by="ai:claude">Agent frontmatter updated to V3 conventions.</span>** <span data-proof="authored" data-by="ai:claude">Fields:</span> <span data-proof="authored" data-by="ai:claude">`name`,</span> <span data-proof="authored" data-by="ai:claude">`description`,</span> <span data-proof="authored" data-by="ai:claude">`model`,</span> <span data-proof="authored" data-by="ai:claude">`tools`,</span> <span data-proof="authored" data-by="ai:claude">`color`. The</span> <span data-proof="authored" data-by="ai:claude">`scope`</span> <span data-proof="authored" data-by="ai:claude">field is retired.</span> <span data-proof="authored" data-by="ai:claude">`model: inherit`</span> <span data-proof="authored" data-by="ai:claude">is the default; research agents keep</span> <span data-proof="authored" data-by="ai:claude">`model: haiku`</span> <span data-proof="authored" data-by="ai:claude">for speed; deep-analysis agents keep</span> <span data-proof="authored" data-by="ai:claude">`model: sonnet`. Tools default to</span> <span data-proof="authored" data-by="ai:claude">`Read, Grep, Glob, Bash`; workflow agents that may write files get the full</span> <span data-proof="authored" data-by="ai:claude">`Read, Edit, Write, Grep, Glob, Bash`</span> <span data-proof="authored" data-by="ai:claude">set.</span>

* **<span data-proof="authored" data-by="ai:claude">Skill frontmatter updated to V3 conventions.</span>** <span data-proof="authored" data-by="ai:claude">Fields:</span> <span data-proof="authored" data-by="ai:claude">`name`,</span> <span data-proof="authored" data-by="ai:claude">`description`,</span> <span data-proof="authored" data-by="ai:claude">`argument-hint`. Skill descriptions enumerate Salesforce-flavored auto-routing trigger phrases.</span>

* ****   

### <span data-proof="authored" data-by="ai:claude">Added</span>

* <span data-proof="authored" data-by="ai:claude">`.cursor-plugin/plugin.json`</span> <span data-proof="authored" data-by="ai:claude">— Cursor manifest for native install in Cursor IDE.</span>

* <span data-proof="authored" data-by="ai:claude">`.codex-plugin/plugin.json`</span> <span data-proof="authored" data-by="ai:claude">— Codex manifest with</span> <span data-proof="authored" data-by="ai:claude">`skills`</span> <span data-proof="authored" data-by="ai:claude">path and</span> <span data-proof="authored" data-by="ai:claude">`interface`</span> <span data-proof="authored" data-by="ai:claude">metadata for native Codex install.</span>

* <span data-proof="authored" data-by="ai:claude">`agents/index.md`</span> <span data-proof="authored" data-by="ai:claude">— V3 flat-layout routing index (rewritten).</span>

*  

* <span data-proof="authored" data-by="ai:claude">This</span> <span data-proof="authored" data-by="ai:claude">`CHANGELOG.md`</span> <span data-proof="authored" data-by="ai:claude">file.</span>

### <span data-proof="authored" data-by="ai:claude">Changed</span>

* <span data-proof="authored" data-by="ai:claude">`.claude-plugin/plugin.json`</span> <span data-proof="authored" data-by="ai:claude">version:</span> <span data-proof="authored" data-by="ai:claude">`2.2.0`</span> <span data-proof="authored" data-by="ai:claude">→</span> <span data-proof="authored" data-by="ai:claude">`3.0.0-alpha.1`. Description and keywords updated for multi-platform / skills-first.</span>

* <span data-proof="authored" data-by="ai:claude">`.claude-plugin/marketplace.json`</span> <span data-proof="authored" data-by="ai:claude">catalog and entry version bumped to</span> <span data-proof="authored" data-by="ai:claude">`3.0.0-alpha.1`.</span>

* <span data-proof="authored" data-by="ai:claude">`CLAUDE.md`</span> <span data-proof="authored" data-by="ai:claude">rewritten for V3 architecture. The "Hosted MCP Key Gotchas" section (8 items) and "Protected Artifacts" rules are preserved verbatim.</span>

* <span data-proof="authored" data-by="ai:claude">`README.md`</span> <span data-proof="authored" data-by="ai:claude">updated: BREAKING migration banner, component counts (35 → 59 agents, 23 → 45 skills), workflow diagram clarified that entry points are skills.</span>

### <span data-proof="authored" data-by="ai:claude">Removed</span>

* <span data-proof="authored" data-by="ai:claude">The</span> <span data-proof="authored" data-by="ai:claude">`commands/`</span> <span data-proof="authored" data-by="ai:claude">directory and its 7 files (`sf-brainstorm.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-plan.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-deepen.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-work.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-review.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-compound.md`,</span> <span data-proof="authored" data-by="ai:claude">`sf-lfg.md`). The bodies were preserved in their new skill homes.</span>

* <span data-proof="authored" data-by="ai:claude">The 7 agent category subdirectories (`agents/{apex,architecture,automation,integration,lwc,research,workflow}/`). All agent files were preserved via</span> <span data-proof="authored" data-by="ai:claude">`git mv`</span> <span data-proof="authored" data-by="ai:claude">so blame and history follow.</span>

* <span data-proof="authored" data-by="ai:claude">`scope`</span> <span data-proof="authored" data-by="ai:claude">field from all agent frontmatter (V3 retired this field).</span>

### <span data-proof="authored" data-by="ai:claude">Migration Guide for v2.x Users</span>

<span data-proof="authored" data-by="ai:claude">If you have scripts, docs, or muscle memory tied to v2.x, here's what changes:</span>

| <span data-proof="authored" data-by="ai:claude">v2.x</span>                                                                                                                                                         | <span data-proof="authored" data-by="ai:claude">v3.x</span>                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`/sf-plan`</span> <span data-proof="authored" data-by="ai:claude">(command, in</span> <span data-proof="authored" data-by="ai:claude">`commands/sf-plan.md`)</span> | <span data-proof="authored" data-by="ai:claude">`/sf-plan`</span> <span data-proof="authored" data-by="ai:claude">(skill, in</span> <span data-proof="authored" data-by="ai:claude">`skills/sf-plan/SKILL.md`)</span>         |
| <span data-proof="authored" data-by="ai:claude">`agents/apex/apex-trigger-architect.md`</span>                                                                                                                      | <span data-proof="authored" data-by="ai:claude">`agents/sf-apex-trigger-architect.agent.md`</span>                                                                                                                            |
| <span data-proof="authored" data-by="ai:claude">`agents/research/sf-learnings-researcher.md`</span>                                                                                                                 | <span data-proof="authored" data-by="ai:claude">`agents/sf-learnings-researcher.agent.md`</span>                                                                                                                              |
| <span data-proof="authored" data-by="ai:claude">`agents/workflow/sf-spec-flow-analyzer.md`</span>                                                                                                                   | <span data-proof="authored" data-by="ai:claude">`agents/sf-spec-flow-analyzer.agent.md`</span>                                                                                                                                |
| <span data-proof="authored" data-by="ai:claude">Agent frontmatter</span> <span data-proof="authored" data-by="ai:claude">`scope: APEX_ONLY`</span>                                                                  | <span data-proof="authored" data-by="ai:claude">(removed; topical grouping is in</span> <span data-proof="authored" data-by="ai:claude">`agents/index.md`</span> <span data-proof="authored" data-by="ai:claude">only)</span> |
| <span data-proof="authored" data-by="ai:claude">Single-target Claude Code install</span>                                                                                                                            | <span data-proof="authored" data-by="ai:claude">Multi-target install (Claude Code, Cursor, Codex)</span>                                                                                                                      |

**<span data-proof="authored" data-by="ai:claude">For most users</span>**<span data-proof="authored" data-by="ai:claude">: re-install the plugin (`/plugin update sf-compound-engineering`). Slash invocations (`/sf-plan`,</span> <span data-proof="authored" data-by="ai:claude">`/sf-debug`,</span> <span data-proof="authored" data-by="ai:claude">`/sf-review`) work identically. Custom scripts that hard-coded paths under</span> <span data-proof="authored" data-by="ai:claude">`commands/`</span> <span data-proof="authored" data-by="ai:claude">or</span> <span data-proof="authored" data-by="ai:claude">`agents/<category>/`</span> <span data-proof="authored" data-by="ai:claude">need updating — see the table above.</span>

## <span data-proof="authored" data-by="ai:claude">[2.2.0] and earlier</span>

 [](./Compound-Engineering-Plugin-Teardown.md)

<!-- PROOF
{
  "version": 2,
  "marks": {
    "m1777279511696_12": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-27T08:45:11.696Z",
      "range": {
        "from": 345,
        "to": 1089
      },
      "content": "22 V3 capability skills as Salesforce-aware sf-* skeletons. Each carries V3 frontmatter (name, description with auto-routing trigger phrases, argument-hint), a Salesforce Angle bullet list, and a self-contained Procedure section. Skills shipped: sf-debug, sf-doc-review, sf-pr-description, sf-resolve-pr-feedback, sf-update, sf-setup, sf-sessions, sf-session-inventory, sf-session-extract, sf-clean-gone-branches, sf-commit, sf-commit-push-pr, sf-ideate, sf-optimize, sf-agent-native-architecture, sf-agent-native-audit, sf-compound-refresh, sf-release-notes, sf-report-bug, sf-slack-research, sf-proof, sf-demo-reel.\n24 V3 review/research agents as Salesforce-aware personas dispatched by sf-review and sf-doc-review:",
      "status": "pending"
    },
    "m1777279511690_11": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-27T08:45:11.690Z",
      "range": {
        "from": 2259,
        "to": 2633
      },
      "content": "Non-Salesforce design / test skills (frontend-design, figma-design-sync, design-iterator, design-implementation-reviewer, gemini-imagegen, test-xcode, test-browser).\nUpstream-only experimental beta variants (work-beta, polish-beta).\nA Bun/TypeScript cross-platform converter CLI — deferred; the existing Python sfce.py CLI is retained as-is.",
      "status": "pending"
    },
    "m1777279511684_10": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-27T08:45:11.684Z",
      "range": {
        "from": 2827,
        "to": 3189
      },
      "content": "commands/ directory removed. All seven workflow entry points (sf-brainstorm, sf-plan, sf-deepen, sf-work, sf-review, sf-compound, sf-lfg) are now skills under skills/<name>/SKILL.md. Direct invocation via /sf-<name> continues to work, and skills now auto-route from natural-language phrases via their description frontmatter — a capability commands cannot match.",
      "status": "pending"
    },
    "m1777279511679_9": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-27T08:45:11.679Z",
      "range": {
        "from": 4026,
        "to": 4205
      },
      "content": "sf- prefix is now the universal namespace. Every agent and skill is prefixed sf- so the Salesforce identity is unambiguous when the plugin coexists with other compound-engineering-style tools.",
      "status": "pending"
    },
    "m1777279511674_8": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-27T08:45:11.674Z",
      "range": {
        "from": 4475,
        "to": 4600
      },
      "content": "skills/index.md — V3 skill index covering core workflow skills, domain knowledge skills, and V3 capability skills (rewritten).",
      "status": "pending"
    },
    "m1777279511666_7": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-04-27T08:45:11.666Z",
      "range": {
        "from": 6588,
        "to": 6900
      },
      "content": "See git history for v2.x release notes. Background research that informed the v3 migration is captured in Compound-Engineering-Plugin-Teardown.md — a 1628-line gap analysis dated 2026-03-02 that surveyed the broader compound-engineering ecosystem before the v3 migration was scoped.",
      "status": "pending"
    }
  }
}
-->

<!-- PROOF:END -->
