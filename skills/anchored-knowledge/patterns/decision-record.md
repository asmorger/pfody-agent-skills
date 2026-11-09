# Decision record

**Use when** a design or scope decision is settled, or an earlier one is reversed. One note per
decision in `decisions/`. The one note type that may run long — up to 120 lines — because the
reasoning is the thing it exists to keep. The full section set is in
[`../references/templates.md`](../references/templates.md).

**Skeleton.** `decisions/credit-hold-blocks-labelling.md`

```markdown
---
id: ADR-0004
aliases: [ADR-0004]
type: decision
status: accepted
summary: An order on credit hold cannot be labelled; the hold is enforced at label creation.
decided: 2026-10-21
deciders: [operations lead, architect]
confidence: high
rules: ["[[ORDER-2]]", "[[LABEL-3]]"]
supersedes: []
review-when: when the finance system exposes a hard-hold flag
created: 2026-10-21
updated: 2026-10-21
tags: [decision]
---

# ADR-0004 — A credit hold blocks labelling

## Context
Credit holds live in the finance system and are advisory there. Clerks were labelling held orders,
and a labelled parcel is treated as committed stock.

## Decision
An order on credit hold cannot be labelled. The check happens at label creation ([[ORDER-2]]).

## Consequences
**Easier** · **Harder** — what this buys and what it costs.

## Alternatives
**Nightly reconciliation.** Rejected: a parcel can leave the warehouse before the sweep runs.

## Assumptions · Future review · Related```

**Notes.**
- `summary` is the one-sentence form, and the MOC's snapshot column reads it from frontmatter. One
  wording, one home ([`moc-note.md`](moc-note.md)).
- Reversal is **supersession**: a new note naming what it supersedes, and the old one takes
  `status: superseded` plus a `[!abstract]` callout. Never overwrite a decision's body
  ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
- A refinement that reverses nothing gets a dated `[!info]` addendum on the existing note.
- **Name how each alternative fails**, not that it lost. An alternative with a verdict and no failure
  will be re-argued; this section is what earns the note.
- `rules` lists what the decision settles, so each rule's backlinks lead here and the rule itself
  only links ([`business-rule-note.md`](business-rule-note.md)).
- A project already numbering its ADR filenames keeps that form
  ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).

**Related.** [`business-rule-note.md`](business-rule-note.md),
[`../practices/record-a-decision.md`](../practices/record-a-decision.md).
