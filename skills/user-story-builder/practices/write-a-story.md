# Write a story

**When** the mode and the sources are settled and a story is wanted. Steps 3 and 4.

**Why.** This is where the governing rule is either held or lost. Every section below has a shape, and
every shape has one failure mode — a quota filled with inference.

**Steps.**

1. **Follow the portable core** for the craft and every anti-inference rule:
   [`../references/portable-core.md`](../references/portable-core.md). Substitute the project's
   vocabulary from the config wherever it shows a `{{placeholder}}` or a generic role.
2. **Write the opening sentence**: a specific role from the config, a need rather than a screen, and a
   business outcome that does not restate the need
   ([`../patterns/as-a-i-want-so-that.md`](../patterns/as-a-i-want-so-that.md)).
3. **Name the buildable output.** Up to four Expected Output bullets, one per sourced deliverable, and
   one bullet is a legitimate story
   ([`../patterns/expected-output.md`](../patterns/expected-output.md)).
4. **Put the rules in `Details`**, with one consolidated `Source grounding` bullet as the developer's
   reading list, and the same ids as wikilinks in the `sources` property
   ([`../principles/cite-once-per-story.md`](../principles/cite-once-per-story.md)).
5. **Write the criteria** — `AC-n [tag] Given … when … then …` — ordered from the primary output
   outward to the edges, with the behaviour embedded so each reads with the source closed
   ([`../patterns/acceptance-criterion.md`](../patterns/acceptance-criterion.md)).
6. **Route every gap** to an Assumption, an Open Question, or omission
   ([`../principles/a-gap-has-three-options.md`](../principles/a-gap-has-three-options.md)).
7. **Fill Technical Notes' three header bullets** always, and the optional ones only where a source
   addresses them ([`../patterns/technical-notes.md`](../patterns/technical-notes.md)).
8. **Run the traceability pass** silently, per bullet and per criterion, before output. Anything you
   cannot source moves or goes
   ([`../principles/per-bullet-traceability.md`](../principles/per-bullet-traceability.md)).
9. **Work the review checklist** before you hand it over
   ([`review-an-existing-story.md`](review-an-existing-story.md)).
10. **Write the note**: frontmatter with `id`, a matching `aliases`, `parent`, `source-mode`,
    `sources`, `testing-complexity` and an empty `tracker-id`; the labels as the body; the filename a
    kebab slug of the title ([`../patterns/user-story.md`](../patterns/user-story.md)).
11. **Return the note only** — no commentary before or after — unless the user asked for an audit.
    Keep every section label, using `- None identified` where a section is empty.

**Done when** every Expected Output bullet and every criterion traces to a named source, every gap is
an Assumption or an Open Question, every label is present, `sources` and the `Source grounding:` line
agree, the story produces something demonstrable, and nothing is wrapped around the note.
