# Agent Skills

Skills for AI-assisted product management. They turn project sources into cited knowledge,
agent-ready PRDs, and traceable work items. Nothing in them names a real project's files or types;
where one assumes a conventional path, it says so in its own *Conventions this skill assumes*
section.

The four skills are [Paul Foty's](https://github.com/pfoty/agent-skills). This fork keeps their
substance and restructures each one to the layout contract below — a thin router over principles,
patterns, practices and anti-patterns — so a model reads the one or two files its task needs instead
of a whole instruction document.

It also changes what they **write**. The originals produce documents; this fork produces an
**Obsidian vault of small, linked, atomic notes** — one note per rule, term, requirement, story,
decision, question and source, each with an immutable id in frontmatter, wikilinks between them, and
index notes that hold a live query over a generated table rather than knowledge of their own. All
four skills are converted.

Each skill carries its own `references/vault-convention.md` describing what it writes, so it stays
independently installable;
[`anchored-knowledge`'s](skills/anchored-knowledge/references/vault-convention.md) is the canonical
one for the parts they share — frontmatter as the query surface, wikilinks as the structure, the
callout vocabulary, the `<!-- generated -->` markers. Where two skills write the same kind of note —
an open question, a source, a decision, a story — they write **the same note**, in the same folder,
with the same type. Two registers for one fact is the failure the one-home rule exists to prevent.

Every skill ships a worked example you can open in Obsidian: a
[knowledge vault](skills/anchored-knowledge/examples), a
[PRD vault](skills/agentic-prd/examples), a
[transcript index](skills/transcript-knowledge-base/examples), and
[two story notes](skills/user-story-builder/examples).

| Skill | What it does | Needs |
|---|---|---|
| [`transcript-knowledge-base`](skills/transcript-knowledge-base) | Turns meeting transcripts into a sourced vault: one note per statement, one per meeting | Python 3 |
| [`anchored-knowledge`](skills/anchored-knowledge) | Creates and audits a citable project knowledge vault | Python 3 for its lint and index generator |
| [`agentic-prd`](skills/agentic-prd) | Creates and reviews agent-ready PRDs as a hub note over atomic requirement notes, then generates Epics, Features and Stories | Python 3 for its scripts |
| [`user-story-builder`](skills/user-story-builder) | Writes sourced User Story notes and can publish them to Azure DevOps | `az` CLI to publish |

`agentic-prd` drafts from a knowledge base where one exists rather than from raw files, which is what
`anchored-knowledge` builds; `anchored-knowledge` delegates every transcript to
`transcript-knowledge-base` instead of parsing one itself. A PRD's requirements and a story's
acceptance criteria are the same discipline at two altitudes, so `user-story-builder` and
`agentic-prd` share their anti-inference rules and differ in what they take as input.

## Install

Copy a skill folder to your Claude Code skills folder, then start a new session:

```bash
git clone https://github.com/asmorger/pfody-agent-skills.git
cp -r pfody-agent-skills/skills/agentic-prd ~/.claude/skills/
```

The skills are independent; copy only the ones you want. `anchored-knowledge` expects a `git-guide`
skill for its git steps and names it where it would be used, so install that separately or expect
those steps to be reported rather than run.

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

    python3 scripts/check-skill-layout.py                    # links resolve, labels match, sizes hold
    python3 scripts/measure-skill-triggers.py fixture        # build the trigger fixture
    python3 scripts/measure-skill-triggers.py run 2 "" 5     # 5 samples per eval query

`check-skill-layout.py` enforces the contract above and is cheap to run on every change.

A skill that writes a vault also ships a checker for its **output**:

    cd skills/anchored-knowledge/examples/vault
    python3 ../../scripts/vault.py lint .   # dangling links, orphans, vocabulary, sizes, ids
    python3 ../../scripts/vault.py moc  .   # refresh the generated index tables

    cd skills/agentic-prd/examples/vault
    python3 ../../scripts/prd.py check .    # ids, patterns, sources, coverage, parents, criteria
    python3 ../../scripts/prd.py moc   .    # rebuild the coverage table from the requirement notes

    cd skills/transcript-knowledge-base/tests && python3 -m unittest discover -s . -t .

These are what make the convention enforceable rather than aspirational: a dangling wikilink, an
orphan note, a `status` outside the vocabulary, a confirmed rule with no source, a requirement whose
coverage claims a story that does not exist, a note over its size budget — all mechanical to detect
and all invisible by eye. Reading front matter rather than parsing markdown tables is what made the
list that long.

    python3 scripts/check-vault-tools.py                     # the checkers, checked

That one runs each checker against its worked example (which must pass) and then against a copy with
defects injected on purpose (which must produce a specific finding for each). A checker that reports
nothing on a clean vault *and* nothing on a broken one is worse than no checker, and breaking
something deliberately is the only way to tell the two apart.

Each skill keeps `evals/trigger-queries.json`: prompts that should and should not load it. The
measurement runs each one as a single-turn `claude -p` inside a fixture holding the skills and
nothing else, so a skill can only be reached through its own description — a false negative means the
description does not reach the task, a false positive means it reaches past it, usually into a
sibling skill's territory. Each query is billed like any other call.

**Two things to know before reading a number.** Run it from a plain terminal, not from inside a
Claude Code session: a nested run inherits `CLAUDECODE=1` and triggers both less often and far more
erratically than a real session. And triggering is probabilistic, so one sample per query is a coin
flip, not a measurement — two identical 56-query runs here disagreed on 19% of their positives. Use
`reps=5` or more and read the per-query rates the summary prints; a 1/5 and a 4/5 mean different
things, and neither is a pass or a fail. Precision is the number that survives the noise, because a
false positive is a real finding whenever it appears.
