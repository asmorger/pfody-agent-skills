# A generated table edited by hand

**Smell.** A status corrected in the MOC's table between the `<!-- generated -->` markers. A row
added there for a rule that has no note. A column tidied, a sort fixed, an id renamed — all of it in
the index, none of it in the record.

**Why it is wrong.** The next regeneration overwrites it without asking, so the work is lost; that is
the lucky outcome. The unlucky one is that nobody regenerates for a month, and in the meantime the
table is the only place the correction exists — so the index and the notes disagree, the Bases view
above it disagrees with both, and a reader has three answers. A hand-added row is worse again: it
asserts a rule the vault does not contain, and every id in it is a dangling citation waiting to be
copied into a story.

**Instead.** Change the note. The table is a snapshot of the notes and the embedded view is a live
query over the same properties, so both follow a frontmatter edit for free. If the table is wrong in
a way no note can fix, the `snapshot` spec in the MOC's frontmatter is wrong — change that and
regenerate. If the table is missing a rule, write the rule note
([`../patterns/moc-note.md`](../patterns/moc-note.md),
[`../practices/regenerate-the-mocs.md`](../practices/regenerate-the-mocs.md)).
