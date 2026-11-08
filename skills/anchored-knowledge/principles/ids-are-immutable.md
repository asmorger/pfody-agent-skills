# Ids are immutable

**Rule.** A rule id, once issued, belongs to that rule forever: never reused, never renumbered, never
deleted. A new rule takes the next free number in its section even when it belongs in a different row
position. Gaps in the numbering are normal and stay.

**Why.** The id is the whole value of the base to everything downstream — a story's source grounding,
an acceptance criterion, a test name, a pull request, a tracker tag, another rule's cross-link.
Renumbering silently re-points every one of those at a different rule, and nothing fails: the test
still passes, against the wrong rule. The immutability is also what lets the base be refined
aggressively. A rule's text can be rewritten freely, because the id is what was cited, not the
wording.

**In the base.**
- `PREFIX-N` per topic section, one unique prefix per section; `PREFIX-0` only for a basic rule that
  must precede rule 1 ([`../patterns/business-rules-file.md`](../patterns/business-rules-file.md)).
- Refine a rule in place. Split it when it has grown two ideas — the original keeps its id and one
  idea, the second idea takes a new number
  ([`../practices/write-a-business-rule.md`](../practices/write-a-business-rule.md)).
- `ADR-NNNN` is sequential and never renumbered; reversal is supersession, not an overwrite
  ([`../patterns/decision-record.md`](../patterns/decision-record.md)).
- Every id cited anywhere must resolve to a real entry. That is what the audit checks
  ([`../practices/audit-the-base.md`](../practices/audit-the-base.md)).

**Breaks when.** Numbering is tidied after a removal →
[`../anti-patterns/renumbered-rule-ids.md`](../anti-patterns/renumbered-rule-ids.md).
