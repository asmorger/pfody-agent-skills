# Two directories; promote to commit

**Rule.** Knowledge is captured and drafted in the working area, and promoted into the record when it
is approved. Only the record is committed. The working area holds intake, the transcript index,
proposals and anything still `Draft` or `Needs Review`; it is never pushed, and when it sits inside
the repository it is gitignored.

**Why.** The record is shared: the team reads it, stories cite it, agents build from it. Half-finished
notes in that tree get read as knowledge, so a base with no staging area is a base nobody trusts —
and the usual reaction is to stop writing anything down until it is certain, which is how knowledge
gets lost. Two directories let capture be fast and loose while the record stays clean, and promotion
is the single visible moment where a statement stops being a note and starts being something a build
can rely on.

**In the base.**
- `working_dir` → intake, `drafts/`, the transcript index. `knowledge_root` → the record, with
  `docs_dir` holding the Reference Layer
  ([`../patterns/the-two-trees.md`](../patterns/the-two-trees.md)).
- The record may share a folder with unrelated project docs. That is fine, because only promoted
  knowledge is written there.
- Promotion is one-way: write the entry into the record with its id, anchors and confirmed status,
  close the working draft, then commit
  ([`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md)).
- Raw sources and the transcript index stay in the working area permanently. They are evidence, not
  record.

**Breaks when.** Drafts reach the repository →
[`../anti-patterns/committing-the-working-area.md`](../anti-patterns/committing-the-working-area.md).
