---
name: agentic-prd
description: >-
  Create, review, and maintain an agent-ready PRD, then generate traceable Epics, Features, User Stories, and acceptance criteria from it. The PRD is a compact Markdown contract with stable requirement IDs, a source for each requirement, a verify method, agent boundaries, and open questions. Use this skill when a person wants to write a PRD, product brief, or functional spec for agentic development; turn transcripts, a SOW, or notes into requirements; define Epics and Features; check whether a PRD is ready for agents; break a PRD into a backlog; or change requirements without backlog drift. Use it also for "spec-driven development", "AI-ready spec", "convert this PRD to stories", or "is this spec ready to build", even if the person does not say "skill". Do not use it for a single bug, a single small story, or a sprint status report.
---

# Agentic PRD

This skill makes the PRD the source of record for **why** and **what**. The work tracker stays the source of record for **state**: sprint, assignee, estimate, and status. People make decisions. Agents draft, check, and generate.

An agent fills an unstated gap with a plausible guess, and the guess looks like a requirement. So this skill makes each gap visible. Each requirement has a source, and each unknown stays an open question.

## Work item levels

Use these names and ID formats in all files, and do not use another name for a level. Each level becomes one tracker item of the same level, except a Requirement and an acceptance criterion.

| Level | ID | What it is | Size test | Where it lives |
|---|---|---|---|---|
| Epic | `EPIC-01` | A business outcome that needs one or more Features | It serves a PRD outcome, and it can take more than one sprint | PRD Section 4 |
| Feature | `FEAT-01` | One capability: one job for one role | It delivers one job, and it needs one or more User Stories | PRD Section 4 |
| User Story | `US-01` | A vertical slice of one Feature | One person can build, test, and demo it in one sprint | Backlog file |
| Requirement | `R-001` | One testable behavior | It states one behavior, and it belongs to one Feature | PRD Section 4 |
| Acceptance criterion | `AC-1` | One Given/When/Then test of a Requirement | Its number restarts in each User Story | Backlog file |

A person decides the Epics and Features at Gate 2. An agent generates the User Stories from them. A PRD and an Epic are different items: one PRD contains one or more Epics.

## Select the mode

| The person wants to | Mode |
|---|---|
| Create a PRD from sources or notes | DRAFT |
| Know whether a PRD is ready, or find its gaps | REVIEW |
| Get Epics, Features, and User Stories from a PRD | DECOMPOSE |
| Change behavior in a PRD with a backlog | CHANGE |
| Put an approved backlog in a work tracker | PUBLISH |

If the request does not name a mode, select the earliest mode that the current files need. If the request names two modes, run them in order. Tell the person which mode you selected.

## Files in this skill

| File | Read it when |
|---|---|
| `assets/prd-template.md` | Before DRAFT. Its "Agent protocol" section is the full rule set for all modes. A PRD holds its own copy, so read that copy in the other modes. |
| `references/backlog-format.md` | Before DECOMPOSE |
| `references/example-prd.md` and `references/example-backlog.md` | When you need a worked example. The example content is invented. |
| `scripts/check_prd.py` | After each mode that writes a file |
| `scripts/extract_text.py` | When a source is `.docx`, `.pdf`, `.vtt`, or `.srt` |

The scripts use only the Python standard library, except that PDF extraction needs `pypdf` or `pymupdf`.

## Rules for all modes

- **Do not invent.** Do not add a metric, a date, a customer need, or a behavior without a source. Write "Unknown", or add an open question.
- **Do not select a side in a conflict.** A newer decision replaces an older statement. If no decision settles a conflict, add an open question.
- **Do not state an implied behavior as sourced.** If a source implies a behavior but does not state it, mark it `PROPOSED` or add an open question.
- **Do not cross a human gate.** Only a person can approve Gate 1 (intent), Gate 2 (requirements), and Gate 3 (backlog). Do not set the status to Accepted unless the approver says so.
- **Protect the sources.** Link to a system of record. Do not copy credentials, customer data, or personnel comments. Use roles, not names. Leave out fee data and candid remarks.
- **Warn about internal sources.** If a citation points to an internal-only source, tell the person before they share the PRD outside the team.
- **Do not publish or push** unless the person asks in this conversation.

## Mode: DRAFT

1. Ask only for what you cannot find: the sources, the owner, and the location. The default location is `docs/prd/PRD-NNN-<slug>.md`.
2. Obey any limit on sources. State the limit at the top of the PRD, and report what you did not read. An excluded file can answer an open question, so the person must know about the exclusion.
3. Read all allowed sources. Use `scripts/extract_text.py <file> --out <dir>` for binary sources. Read long transcripts completely, because a later meeting often reverses an earlier one. Start your decision list from the newest source.
4. Select the size from the table in the template. Use the smallest size that removes guesswork.
5. Copy `assets/prd-template.md` and fill it. Group the work into Epics and Features, and list them in the work item map. Delete the guidance text. Keep the Agent protocol section, so that an agent without this skill can use the PRD.
6. Cite each requirement with a locator: a time (`SRC-07 @1:13:06`), a page (`SRC-02 p.4`), or a line in plain notes (`SRC-03 L12`). Compare the locator to the source when you write it. Record a date as the source gives it.
7. Fill each coverage line with requirement IDs, "N/A" and a reason, or "Gap: Q-xx".
8. Record each priority that no stakeholder assigned as an inference.
9. Run the checks. Then offer REVIEW.

## Mode: REVIEW

1. Run the checks, and put the result in the review. Do not change the PRD, even if the check fails. Write the findings to `<prd-name>.review.md`.
2. Use the REVIEW checklist in the Agent protocol. If a contract or earlier requirements exist, compare the PRD to them, because scope drift is often the largest finding.
3. Group the findings as conflicts, requirement quality, and coverage. Each finding names the item and the action.
4. State whether the PRD is ready for its next gate.
5. End with the questions to ask first, in order. Put first the answer that can change the most scope.

## Mode: DECOMPOSE

1. Read `references/backlog-format.md`.
2. Follow the DECOMPOSE steps in the Agent protocol. Write the result next to the PRD as `<prd-name>.backlog.md`.
3. If the status is not Accepted, stop and ask whether the person wants a preview. Mark a preview as `PREVIEW` at the top of the file, and do not publish it.
4. Do not add behavior, estimates, or tasks. Do not change an Accepted PRD in this mode. Report a new gap, because the person decides whether to use CHANGE. Design and tasks belong to engineering at build time.
5. Run the checks with `--backlog`. Do not report success until the check passes.

## Mode: CHANGE

1. Follow the CHANGE steps in the Agent protocol. The PRD changes first.
2. Keep the current IDs. Regenerate only the affected User Stories. Show the diff of each User Story.
3. Run the checks with `--backlog`.

## Mode: PUBLISH

Publish only when the person asks, the status is Accepted, and a person approved the backlog at Gate 3.

1. Find the available tracker tools. If none exist, give the person the backlog file and stop.
2. Show the items that you will create, and get a clear yes.
3. Create parents before children: Epic, then Feature, then User Story. For Azure DevOps, read the organization and the project from `az devops configure -l`. Do not assume a project.
4. Put the `EPIC-01`, `FEAT-01`, or `US-01` ID at the start of each item title. Add the `PRD-NNN` ID as a tag. This lets a person trace each item.
5. On Windows, convert tracker text to plain ASCII, because the command line can corrupt other characters.
6. Read back the created items, and record their IDs in the coverage table.

## Run the checks

```bash
python <skill-folder>/scripts/check_prd.py <prd.md>
python <skill-folder>/scripts/check_prd.py <prd.md> --backlog <backlog.md>
python <skill-folder>/scripts/check_prd.py <prd.md> --backlog <backlog.md> --source SRC-07=<transcript.txt>
```

Use the full path to the script, because the PRD is usually in another folder. Use `--source` with a text copy of a source to confirm that each time or line locator exists.

Exit code 0 means no structure or traceability errors. A warning can stay in a draft, but a person must resolve or accept each warning before Gate 2. The script cannot judge whether a citation means what the requirement says, whether a User Story slice is good, or whether a criterion is faithful to its requirement. Tell the person what the check did not cover.

## Report the result

Tell the person:
- what you wrote, and where
- the counts of Epics, Features, and User Stories
- the requirement counts: covered, blocked, proposed
- the check result and its limits
- the decisions that the person must make, with the most important decision first
