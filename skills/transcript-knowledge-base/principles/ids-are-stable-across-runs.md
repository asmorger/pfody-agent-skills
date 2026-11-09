# Ids are stable across runs

**Rule.** On a known domain, seed `categories` in the config with an ordered list of names and
prefixes. Ids are assigned per category — `ORDER-1`, `LABEL-1` — so a seeded taxonomy keeps both the
ids and the section order stable as the corpus grows.

**Why.** The ids are what anything outside this index cites: a story's source grounding, a reconciled
rule in a project's rule set, a note in a ticket. Letting categories emerge means the prefix is
derived from whatever category name the extraction happened to use first, and the section order
follows first appearance — so a new transcript can reorder the document and a slightly differently
named category can start a second section with a different prefix for the same topic. Then the
citations in other documents point at the wrong rules, and nothing failed.

**In the index.**
- Seeded: `categories: [{name: Orders, prefix: ORDER}, {name: Labels, prefix: LABEL}]`, ordered as you
  want the document ([`../patterns/category-taxonomy.md`](../patterns/category-taxonomy.md)).
- Emergent is fine for a one-off exploration of an unknown domain, and only then.
- Reuse an existing item's category name **exactly**. A near-miss creates a new section rather than
  joining the right one ([`../practices/seed-the-taxonomy.md`](../practices/seed-the-taxonomy.md)).
- Seeding is also how the output is made to mirror an existing rules document — same sections, same
  prefixes, so the two can be read side by side.

**Breaks when.** A known domain is left to emerge →
[`../anti-patterns/emergent-categories-on-a-known-domain.md`](../anti-patterns/emergent-categories-on-a-known-domain.md).
