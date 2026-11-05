# Agentic PRD skill

This skill helps Claude create and maintain an agent-ready PRD, and generate traceable Epics, Features, User Stories, and acceptance criteria from it.

## Install

1. Save `agentic-prd.skill` from the file card, or open it in the Claude desktop app.
2. For Claude Code, you can also unzip the file to `~/.claude/skills/agentic-prd/`.
3. Start a new session.

The skill needs no other skill or plugin. The scripts need Python 3. PDF extraction also needs `pypdf` or `pymupdf`. Azure DevOps publishing needs the `az` CLI with the `azure-devops` extension.

## Use

Ask in plain language:

- "Draft a PRD from the SOW and the transcripts in this folder."
- "Review this PRD. Is it ready for agents?"
- "Break this accepted PRD into Epics, Features, and User Stories."
- "Change R-012 so that a clerk can also void a label. Show the affected User Stories."

## Work item IDs

| Level | ID format |
|---|---|
| Epic | `EPIC-01` |
| Feature | `FEAT-01` |
| User Story | `US-01` |

## How it works

| Stage | Person | Agent |
|---|---|---|
| Intent and scope | Approves at Gate 1 | Drafts from sources and challenges weak evidence |
| Epics, Features, and requirements | Approves at Gate 2 | Drafts, and finds gaps and conflicts |
| Backlog | Reviews the diff at Gate 3 | Generates User Stories and proves coverage |
| Publish | Asks for it | Creates tracker items and reads them back |

## Limits

- The check script finds structure and traceability defects. It cannot prove that a citation means what a requirement says.
- The skill does not estimate work. Estimates stay in your own estimate process.
- The example files are invented. Do not use them as evidence.
