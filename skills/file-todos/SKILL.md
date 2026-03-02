# <span data-proof="authored" data-by="ai:claude">File-Based Todos Skill</span>

<span data-proof="authored" data-by="ai:claude">Track project tasks as individual markdown files in the</span> <span data-proof="authored" data-by="ai:claude">`todos/`</span> <span data-proof="authored" data-by="ai:claude">directory. Each file is a self-contained task with status, priority, and context.</span>

## <span data-proof="authored" data-by="ai:claude">File Naming Convention</span>

```
todos/{issue}-{status}-{priority}-{description}.md
```

| <span data-proof="authored" data-by="ai:claude">Segment</span>         | <span data-proof="authored" data-by="ai:claude">Values</span>                                                                                                                                                                                                      | <span data-proof="authored" data-by="ai:claude">Example</span>                                                                                                                                  |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`{issue}`</span>       | <span data-proof="authored" data-by="ai:claude">Issue/ticket number or</span> <span data-proof="authored" data-by="ai:claude">`local`</span>                                                                                                                       | <span data-proof="authored" data-by="ai:claude">`GH-42`,</span> <span data-proof="authored" data-by="ai:claude">`LIN-15`,</span> <span data-proof="authored" data-by="ai:claude">`local`</span> |
| <span data-proof="authored" data-by="ai:claude">`{status}`</span>      | <span data-proof="authored" data-by="ai:claude">`pending`,</span> <span data-proof="authored" data-by="ai:claude">`active`,</span> <span data-proof="authored" data-by="ai:claude">`done`,</span> <span data-proof="authored" data-by="ai:claude">`blocked`</span> | <span data-proof="authored" data-by="ai:claude">`active`</span>                                                                                                                                 |
| <span data-proof="authored" data-by="ai:claude">`{priority}`</span>    | <span data-proof="authored" data-by="ai:claude">`p0`,</span> <span data-proof="authored" data-by="ai:claude">`p1`,</span> <span data-proof="authored" data-by="ai:claude">`p2`,</span> <span data-proof="authored" data-by="ai:claude">`p3`</span>                 | <span data-proof="authored" data-by="ai:claude">`p1`</span>                                                                                                                                     |
| <span data-proof="authored" data-by="ai:claude">`{description}`</span> | <span data-proof="authored" data-by="ai:claude">Kebab-case summary (3-5 words)</span>                                                                                                                                                                              | <span data-proof="authored" data-by="ai:claude">`fix-soql-in-trigger`</span>                                                                                                                    |

### <span data-proof="authored" data-by="ai:claude">Examples</span>

```
todos/GH-42-active-p0-fix-soql-in-trigger.md
todos/local-pending-p1-add-bulk-tests.md
todos/LIN-15-done-p2-update-sharing-rules.md
todos/local-blocked-p1-waiting-on-api-access.md
```

## <span data-proof="authored" data-by="ai:claude">Todo File Template</span>

```markdown proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NDE4LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
---
issue: {issue_id}
status: {pending|active|done|blocked}
priority: {p0|p1|p2|p3}
created: YYYY-MM-DD
updated: YYYY-MM-DD
blocked_by: {optional - what's blocking}
related_files:
  - {file_path}
tags: ["{tag1}", "{tag2}"]
---

# {Task Title}

## Description
{What needs to be done}

## Acceptance Criteria
- [ ] {criterion 1}
- [ ] {criterion 2}

## Notes
{Any context, links, or decisions}

## Log
- {date}: {update}
```

## <span data-proof="authored" data-by="ai:claude">Status Transitions</span>

```
pending → active → done
    │         │
    │         └→ blocked → active → done
    └→ blocked → pending → active → done
```

## <span data-proof="authored" data-by="ai:claude">Priority Levels</span>

| <span data-proof="authored" data-by="ai:claude">Priority</span> | <span data-proof="authored" data-by="ai:claude">Meaning</span>                                    | <span data-proof="authored" data-by="ai:claude">Response Time</span>  |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`p0`</span>     | <span data-proof="authored" data-by="ai:claude">Critical — production issue or blocker</span>     | <span data-proof="authored" data-by="ai:claude">Immediate</span>      |
| <span data-proof="authored" data-by="ai:claude">`p1`</span>     | <span data-proof="authored" data-by="ai:claude">High — needed for current sprint/iteration</span> | <span data-proof="authored" data-by="ai:claude">This week</span>      |
| <span data-proof="authored" data-by="ai:claude">`p2`</span>     | <span data-proof="authored" data-by="ai:claude">Medium — important but not urgent</span>          | <span data-proof="authored" data-by="ai:claude">Next sprint</span>    |
| <span data-proof="authored" data-by="ai:claude">`p3`</span>     | <span data-proof="authored" data-by="ai:claude">Low — nice to have, backlog</span>                | <span data-proof="authored" data-by="ai:claude">When available</span> |

## <span data-proof="authored" data-by="ai:claude">Common Operations</span>

### <span data-proof="authored" data-by="ai:claude">Create a todo</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NzEsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
# Create new todo file
touch "todos/local-pending-p1-add-bulk-tests.md"
```

### <span data-proof="authored" data-by="ai:claude">List all active todos</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MjIsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
ls todos/*-active-*.md
```

### <span data-proof="authored" data-by="ai:claude">List by priority</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTcsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
ls todos/*-p0-*.md  # Critical
ls todos/*-p1-*.md  # High
```

### <span data-proof="authored" data-by="ai:claude">Move to done</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTAwLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
# Rename: change status segment
mv todos/GH-42-active-p0-fix-soql.md todos/GH-42-done-p0-fix-soql.md
```

### <span data-proof="authored" data-by="ai:claude">Find blocked todos</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MjMsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
ls todos/*-blocked-*.md
```

## <span data-proof="authored" data-by="ai:claude">Integration with Workflow</span>

* <span data-proof="authored" data-by="ai:claude">`/sf-plan`</span> <span data-proof="authored" data-by="ai:claude">creates todos for implementation tasks</span>

* <span data-proof="authored" data-by="ai:claude">`/sf-work`</span> <span data-proof="authored" data-by="ai:claude">marks todos as active, then done</span>

* <span data-proof="authored" data-by="ai:claude">`/sf-review`</span> <span data-proof="authored" data-by="ai:claude">may create new todos for findings</span>

* <span data-proof="authored" data-by="ai:claude">`/sf-lfg`</span> <span data-proof="authored" data-by="ai:claude">manages todos through the full pipeline</span>

* <span data-proof="authored" data-by="ai:claude">`/sf-compound`</span> <span data-proof="authored" data-by="ai:claude">archives done todos and captures learnings</span>

## <span data-proof="authored" data-by="ai:claude">Cleanup</span>

<span data-proof="authored" data-by="ai:claude">Periodically move completed todos to an archive:</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTgsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
mkdir -p todos/archive
mv todos/*-done-*.md todos/archive/
```