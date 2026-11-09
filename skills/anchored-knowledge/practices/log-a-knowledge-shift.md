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
4. **Add a dated callout to every note in `affects`** — rule, decision, question, scope-watch item —
   and list them in the change note's `affects` so the links run both ways
   ([`../patterns/status-callouts.md`](../patterns/status-callouts.md)).
5. **Preserve the superseded understanding** with its anchors. A superseded boundary keeps its own
   note; a superseded rule keeps its note, its id, `status: superseded` and a `superseded-by`
   ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
6. **Open what the shift implies**: a question where authority does not settle it, a scope-watch item
   where the new understanding costs more than the baseline allows.
7. **Propose, do not apply.** The shift reaches the record through approval and promotion
   ([`promote-to-the-record.md`](promote-to-the-record.md)).
8. **Add it to the start note's Recently changed list**, so a reader sees it without searching. That
   list is judgement, not a query, which is why it is written by hand
   ([`../patterns/start-note.md`](../patterns/start-note.md)).

**Done when** `CH-NNNN` names both anchors and the interpretation, every affected entry carries a
dated note, the previous understanding is preserved with its anchor, and anything the shift opened has
its own entry.
