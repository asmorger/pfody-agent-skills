# Backlog format for Mode: DECOMPOSE

A short, sourced User Story is better than a complete-looking User Story with invented behavior. This rule governs all other rules in this file.

## Do not add behavior

Do not add audit trails, validation rules, permissions, error messages, retries, notifications, integrations, export formats, or "standard" expectations unless a requirement states them. A similar feature is not a source. If a gap appears, make the User Story narrower and report the gap.

## Levels

Copy each Epic and Feature from the PRD work item map with its ID and name. Do not create, merge, or rename an Epic or a Feature in this mode. If a Feature does not fit, report it.

## User Story rules

- A User Story belongs to exactly one Feature. Its ID has the format `US-01`, and it is unique in the backlog. Do not reuse an ID.
- A User Story is a vertical slice that one person can build, test, and demo in one sprint. Slice by outcome, not by technical layer.
- A valid User Story produces a workflow, persisted data, enforcement behavior, permission behavior, integration behavior, or reporting output.
- Use a specific role, not "user". Describe a need, not a screen. The "so that" clause states a business reason and does not repeat the need.
- Keep a failure behavior with its main path when one person can build and demo both in a sprint. Split it when it has separate complexity. This is a judgment, so the check script does not test it.
- P0 and P1 requirements can share a User Story. Tag the highest priority.
- Put a P2 requirement in a User Story with the `Stretch` tag. Do not mix it with P0 or P1 requirements.
- Put an `X-` requirement that names a Feature in each User Story of that Feature whose behavior it changes. Do not add it to a User Story that it does not change.

## Acceptance criteria

Write one or more criteria for each requirement. Each criterion has the ID of its requirement:

`AC-1 [R-001] Given <precondition>, when <trigger>, then <observable result>.`

The ID keeps a machine-readable link from each test to its source. Put no other citation in a criterion.

Convert the requirement patterns in this way:

| Requirement pattern | Criterion |
|---|---|
| When X, the system shall Y | Given the precondition, when X, then Y |
| While S, the system shall Y | Given S, when the person views or acts, then Y |
| If X, then the system shall Y | Given a state where X can occur, when X occurs, then Y |
| The system shall Y | Given the related screen or data, when it is used, then Y |

Order the criteria from the main output to edge cases. Do not add a criterion to reach a count.

The verify value of a requirement shapes its criterion. For `Manual`, the UAT Approach names the check. For `Telemetry`, the criterion names the event and its fields. For `Eval`, the criterion names the data set and the threshold.

## Field values

- **Testing Complexity:** High for financial logic, security, multi-system integration, migration, or concurrency. Medium for business rules or one integration. Low for display or configuration.
- **Permission:** a capability name, such as "Void label". Use `None` if no access rule applies.
- **Feature flag:** the flag name in the PRD rollout section. If the PRD names none, use `To be determined by engineering`.
- **Design assets:** a real link. Use `None` if the PRD has only a placeholder.
- **Open Questions:** each open question that can change this User Story, including a question that blocks a related requirement.

## Output format

Keep all labels, even when a section is empty. Use `None identified` for an empty section.

```markdown
### User Story: US-01 <Short title>

As a <specific role>, I want to <need>, so that <business reason>.

**Expected Output**
- <Concrete deliverable, up to four bullets>

**Details**
- Source grounding: PRD-001 R-001, R-002, X-004.

**Assumptions**
- <A-xx statement, or None identified>

**Testing Strategy**
- **Testing Complexity**: <Low | Medium | High>
- **UAT Approach**: <What a person does and sees in a demo>

**Open Questions**
- <Q-xx question, or None identified>

**Technical Notes**
- **Permission**: <Conceptual capability, or None>
- **Feature flag**: <Name, None, or To be determined by engineering>
- **Design assets**: <Link, or None>

**Acceptance Criteria**
1. AC-1 [R-001] Given ..., when ..., then ...

**Tags**
- PRD-001, EPIC-01, FEAT-01, P0
```

`Source grounding` must list exactly the IDs in the User Story criteria. The check script compares them.

## File layout

```markdown
# Backlog for PRD-001, version 1.0

> PREVIEW. Do not publish.        (Only when the PRD status is not Accepted.)

## Work item summary

| ID | Level | Title | Parent |
|---|---|---|---|
| EPIC-01 | Epic | <Epic name> | PRD-001 |
| FEAT-01 | Feature | <Feature name> | EPIC-01 |
| US-01 | User Story | <Short title> | FEAT-01 |

## Definition of Done for all User Stories

1. DoD-1 [X-001] <Requirement that applies to all User Stories>

# Epic: <Epic name> (EPIC-01)

## Feature: <Feature name> (FEAT-01)

### User Story: US-01 <Short title>

# Coverage

| Requirement | Pri | Verify | User Story | Criterion | Status |
|---|---|---|---|---|---|
| R-001 | P0 | Auto | US-01 | AC-1 | Covered |
| R-002 | P1 | Auto | None | None | Blocked by Q-01 |
| R-003 | P2 | Auto | None | None | Skipped: PROPOSED |
| R-004 | P3 | Auto | None | None | Skipped: P3 |
| X-001 | P0 | Manual | All | DoD-1 | Covered |

**Counts.** Requirements: 5. Covered: 2. Blocked: 1. Skipped PROPOSED: 1. Skipped P3: 1. Epics: 1. Features: 1. User Stories: 1.
```

Leave out the Definition of Done section when no `X-` requirement applies to "All". The coverage row of an `X-` requirement names the first User Story that has it. The Requirements count includes `X-` requirements.
