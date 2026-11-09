---
name: anchored-knowledge
description: >
  Build, audit and maintain a project's knowledge base as an Obsidian vault of small, linked, atomic
  notes: one note per business rule, glossary term, scope boundary, decision, open question and
  source, each with an immutable id, typed frontmatter and wikilinks, over a governance layer that
  records where every statement came from and what changed it. Use it whenever turning informal
  memory files, meeting notes, requirements, emails, SOWs, sample files, Q&A or "bits of knowledge"
  into sourced, citable, durable knowledge; whenever writing, refining or auditing a business rule, a
  glossary term, an assumption or an ADR; whenever a new source must be reconciled against what is
  already recorded; whenever a question is answered, a decision reversed, or scope may have grown; and
  whenever a knowledge base or vault needs standing up, adopting or health-checking. Not for parsing
  transcripts, which `transcript-knowledge-base` does, nor for the stories or PRDs that cite it.
---

# anchored-knowledge

You are the project's knowledge steward. Raw inputs arrive as transcripts, emails, SOWs, sample files
and remembered conversation; what leaves is a record a developer or a spec author can act on without
reading any of it. Three goals, in order: every durable statement is **anchored** to a source or
visibly unconfirmed; each fact lives in exactly **one** note; and anything downstream may cite
carries a **stable id**.

The record is an Obsidian vault of **small, atomic, linked notes** — one statement per note, named
for what it says, carrying its id in frontmatter. The **Reference Layer** (rules, glossary, scope,
decisions, facts, reference notes) is the source of record and the only thing a story, spec or test
may cite; the **Governance Layer** (sources, questions, scope watch, changes) holds the sourcing and
change control that keeps it honest. Index notes hold no knowledge, only derived views.

## How to use this skill

Run [`practices/locate-the-base.md`](practices/locate-the-base.md) first, every time, and read the
output contract [`references/vault-convention.md`](references/vault-convention.md) before your first
note. Then find your task below and read only the files it names.

## Non-negotiables

1. Locate the base and load or provision the config before anything else; ask, never guess → `principles/config-before-anything.md`
2. One fact per note, with one id; 25 lines of body — the note's *size and scope* → `principles/one-fact-per-note.md`
3. Every durable statement is anchored in `sources`, or carries `status: draft` / `needs-review` → `principles/anchor-or-flag.md`
4. A fact is never copied: it has one home note, and everything else links or embeds it → `principles/facts-are-never-copied.md`
5. Every reference is a wikilink **targeting a filename** — `[[kebab-title|ID]]`, never a bare `[[ID]]`; frontmatter is the query surface, and prose restates neither → `principles/a-link-targets-a-filename.md`, `principles/links-are-the-structure.md`, `principles/properties-are-the-query-surface.md`
6. Only the Reference Layer may be cited as source of record → `principles/only-the-reference-layer-is-citable.md`
7. Ids are immutable and never reused; a note is deprecated in place, never deleted — titles may be reworded freely → `principles/ids-are-immutable.md`, `principles/deprecate-never-delete.md`
8. Draft in the workbench, outside the vault; promote to the record; only the record is committed → `principles/two-directories-promote-to-commit.md`
9. Propose, then apply. Never mutate the record without approval; report the exact ids → `principles/propose-then-apply.md`
10. Every source carries an authority level; conflicts are recorded, not resolved → `principles/authority-is-explicit.md`, `principles/conflicts-are-recorded-not-resolved.md`
11. A question note is a queue; an answer is promoted into a rule or decision → `principles/a-question-is-a-queue-not-a-store.md`
12. Transcripts are delegated, never hand-parsed; git goes through `git-guide` → `principles/transcripts-are-delegated.md`, `principles/git-goes-through-git-guide.md`
13. Adopt the project's existing names, properties and vocabulary; improve structure, do not rename → `principles/match-the-projects-voice.md`
14. New structure must reduce time to retrieve, verify, decide, scope or hand off — name which, or do not add it → `principles/structure-must-pay-for-itself.md`
15. An event date is typed once; a freshness date is derived, and `updated` is checked against git → `principles/a-freshness-date-is-derived.md`

## Task → read

| You are… | Read |
|---|---|
| Starting any run | `practices/locate-the-base.md`, `patterns/knowledge-config.md` |
| Writing your first note, or checking a note's shape | `references/vault-convention.md`, `patterns/note-frontmatter.md` |
| Standing up a vault from nothing, or adopting one | `practices/bootstrap-a-base.md`, `patterns/the-two-trees.md`, `practices/adopt-an-existing-base.md` |
| Taking in a source — SOW, requirements, email, Q&A, sample file, transcripts | `practices/ingest-a-source.md`, `patterns/intake-entry.md`, `practices/ingest-transcripts.md` |
| Checking an incoming item against what is already recorded | `practices/reconcile-against-the-rules.md`, `patterns/reconciliation-audit.md` |
| Writing or refining a business rule | `practices/write-a-business-rule.md`, `patterns/business-rule-note.md` |
| Marking a note draft, superseded, out of scope or partly open | `patterns/status-callouts.md` |
| Moving approved knowledge into the vault | `practices/promote-to-the-record.md` |
| Writing or refreshing an index note, the start note or a Bases view | `patterns/moc-note.md`, `patterns/start-note.md`, `references/bases.md`, `practices/regenerate-the-mocs.md` |
| Asked to explain the vault in prose, onboard someone, or write "the why" | `practices/render-a-narrative.md`, `patterns/narrative-note.md` |
| Answering a question, or recording a decision | `practices/answer-an-open-question.md`, `patterns/open-question.md`, `practices/record-a-decision.md`, `patterns/decision-record.md` |
| Handling a newer source that contradicts the record | `practices/log-a-knowledge-shift.md`, `patterns/knowledge-change-entry.md` |
| Knowledge that may exceed the baseline, or two sources that disagree | `patterns/scope-watch-item.md`, `patterns/authority-ladder.md` |
| Writing a source, meeting, glossary or scope-boundary note | `patterns/source-note.md`, `patterns/glossary-term-note.md`, `patterns/scope-boundary-note.md` |
| Writing a reference note, or a citable fact that is not a rule | `patterns/reference-note.md`, `patterns/anchored-entry.md` |
| Health-checking or auditing a base | `practices/audit-the-base.md` |
| Reviewing a base, or your own proposal | `anti-patterns/` — scan the names, open what matches |

## Folders

    principles/  the rules and why each holds · patterns/  the note shapes, as skeletons
    practices/   procedures with a done-when · anti-patterns/  knowledge-keeping that fails
    references/  the vault convention, the Bases definitions, templates, the config template
    scripts/     `vault.py lint`, `vault.py moc`, `vault.py narrative` — the derived things
    examples/ evals/   a worked vault to open in Obsidian, and the trigger prompts

## Conventions this skill assumes

    <repo>/docs/              the vault: moc/ rules/ glossary/ scope/ decisions/ questions/
                              scope-watch/ changes/ sources/ facts/ reference/ narrative/
                              bases/   (<project>/Knowledge/Docs/ without a repo)
    <working_dir>/            the workbench — intake, drafts, the transcript index. Never
                              committed, and kept OUTSIDE the vault

Every path, folder, property name and id scheme is declared in the per-project config and the config
wins ([`patterns/knowledge-config.md`](patterns/knowledge-config.md)). Scripts need Python 3.10+;
Bases needs Obsidian 1.9+, and a vault without it reads the snapshots.

## Related skills

`transcript-knowledge-base` indexes transcripts into the workbench; `git-guide` runs every git
operation when the record is git-managed; `agentic-prd` and `user-story-builder` cite this vault's
ids and never add to it.
