# Structure must pay for itself

**Rule.** New structure earns its place only by reducing the time to **retrieve, verify, decide,
scope or safely hand off** — and the person asking for it names which. Absent that, do not add it.
Specifically, do not import: a tag program, a PARA or folder hierarchy, a layer of MOCs over the
MOCs, a second id scheme, a hand-maintained dashboard, a property nothing queries, or a note type
with one instance. When in doubt the answer is no, because the cost of structure is paid on every
note forever and the benefit is usually paid once, to the person who added it.

**Why.** A skill whose whole premise is decomposing documents into a graph of notes has a built-in
bias: every run is an opportunity to add shape, every piece of shape looks principled in isolation,
and none of it ever gets removed. The result is a vault that is more elaborate every month and no
faster to answer a question — and the elaboration is itself a cost, because each addition is another
thing to keep consistent, another thing a check must cover, and another thing a newcomer must learn
before they can contribute.

The failure is not that structure is bad. It is that **unverified structure rots into drift**. Any
duplicated field that nothing reconciles will eventually disagree with itself, so a convention that
adds a field without adding its check has added a future contradiction
([`facts-are-never-copied.md`](facts-are-never-copied.md)).

**In the base.**
- **The worked example.** This convention used to carry `tags: [rule/orders]`, duplicating `type` and
  `topic`, justified by the tag pane. Nothing derived it and nothing checked it, so it was a third
  hand-kept copy of two fields — and it undid the reason the folders are flat, since topic is a
  property precisely so that changing it is *one* edit. It was removed
  ([`../references/vault-convention.md`](../references/vault-convention.md) §4).
- **The test for a new property:** name the query that reads it. If the answer is "a person might
  want to filter on it", that is not a query, that is a hope.
- **The test for a new note type:** name two instances that exist today and the thing they can do as
  notes that they cannot do as a property on an existing note.
- **Prefer deriving over recording.** A backlinks pane beats a maintained list; a generated table
  beats a typed one; a git date beats a `updated` somebody has to remember
  ([`a-freshness-date-is-derived.md`](a-freshness-date-is-derived.md)).
- Structure the project already uses is **adopted, not judged** by this rule — it applies to what
  this skill proposes, not to what it finds
  ([`match-the-projects-voice.md`](match-the-projects-voice.md)).

**Breaks when.** A register is kept beside the notes it indexes →
[`../anti-patterns/the-register-as-a-knowledge-store.md`](../anti-patterns/the-register-as-a-knowledge-store.md).
A generated table is edited by hand →
[`../anti-patterns/a-generated-table-edited-by-hand.md`](../anti-patterns/a-generated-table-edited-by-hand.md).
