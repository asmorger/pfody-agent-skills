# Agent Skills

Skills for AI-assisted product management. They turn project sources into cited knowledge,
agent-ready PRDs, and traceable work items. Nothing in them names a real project's files or types;
where one assumes a conventional path, it says so in its own *Conventions this skill assumes*
section.

| Skill | What it does | Needs |
|---|---|---|
| [`transcript-knowledge-base`](skills/transcript-knowledge-base) | Builds a sourced knowledge index from meeting transcripts | Python 3 |
| [`anchored-knowledge`](skills/anchored-knowledge) | Creates and audits a citable project knowledge system | Nothing extra |
| [`agentic-prd`](skills/agentic-prd) | Creates and reviews agent-ready PRDs, then generates Epics, Features and User Stories | Python 3 for its scripts |
| [`user-story-builder`](skills/user-story-builder) | Writes sourced User Stories and can publish them to Azure DevOps | `az` CLI to publish |

`agentic-prd` drafts from a knowledge base where one exists rather than from raw files, which is what
`anchored-knowledge` builds; `anchored-knowledge` delegates every transcript to
`transcript-knowledge-base` instead of parsing one itself. A PRD's requirements and a story's
acceptance criteria are the same discipline at two altitudes, so `user-story-builder` and
`agentic-prd` share their anti-inference rules and differ in what they take as input.

## Install

Copy a skill folder to your Claude Code skills folder, then start a new session:

```bash
git clone https://github.com/pfoty/agent-skills.git
cp -r agent-skills/skills/agentic-prd ~/.claude/skills/
```

## Use

Ask in plain language. For example:

- "Build a knowledge index from the transcripts in this folder."
- "Draft a PRD from this SOW and these notes."
- "Break this accepted PRD into Epics, Features, and User Stories."

A person approves scope and publishing. Check the output against its sources before you use it.

## Layout contract

Each skill is a thin `SKILL.md` router over four folders. The router names the non-negotiables and
maps *the task you are doing* to *the one or two files to read*. A model should never need to read a
whole folder.

    SKILL.md            router: purpose, non-negotiables, task → file table. Under 100 lines.
    principles/         one rule per file. Sections: Rule · Why · In the PRD · Breaks when.
    patterns/           one reusable shape per file. Sections: Use when · Skeleton · Notes · Related.
    practices/          one procedure per file. Sections: When · Why · Steps · Done when.
    anti-patterns/      one rejected design per file. Sections: Smell · Why it is wrong · Instead.

Every folder file is self-contained, under 60 lines, and links to its neighbours by relative path. A
principle links to the anti-pattern that violates it and the pattern that embodies it; a practice
links to the patterns it instantiates. A *Why* names the rule, the cost or the failure it protects
against — never taste.

A skill may also carry what the four folders cannot hold: `assets/` for a template a project copies,
`references/` for a format spec or a worked example, `scripts/` and a package for code, `prompts/`
for an extraction contract. These are artifacts, not prose a model reads to learn a rule, and they
are exempt from the size limit. Everything a model reads *as instruction* belongs in the four
folders.

Skeletons use a neutral `Order` / shipping-label domain — a shipping clerk, a support agent, an
operations lead. Keep it that way: a skeleton that names a real project's roles or entities stops
being a skeleton. Worked examples say in their first lines that their content is invented.

## Adding to a skill

- A new rule is a new `principles/` file plus one row in the router's non-negotiables or task table.
- A new shape is a new `patterns/` file; add it to the task table under the task that needs it.
- A rejected alternative is a new `anti-patterns/` file, linked from the principle it violates.
- Do not grow `SKILL.md` with content. If a router row needs more than a sentence, it is a file.

## Checks

    python3 scripts/check-skill-layout.py                  # links resolve, labels match, sizes hold
    python3 scripts/measure-skill-triggers.py fixture       # build the trigger fixture
    python3 scripts/measure-skill-triggers.py run 4         # one `claude -p` per eval query

`check-skill-layout.py` enforces the contract above and is cheap to run on every change.

Each skill keeps `evals/trigger-queries.json`: prompts that should and should not load it. The
measurement runs each one as a single-turn `claude -p` inside a fixture holding the skills and
nothing else, so a skill can only be reached through its own description — a false negative means the
description does not reach the task, a false positive means it reaches past it, usually into a
sibling skill's territory. One sample per query, so treat ±1 as noise, and each query is billed like
any other call.
