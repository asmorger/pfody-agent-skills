# Seed the taxonomy

**When** before the first run on a domain you already understand — which is most of them.

**Why.** Ids are what anything outside this index cites. Letting the categories emerge means the
prefixes and the section order depend on which transcript happened to be read first, so a later run
can renumber rules that other documents already point at.

**Steps.**

1. **List the topics the corpus is about**, in the order you want the document to read. Four to eight
   is usual.
2. **Give each a short uppercase prefix** — `ORDER`, `LABEL`, `CARR`, `SCOPE`. One prefix per
   category, never shared.
3. **Put them in the config** as an ordered list of `{name, prefix}`, and set `title` and `intro`
   there too ([`../patterns/tool-config.md`](../patterns/tool-config.md)).
4. **Mirror an existing rules document** where there is one: same section names, same prefixes. The
   two can then be read side by side, and reconciling one into the other is mechanical.
5. **Use the names verbatim when extracting.** "Labels" and "Labelling" are two sections with two
   prefixes for one topic, and the dedup will not merge across them
   ([`../patterns/category-taxonomy.md`](../patterns/category-taxonomy.md)).
6. **Add a category rather than stretching one.** A new topic gets its own section and prefix; ids are
   per category, so adding one does not disturb the others.
7. **Leave it emergent only for a genuine exploration** of a domain nobody has mapped yet, and say
   that is what you did.

**Done when** the config holds an ordered category list with one unique prefix each, the extraction
uses those names exactly, and the ids are stable enough for another document to cite.
