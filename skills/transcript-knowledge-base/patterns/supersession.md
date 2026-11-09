# Supersession

**Use when** a meeting replaces an understanding an earlier meeting established. The older item is
marked, not removed, and keeps every source it had.

**Skeleton.**

```json
{
  "category": "Labels",
  "statement": "One label is created per parcel; a split order produces several labels.",
  "status": "confirmed",
  "note": "replaces the per-order rule agreed in January",
  "supersedes": ["LABEL-1"],
  "sources": [
    {"meeting": "November Review", "date": "2026-11-08", "speaker": "Dana Lee",
     "timestamp": "0:41:02", "quote": "the carrier counts per parcel, always has",
     "turn_id": "t0310"}
  ]
}
```

After the merge, `LABEL-1` keeps its text, its id and its January sources, and its status becomes
`superseded`. The new item takes the next id in the category.

**Notes.**
- `supersedes` takes the id where you know it, or the statement where you do not. Prefer the id — it
  is unambiguous and the merge can act on it.
- The old item is never deleted. "We used to think one label per order", with its original citation,
  is the answer to why existing code looks the way it does
  ([`../principles/evidence-is-never-discarded.md`](../principles/evidence-is-never-discarded.md)).
- A *refinement* is not a supersession. A rule that gets more specific is the same rule gaining a
  source — restate it and let the dedup merge it.
- An explicit supersession is also the only reliable way to link the two across a lexical dedup that
  would not have matched them.
- Use `note` to say in one clause what changed, for a reader scanning the rendered table.

**Related.** [`knowledge-item.md`](knowledge-item.md), [`vault-notes.md`](vault-notes.md),
[`../anti-patterns/deleting-a-superseded-item.md`](../anti-patterns/deleting-a-superseded-item.md).
