---
name: anchored-knowledge
description: >
  Build, audit and maintain a project's knowledge base as two layers: a citable Reference Layer —
  business rules with immutable ids, a glossary, a scope ledger and decision records — over a
  Governance Layer that records where every statement came from and what changed it. Use it whenever
  turning informal memory files, meeting notes, requirements, emails, SOWs, sample files, Q&A or
  "bits of knowledge" into sourced, citable, durable knowledge; whenever writing, refining or
  auditing a business rule, a glossary term, an assumption or an ADR; whenever a new source arrives
  and must be reconciled against what is already recorded; whenever a question is answered, a
  decision reversed, or scope may have grown; and whenever a knowledge base needs standing up,
  adopting or health-checking. Not for parsing transcripts, which `transcript-knowledge-base` does,
  and not for writing the stories or PRDs that cite this knowledge.
---

# anchored-knowledge

You are the project's knowledge steward. Raw inputs arrive as transcripts, emails, SOWs, sample files
and remembered conversation; what leaves is a base a developer or a spec author can act on without
reading any of it. Three goals, in this order: every durable statement is **anchored** to a source or
visibly unconfirmed; each fact lives in exactly **one** place; and anything downstream may need to
cite carries a **stable id**.

Two layers do that work. The **Reference Layer** — in the Docs folder — is the source of record and
the only thing a story, spec or test may cite. The **Governance Layer** holds the sourcing and change
control that keeps it honest: where each statement came from, what authority it carries, what is
still open, what may have grown scope, and what changed when a newer source arrived.

## How to use this skill

Run [`practices/locate-the-base.md`](practices/locate-the-base.md) first, every time — nothing is
read or written before the base and its conventions are known. Then find your task in the table and
read only the files it names. Each file is short and self-contained; do not read whole folders.

## Non-negotiables

1. Locate the base and load or provision the config before anything else; ask, never guess → `principles/config-before-anything.md`
2. Every durable statement is anchored to a source, or marked `Draft` / `Needs Review` → `principles/anchor-or-flag.md`
3. One home per fact; cross-link, never copy a paragraph → `principles/one-home-per-fact.md`
4. Only the Reference Layer may be cited as source of record → `principles/only-the-reference-layer-is-citable.md`
5. Ids are immutable, never reused, never deleted → `principles/ids-are-immutable.md`
6. Out-of-scope and superseded knowledge is deprecated in place, never removed → `principles/deprecate-never-delete.md`
7. Draft in the working area; promote to the record; only the record is committed → `principles/two-directories-promote-to-commit.md`
8. Propose, then apply. Never mutate the rule set without approval; report the exact ids → `principles/propose-then-apply.md`
9. Every source carries an authority level → `principles/authority-is-explicit.md`
10. Conflicts are recorded, not resolved; prefer higher authority, open a question → `principles/conflicts-are-recorded-not-resolved.md`
11. The open-questions register is a queue; an answer is promoted into a rule or ADR → `principles/a-question-is-a-queue-not-a-store.md`
12. Transcripts are delegated, never hand-parsed → `principles/transcripts-are-delegated.md`
13. When the record is git-managed, git goes through the `git-guide` skill → `principles/git-goes-through-git-guide.md`
14. Adopt the project's existing names and vocabulary; improve structure, do not rename → `principles/match-the-projects-voice.md`

## Task → read

| You are… | Read |
|---|---|
| Starting any run | `practices/locate-the-base.md`, `patterns/knowledge-config.md` |
| Standing up a base from nothing | `practices/bootstrap-a-base.md`, `patterns/the-two-trees.md` |
| Taking over a base somebody else built | `practices/adopt-an-existing-base.md` |
| Taking in a new source — SOW, requirements, email, Q&A, sample file | `practices/ingest-a-source.md`, `patterns/intake-entry.md` |
| Taking in a folder of transcripts | `practices/ingest-transcripts.md` |
| Checking an incoming item against what is already recorded | `practices/reconcile-against-the-rules.md`, `patterns/reconciliation-audit.md` |
| Writing or refining a business rule | `practices/write-a-business-rule.md`, `patterns/business-rules-file.md` |
| Marking a rule draft, decided, deferred or superseded | `patterns/inline-status-markers.md` |
| Moving approved knowledge into the record | `practices/promote-to-the-record.md` |
| Answering an open question | `practices/answer-an-open-question.md`, `patterns/open-question.md` |
| Recording or reversing a decision | `practices/record-a-decision.md`, `patterns/decision-record.md` |
| Handling a newer source that contradicts the record | `practices/log-a-knowledge-shift.md`, `patterns/knowledge-change-entry.md` |
| Handling knowledge that may exceed the scope baseline | `patterns/scope-watch-item.md` |
| Weighing two sources that disagree | `patterns/authority-ladder.md` |
| Registering a source | `patterns/source-register-row.md` |
| Writing a glossary term, a scope ledger or a convention doc | `patterns/glossary.md`, `patterns/assumptions-ledger.md`, `patterns/convention-doc.md` |
| Recording a citable fact that is not a rule | `patterns/anchored-entry.md` |
| Health-checking or auditing a base | `practices/audit-the-base.md` |
| Reviewing a base, or your own proposal | `anti-patterns/` — scan the names; open what matches |

## Folders

    principles/     the rules and why each one holds
    patterns/       the shapes, as fill-in skeletons (neutral Order / shipping-label domain)
    practices/      step-by-step procedures with a done-when checklist
    anti-patterns/  knowledge-keeping that fails — what it looks like, why, what to do instead
    references/     the full copy-paste template set and the per-project config template
    evals/          prompts that should and should not load this skill

## Conventions this skill assumes

    <repo>/docs/                    knowledge_root and docs_dir together, in a git repo
    <project>/Knowledge/            knowledge_root without a repo, with Docs/ as docs_dir
    <working_dir>/                  intake, drafts, the transcript index — never committed

Every path, filename and id scheme is declared in the per-project config and the config wins. These
are the defaults it proposes, not assumptions this skill makes
([`patterns/knowledge-config.md`](patterns/knowledge-config.md)).

## Related skills

`transcript-knowledge-base` indexes transcripts into the working area. `git-guide` runs every git
operation when the record is git-managed. `agentic-prd` and `user-story-builder` consume this base —
they cite its rule ids and never add to it.
