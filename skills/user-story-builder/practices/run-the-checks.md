# Run the checks

**When** you have written or changed a story note, before you report the backlog as done, and
before any publish.

**Why** the shape is a publishing contract. An adapter maps the labels to tracker fields
positionally, so a missing or reordered label puts a story's criteria in its description; a
`tracker-id` on an unpublished note makes the next run create a duplicate; and `sources` disagreeing
with the `Source grounding:` line means one of the two is what the tracker receives and the other is
what a reviewer reads. None of it is visible by eye.

**Steps.**

1. **Check the backlog.** From the vault root:

       python3 scripts/story.py check . --knowledge <record-vault>

   `--knowledge` is the record vault — `anchored-knowledge`'s `docs/`, or wherever the config's
   `knowledge_root` points. Pass it whenever a story is Mode A. Without it a citation into the
   record is reported as a **warning**, because a backlog on its own cannot tell a missing note from
   a knowledge base it was not given
   ([`../principles/delegation-not-inclusion.md`](../principles/delegation-not-inclusion.md)).

2. **Read the warnings, do not skip them.** A warning is a citation or a parent the checker could
   not reach. Either pass `--knowledge`, or the link is wrong.

3. **Regenerate the index** when the backlog has more than one story:

       python3 scripts/story.py moc .

   Use `--check` in review: it writes nothing and fails on a stale block, instead of repairing one
   in silence and throwing away whatever a person had edited there
   ([`../patterns/backlog-notes.md`](../patterns/backlog-notes.md)).

4. **On an adopted backlog, take a baseline.** `--baseline findings.txt` reports only what your
   change broke. A first run over somebody else's backlog reports everything at once, and a list
   nobody has time to read is a checker nobody runs.

5. **Say what the check did not cover.** It reads front matter and labels, so it finds structure and
   never meaning. It cannot tell whether a source supports the criterion citing it, whether a slice
   is sound, or whether the *So that* is a real outcome. Name those as unchecked when you report
   ([`../principles/factuality-over-completeness.md`](../principles/factuality-over-completeness.md)).

**Done when** `check` reports zero errors, every warning is explained or fixed, `moc --check`
passes, and your report says which judgements a person still has to make.

**Related.** [`write-a-story.md`](write-a-story.md),
[`review-an-existing-story.md`](review-an-existing-story.md),
[`publish-to-a-tracker.md`](publish-to-a-tracker.md).
