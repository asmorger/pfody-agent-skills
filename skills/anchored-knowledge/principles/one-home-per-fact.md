# One home per fact

**Rule.** Each fact, rule, term or decision lives in exactly one note. Everything else links to it,
or embeds it with `![[…]]`. Never copy a sentence between notes, never restate a rule's mechanics in
a second note, and never restate in prose what a property already says.

**Why.** Two copies of a rule are one rule and one bug waiting for the next correction. The
correction always reaches one copy, and nothing announces that the other has gone stale — so the base
starts answering the same question two ways, and the reader who finds the wrong copy has no signal
that a right one exists. A link cannot go stale this way: it resolves to whatever the fact says now.

**In the base.**
- Rules state the behaviour; long mechanics go in a reference note the rule links to
  ([`../patterns/reference-note.md`](../patterns/reference-note.md)).
- Vocabulary is defined once, in a glossary note, and used verbatim everywhere else
  ([`../patterns/glossary-term-note.md`](../patterns/glossary-term-note.md)).
- Cross-link with wikilinks: `[[partial-despatch-is-allowed|ORDER-8]]`, `[[enforce-credit-hold-at-label-creation|ADR-0004]]`, `[[parcel]]`. **Embedding is not
  copying** — `![[order-address-frozen-on-confirmation]]` resolves to whatever that note says now, so a reader gets the words in
  place and the fact keeps one home
  ([`links-are-the-structure.md`](links-are-the-structure.md)).
- An index note holds no knowledge, only a query and a derived table
  ([`../patterns/moc-note.md`](../patterns/moc-note.md)).
- A source note never lists what it updated; its backlinks are that list
  ([`properties-are-the-query-surface.md`](properties-are-the-query-surface.md)).
- An answered question does not keep its answer; the answer is promoted and the question links to it
  ([`a-question-is-a-queue-not-a-store.md`](a-question-is-a-queue-not-a-store.md)).
- Business rules say *what*; convention notes say *how the team builds*. A statement that fits both
  is split, not duplicated.

**Breaks when.** The same rule is readable in two files →
[`../anti-patterns/knowledge-in-two-places.md`](../anti-patterns/knowledge-in-two-places.md).
