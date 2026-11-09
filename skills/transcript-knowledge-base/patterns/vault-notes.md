# Vault notes

**Use when** you need to say what the deliverable looks like, or to check that a render came out
right. A folder of small linked notes: one per statement, one per meeting, and one MOC. The full
contract is [`../references/vault-convention.md`](../references/vault-convention.md).

**Skeleton.** `items/one-label-is-created-per-parcel.md`

```markdown
---
id: LABEL-2
aliases: [LABEL-2]
type: transcript-item
status: confirmed
category: Labels
sources: ["[[2026-11-08-november-review]]", "[[2026-11-15-carrier-sync]]"]
supersedes: ["[[one-label-per-parcel|LABEL-1]]"]
citable: false
tags: [transcript-item/labels]
---

# LABEL-2 — One label is created per parcel; a split order produces several labels.

> [!abstract] Superseded
> Supersedes [[one-label-per-parcel|LABEL-1]].

> [!quote] Evidence
> "if it's two boxes the carrier wants two labels"
> — Dana Lee, [[2026-11-08-november-review]] 00:14:22
```

The MOC, `moc/knowledge-index.md`, carries the prose, `![[knowledge-index.base]]`, and a table
between `<!-- generated: … -->` and `<!-- /generated -->` with one row per statement.

**Notes.**
- **The statement is the H1 and nowhere else.** Status is a property; a caveat is a callout. The
  statement stays clean
  ([`../principles/status-is-a-field-not-a-sentence.md`](../principles/status-is-a-field-not-a-sentence.md)).
- **`LABEL-2` with two sources is the output working as intended**: one statement, cited to two
  meetings months apart. Two evidence callouts, not a duplicate note
  ([`../principles/evidence-is-never-discarded.md`](../principles/evidence-is-never-discarded.md)).
- `type: transcript-item` and `citable: false` on every note. This is evidence; a story or a test
  cites the project's record, never this
  ([`../anti-patterns/the-generated-index-shipped-as-finished.md`](../anti-patterns/the-generated-index-shipped-as-finished.md)).
- Category order and id prefixes come from the seeded taxonomy; `title` and `intro` come from the
  config, and the title also names the MOC and the `.base` file
  ([`tool-config.md`](tool-config.md)).
- Every note is generated. Fix a wording by re-extracting and re-rendering, never by editing a note —
  the next run overwrites it
  ([`../anti-patterns/editing-a-generated-note.md`](../anti-patterns/editing-a-generated-note.md)).
- The renderer escapes pipes in the MOC table and leaves the notes alone, which is one of several
  reasons not to write these by hand
  ([`../anti-patterns/hand-writing-the-index.md`](../anti-patterns/hand-writing-the-index.md)).

**Related.** [`state-file.md`](state-file.md),
[`../practices/render-the-vault.md`](../practices/render-the-vault.md).
