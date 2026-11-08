# Convention and reference docs

**Use when** the base needs to say *how the team builds* rather than what the system does, or needs
to hold mechanics too long for a rule row. Both kinds sit flat in the Docs folder.

**Skeleton.** A convention doc, `api-conventions.md`:

```markdown
# API Conventions

## Purpose
How this project shapes its HTTP surface, so a reviewer and an agent reach the same answer.

## General Principles
- Resources are plural nouns; actions are verbs on a sub-path.

## Error Responses
- Every failure returns the carrier's own reason text where one exists (LABEL-2).
```

A domain reference doc, `order-data-mapping.md`:

```markdown
# Order Data Mapping

## Purpose
How order fields map to the carrier's label request.

## Field Map
| Order field | Carrier field | Notes |
| --- | --- | --- |
| `order.shipTo.line1` | `AddressLine1` | Truncated at 35 characters by the carrier. |
```

**Notes.**
- Both start with `## Purpose`. A doc whose purpose cannot be stated in a sentence is two docs.
- **Business rules state what the system does; convention docs state how the team builds it.** A
  statement that fits both is split between them, never duplicated
  ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).
- Keep them flat in the Docs folder, not in a subfolder — they are Reference Layer and citable.
- When a rule needs long mechanics, the mechanics go in a reference doc and the rule links to it. The
  rule stays one testable sentence.
- Supporting folders (`meetings/`, `examples/`, `answered-questions/`) are *not* this. They are
  supplemental and not citable
  ([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md)).

**Related.** [`business-rules-file.md`](business-rules-file.md), [`the-two-trees.md`](the-two-trees.md).
