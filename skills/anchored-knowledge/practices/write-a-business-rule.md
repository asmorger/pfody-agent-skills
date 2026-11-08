# Write a business rule

**When** adding a rule, refining one, or splitting one that has grown two ideas.

**Why.** The rule row is what every story, criterion and test ultimately cites. A rule that is not
self-contained forces a reader back into the sources, which is the thing the base exists to prevent.

**Steps.**

1. **Place it in the right topic section.** One prefix per section, no two sections sharing one. A
   rule that fits no section means a new section and a new prefix, per the config
   ([`../patterns/business-rules-file.md`](../patterns/business-rules-file.md)).
2. **Take the next free number in that section**, even when the row belongs higher up the table. Never
   renumber to keep the table tidy
   ([`../principles/ids-are-immutable.md`](../principles/ids-are-immutable.md)).
3. **Write one testable idea, self-contained.** A reader should not need another file to know whether
   the system obeys it. State mechanics — fields, formulas, thresholds — once they are decided.
4. **Put long mechanics in a reference doc** and link to it, so the rule stays one sentence
   ([`../patterns/convention-doc.md`](../patterns/convention-doc.md)).
5. **Mark its status inline, with a date.** No marker means confirmed; everything else names the
   marker, the stakeholder and the date
   ([`../patterns/inline-status-markers.md`](../patterns/inline-status-markers.md)).
6. **Cross-link inline**: `(see LABEL-3)` for rules, `[ADR-0004](adr/0004-title.md)` for decisions,
   the tracker id for work items. Field and entity names in backticks, key decisions in bold.
7. **Refine in place; split when it holds two ideas.** The original keeps its id and one idea; the
   second idea takes a new number, and the two cross-link
   ([`../anti-patterns/one-rule-two-ideas.md`](../anti-patterns/one-rule-two-ideas.md)).
8. **Use the glossary's words**, and add the term there if the rule needed one that is missing
   ([`../patterns/glossary.md`](../patterns/glossary.md)).

**Done when** the rule states one testable idea, carries a date-bearing marker or none at all, sits
in a section whose prefix it uses, took the next free number, and every id it cites resolves.
