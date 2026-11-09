# One note, one fact

**Rule.** Each rule, term, boundary, decision, question and source is its own note, named for what it
says, holding one statement and a body of at most 25 lines. A note that needs a second `##` heading
is two notes. Decision notes may run to 120 lines because the reasoning is the point; reference notes
are the designated home for long mechanics and are unbounded.

**Why.** A document is read by whoever opens it, start to finish, and nothing else can point into the
middle of it. A note can be cited, embedded, superseded, queried and linked as a unit — so a rule in
its own note can be marked draft without the rest of the section looking unsettled, can be superseded
without a diff that touches its neighbours, and can collect its own backlinks, which is how you find
out what depends on it. Size is the mechanism, not a style preference: the moment a note holds two
statements, every one of those operations applies to the wrong scope. Small notes also make the
expensive failure cheap — a contradiction between two notes is visible, where a contradiction inside
one paragraph is not.

**In the base.**
- One note per entity, in the folder for its type, flat, with topic as a property
  ([`../patterns/the-two-trees.md`](../patterns/the-two-trees.md)).
- A rule states one testable idea. Two ideas joined by "and" means split, each keeping its own status
  and source ([`../anti-patterns/one-rule-two-ideas.md`](../anti-patterns/one-rule-two-ideas.md)).
- Long mechanics, field maps and state machines live in a reference note the rule links to
  ([`../patterns/reference-note.md`](../patterns/reference-note.md)).
- An index note holds no knowledge: a query and a generated table, both derived
  ([`../patterns/moc-note.md`](../patterns/moc-note.md)).

**Breaks when.** A note accumulates sections until it is a document again →
[`../anti-patterns/a-note-that-grew-into-a-document.md`](../anti-patterns/a-note-that-grew-into-a-document.md).
