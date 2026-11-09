# Glossary term note

**Use when** the project needs a word to mean one thing. One note per term in `glossary/`. The
cheapest notes in the vault and the ones that prevent the most rework — and in a vault they do a
second job: a retired name kept as an alias makes every old reference resolve to the current term.

**Skeleton.** `glossary/parcel.md`

```markdown
---
type: glossary-term
term: Parcel
aliases: [Parcel, Shipment]
category: core-concepts
status: confirmed
governed-by: ["[[LABEL-1]]"]
created: 2026-10-02
updated: 2026-11-08
tags: [term/core-concepts]
---

# Parcel

One physical box leaving the warehouse. A split order produces several ([[ORDER-5]]).

> [!abstract] Retired name — Shipment, 2026-11-08
> "Shipment" meant both this and a carrier collection, so it was retired. [[CH-0004]] records the
> rename. The alias stays, so older notes and code comments still resolve here.
```

**Notes.**
- **Put retired names in `aliases`.** `[[Shipment]]` then lands on this note instead of dangling, and
  the graph shows one concept rather than two. This is the one case where an alias is not an id
  ([`note-frontmatter.md`](note-frontmatter.md)).
- The definition says what the word means and **links** the governing rule. It never restates the
  rule ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).
- `category` sets the tag's second segment and the MOC's grouping — core concepts, systems and
  integration, roles, whatever the project already uses.
- Two terms for one meaning, and one term used two ways, are both audit findings. Reconcile them
  here, by making one note the home and the other name an alias of it — never by picking a winner in
  prose ([`../practices/audit-the-base.md`](../practices/audit-the-base.md)).
- Adopt the team's word even when a better one exists. A glossary that argues with its readers is
  not consulted ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).
- Write the term in `term` as the project capitalises it; the filename is its kebab form.

**Related.** [`business-rule-note.md`](business-rule-note.md),
[`status-callouts.md`](status-callouts.md), [`moc-note.md`](moc-note.md).
