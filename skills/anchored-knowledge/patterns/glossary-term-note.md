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
governed-by: ["[[one-label-per-parcel|LABEL-1]]"]
created: 2026-10-02
updated: 2026-11-08
---

# Parcel

One physical box leaving the warehouse. A split order produces several ([[confirmed-order-may-split-across-parcels|ORDER-5]]).

> [!abstract] Retired name — Shipment, 2026-11-08
> "Shipment" meant both this and a carrier collection, so it was retired.
> [[one-label-per-parcel-not-per-order|CH-0004]] records the rename. The alias stays, so the old
> word still finds this note in search.
```

**Notes.**
- **Put retired names in `aliases`.** The old word then finds this note in search and autocomplete,
  and the graph shows one concept rather than two. It does **not** make `[[Shipment]]` resolve —
  nothing does but a file of that name. Renaming the file is what repairs the links that already
  exist, because Obsidian rewrites all of them; leave a stub note at the old name only if something
  outside the vault cites it ([`note-frontmatter.md`](note-frontmatter.md)).
- The definition says what the word means and **links** the governing rule. It never restates the
  rule ([`../principles/facts-are-never-copied.md`](../principles/facts-are-never-copied.md)).
- `category` sets the MOC's grouping and the Bases views' `groupBy` — core concepts, systems and
  integration, roles, whatever the project already uses.
- Two terms for one meaning, and one term used two ways, are both audit findings. Reconcile them
  here, by making one note the home and the other name an alias of it — never by picking a winner in
  prose ([`../practices/audit-the-base.md`](../practices/audit-the-base.md)).
- Adopt the team's word even when a better one exists. A glossary that argues with its readers is
  not consulted ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).
- Write the term in `term` as the project capitalises it; the filename is its kebab form.

**Related.** [`business-rule-note.md`](business-rule-note.md),
[`status-callouts.md`](status-callouts.md), [`moc-note.md`](moc-note.md).
