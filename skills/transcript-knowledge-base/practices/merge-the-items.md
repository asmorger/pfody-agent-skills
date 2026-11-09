# Merge the items

**When** a batch of items is written. Step 3. Dedup, provenance enforcement and id assignment happen
here.

**Why.** The merge is what turns a list of extractions into an index: the same rule from three
meetings becomes one item with three sources, and anything unsourced is thrown out and counted.

**Steps.**

1. **Run it:**

       python -m tkb.cli merge --items items.json --state knowledge-index.state.json

2. **Read the dropped count.** Items missing provenance are dropped and reported. A non-zero count is
   a finding about your extraction, not noise — go back and either cite or delete those items
   ([`../principles/every-item-carries-a-source.md`](../principles/every-item-carries-a-source.md)).
3. **Check what merged.** Near-duplicate statements fold into one item with several sources; evidence
   is appended, never replaced
   ([`../principles/evidence-is-never-discarded.md`](../principles/evidence-is-never-discarded.md)).
4. **Check what did not merge but should have.** Dedup is lexical, so two phrasings of one rule can
   both survive. Lower `dedup_threshold`, or align the statements and re-merge
   ([`curate-a-large-corpus.md`](curate-a-large-corpus.md)).
5. **Let ids be assigned.** They come out per category — `ORDER-1`, `LABEL-1` — and you never write
   one ([`../patterns/category-taxonomy.md`](../patterns/category-taxonomy.md)).
6. **Never edit the state file to fix an item.** Fix the extraction and merge again; the step is
   idempotent ([`../patterns/state-file.md`](../patterns/state-file.md)).
7. **Merge after each batch** on a large corpus, so each batch's hashes land before the next one
   ([`batch-long-transcripts.md`](batch-long-transcripts.md)).

**Done when** the merge reported zero unsourced drops or you have fixed the ones it named, the files
in this batch are marked ingested, and anything that should have merged and did not has been dealt
with deliberately.
