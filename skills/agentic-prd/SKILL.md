---
name: agentic-prd
description: >
  Create, review, change and decompose an agent-ready PRD as an Obsidian vault: a hub note of
  readable prose over atomic notes — one per requirement, open question, outcome metric, Epic,
  Feature and User Story — where every requirement carries a stable id, a source with a locator, a
  priority, a verify method and its own coverage, and every gap is an open question rather than a
  guess. Use it whenever writing a PRD, product brief or functional spec that agents will build
  from; turning a SOW, transcripts, emails or notes into requirements; deciding the Epics and
  Features a release needs; judging whether a spec is ready to hand to an agent; generating User
  Stories and acceptance criteria; changing a requirement without leaving the backlog behind; or
  publishing a backlog to a tracker. Also for "spec-driven development", "AI-ready spec" and
  "convert this PRD to stories". Not for a single bug, one small story, a sprint status report,
  design documents, task breakdowns or estimates.
---

# agentic-prd

The PRD is the source of record for **why** and **what**; the tracker is for **state**. People
decide; agents draft, check and generate. An agent asked to build from an incomplete spec fills the
gap with a plausible guess, and on the page a guess is indistinguishable from a requirement. A
requirement carries a source and a locator, an unknown carries a question id, and only a person moves
either across a gate.

The output is a vault. The **hub note** keeps intent, scope, agent boundaries and rollout as prose,
because a PRD is read cold by agents that never loaded this skill — and it **embeds** rather than
summarises its notes, so it cannot go stale. Everything cited, superseded or covered on its own is a
note; coverage lives on the requirement and the table is generated from it
([`references/vault-convention.md`](references/vault-convention.md)).

## How to use this skill

Find your mode in the first table and your task in the second, then read only the files they name —
each is short. Where a rule conflicts with convenience the rule wins.

## Non-negotiables

1. Every requirement cites a source with a locator — a time, a page, a line — and links the system of record rather than copying it → `principles/every-requirement-cites-a-source.md`, `principles/link-the-source-never-copy-it.md`
2. A gap is an open question, never a guess; a behaviour a source implies but never states is `PROPOSED` → `principles/a-gap-is-a-question-not-a-guess.md`, `principles/implied-is-not-stated.md`
3. One behaviour per requirement, sliced by outcome and never by technical layer → `principles/one-behaviour-per-requirement.md`, `principles/slice-by-outcome-not-by-layer.md`
4. A conflict is recorded, not resolved; the newer decision supersedes → `principles/a-conflict-is-recorded-not-resolved.md`
5. Only a person crosses a gate, and the PRD changes before the backlog, always → `principles/only-a-person-crosses-a-gate.md`, `principles/the-prd-changes-before-the-backlog.md`
6. The PRD owns why and what; the tracker owns state; neither holds design, tasks or estimates → `principles/the-prd-owns-why-and-what.md`
7. Each level has one name and one id format; ids are never reused or renumbered, and a dropped requirement is retired in place → `principles/one-name-and-one-id-per-level.md`, `principles/ids-are-never-reused.md`
8. Every coverage line is answered — requirement links, `N/A` and a reason, or `Gap:` — and coverage lives on the requirement note, where the table is generated from it → `principles/every-coverage-line-is-answered.md`, `anti-patterns/a-hand-kept-coverage-table.md`
9. A number without a baseline, target, population, denominator and window is not a metric → `principles/a-metric-needs-every-field.md`
10. The check script finds structure, never meaning; say what it did not cover → `principles/the-check-is-not-a-reviewer.md`
11. The hub embeds its notes; it never summarises them → `anti-patterns/a-hub-that-summarises-its-notes.md`

## Mode → read

Pick the earliest mode the files need; name two and they run in order.

| The person wants | Mode | Read |
|---|---|---|
| A PRD from sources or notes | DRAFT | `practices/draft-a-prd.md`, `patterns/prd-hub-note.md`, `references/vault-convention.md` |
| To know whether a PRD is ready, or where its gaps are | REVIEW | `practices/review-a-prd.md`, `patterns/review-findings.md` |
| Epics, Features and User Stories out of a PRD | DECOMPOSE | `practices/decompose-a-prd.md`, `references/vault-convention.md` |
| A behaviour changed in a PRD that already has a backlog | CHANGE | `practices/change-a-requirement.md` |
| An approved backlog put into a tracker | PUBLISH | `practices/publish-a-backlog.md`, `patterns/tracker-item.md` |

## Task → read

| You are… | Read |
|---|---|
| Choosing how much PRD the work deserves, or writing a requirement | `practices/choose-the-prd-size.md`, `patterns/requirement-note.md` |
| Writing a citation, reading a `.docx`/`.pdf`/`.vtt` source, or filling an outcome metric | `practices/cite-a-source.md`, `patterns/knowledge-ledger.md`, `practices/read-a-binary-source.md`, `patterns/outcome-metric.md`, `patterns/coverage-check.md` |
| Recording a question, or bounding the build | `patterns/open-question.md`, `patterns/agent-boundaries.md` |
| Slicing a Feature into Stories, and laying out the backlog | `practices/slice-a-feature.md`, `patterns/user-story.md`, `patterns/acceptance-criterion.md`, `patterns/backlog-notes.md`, `patterns/coverage-moc.md` |
| Running the check, regenerating the MOCs, and reporting the result | `practices/run-the-checks.md`, `practices/report-the-result.md` |
| Asked for the PRD somewhere Obsidian is not — GitHub, a diff, a pasted brief | `practices/render-a-readable-prd.md` |
| Reviewing a PRD, a backlog or your own draft | `anti-patterns/` — scan the names; open what matches |

## Folders

    principles/  the rules and why each holds · patterns/  the note shapes, as skeletons
    practices/   procedures with a done-when · anti-patterns/  specs that fail, and why
    assets/ references/   the PRD hub template, and the vault convention
    examples/ evals/      a worked PRD vault to open in Obsidian, and trigger queries
    scripts/     `prd.py check`, `prd.py moc`, `prd.py render`, and the text extractor

## Conventions this skill assumes

    docs/prd/<slug>.md         the hub note, one per PRD · `.review.md` beside it
    docs/requirements/         one note per R- and X- requirement
    docs/metrics/ questions/   outcome metrics, open questions
    docs/backlog/              Epics, Features and Stories, flat, level in `type`
    docs/sources/ moc/ bases/  sources, decisions, the indexes, the Bases definitions

A project that keeps them elsewhere says so once in its `CLAUDE.md`; the shapes do not change. The
scripts need Python 3; PDF extraction also needs `pypdf` or `pymupdf`, publishing to Azure DevOps
needs `az`, and Bases views need Obsidian 1.9+ (a vault without them reads the snapshots).

## Knowledge

Draft from a sourced knowledge base where one exists, not from raw files: load `anchored-knowledge`,
a sibling of this folder, and cite its rule ids as sources. Transcripts go through
`transcript-knowledge-base` first. Where both are installed, an open question, a source and a
decision are **the same note** in the same folder.
