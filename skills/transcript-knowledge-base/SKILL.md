---
name: transcript-knowledge-base
description: >
  Turn a folder of conversation transcripts into a curated, categorised Obsidian vault of durable
  knowledge — rules, decisions, requirements, constraints, scope — where each statement is its own
  small note with a stable id, a wikilink to the meeting it came from, and the verbatim quote, speaker
  and timestamp behind it. Handles Copilot and Teams exports and `.docx`, `.txt`, `.md`, `.json`,
  `.vtt`, `.srt` and `.csv`. Use it whenever transcripts, discovery calls or meeting recordings must
  become a sourced rules, requirements or decisions index; whenever someone asks "what did we decide
  about X, and where did that come from"; whenever newly added transcripts must be folded into an
  existing index without redoing prior work; and even when the request is only "summarise what we
  agreed across these calls, with sources". Not for reconciling the result into a project's rule set,
  which `anchored-knowledge` does, nor for transcription itself.
---

# transcript-knowledge-base

A folder of transcripts becomes a vault of small linked notes — one per statement, one per meeting,
one index — plus a small JSON state cache. Each statement carries the meeting, date, speaker,
timestamp and exact words behind it. No database.

**Everything it writes is generated.** A re-run overwrites the notes and deletes the ones it no longer
produces, so the output folder belongs to this skill alone, never to a project's record vault. What
leaves here is evidence: nothing in it is citable until `anchored-knowledge` reconciles it.

The split of labour is the whole design. The bundled Python tool does the mechanical work — scan,
change-detect, parse, deduplicate, render — deterministically and idempotently. **You do the
synthesis**: reading briefs and writing clean statements. It is the only step that can invent
something, so most of the rules below are about it.

## How to use this skill

Run the four steps in order: prepare, extract, merge, render. Confirm Python once, first. Then find
your task below and read only the files it names — each is short and self-contained.

## Non-negotiables

1. Never hand-write a note; the deterministic steps are what make the output trustworthy → `principles/the-tool-does-the-mechanics.md`
2. Every item carries a source with a real `turn_id` and a quote copied from the brief; never invent one, and drop what you cannot cite → `principles/every-item-carries-a-source.md`
3. Precision over volume — a meeting yields a handful of real rules, not dozens; a large corpus yields a superset to curate, not a finished index → `principles/precision-over-volume.md`, `principles/a-large-corpus-is-a-superset.md`
4. A statement is declarative and spec-style, one rule per item — never a quote or a paraphrase of chatter → `principles/a-statement-is-not-a-quote.md`, `principles/one-rule-per-item.md`
5. Caveats go in `status` and `note`, never buried in the statement → `principles/status-is-a-field-not-a-sentence.md`
6. Evidence is never discarded: duplicates merge sources, supersession marks and keeps → `principles/evidence-is-never-discarded.md`
7. Copy each file's hash from the manifest, and seed the taxonomy, so nothing churns between runs → `principles/the-content-hash-is-the-unit-of-work.md`, `principles/ids-are-stable-across-runs.md`
8. No interpreter means stop and say so — never produce the notes by hand → `principles/never-fake-the-output.md`
9. Every note is generated — fix a wording by re-extracting, never by editing output — and all of it is evidence, not record → `anti-patterns/editing-a-generated-note.md`, `anti-patterns/the-generated-index-shipped-as-finished.md`

## The workflow

| Step | Command | Read |
|---|---|---|
| 0 Preflight | `python --version` — needs 3.10+ | `practices/confirm-python.md` |
| 1 Prepare | `python -m tkb.cli prepare --folder <dir> --state <s.json>` | `practices/prepare-the-briefs.md` |
| 2 Extract | *you read each brief and write `items.json`* | `practices/extract-knowledge-items.md` |
| 3 Merge | `python -m tkb.cli merge --items items.json --state <state.json>` | `practices/merge-the-items.md` |
| 4 Render | `python -m tkb.cli render --out <vault-dir> --state <state.json>` | `practices/render-the-vault.md` |

## Task → read

| You are… | Read |
|---|---|
| Reading a brief and writing items | `practices/extract-knowledge-items.md`, `patterns/knowledge-item.md`, `patterns/items-json.md`, `patterns/transcript-brief.md` |
| Processing many or long transcripts, or a failed run | `practices/batch-long-transcripts.md`, `practices/diagnose-a-failed-run.md` |
| Setting the categories and id prefixes | `practices/seed-the-taxonomy.md`, `patterns/category-taxonomy.md` |
| Configuring the tool, picking where the vault goes, or marking a supersession | `patterns/tool-config.md`, `patterns/supersession.md` |
| Folding newly added transcripts into an existing index | `practices/run-an-incremental-update.md` |
| Asked what the deliverable looks like | `patterns/vault-notes.md`, `references/vault-convention.md` |
| Asked why a re-run skipped a file, or what notes regenerate from | `patterns/state-file.md` |
| Curating a status-heavy corpus, or running this on a schedule | `practices/curate-a-large-corpus.md`, `practices/schedule-a-recurring-run.md` |
| Reviewing an index, or your own extraction | `anti-patterns/` — scan the names; open what matches |

## Folders

    principles/     the rules and why each one holds
    patterns/       the shapes, as fill-in skeletons (neutral Order / shipping-label domain)
    practices/      step-by-step procedures with a done-when checklist
    anti-patterns/  extractions that fail — what they look like, why, what to do instead
    prompts/ references/   the extraction contract, and the vault convention
    tkb/ tests/     the deterministic tool, and the behaviour it guarantees
    examples/ sample_data/ evals/   a demo (`python examples/demo.py`), trigger prompts

## Conventions this skill assumes

    transcript-knowledge/        the vault — THIS SKILL OWNS EVERY FILE IN IT
      moc/ items/ meetings/ bases/   the index, a note per statement, a note per
                                 meeting, and the Bases definition the MOC embeds
    knowledge-index.state.json   the merge cache; what the notes regenerate from
    .knowledge-index.work/       briefs and the manifest, regenerated each run

All of it is overridable in the config, and a caller embedding this skill **must** override the output
paths into a working directory ([`patterns/tool-config.md`](patterns/tool-config.md)). Needs Python
3.10+ and the standard library only; the Bases embed needs Obsidian 1.9+, and a vault without it
reads the generated table.

## Related skills

`anchored-knowledge` consumes this vault as a supplemental source: it reconciles the statements into
its own record, promotes the meeting notes it needs, and carries each quote onto the rule it anchors.
It is the caller that must override the output paths into its workbench — this renderer deletes what
it no longer generates and cannot tell a hand-written note from its own.
