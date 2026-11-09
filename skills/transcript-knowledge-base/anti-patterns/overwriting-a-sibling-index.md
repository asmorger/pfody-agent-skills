# Overwriting a sibling index

**Smell.** `render --out` pointed at a project's record vault, or at a folder that already holds
hand-written notes, because the notes "all go in the vault anyway". The run reports success.

**Why it is wrong.** This renderer owns every file it writes. It records them in
`.tkb-manifest.json` and, on the next run, **deletes the ones it no longer generates** — and it
cannot tell a hand-written rule from a statement it rendered last month. The manifest limits the
damage to files this renderer created, so a note somebody wrote by hand survives; what does not
survive is the distinction. The record vault now holds `transcript-item` notes that look like record,
sitting in the same graph and the same searches as the rules, and the next person cites a transcript
as source of record. The state file collision is the second half: two tools writing one state file
makes every later incremental run behave unpredictably.

**Instead.** Point `--out` and `state_path` at a folder that belongs to this skill, in the workbench,
never at the record. A caller driving this skill is responsible for naming them; `anchored-knowledge`
does exactly that, rendering into `knowledge-working/transcript-knowledge/` and reconciling the
statements into its own vault afterwards
([`../patterns/tool-config.md`](../patterns/tool-config.md),
[`../practices/prepare-the-briefs.md`](../practices/prepare-the-briefs.md)).
