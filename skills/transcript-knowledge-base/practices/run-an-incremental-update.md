# Run an incremental update

**When** new transcripts have landed, or an existing one has been corrected, and an index already
exists.

**Why.** Staying current is the whole reason the state is keyed on content hashes. A base that is
expensive to update stops being updated, and a stale sourced index is worse than none because it is
still trusted.

**Steps.**

1. **Use the same four steps.** There is no separate incremental mode: `prepare` against the same
   folder and the same state file surfaces only what is new or changed
   ([`prepare-the-briefs.md`](prepare-the-briefs.md)).
2. **Confirm the state file is the one from last time.** A missing or wrong state file means
   everything is reprocessed and the previous quotes are gone
   ([`../patterns/state-file.md`](../patterns/state-file.md)).
3. **Extract only from the briefs that appeared.** A brief that is not there has not changed.
4. **Reuse the existing category names exactly**, so a restated rule gains a source on the existing
   item rather than starting a near-duplicate
   ([`../patterns/category-taxonomy.md`](../patterns/category-taxonomy.md)).
5. **Mark genuine replacements** with `supersedes`. The older item keeps its text, id and sources and
   becomes `superseded` ([`../patterns/supersession.md`](../patterns/supersession.md)).
6. **Merge and render.** Existing rules gain sources, genuinely new rules take new ids, superseded
   ones are marked.
7. **Report what changed**: items added, items that gained a source, items superseded. That list is
   what a reader actually wants from an update.
8. **An edited transcript correctly reprocesses** — the hash changed. Expect its items to re-merge
   into themselves.

**Done when** only the new or changed transcripts were extracted, the index gained sources rather
than duplicates where rules were restated, and the user has the list of what changed.
