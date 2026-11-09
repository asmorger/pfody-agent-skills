# Backlog file

**Use when** writing more than one story to a file. Leave out any heading with no content, and never
invent an Epic or a Feature to fill one.

**Skeleton.**

```markdown
# Backlog for PRD-001, version 1.0

> PREVIEW. Do not publish.          (only when the source PRD is not Accepted)

## Work item summary

| ID | Level | Title | Parent |
|---|---|---|---|
| EPIC-01 | Epic | Shipping labels at order processing | PRD-001 |
| FEAT-02 | Feature | Void a label | EPIC-01 |
| US-03 | User Story | Void a printed label | FEAT-02 |

## Definition of Done for all User Stories

1. DoD-1 [X-002] Every label action is recorded against the order with the acting clerk and a
   timestamp.

# Epic: Shipping labels at order processing (EPIC-01)

## Feature: Void a label (FEAT-02)

### User Story: US-03 Void a printed label
…

# Coverage

| Requirement | Pri | Verify | User Story | Criterion | Status |
|---|---|---|---|---|---|
| R-012 | P0 | Auto | US-03 | AC-1 | Covered |
| R-014 | P1 | Auto | None | None | Blocked by Q-03 |
| X-002 | P0 | Manual | All | DoD-1 | Covered |

**Counts.** Requirements: 3. Covered: 2. Blocked: 1. Epics: 1. Features: 1. User Stories: 1.
```

**Notes.**
- **Omit `# Coverage` in Mode B and Mode C** — there are no requirement ids to trace
  ([`../principles/mode-honesty.md`](../principles/mode-honesty.md)).
- Keep the Epic and Feature names exactly as the source has them, and their ids with them
  ([`../principles/one-name-and-one-id-per-level.md`](../principles/one-name-and-one-id-per-level.md)).
- The definition of done carries `X-` requirements that apply to `All`, stated once rather than
  repeated in every story.
- The Requirements count includes `X-` rows, and an `X-` row names the first story that carries it.
- `PREVIEW` is a hard gate, not a label: a preview is not published
  ([`../practices/build-from-a-prd.md`](../practices/build-from-a-prd.md)).

**Related.** [`user-story.md`](user-story.md),
[`../practices/slice-a-feature-into-stories.md`](../practices/slice-a-feature-into-stories.md).
