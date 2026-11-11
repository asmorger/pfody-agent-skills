---
name: legacy-slicing
description: >
  Replace a legacy application one reversible slice at a time: read what the old system actually does
  out of its own code, database and logs into a disposable survey, turn the parts a person must rule
  on into a frozen slice brief, and leave behind characterisation tests that outlive both. Use it
  whenever a legacy, inherited or vendor-written system must be rewritten, replaced, strangled or
  migrated and nobody can state the requirements; whenever someone asks what the old screen actually
  does, which of its behaviours are bugs worth keeping, which are dead, or how to carve work small
  enough to be wrong cheaply; whenever a survey or a slice brief must be written, reviewed, frozen,
  flipped or deleted; and whenever a finding from a flipped slice has to change the next one. Not for
  greenfield scope, which `agentic-prd` owns, nor for writing the stories a shaped slice becomes,
  which `user-story-builder` owns.
allowed-tools: Read, Write, Edit, Glob, Grep
metadata:
  requires: []
  related: [agentic-prd, user-story-builder]
---

# legacy-slicing

The old system is the specification. The governing rule is **the oracle outranks the survey**: where
a written note and the running legacy system disagree, the system is right and the note is a defect
to regenerate ([`principles/the-oracle-outranks-the-survey.md`](principles/the-oracle-outranks-the-survey.md)).

Three artifacts, two of them disposable. A **survey** is derived from the old code and deleted at the
flip. A **slice brief** is decided, frozen when building starts, and superseded at the flip. A
**characterisation suite** is the only one that outlives a slice, and the only one that can fail.

What separates this from writing a requirements document up front is not how much gets written down.
It is that everything written down is scheduled to die, carries where it came from, and is produced
one slice ahead of the building rather than months ahead of it.

## How to use this skill

Survey one area ahead of the slice you are shaping — never the whole application
([`anti-patterns/surveying-the-whole-app-first.md`](anti-patterns/surveying-the-whole-app-first.md)).
Then find your task below and read only the files it names.

## Non-negotiables

1. The running legacy system outranks any note about it → `principles/the-oracle-outranks-the-survey.md`
2. A survey is derived: regenerate it, never hand-edit it to record a ruling → `principles/a-survey-is-derived-and-disposable.md`
3. Every observed line carries its provenance tag, guesses included → `principles/every-line-carries-its-provenance.md`
4. A claim about absence needs an exhaustive sweep; a ranked search cannot prove a negative → `principles/absence-needs-an-exhaustive-sweep.md`
5. Blast radius, not hours, is what makes a slice cheap to be wrong about → `principles/blast-radius-not-size.md`
6. Characterisation tests come from driving the old system, never from reading the survey → `principles/the-oracle-outranks-the-survey.md`
7. A frozen brief is appended to, never rewritten → `principles/a-frozen-brief-is-appended-never-rewritten.md`
8. `Decisions outstanding` reads 0 before building starts, and `DEFER` is how it gets there → `principles/decisions-outstanding-must-read-zero.md`

## Task → read

| You are… | Read |
|---|---|
| Starting on an area nobody can describe | `practices/survey-an-area.md`, `patterns/survey-note.md` |
| Writing or checking a survey line | `patterns/provenance-tag.md` |
| Claiming something is unused, dead or referenced nowhere | `principles/absence-needs-an-exhaustive-sweep.md` |
| Taking findings to the business | `practices/review-the-findings.md` |
| Turning rulings into a unit of work | `practices/shape-a-slice.md`, `patterns/slice-brief.md` |
| Deciding what must pass before the switch | `patterns/check-set.md` |
| Sizing a slice, or arguing one is too big | `principles/blast-radius-not-size.md`, `anti-patterns/a-slice-with-a-migration-in-it.md` |
| Switching a slice on, and cleaning up after | `practices/flip-a-slice.md` |
| Something died, hurt or surprised you | `practices/file-a-finding.md` |
| An area whose every workflow depends on it, such as sign-in | `practices/shape-a-slice.md` |
| Reviewing a survey or a brief, or your own draft | `anti-patterns/` — scan the names; open what matches |

## Folders

    principles/     the rules and why each one holds
    patterns/       the two note shapes, as fill-in skeletons (neutral Order / shipping domain)
    practices/      step-by-step procedures with a done-when checklist
    anti-patterns/  surveys and slices that fail — what they look like, why, what to do instead
    references/     the shared note taxonomy this skill's two types are registered in
    examples/ evals/   a worked survey and brief, and the trigger prompts

## Conventions this skill assumes

    survey/<area>.md              one per legacy area · type `survey` · deleted at the flip
    slices/<kebab-title>.md       one per slice · type `slice-brief` · `SL-nnn` in front matter
    tests/characterization/       the suite · grows every slice, never pruned

The two note types, their status ladders and their grouping key are declared in
[`references/vault-taxonomy.json`](references/vault-taxonomy.json), which is the registry the four
sibling skills share. A project may move the folders; nothing else about the shapes changes.

## Related skills

`agentic-prd` owns scope that does not exist yet — a survey is the opposite case, where the behaviour
exists and the record does not. Where both are installed, a ruling in a brief is the kind of decision
a PRD requirement cites, and a `DEFER` row is an open question by another name. `user-story-builder`
takes a shaped slice and writes the stories for it; this skill stops at the brief.
