# A Tags label restating the parent

**Smell.** A story note ending in a label whose whole content is already in its front matter:

```markdown
**Tags**
- EPIC-01, FEAT-01
```

`parent` says `[[create-and-print-a-label|FEAT-01]]`, that Feature's `parent` says `EPIC-01`, and
the Epic's says `PRD-001`. `priority` is a property. The config's `Review Required` tag follows from
`review-required: true`. The label adds nothing and is typed by hand.

**Why it is wrong.** It is the `tags` property again, wearing a label instead of a key. Nothing
derives it and nothing checked it, so it is a third copy of three fields — and it is the copy a
publish step reads, which is the worst place for one. Re-parent a story and the label still names
the old Feature; the tracker takes the stale value, reporting rolls up against it, and the note
itself looks fine. A story's parentage is one edit in `parent` precisely so that it is one edit
([`../principles/one-name-and-one-id-per-level.md`](../principles/one-name-and-one-id-per-level.md)).

That a tracker wants tags is not an argument for the label. The adapter has `parent` and `priority`
in front of it and can walk them; asking the body for what front matter already states is the
redundancy, not the tagging.

**Instead.** Eight labels, ending at **Acceptance Criteria**. The publish step derives the tracker's
tags from `parent` — walked up to its Feature, Epic and PRD — plus `priority` and the config's
required tags ([`../patterns/tracker-item.md`](../patterns/tracker-item.md)).

`prd.py check` **reports a story that carries the label** rather than requiring one. It was in the
required set until this was decided, so every story written to the old shape still has one, and a
check that merely stopped asking would have left them all in place.

**Related.** [`../patterns/user-story.md`](../patterns/user-story.md),
[`a-hand-kept-coverage-table.md`](a-hand-kept-coverage-table.md).
