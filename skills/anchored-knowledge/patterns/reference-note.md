# Reference and convention notes

**Use when** the record needs to say *how the team builds* rather than what the system does, or needs
to hold mechanics too long for a rule. These are the only notes in the vault without a size budget,
and the designated home for everything a rule note must not carry.

**Skeleton.** `docs/reference/api-conventions.md`

```markdown
---
type: reference
topic: api
status: confirmed
governs: ["[[LABEL-2]]"]
decisions: ["[[ADR-0003]]"]
created: 2026-10-02
updated: 2026-11-08
tags: [reference/api]
---

# API Conventions

How this project shapes its HTTP surface, so a reviewer and an agent reach the same answer.

## Resources
Resources are plural nouns; actions are verbs on a sub-path.

## Error responses
Every failure returns the carrier's own reason text where one exists ([[LABEL-2]]).
```

`docs/reference/order-data-mapping.md` is the same shape holding a field map, a state machine or a message
contract — the mechanics that [[LABEL-1]] links to rather than stating.

**Notes.**
- **No id, and cited by name**: `[[api-conventions]]`. These notes are Reference Layer and citable,
  but they are not single statements, so an id would promise something they cannot keep.
- The first line after the H1 says the purpose in one sentence. A note whose purpose cannot be stated
  in a sentence is two notes.
- **Rules say what the system does; convention notes say how the team builds it.** A statement that
  fits both is split between them, never duplicated
  ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).
- When a rule needs long mechanics, the mechanics come here and the rule links. The rule stays one
  testable sentence ([`business-rule-note.md`](business-rule-note.md)).
- `governs` lists the rules that depend on this note, so the rule and its mechanics find each other
  from either end.
- Multiple `##` headings are expected here and nowhere else in the record
  ([`../principles/one-note-one-fact.md`](../principles/one-note-one-fact.md)).
- Supporting material — raw exports, examples, meeting recordings — is **not** this. It stays in the
  workbench and is registered as a source
  ([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md)).

**Related.** [`business-rule-note.md`](business-rule-note.md),
[`decision-record.md`](decision-record.md), [`the-two-trees.md`](the-two-trees.md).
