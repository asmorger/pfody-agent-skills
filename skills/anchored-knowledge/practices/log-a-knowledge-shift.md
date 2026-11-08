# Log a knowledge shift

**When** a newer source refines, contradicts or supersedes what the base already says. Standing
operating procedure E.

**Why.** The shift is the most valuable thing in the base and the easiest to lose. Without the entry,
the rule simply reads differently than it did last month and nobody can tell whether that was a
decision or a drift.

**Steps.**

1. **Classify it first**: contradiction · scope refinement · terminology shift · decision update ·
   requirement update · source correction. The classification decides everything that follows, and
   naming it stops a refinement being logged as a reversal
   ([`../principles/conflicts-are-recorded-not-resolved.md`](../principles/conflicts-are-recorded-not-resolved.md)).
2. **Compare authority** between the older and newer anchors
   ([`../patterns/authority-ladder.md`](../patterns/authority-ladder.md)). A higher level wins; equal
   levels do not settle it, and that becomes a question.
3. **Write `CH-NNNN`** with both anchor sets, the previous understanding, the new understanding, the
   interpretation and the action taken
   ([`../patterns/knowledge-change-entry.md`](../patterns/knowledge-change-entry.md)). Both anchor
   sets are mandatory.
4. **Add a dated History or amendment note** to every affected entry — rule, ADR, question,
   scope-watch item.
5. **Preserve the superseded understanding** with its anchors. A superseded assumption stays in the
   ledger; a superseded rule is deprecated in place
   ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
6. **Open what the shift implies**: a question where authority does not settle it, a scope-watch item
   where the new understanding costs more than the baseline allows.
7. **Propose, do not apply.** The shift reaches the record through approval and promotion
   ([`promote-to-the-record.md`](promote-to-the-record.md)).
8. **Add the entry to the index's recently-changed list**, so a reader sees it without searching.

**Done when** `CH-NNNN` names both anchors and the interpretation, every affected entry carries a
dated note, the previous understanding is preserved with its anchor, and anything the shift opened has
its own entry.
