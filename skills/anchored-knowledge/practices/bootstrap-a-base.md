# Bootstrap a base

**When** a project has knowledge scattered across notes, transcripts and people's heads, and no base.
Standing operating procedure A.

**Why.** The first pass sets the authority ladder, the id scheme and the vocabulary everything else
will be judged against. Getting the baseline source identified now is what makes every later conflict
decidable.

**Steps.**

1. **Run [`locate-the-base.md`](locate-the-base.md)**: choose both directories, provision the config.
2. **Stand up both trees** ([`../patterns/the-two-trees.md`](../patterns/the-two-trees.md)). If the
   working area sits inside the repository, add it to `.gitignore` and record
   `working_dir_gitignored: true`.
3. **Find the scope baseline.** The SOW, or whatever serves as the top-authority scope artifact. If
   you cannot find it, **ask what it is and where it lives** and record the answer in the config. A
   project with none sets `sow_present: false` and names its baseline in `scope_baseline_note`.
4. **Inspect what already exists** and preserve good structure. An existing folder with weak
   organisation is improved in place, not replaced
   ([`adopt-an-existing-base.md`](adopt-an-existing-base.md)).
5. **Seed the Source Register highest authority first** — baseline, then approved requirements, then
   clarifications — so the base is built outward from what is contractual
   ([`../patterns/source-register-row.md`](../patterns/source-register-row.md)).
6. **Draft the glossary first.** It is the cheapest file and the one that prevents the most rework
   ([`../patterns/glossary.md`](../patterns/glossary.md)).
7. **Draft a `business-rules.md` skeleton** from the baseline documents: topic sections with their
   prefixes, rules marked `Draft` with dates until anchored
   ([`../patterns/business-rules-file.md`](../patterns/business-rules-file.md)).
8. **Capture every unknown as an open question**, each with an owner and a needed-by
   ([`../patterns/open-question.md`](../patterns/open-question.md)).
9. **Write the index** so a newcomer learns which files they may cite
   ([`../patterns/knowledge-index.md`](../patterns/knowledge-index.md)).
10. **Define review cadence and ownership** in the config, and report what is still `Draft`.

**Done when** both trees exist, the config records the locations, the baseline source and the id
scheme, every seeded rule is anchored or dated-`Draft`, every unknown is a question with an owner, and
the working area is gitignored if it lives in the repository.
