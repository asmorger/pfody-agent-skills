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
- The Reference Layer is the vault's `rules/`, `glossary/`, `scope/`, `decisions/`, `facts/` and
  `reference/` notes. Governance is `sources/`, `questions/`, `scope-watch/` and `changes/`.
  Everything unpromoted is in the workbench, outside the vault
  ([`../patterns/the-two-trees.md`](../patterns/the-two-trees.md)).
- Every source note carries `citable: false`, so the distinction is queryable rather than
  remembered ([`../patterns/source-note.md`](../patterns/source-note.md)).
- The home note states the three layers. It is the only place a newcomer learns which they may cite
  ([`../patterns/home-note.md`](../patterns/home-note.md)).
- The transcript index is registered as a supplemental source and reconciled in, never cited
  ([`transcripts-are-delegated.md`](transcripts-are-delegated.md)).
- Keep supplemental material out of the vault entirely rather than in a folder inside it. A note that
  appears in search, the graph and a Bases view will be cited whatever its folder says.
- The test of a finished base: a developer or spec author can act on the Reference Layer alone,
  without opening a raw source.

**Breaks when.** A story cites a transcript or an intake note →
[`../anti-patterns/citing-a-transcript-as-record.md`](../anti-patterns/citing-a-transcript-as-record.md).
