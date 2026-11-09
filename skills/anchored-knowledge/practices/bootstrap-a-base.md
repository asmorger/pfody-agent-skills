# Bootstrap a base

**When** a project has knowledge scattered across notes, transcripts and people's heads, and no base.
Standing operating procedure A.

**Why.** The first pass sets the authority ladder, the id scheme and the vocabulary everything else
will be judged against. Getting the baseline source identified now is what makes every later conflict
decidable.

**Steps.**

1. **Run [`locate-the-base.md`](locate-the-base.md)**: choose both directories, provision the config.
2. **Stand up both trees** ([`../patterns/the-two-trees.md`](../patterns/the-two-trees.md)). Keep the
   workbench outside the vault; if it sits inside the repository, add it to `.gitignore` and record
   `working_dir_gitignored: true`. Gitignore `.obsidian/workspace.json`.
3. **Find the scope baseline.** The SOW, or whatever serves as the top-authority scope artifact. If
   you cannot find it, **ask what it is and where it lives** and record the answer in the config. A
   project with none sets `sow_present: false` and names its baseline in `scope_baseline_note`.
4. **Inspect what already exists** and preserve good structure. An existing folder with weak
   organisation is improved in place, not replaced
   ([`adopt-an-existing-base.md`](adopt-an-existing-base.md)).
5. **Write source notes highest authority first** — baseline, then approved requirements, then
   clarifications — so the base is built outward from what is contractual
   ([`../patterns/source-note.md`](../patterns/source-note.md)).
6. **Write the glossary notes first.** The cheapest notes in the vault and the ones that prevent the
   most rework ([`../patterns/glossary-term-note.md`](../patterns/glossary-term-note.md)).
7. **Write a rule note per statement** in the baseline documents, each with its topic, its source and
   `status: draft` with a date until anchored
   ([`../patterns/business-rule-note.md`](../patterns/business-rule-note.md)).
8. **Capture every unknown as an open question**, each with an owner and a needed-by
   ([`../patterns/open-question.md`](../patterns/open-question.md)).
9. **Write the start note and one MOC per type**, with a `.base` beside each, so a newcomer learns
   which notes they may cite ([`../patterns/start-note.md`](../patterns/start-note.md),
   [`../patterns/moc-note.md`](../patterns/moc-note.md),
   [`../references/bases.md`](../references/bases.md)).
10. **Lint, regenerate, and report what is still draft.** Define review cadence and ownership in the
    config or the start note ([`regenerate-the-mocs.md`](regenerate-the-mocs.md)).

**Done when** both trees exist, the config records the locations, the baseline source and the id
scheme, every seeded rule is anchored or dated-`Draft`, every unknown is a question with an owner, and
the workbench is gitignored if it lives in the repository.
