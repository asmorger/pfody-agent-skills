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

It does not make the vault the only way to read the work. A readable document is fine — as long as it
is **derived and checked** rather than typed beside the notes it summarises. `anchored-knowledge`
renders a narrative (`vault.py narrative`) whose every claim links the note that holds it, whose only
date is written by the script, and which lists what it could not source under *Gaps found while
deriving* instead of inventing it. `agentic-prd` renders the PRD with its embeds resolved
(`prd.py render`), because `![[note]]` shows nothing on GitHub, in a diff, or to an agent reading the
raw file. Both fail a check once the notes move on, so a stale document is visible rather than
believed.

**There is no `tags` property.** It used to carry `type` and `topic` a second time, as "the one
sanctioned redundancy", justified by the tag pane. Nothing derived it and nothing checked it, so it
was a hand-kept third copy of two fields — and it undid the reason the folders are flat, since
`topic` is a property precisely so that changing it is *one* edit. `type` and `topic` are what the
Bases views and MOCs group by now, which is what the tag encoded anyway. That decision has a
principle behind it, `structure-must-pay-for-itself.md`: new structure earns its place by reducing
the time to retrieve, verify, decide, scope or hand off, and the person adding it names which.

**The story body's `**Tags**` label went the same way, for the same reason.** It held
`EPIC-01, FEAT-01` — the PRD, Epic and Feature ids, the priority, and the config's required tag —
every one of which is already `parent`, `priority` and `review-required` in front matter. So it was
the `tags` property again, wearing a label instead of a key: a hand-kept copy of three fields, in
the one place a publish step would read it. The tracker still gets its tags; the adapter **derives**
them by walking `parent` up to its Feature, Epic and PRD. `prd.py` now reports a story that still
carries the label rather than requiring one, because the old shape had it in the required set and a
story written to that shape would otherwise keep it forever
([`a-tags-label-restating-the-parent.md`](skills/agentic-prd/anti-patterns/a-tags-label-restating-the-parent.md)).

**Which makes the grouping key load-bearing, so every type now declares one and every note carries
it.** Removing the tag only paid off where something replaced it, and `topic` existed on three types
in one skill: a requirement, a story, a decision, a question, a metric and a transcript item each
had `type` and nothing else to slice by. The registry names the key per type — `topic` for most,
`category` for a glossary term and a transcript item, `area` for a scope boundary, `source-type` for
a source — and both linters report a note without it. One key per type, not a second copy of an
existing one: a glossary term's `category` *is* its topic, so it does not get both.

**Citations are `[[file-name|ID]]`, never a bare `[[ID]]`.** Obsidian resolves a wikilink against
file names and paths and never against `aliases`, so a bare id link opens a new empty note — and a
linter that accepts the alias cannot tell the difference, which is how a vault ends up with a hollow
citation layer and every check green. The ids stay in `aliases` for search and autocomplete. The
linters resolve links the way Obsidian does, check `#heading` and `#^block` anchors, reject two notes
sharing a file name, and compare id-shaped display text against the target's real id.

Each skill carries its own `references/vault-convention.md` describing what it writes, so it stays
independently installable;
[`anchored-knowledge`'s](skills/anchored-knowledge/references/vault-convention.md) is the canonical
one for the parts they share — frontmatter as the query surface, wikilinks as the structure, the
callout vocabulary, the `<!-- generated -->` markers. Where two skills write the same kind of note —
an open question, a source, a decision, a story — they write **the same note**, in the same folder,
with the same type. Two registers for one fact is the failure the one-home rule exists to prevent.

**That last sentence used to be a promise. It is a check now.**
[`shared/vault-taxonomy.json`](shared/vault-taxonomy.json) declares every note type once — its
owning skill, folder, id pattern, status vocabulary, grouping key, whether it is citable, and its
body budget — and `vault.py` and `prd.py` both read it instead of each holding its own constants.
Each skill carries a byte-identical copy so it still installs alone, and
`scripts/check-taxonomy.py` fails when a copy drifts, when a convention file or a skeleton
contradicts the registry, or when two skills' worked examples disagree about a note they both write.
It had to be built. The three shared types carried **two id widths** (`SRC-01` against `SRC-0001`),
one decision was written down twice under **two prefixes** (`DEC-02` and `ADR-0004`) with the same
summary and the same date, the PRD hub's status was Title Case while every other note's was
lowercase, a story was `accepted` in one skill and `draft | ready | published` in the other, and
`agentic-prd`'s own checker **rejected every citation form its SKILL.md tells you to use** —
`source: LABEL-2` came back as *not SRC-nn with a locator, DEC-nn, A-nn or PROPOSED*. None of it was
visible, because each contract lived in prose in two places and each checker only ever saw its own
skill's example.

Every skill ships a worked example you can open in Obsidian: a
[knowledge vault](skills/anchored-knowledge/examples) with a
[derived narrative](skills/anchored-knowledge/examples/vault/narrative), a
[PRD vault](skills/agentic-prd/examples) with its
[rendered document](skills/agentic-prd/examples/vault/render), a
[transcript index](skills/transcript-knowledge-base/examples), and
and a [story backlog](skills/user-story-builder/examples) with its generated index.

| Skill | What it does | Needs |
|---|---|---|
| [`transcript-knowledge-base`](skills/transcript-knowledge-base) | Turns meeting transcripts into a sourced vault: one note per statement, one per meeting, every quote verified against the transcript | Python 3 |
| [`anchored-knowledge`](skills/anchored-knowledge) | Creates and audits a citable project knowledge vault | Python 3 for its lint and index generator |
| [`agentic-prd`](skills/agentic-prd) | Creates and reviews agent-ready PRDs as a hub note over atomic requirement notes, then generates Epics, Features and Stories | Python 3 for its scripts |
| [`user-story-builder`](skills/user-story-builder) | Writes sourced User Story notes and can publish them to Azure DevOps | Python 3 for its checker; `az` CLI to publish |

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

A skill folder is self-contained: it carries its own copy of `references/vault-taxonomy.json` and
its scripts read that copy, so nothing outside the folder has to come with it. Each skill's
`metadata.requires` and `metadata.related` name the siblings it hands work to.

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

    SKILL.md            router: purpose, non-negotiables, task → file table. Body under 100 lines.
    principles/         one rule per file. Sections: Rule · Why · In the PRD · Breaks when.
    patterns/           one reusable shape per file. Sections: Use when · Skeleton · Notes · Related.
    practices/          one procedure per file. Sections: When · Why · Steps · Done when.
    anti-patterns/      one rejected design per file. Sections: Smell · Why it is wrong · Instead.

Every folder file is self-contained, under 60 lines, and links to its neighbours by relative path. A
principle links to the anti-pattern that violates it and the pattern that embodies it; a practice
links to the patterns it instantiates. A *Why* names the rule, the cost or the failure it protects
against — never taste.

The router's front matter carries five keys, and the budget above is on the **body**, because front
matter is metadata the harness reads rather than prose a model reads to learn a rule:

    name                 the folder name, exactly. The folder is what a project installs.
    description          what the model matches a task against. At most 1024 characters.
    allowed-tools        what the skill's own documented commands need, and nothing more.
    metadata.requires    a skill it hands work to and will not do itself. Absent → report the step.
    metadata.related     a skill it reads from or hands to, and degrades without.

`requires` and `related` replace *Related skills* prose as the record, because a list can be
checked and a paragraph cannot: every name must resolve to a skill in this repo or to a declared
external. Nothing read the front matter before, which is how a 1027-character description and a
non-negotiables list numbered 1 2 3 4 5 **7** 8 9 10 both survived in files five other checkers
walked over on every run.

A skill may also carry what the four folders cannot hold: `assets/` for a template a project copies,
`references/` for a format spec or a worked example, `scripts/` and a package for code, `prompts/`
for an extraction contract. These are artifacts, not prose a model reads to learn a rule, and they
are exempt from the size limit. Everything a model reads *as instruction* belongs in the four
folders.

Two of those artifacts are **shared files, copied**: `references/vault-taxonomy.json` and
`scripts/vaultlib.py`. Each lives once in `shared/` and is copied byte-identically into every skill
that needs it, because a skill folder has to work when it is the only thing installed — nothing
outside it may be required at run time. `check-taxonomy.py --fix` pushes the canonical version and
the check fails on any drift, which is the whole of the discipline: one source, copies checked. Edit
the file in `shared/`, never a copy.

Skeletons use a neutral `Order` / shipping-label domain — a shipping clerk, a support agent, an
operations lead. Keep it that way: a skeleton that names a real project's roles or entities stops
being a skeleton. Worked examples say in their first lines that their content is invented.

## Adding to a skill

- A new rule is a new `principles/` file plus one row in the router's non-negotiables or task table.
- A new shape is a new `patterns/` file; add it to the task table under the task that needs it.
- A rejected alternative is a new `anti-patterns/` file, linked from the principle it violates.
- Do not grow `SKILL.md` with content. If a router row needs more than a sentence, it is a file.

## Checks

    python3 scripts/check-skill-layout.py                    # front matter, links, labels, sizes
    python3 scripts/check-taxonomy.py                        # one registry, and nothing contradicting it
    python3 scripts/check-taxonomy.py --fix                  # push the registry to the skill copies
    python3 scripts/check-allowed-tools.py                   # declared tools vs instructed commands
    python3 scripts/measure-skill-triggers.py fixture        # build the trigger fixture
    python3 scripts/measure-skill-triggers.py run 2 "" 5     # 5 samples per eval query

`check-skill-layout.py` enforces the contract above and is cheap to run on every change.
`check-allowed-tools.py` exists because `allowed-tools` is the one piece of front matter that
**fails closed**: declare too little and step 1 of a run is denied, with nothing in the skill's own
files to explain why. So it reads the prose mechanically — every fenced `bash` block, every indented
command block, and every inline backticked command in `SKILL.md`, `practices/` and `references/` —
and asks whether some `Bash(...)` entry covers each one. It found two gaps the first time it ran:
`anchored-knowledge` instructs `git rev-parse --show-toplevel` in step 3 of **every** run while
declaring no git permission at all, and `agentic-prd` instructed `python …/extract_text.py` where
its own router says Python 3 and every other command says `python3`. It reports over-grants too, as
warnings. `anti-patterns/` and `principles/` are deliberately not scanned for inline commands: a
command named there is usually the one the skill is telling you *not* to run, and demanding a
permission for the forbidden thing is the exact inversion the check exists to prevent.

`check-taxonomy.py` enforces the copy discipline for both shared files, and the contract in
`shared/vault-taxonomy.json`: the per-skill copies are
identical, every front matter block in every skill — the worked examples **and the skeletons inside
fenced blocks**, because a skeleton is what a model copies — has a known type, a status in that
type's vocabulary, an id matching its pattern and its grouping key filled in, every inline
`# draft | accepted | retired` comment still agrees with the registry, every note in a worked
example sits in its type's folder, and two skills' examples agree about any note they both write.

Every skill that writes a vault ships a checker for its **output**:

    cd skills/anchored-knowledge/examples/vault
    python3 ../../scripts/vault.py lint      .            # links, anchors, vocabulary, sizes, ids
    python3 ../../scripts/vault.py lint      . --baseline findings.txt   # only what a change broke
    python3 ../../scripts/vault.py lint      . --git     # an `updated` older than the last commit
    python3 ../../scripts/vault.py moc       . [--check]  # refresh the index tables, or fail if stale
    python3 ../../scripts/vault.py narrative . [--check]  # stamp the derived narrative, or fail if stale

    cd skills/agentic-prd/examples/vault
    python3 ../../scripts/prd.py check  .    # ids, patterns, sources, coverage, parents, criteria
    python3 ../../scripts/prd.py moc    . [--check]   # rebuild the coverage table from the notes
    python3 ../../scripts/prd.py render . --out render/prd-001.md [--check]   # embeds resolved

    cd skills/user-story-builder/examples/vault
    python3 ../../scripts/story.py check . --knowledge <record-vault>  # labels, modes, tags, publish state
    python3 ../../scripts/story.py moc   . [--check]  # rebuild the backlog index, or fail if stale

    cd skills/transcript-knowledge-base
    python3 -m tkb.cli verify --vault <vault> --folder <transcripts>   # every quote, re-read
    cd tests && python3 -m unittest discover -s . -t .

The three checkers share one implementation of everything underneath them —
[`shared/vaultlib.py`](shared/vaultlib.py): notes, wikilinks, front matter, the taxonomy check, the
provenance stamp, and the row and cell rendering. They each held their own copy until the third one
shipped, and the copies had already drifted: two spellings of the same finding, two sort keys, and a
`title` cell that collapsed whitespace in one script and not in another, which would have ended a
table row early the day a heading wrapped. Sharing the cell renderer is also what lets two
generators own one index — `moc/backlog.md` has two, since `agentic-prd` writes stories as well —
because they cannot disagree about a table they render with the same code. What is *not* shared is
each `moc` generator itself: one stamps the marker with a date and reads `as-of`, one leaves the
marker alone, one refuses to touch a snapshot it does not own. Those are decisions about a
particular vault, not primitives.

These are what make the convention enforceable rather than aspirational: a dangling wikilink, a bare
id that opens an empty note, a `#heading` that does not exist, two notes sharing a file name, an
orphan note, a `status` outside the vocabulary, a confirmed rule with no source, a requirement whose
coverage claims a story that does not exist, a note over its size budget, an index that no longer
matches the notes under it, a narrative claim with no link, a story whose eight labels are out of
order, a criterion whose source tag is not in its own `sources`, a `tracker-id` on a note that does
not say `published` — all mechanical to detect and all invisible by eye. Reading front matter rather
than parsing markdown tables is what made the list that long.

Four of them are worth calling out, because they check things the rest cannot:

- **`tkb verify` is the only check that reads meaning.** It parses the transcripts again and confirms
  that each cited cue exists, that the speaker at that cue is the one the note names, and that every
  quoted word is in the turns at that cue — ellipsis allowed, punctuation ignored, since the
  transcription service supplied it. Everything else in this repo passes an extraction that moved a
  sentence to the wrong timestamp or put it in the wrong mouth, and for output whose entire purpose
  is to be evidence, a citation nobody can check is worse than none: a missing quote invites a
  question, a wrong one ends it. A quotation it cannot reach is reported as **unchecked** rather than
  as passing.
- **`--check` fails on drift instead of repairing it.** The generators used to rewrite a stale block
  in silence, which hides a committed index that disagrees with its notes and discards a hand edit
  without saying so. A generated note now carries `generator`, `input-paths` and
  `input-manifest-sha256`, so "is this current?" has a mechanical answer.
- **`--baseline` judges a change by what it broke.** Without it the first run on an adopted vault
  reports everything at once, and a list nobody has time to read is a checker nobody runs.
- **`story.py check` is the only one that can be given a second vault.** A Mode A story cites rule
  and decision ids that live in the record vault, so a backlog on its own cannot tell a missing note
  from a knowledge base it was not handed: `--knowledge <dir>` resolves across both, and without it
  an unreachable citation is a **warning** rather than an error. A **bare id** stays an error either
  way, because that is a fact about the link's form — `[[LABEL-2]]` opens a new empty note whatever
  else is installed. `moc/backlog.md` has two possible owners, since `agentic-prd` writes stories
  too when a whole backlog is decomposed at once, so both generators produce that block byte for
  byte and the suite asserts each reports the other's as current.
- **`--git` catches the date nobody bumps.** `updated` is a claim about the file rather than a fact
  about the world, so it rots — and the MOC tables and Bases views that sort on it then sort on
  fiction. Git already knows when each note last changed, so the check compares the two, reading the
  *author* date because a rebase resets the committer date and would flag the whole vault at once.
  It is opt-in: a vault's dates may legitimately be fictional, as this repo's worked examples are.
  (Verified in a scratch repo rather than in `check-vault-tools.py`, for that reason.)

    python3 scripts/check-vault-tools.py                     # the checkers, checked

That one runs each checker against its worked example (which must pass) and then against a copy with
defects injected on purpose (which must produce a specific finding for each). A checker that reports
nothing on a clean vault *and* nothing on a broken one is worse than no checker, and breaking
something deliberately is the only way to tell the two apart. Ten cases, covering the bare-id
link, the mismatched display id, the dead anchor, the hand-edited generated block, the missing
provenance, the index gone stale, the narrative claim with no link, and the rendition left behind by
its notes. `tkb verify` is covered the same way by its own unit tests — `tests/test_verify.py`
plants an invented quote, a misattributed one and one at a timestamp nobody spoke at.

**The eighth case is the only one that is not about a single skill**, and it is the one that found
the most. It composes `anchored-knowledge`'s worked example, `agentic-prd`'s and a
`user-story-builder` story into **one vault**, which is what a project that installs them together
actually has — `questions/`, `sources/`, `decisions/`, `moc/`, `bases/` and `backlog/` are shared
folders by design — then requires **both** linters to pass it. Until it existed every checker ran on
its own skill's example and went green, which is how every divergence in the paragraph above
survived. Composing them immediately turned up one more that nobody had argued about: the knowledge
base's retired rule and the PRD's retired requirement were both `one-label-per-order.md`, so **nine
citations in the knowledge vault silently reopened to the PRD's requirement** — Obsidian resolves a
wikilink by file name and picks by proximity, so each link still worked and nothing looked wrong.
The record layer now keeps the plain name and the later layer takes its level as a suffix
(`-requirement`, `-story`); §3 of the canonical convention says so, and the composed case fails if
it stops being true. Its broken half injects a story named for its requirement's behaviour, a story
status reverted to the PRD's word, a source id reverted to the narrow width, and a note with its
grouping key removed.

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
