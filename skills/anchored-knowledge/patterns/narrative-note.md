# Narrative note

**Use when** the vault needs a readable surface — an onboarding story, a design explanation, a "why
is it like this". A narrative is **derived**: readable prose that holds no facts of its own.

**Skeleton.** `narrative/how-labelling-works.md`

```markdown
---
type: narrative
status: current                 # draft | current | stale
derived-from: [rules, scope, decisions, questions]
covers-through: 2026-11-08      # written by the script; the ONLY date in the note
input-manifest-sha256: ""       # written by the script
---

# How labelling works

The readable story, derived from the notes. **It owns no facts.**

## What the system does

- One label per parcel, so a split order gets one label per box
  ([[one-label-per-parcel|LABEL-1]]).
- An order on credit hold cannot be labelled, checked at label creation
  ([[credit-hold-blocks-labelling|ORDER-2]], decided in
  [[enforce-credit-hold-at-label-creation|ADR-0004]]).

## Gaps found while deriving

- Nothing records what happens to a voided label's carrier charge. Belongs in a rule.
```

**Notes.**
- **Every section cites, and every claim of eight words or more links.** The lint enforces both. A
  section that cites nothing is a section whose claims have no home
  ([`../principles/facts-are-never-copied.md`](../principles/facts-are-never-copied.md)).
- **`covers-through` is the only date.** `vault.py narrative` writes it from the newest input note,
  and the lint rejects a hand-written "last updated" line in the prose — a freshness claim nobody
  maintains is worse than no claim.
- **The gaps section is required, even when empty.** It is the pressure valve that keeps the story
  from inventing the connective tissue it needs. Say "none" rather than deleting the heading.
- **Status travels with every claim.** Describe a draft rule as draft in the sentence; a narrative
  that flattens status reads as agreement the vault never recorded.
- **A narrative is never cited.** It is a reading surface, not a home
  ([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md)).
- It may be long. The body budget does not apply, because length is the point here — but each
  statement is still one line.

**Related.** [`../practices/render-a-narrative.md`](../practices/render-a-narrative.md),
[`moc-note.md`](moc-note.md),
[`../anti-patterns/a-note-that-grew-into-a-document.md`](../anti-patterns/a-note-that-grew-into-a-document.md).
