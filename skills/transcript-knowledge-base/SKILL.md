---
name: transcript-knowledge-base
description: >
  Turn a folder of conversation transcripts into a curated, categorised markdown index of durable
  knowledge — rules, decisions, requirements, constraints, scope — where each entry is a clean
  declarative statement with a stable id and a citation back to the meeting, speaker, timestamp and
  verbatim quote it came from. Handles Copilot and Teams exports and `.docx`, `.txt`, `.md`, `.json`,
  `.vtt`, `.srt` and `.csv`. Use it whenever transcripts, discovery calls or meeting recordings must
  become a sourced rules, requirements or decisions index; whenever someone asks "what did we decide
  about X, and where did that come from"; whenever newly added transcripts must be folded into an
  existing index without redoing prior work; and even when the request is only "summarise what we
  agreed across these calls, with sources". Not for reconciling the result into a project's rule set,
  which `anchored-knowledge` does, and not for transcription itself.
---

# transcript-knowledge-base

A folder of transcripts becomes one markdown document of durable knowledge, plus a small JSON state
cache. Each entry reads like a line from a business-rules document and carries the meeting, date,
speaker, timestamp and exact words behind it. No database.

The split of labour is the whole design. The bundled Python tool does the mechanical work — scan,
content-hash change detection, parse every format, deduplicate, render — deterministically and
idempotently. **You do the synthesis**: reading briefs and writing clean, spec-quality statements.
That is what gives the output its quality, and it is also the only step that can invent something, so
most of the rules below are about it.

## How to use this skill

Run the four steps in order: prepare, extract, merge, render. Confirm Python once, first. Then find
your task in the table and read only the files it names — each is short and self-contained.

## Non-negotiables

1. Never hand-write the index; the deterministic steps are what make it trustworthy → `principles/the-tool-does-the-mechanics.md`
2. Every item carries a source with a real `turn_id` and a quote copied from the brief; never invent one, and drop what you cannot cite → `principles/every-item-carries-a-source.md`
3. Precision over volume — a meeting yields a handful of real rules, not dozens → `principles/precision-over-volume.md`
4. A statement is declarative and spec-style, not a quote or a paraphrase of chatter → `principles/a-statement-is-not-a-quote.md`
5. One rule per item; split compound statements → `principles/one-rule-per-item.md`
6. Caveats go in `status` and `note`, never buried in the statement → `principles/status-is-a-field-not-a-sentence.md`
7. Evidence is never discarded: duplicates merge sources, supersession marks and keeps → `principles/evidence-is-never-discarded.md`
8. Copy each file's hash from the manifest, or it reprocesses on every run → `principles/the-content-hash-is-the-unit-of-work.md`
9. Seed the taxonomy on a known domain, so ids and section order stay stable → `principles/ids-are-stable-across-runs.md`
10. A large corpus yields a sourced superset to curate, not a finished document → `principles/a-large-corpus-is-a-superset.md`
11. No interpreter means stop and say so — never produce the index by hand → `principles/never-fake-the-output.md`

## The workflow

| Step | Command | Read |
|---|---|---|
| 0 Preflight | `python --version` — needs 3.10+ | `practices/confirm-python.md` |
| 1 Prepare | `python -m tkb.cli prepare --folder <dir> --state <state.json>` | `practices/prepare-the-briefs.md` |
| 2 Extract | *you read each brief and write `items.json`* | `practices/extract-knowledge-items.md` |
| 3 Merge | `python -m tkb.cli merge --items items.json --state <state.json>` | `practices/merge-the-items.md` |
| 4 Render | `python -m tkb.cli render --out <index.md> --state <state.json>` | `practices/render-the-index.md` |

## Task → read

| You are… | Read |
|---|---|
| Reading a brief and writing items | `practices/extract-knowledge-items.md`, `patterns/knowledge-item.md` |
| Writing the `items.json` file | `patterns/items-json.md` |
| Working out what a brief line means | `patterns/transcript-brief.md` |
| Processing many or long transcripts | `practices/batch-long-transcripts.md` |
| Setting the categories and id prefixes | `practices/seed-the-taxonomy.md`, `patterns/category-taxonomy.md` |
| Configuring the tool | `patterns/tool-config.md` |
| Marking a rule that replaces an older one | `patterns/supersession.md` |
| Folding newly added transcripts into an existing index | `practices/run-an-incremental-update.md` |
| Asked where a rule's exact words are | `patterns/state-file.md` |
| Asked what the deliverable looks like, or curating a status-heavy corpus | `patterns/rendered-index.md`, `practices/curate-a-large-corpus.md` |
| Running this on a schedule | `practices/schedule-a-recurring-run.md` |
| Looking at a failed or surprising run | `practices/diagnose-a-failed-run.md` |
| Reviewing an index, or your own extraction | `anti-patterns/` — scan the names; open what matches |

## Folders

    principles/     the rules and why each one holds
    patterns/       the shapes, as fill-in skeletons (neutral Order / shipping-label domain)
    practices/      step-by-step procedures with a done-when checklist
    anti-patterns/  extractions that fail — what they look like, why, what to do instead
    prompts/        the extraction contract, as a fillable prompt
    tkb/ tests/     the deterministic tool, and the behaviour it guarantees
    examples/ sample_data/   a runnable end-to-end demo: `python examples/demo.py`
    evals/          prompts that should and should not load this skill

## Conventions this skill assumes

    knowledge-index.md              the deliverable
    knowledge-index.state.json      the state cache — keep it beside the index
    .knowledge-index.work/          briefs and the manifest, regenerated each run

All four are overridable in the config, and a caller embedding this skill in a larger base **must**
override them ([`patterns/tool-config.md`](patterns/tool-config.md)). Needs Python 3.10+ and the
standard library only.

## Related skills

`anchored-knowledge` consumes this index as a supplemental source and reconciles its items into a
project's rule set. It is the caller that must override the output paths, because its own index shares
this skill's default name.
