# Only the Reference Layer is citable

**Rule.** A story, a specification, an acceptance criterion or a test may cite only the Reference
Layer: business rules, the glossary, the scope ledger, ADRs, convention and domain reference docs.
Intake, raw sources, the transcript index, governance logs and supporting folders are supplemental.
A fact that lives only in a transcript is promoted into the Reference Layer before anything cites it.

**Why.** The two kinds of document make different promises. A Reference Layer entry has been
reconciled against everything else in the base, carries an immutable id, and is wrong only if the
base is wrong. A transcript line is evidence that somebody said something once — true as a record,
unreliable as a requirement, because the meeting two weeks later may have reversed it. Citing the
second kind as though it were the first imports that unreliability into a build, and the citation
makes it look checked.

**In the base.**
- Reference Layer lives under `docs_dir`; everything governance lives under `knowledge_root`;
  everything unpromoted lives in `working_dir`
  ([`../patterns/the-two-trees.md`](../patterns/the-two-trees.md)).
- The transcript index is registered as a supplemental source and reconciled in, never cited
  ([`transcripts-are-delegated.md`](transcripts-are-delegated.md)).
- Supporting folders — `meetings/`, `examples/`, `answered-questions/` — are supplemental even though
  they sit inside the Docs folder. Register each one in the Source Register.
- The test of a finished base: a developer or spec author can act on the Reference Layer alone,
  without opening a raw source.

**Breaks when.** A story cites a transcript or an intake note →
[`../anti-patterns/citing-a-transcript-as-record.md`](../anti-patterns/citing-a-transcript-as-record.md).
