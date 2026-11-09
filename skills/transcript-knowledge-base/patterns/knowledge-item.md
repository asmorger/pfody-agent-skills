# Knowledge item

**Use when** writing any item. One durable rule, its status, and the provenance behind it. No item
exists without at least one source — `validate()` rejects it and `merge` drops it.

**Skeleton.**

```json
{
  "category": "Labels",
  "statement": "A label is created for the order's shipping address at the moment a clerk requests it.",
  "status": "confirmed",
  "note": null,
  "related": [],
  "supersedes": [],
  "sources": [
    {
      "meeting": "Order Fulfilment Scope Call",
      "date": "2026-01-21",
      "speaker": "Dana Lee",
      "timestamp": "0:17:11",
      "quote": "after submit the address is frozen",
      "turn_id": "t0081"
    }
  ]
}
```

**Notes.**
- `statement` is declarative, present tense, self-contained, role-based — a line from a rules
  document, not a quote
  ([`../principles/a-statement-is-not-a-quote.md`](../principles/a-statement-is-not-a-quote.md)).
- `status` is one of `confirmed`, `tentative`, `draft`, `pending`, `deferred`, `superseded`. `note` is
  a short qualifier, not a paragraph
  ([`../principles/status-is-a-field-not-a-sentence.md`](../principles/status-is-a-field-not-a-sentence.md)).
- A `Source` is meeting, date, speaker, timestamp, quote, turn id — and the file, which the tool
  fills. Several sources on one item is the goal, not a problem
  ([`../principles/evidence-is-never-discarded.md`](../principles/evidence-is-never-discarded.md)).
- `category` must match an existing category name exactly, or a new section is created
  ([`category-taxonomy.md`](category-taxonomy.md)).
- The id is assigned by `merge`, per category. You never write one
  ([`../principles/ids-are-stable-across-runs.md`](../principles/ids-are-stable-across-runs.md)).
- `related` holds cross-references you are confident about; leave it empty otherwise.

**Related.** [`items-json.md`](items-json.md), [`supersession.md`](supersession.md),
[`../prompts/index_extraction_prompt.md`](../prompts/index_extraction_prompt.md).
