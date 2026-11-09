# Deprecate, never delete

**Rule.** Knowledge that goes out of scope, gets deferred or is superseded keeps its note, its id and
its anchors. Change `status`, add a dated callout saying what is now true, and leave the note where
it is. **A note in the record is never deleted** — and in a vault that is not only a discipline:
deleting a note dangles every wikilink that cited it, from other notes, from stories, from code
comments.

**Why.** "Did we ever agree to that?" is the question a knowledge base is most often asked, and a
deleted rule cannot answer it. Worse, deletion loses the anchor: the rule was recorded because a
source said something, and that source is still what it is. Six weeks later the behaviour gets
re-proposed as new, re-argued from scratch, and nobody can show it was considered and dropped. A
deprecated rule answers in one read and costs one line.

**In the base.**
- Out of scope or deferred: `status: out-of-scope`, a `[!failure]` callout naming the phase, and a
  link to the scope-watch note that would bring it back.
- Superseded: `status: superseded`, `superseded-by` pointing at the replacement, and an
  `[!abstract]` callout holding the earlier understanding **and its anchor**
  ([`../patterns/status-callouts.md`](../patterns/status-callouts.md)).
- A superseded scope boundary keeps its own note rather than being edited into the new one
  ([`../patterns/knowledge-change-entry.md`](../patterns/knowledge-change-entry.md)).
- A decision is superseded by a later decision, never overwritten. A refinement that reverses nothing
  gets a dated addendum ([`../patterns/decision-record.md`](../patterns/decision-record.md)).
- A retired term stays in the replacement note's `aliases`, so the old word still finds the note in
  search; a link written to the old name resolves only while a file carries that name
  ([`../patterns/glossary-term-note.md`](../patterns/glossary-term-note.md)).
- Deprecated notes stay out of the way without leaving the record: the MOC's snapshot excludes them
  and a Bases view collects them ([`../references/bases.md`](../references/bases.md)).

**Breaks when.** A rule is removed because it is no longer being built →
[`../anti-patterns/deleting-an-out-of-scope-rule.md`](../anti-patterns/deleting-an-out-of-scope-rule.md).
