# Backlog file

**Use when** writing the decomposition output. One file beside the PRD, named
`<prd-name>.backlog.md`: a summary, a definition of done, the stories under their Epics and Features,
and a coverage table that proves every requirement was placed.

**Skeleton.**

```markdown
# Backlog for PRD-001, version 1.0

> PREVIEW. Do not publish.          (only when the PRD is not yet Accepted)

## Work item summary

| ID | Level | Title | Parent |
|---|---|---|---|
| EPIC-01 | Epic | Shipping labels at order processing | PRD-001 |
| FEAT-01 | Feature | Create and print a label | EPIC-01 |
| US-01 | User Story | Create a label for a confirmed order | FEAT-01 |

## Definition of Done for all User Stories

1. DoD-1 [X-002] Every label action is recorded against the order with the acting clerk and a
   timestamp.

# Epic: Shipping labels at order processing (EPIC-01)

## Feature: Create and print a label (FEAT-01)

### User Story: US-01 Create a label for a confirmed order
…

# Coverage

| Requirement | Pri | Verify | User Story | Criterion | Status |
|---|---|---|---|---|---|
| R-001 | P0 | Auto | US-01 | AC-1 | Covered |
| R-012 | P1 | Auto | None | None | Blocked by Q-03 |
| R-014 | P2 | Auto | None | None | Skipped: PROPOSED |
| R-015 | P3 | Auto | None | None | Skipped: P3 |
| X-002 | P0 | Manual | All | DoD-1 | Covered |

**Counts.** Requirements: 5. Covered: 2. Blocked: 1. Skipped PROPOSED: 1. Skipped P3: 1.
Epics: 1. Features: 1. User Stories: 1.
```

**Notes.**
- Heading levels are fixed: `# Epic:`, `## Feature:`, `### User Story:`. The check script and the
  publish step both read them.
- The definition of done holds the `X-` requirements that apply to `All`, stated once instead of
  repeated in every story; leave the section out when there are none.
- An `X-` requirement naming specific Features goes into each story of those Features whose
  behaviour it changes, and no others. Coverage has one row per requirement, `X-` rows included, with
  those four statuses and no others; an `X-` row names the first story carrying it.
- The counts are the honest summary of the run: blocked and skipped are results, not failures
  ([`../practices/report-the-result.md`](../practices/report-the-result.md)).

**Related.** [`user-story.md`](user-story.md), [`../practices/decompose-a-prd.md`](../practices/decompose-a-prd.md),
[`../references/example-backlog.md`](../references/example-backlog.md).
