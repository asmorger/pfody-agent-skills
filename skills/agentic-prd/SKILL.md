---
name: agentic-prd
description: >
  Create, review, change and decompose an agent-ready PRD: a Markdown contract whose every
  requirement carries a stable id, a source with a locator, a priority and a verify method, and
  whose every gap is an open question rather than a guess. Use it whenever writing a PRD, product
  brief or functional spec that agents will build from; turning a SOW, transcripts, emails or notes
  into requirements; deciding the Epics and Features a release needs; judging whether a spec is
  ready to hand to an agent; generating User Stories and acceptance criteria; changing a requirement
  without leaving the backlog behind; or publishing a backlog to a tracker. Also for "spec-driven
  development", "AI-ready spec" and "convert this PRD to stories". Not for a single bug, one small
  story, a sprint status report, design documents, task breakdowns or estimates.
---

# agentic-prd

The PRD is the source of record for **why** and **what**; the tracker is the source of record for
**state**. People decide; agents draft, check and generate. An agent asked to build from an
incomplete spec fills the gap with a plausible guess, and on the page a guess is indistinguishable
from a requirement. Everything below keeps the two apart: a requirement carries a source and a
locator, an unknown carries a question id, and only a person moves either one across a gate.

## How to use this skill

Find your mode in the first table and your task in the second, then read only the files they name.
Each file is short and self-contained; do not read whole folders. When a rule here conflicts with
convenience, the rule wins — changing one is a decision to raise with the person, not a cleanup.

## Non-negotiables

1. Every requirement cites a source with a locator — a time, a page, a line → `principles/every-requirement-cites-a-source.md`
2. A gap is an open question, never a guess → `principles/a-gap-is-a-question-not-a-guess.md`
3. A behaviour a source implies but never states is `PROPOSED`, not sourced → `principles/implied-is-not-stated.md`
4. One behaviour per requirement, stated so a test can check it → `principles/one-behaviour-per-requirement.md`
5. A conflict is recorded, not resolved; the newer decision supersedes → `principles/a-conflict-is-recorded-not-resolved.md`
6. Only a person crosses Gate 1, Gate 2 or Gate 3 → `principles/only-a-person-crosses-a-gate.md`
7. The PRD owns why and what; the tracker owns state; neither holds design, tasks or estimates → `principles/the-prd-owns-why-and-what.md`
8. Each level has one name and one id format → `principles/one-name-and-one-id-per-level.md`
9. Ids are never reused or renumbered; a dropped requirement is retired in place → `principles/ids-are-never-reused.md`
10. Every coverage line is answered — ids, `N/A` and a reason, or `Gap: Q-xx` → `principles/every-coverage-line-is-answered.md`
11. The PRD changes before the backlog, always → `principles/the-prd-changes-before-the-backlog.md`
12. A number without a baseline, target, population, denominator and window is not a metric → `principles/a-metric-needs-every-field.md`
13. Link the system of record; never copy credentials, customer data or named remarks into it → `principles/link-the-source-never-copy-it.md`
14. User Stories slice by outcome, never by technical layer → `principles/slice-by-outcome-not-by-layer.md`
15. The check script finds structure, never meaning; say what it did not cover → `principles/the-check-is-not-a-reviewer.md`

## Mode → read

Pick the earliest mode the files need; if the request names two, run them in order. Say which.

| The person wants | Mode | Read |
|---|---|---|
| A PRD from sources or notes | DRAFT | `practices/draft-a-prd.md`, `patterns/prd-document.md` |
| To know whether a PRD is ready, or where its gaps are | REVIEW | `practices/review-a-prd.md`, `patterns/review-findings.md` |
| Epics, Features and User Stories out of a PRD | DECOMPOSE | `practices/decompose-a-prd.md`, `references/backlog-format.md` |
| A behaviour changed in a PRD that already has a backlog | CHANGE | `practices/change-a-requirement.md` |
| An approved backlog put into a work tracker | PUBLISH | `practices/publish-a-backlog.md`, `patterns/tracker-item.md` |

## Task → read

| You are… | Read |
|---|---|
| Choosing how much PRD the work deserves | `practices/choose-the-prd-size.md` |
| Writing or fixing a requirement row | `patterns/requirement-row.md` |
| Writing a citation, or checking one you wrote | `practices/cite-a-source.md`, `patterns/knowledge-ledger.md` |
| Reading a `.docx`, `.pdf`, `.vtt` or `.srt` source | `practices/read-a-binary-source.md` |
| Filling the outcome metrics, or a coverage check | `patterns/outcome-metric.md`, `patterns/coverage-check.md` |
| Recording something nobody has answered | `patterns/open-question.md` |
| Setting what agents may and may not do in the build | `patterns/agent-boundaries.md` |
| Slicing a Feature into User Stories | `practices/slice-a-feature.md`, `patterns/user-story.md` |
| Turning a requirement into acceptance criteria | `patterns/acceptance-criterion.md` |
| Laying out the backlog file | `patterns/backlog-file.md` |
| Running the structural check | `practices/run-the-checks.md` |
| Telling the person what you did | `practices/report-the-result.md` |
| Reviewing a PRD, a backlog or your own draft | `anti-patterns/` — scan the names; open what matches |

## Folders

    principles/     the rules and why each one holds
    patterns/       the shapes, as fill-in skeletons (neutral Order / shipping-label domain)
    practices/      step-by-step procedures with a done-when checklist
    anti-patterns/  specs that fail — what they look like, why, what to do instead
    assets/ references/   the PRD template, the backlog format, two invented worked examples
    scripts/ evals/        the structural check, the text extractor, the trigger queries

## Conventions this skill assumes

    docs/prd/PRD-NNN-<slug>.md              one PRD each, NNN zero-padded
    docs/prd/PRD-NNN-<slug>.backlog.md      its backlog, beside it
    docs/prd/PRD-NNN-<slug>.review.md       review findings, beside it

A project that keeps them elsewhere says so once in its `CLAUDE.md`; the shapes do not change. The
scripts need Python 3; PDF extraction also needs `pypdf` or `pymupdf`, and publishing to Azure DevOps
needs `az` with the `azure-devops` extension.

## Knowledge

Draft from a sourced knowledge base where one exists, not from raw files: load `anchored-knowledge`,
a sibling of this folder, and cite its rule ids as sources. A folder of transcripts is indexed by
`transcript-knowledge-base` first, never read into a PRD by hand.
