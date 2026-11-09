# items.json

**Use when** handing a batch of extracted items to `merge`. Two keys: the files you read, and the
items you found. This is the only file you write.

**Skeleton.**

```json
{
  "processed_files": [
    {
      "path": "/transcripts/2026-01-21-scope-call.docx",
      "name": "2026-01-21-scope-call.docx",
      "hash": "9f2c1ab4e7d05c38",
      "meeting": "Order Fulfilment Scope Call",
      "date": "2026-01-21"
    }
  ],
  "items": [
    {
      "category": "Labels",
      "statement": "A label is created for the order's shipping address at the moment a clerk requests it.",
      "status": "confirmed",
      "sources": [
        {"meeting": "Order Fulfilment Scope Call", "date": "2026-01-21", "speaker": "Dana Lee",
         "timestamp": "0:17:11", "quote": "after submit the address is frozen", "turn_id": "t0081"}
      ]
    }
  ]
}
```

**Notes.**
- **Copy each file's `hash` from the manifest**, verbatim. It is what marks the file ingested, and
  without it the file reprocesses on every run
  ([`../principles/the-content-hash-is-the-unit-of-work.md`](../principles/the-content-hash-is-the-unit-of-work.md)).
- List every file you read, including one that yielded no items. An empty brief is still ingested.
- `note`, `related` and `supersedes` are optional and may be omitted rather than sent as nulls.
- One `items.json` per batch. Merge after each batch, so each batch's hashes land before the next
  ([`../practices/batch-long-transcripts.md`](../practices/batch-long-transcripts.md)).
- `merge` reports how many items it dropped for missing provenance. A non-zero count is a finding
  about your extraction, not noise
  ([`../practices/merge-the-items.md`](../practices/merge-the-items.md)).

**Related.** [`knowledge-item.md`](knowledge-item.md), [`transcript-brief.md`](transcript-brief.md).
