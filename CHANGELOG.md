# Changelog

All notable changes to the Salesforce Compound Engineering Plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-29

### Added
- **23 Specialized Agents**
  - Apex (6): governor-guardian, security-sentinel, bulkification-reviewer, trigger-architect, test-coverage-analyst, exception-handler
  - LWC (5): performance-oracle, security-reviewer, accessibility-guardian, architecture-strategist, aura-migration-advisor
  - Automation (4): flow-complexity-analyzer, flow-governor-monitor, process-automation-strategist, validation-rule-reviewer
  - Integration (4): rest-api-architect, callout-pattern-reviewer, platform-event-strategist, integration-security-sentinel
  - Architecture (4): data-model-architect, sharing-security-analyst, metadata-consistency-checker, pattern-recognition-specialist

- **9 Commands**
  - `/sf:plan` - Create implementation plans
  - `/sf:work` - Execute plans systematically
  - `/sf:review` - Multi-agent code review
  - `/sf:test` - Test execution and analysis
  - `/sf:deploy` - Deployment checklists
  - `/sf:health` - Org health analysis
  - `/sf:triage` - Process review findings
  - `/sf:resolve` - Fix triaged issues
  - `/sf:document` - Generate documentation

- **6 Skills**
  - `governor-limits` - Complete limits reference
  - `security-guide` - CRUD/FLS, injection prevention
  - `apex-patterns` - Trigger handler, selector, service patterns
  - `lwc-patterns` - Component communication, state management
  - `test-factory` - TestDataFactory patterns
  - `integration-patterns` - REST, callouts, platform events

- **Auto-Dispatch Rules** in CLAUDE.md
  - Automatic agent selection based on file type
  - Skill references for common scenarios

- **GitHub Actions CI/CD**
  - JSON validation
  - Component count verification
  - Automated releases

### Notes
- Initial release
- Inspired by [Every.to Compound Engineering](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it)

---

## Future Releases

### Planned for 1.1.0
- [ ] Additional agents for Experience Cloud
- [ ] Batch Apex patterns skill
- [ ] `/sf:migrate` command for Process Builder → Flow
- [ ] MCP server for Salesforce CLI integration

### Planned for 1.2.0
- [ ] Package dependency analyzer agent
- [ ] Technical debt scoring
- [ ] Integration with Linear/Jira for issue tracking
