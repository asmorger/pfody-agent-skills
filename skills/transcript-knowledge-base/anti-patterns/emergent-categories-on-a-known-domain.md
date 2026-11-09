# Emergent categories on a known domain

**Smell.** No `categories` in the config on a project whose topics everybody already knows. A rendered
index whose section order follows whichever transcript was read first. A `Labels` section and a
`Labelling` section with two prefixes, holding one topic between them.

**Why it is wrong.** Ids are assigned per category, so the prefix depends on whatever category name
the extraction happened to use first, and the section order follows first appearance. A later
transcript can therefore reorder the document and start a second section for an existing topic — and
every citation written elsewhere, in a story's source grounding or a reconciled rule set, now points
at a different rule than it did. Nothing fails; the citations are simply wrong. The near-miss category
name compounds it, because the dedup cannot merge across sections.

**Instead.** Seed the taxonomy: an ordered list of `{name, prefix}` in the config, four to eight
categories, one unique prefix each. Reuse those names **exactly** when extracting. Where a rules
document already exists, mirror its sections and prefixes so the two can be read side by side. Leave
it emergent only for a genuine first exploration of an unmapped domain, and say that is what you did
([`../principles/ids-are-stable-across-runs.md`](../principles/ids-are-stable-across-runs.md),
[`../practices/seed-the-taxonomy.md`](../practices/seed-the-taxonomy.md)).
