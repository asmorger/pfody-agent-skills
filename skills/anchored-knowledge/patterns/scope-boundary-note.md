# Scope boundary note

**Use when** recording what is in and out of scope. One note per boundary statement in `scope/`,
each naming the source that decided it. Together they are the assumptions ledger — and they make "we
never agreed to that" provable one note at a time.

**Skeleton.** `scope/bulk-printing-excluded.md`

```markdown
---
type: scope-boundary
status: confirmed
area: label-creation
inclusion: not-included
authority: 1-contractual
sources: ["[[order-fulfilment-sow-v3]]"]
scope-watch: ["[[SW-0002]]"]
rules: ["[[LABEL-3]]"]
created: 2026-10-02
updated: 2026-11-08
tags: [scope/label-creation]
---

# Bulk printing across orders is not included

Printing one batch of labels for several orders is outside Phase 1.
[[order-fulfilment-sow-v3]] §4.5 scopes label creation one order at a time. Deferred rather than
refused: [[SW-0002]] carries it if the client asks again.
```

An included boundary is the same shape with `inclusion: included`, and is often one line:
"Creating and printing a label for a confirmed order is in scope. [[order-fulfilment-sow-v3]] §4.2."

**Notes.**
- **One boundary per note**, so each carries its own source, its own authority and its own date. An
  area's whole in/out picture is the MOC grouped by `area`, which nobody maintains by hand
  ([`../references/bases.md`](../references/bases.md)).
- `inclusion` is the property that does the work. A note with `not-included` and no source is an
  opinion about scope, not a boundary.
- "No source addresses them" is an honest and useful note — it says the boundary was considered.
  Write it in the body with `authority: 5-internal-interpretation`.
- **Unknowns do not go here.** They are questions ([`open-question.md`](open-question.md)). Knowledge
  that may push past the baseline is a scope-watch item
  ([`scope-watch-item.md`](scope-watch-item.md)).
- A superseded boundary keeps its note and gains a `[!abstract] Superseded` callout with its anchor
  ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
- A boundary that names a behaviour usually has a rule note too; link them both ways and let the rule
  hold the behaviour ([`business-rule-note.md`](business-rule-note.md)).

**Related.** [`authority-ladder.md`](authority-ladder.md),
[`../practices/bootstrap-a-base.md`](../practices/bootstrap-a-base.md).
