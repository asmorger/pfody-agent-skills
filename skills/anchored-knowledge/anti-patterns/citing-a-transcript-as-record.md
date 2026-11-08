# Citing a transcript as record

**Smell.** A user story whose source grounding is `transcript-knowledge.md BID-7`. An acceptance
criterion citing an intake note. A specification resting on a line from the November review, because
the line was clear and specific and nobody had written the rule yet.

**Why it is wrong.** The two kinds of document make different promises. A Reference Layer rule has been
reconciled against everything else in the base and carries an immutable id. A transcript line is
evidence that somebody said something once — true as a record, unreliable as a requirement, because
the meeting two weeks later may have reversed it and the index will faithfully hold both. Citing it
imports that unreliability into a build, and the citation makes it look checked. The id is unstable
too: a transcript item's id belongs to the index, which is regenerated.

**Instead.** Promote it first. Reconcile the item against the existing rules, give it a rule id, mark
its status, and let the story cite that. The transcript index keeps its role — it is the evidence
behind the rule's anchor, registered as supplemental, which is exactly what makes the promoted rule
defensible ([`../principles/only-the-reference-layer-is-citable.md`](../principles/only-the-reference-layer-is-citable.md),
[`../practices/reconcile-against-the-rules.md`](../practices/reconcile-against-the-rules.md)).
