# Write a business rule

**When** adding a rule, refining one, or splitting one that has grown two ideas.

**Why.** The rule note is what every story, criterion and test ultimately cites. A rule that is not
self-contained forces a reader back into the sources, which is the thing the record exists to
prevent — and a rule sharing a note with its neighbours cannot be marked, superseded or cited on its
own.

**Steps.**

1. **Write one testable idea, self-contained**, as one or two sentences of prose. A reader should not
   need another note to know whether the system obeys it. Two ideas means two notes
   ([`../anti-patterns/one-rule-two-ideas.md`](../anti-patterns/one-rule-two-ideas.md)).
2. **Name the note for what it says**, kebab-case, no id in the filename: `rules/
   order-address-frozen-on-confirmation.md`. The H1 is `# <ID> — <Title>`
   ([`../patterns/business-rule-note.md`](../patterns/business-rule-note.md)).
3. **Take the next free number for its topic**, and put it in `id` with a matching `aliases` entry so
   `[[confirmed-order-may-split-across-parcels|ORDER-5]]` resolves. One prefix per topic, from the config; a rule that fits no topic means a
   new topic, which is a config decision
   ([`../principles/ids-are-immutable.md`](../principles/ids-are-immutable.md)).
4. **Fill the frontmatter.** `type`, `status`, `topic`, `authority`, `sources` and the dates —
   there is no `tags`. A confirmed rule needs `confirmed` and a non-empty `sources`
   ([`../patterns/note-frontmatter.md`](../patterns/note-frontmatter.md)).
5. **Add a callout only if the property cannot say it** — the stakeholder a draft waits on, what a
   supersession replaced, which clause is still open. A confirmed rule carries none
   ([`../patterns/status-callouts.md`](../patterns/status-callouts.md)).
6. **Put long mechanics in a reference note** and link to it, so the rule stays one sentence
   ([`../patterns/reference-note.md`](../patterns/reference-note.md)).
7. **Link it in, both ways.** Wikilink the rules, terms, decisions and facts a reader will want next;
   add it to a neighbouring rule's **Also** line so it is not an orphan. Field and entity names in
   backticks ([`../principles/links-are-the-structure.md`](../principles/links-are-the-structure.md)).
8. **Refine in place; split when it holds two ideas.** The original keeps its id and one idea, the
   second takes a new number, and the two cross-link. Reword a title freely — the id is what was
   cited, not the wording.
9. **Use the glossary's words**, and write the term's note if the rule needed one that is missing
   ([`../patterns/glossary-term-note.md`](../patterns/glossary-term-note.md)).
10. **Lint and regenerate** before reporting
    ([`regenerate-the-mocs.md`](regenerate-the-mocs.md)).

**Done when** the note states one testable idea, carries a status with the dates that status needs,
took the next free number for its topic, has at least one inbound link, and every wikilink in it
resolves.
