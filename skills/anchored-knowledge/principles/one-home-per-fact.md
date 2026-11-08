# One home per fact

**Rule.** Each fact, rule, term or decision lives in exactly one place. Everything else links to it.
Never copy a paragraph between documents, and never restate a rule's mechanics in a second file
because it would be convenient to have them there.

**Why.** Two copies of a rule are one rule and one bug waiting for the next correction. The
correction always reaches one copy, and nothing announces that the other has gone stale — so the base
starts answering the same question two ways, and the reader who finds the wrong copy has no signal
that a right one exists. A link cannot go stale this way: it resolves to whatever the fact says now.

**In the base.**
- Rules state the behaviour; long mechanics go in a domain reference doc the rule links to
  ([`../patterns/convention-doc.md`](../patterns/convention-doc.md)).
- Vocabulary is defined once, in the glossary, and used verbatim everywhere else
  ([`../patterns/glossary.md`](../patterns/glossary.md)).
- Cross-link inline: `(see ORDER-8, ORDER-9)` for rules, `[ADR-0004](adr/0004-title.md)` for
  decisions, the tracker id for work items.
- An answered question does not keep its answer; the answer is promoted and the question links to it
  ([`a-question-is-a-queue-not-a-store.md`](a-question-is-a-queue-not-a-store.md)).
- Business rules say *what*; convention docs say *how the team builds*. A statement that fits both is
  split, not duplicated.

**Breaks when.** The same rule is readable in two files →
[`../anti-patterns/knowledge-in-two-places.md`](../anti-patterns/knowledge-in-two-places.md).
