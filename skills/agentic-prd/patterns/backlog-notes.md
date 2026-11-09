# Backlog notes

**Use when** writing the decomposition output. One note per work item in `backlog/` — Epic, Feature
and Story — each naming its parent, plus the MOCs that index them. No single backlog file.

**Skeleton.** `backlog/create-and-print-a-label.md`

```markdown
---
id: FEAT-01
aliases: [FEAT-01]
type: feature              # epic | feature | user-story
status: accepted
topic: labels
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
parent: "[[carrier-labels-on-the-order-screen|EPIC-01]]"
sources: ["[[create-a-label-on-order-confirmation|R-001]]", "[[show-the-carrier-rejection-reason|R-002]]", "[[refuse-a-label-on-credit-hold|R-003]]"]
checks:                    # the seven coverage lines — features only
  empty-state: "N/A — a confirmed order always has at least one line."
  …
---

# FEAT-01 — Create and print a label

One job for one role: a clerk turns a confirmed order into a printed carrier label.

**Stories** [[create-a-label-for-a-confirmed-order|US-01]]
```

`moc/backlog.md` carries the definition of done and the generated work-item table:

```markdown
## Definition of Done for all User Stories

1. DoD-1 [[record-every-label-action|X-002]] Every label action is recorded against the order with the acting user and a
   timestamp.

![[backlog.base]]

<!-- generated: do not edit -->
<!-- /generated -->
```

**Notes.**
- **`parent` is the structure**, and the check enforces the chain: an Epic's parent is the PRD, a
  Feature's is an Epic, a Story's is a Feature. Heading levels no longer carry it
  ([`../principles/one-name-and-one-id-per-level.md`](../principles/one-name-and-one-id-per-level.md)).
- A Story's `requirements` must belong to its parent Feature, or be cross-cutting. The check catches
  the mismatch, which used to be invisible once published
  ([`../anti-patterns/slicing-by-layer.md`](../anti-patterns/slicing-by-layer.md)).
- The definition of done holds the `X-` requirements that apply to `All`, stated once in the MOC
  rather than repeated in every story. Leave the section out when there are none.
- An `X-` requirement naming specific Features goes into each story of those Features whose
  behaviour it changes, and no others. Nothing here carries a task or an estimate
  ([`../anti-patterns/tasks-and-estimates-in-the-backlog.md`](../anti-patterns/tasks-and-estimates-in-the-backlog.md)).
- While the PRD is not `accepted`, every story note says `PREVIEW` in its first lines, and the check
  enforces it ([`../practices/decompose-a-prd.md`](../practices/decompose-a-prd.md)).

**Related.** [`user-story.md`](user-story.md), [`coverage-moc.md`](coverage-moc.md),
[`../references/vault-convention.md`](../references/vault-convention.md).
