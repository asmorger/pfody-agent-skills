# Vault convention

The output contract: a PRD is a **hub note** of readable prose over **atomic notes** for everything
that gets cited, superseded or covered on its own — requirements, open questions, outcome metrics,
decisions, and the backlog's Epics, Features and Stories.

If you have `anchored-knowledge` installed, its `references/vault-convention.md` is the canonical
contract for the shared parts: frontmatter as the query surface, wikilinks as the structure, the
callout vocabulary, and the MOC's `<!-- generated -->` markers. This file is the part specific to a
PRD. Where both skills write the same kind of note — an open question, a decision, a source — they
write **the same note**, in the same folder, with the same type. A PRD's gap is a question the
project needs answered; two question registers is the failure the never-copy rule exists to prevent.

**That sentence is now a check rather than a promise.** Every type, id pattern, status vocabulary
and grouping key below is declared once in
[`vault-taxonomy.json`](vault-taxonomy.json), which `prd.py` and `anchored-knowledge`'s `vault.py`
both read, and which the repo's `check-taxonomy.py` compares against this file and against the worked
example. It had to be built: the same three shared types used to carry two id widths (`SRC-01` here,
`SRC-0002` there), two prefixes for one decision, two status casings, and six types the other
skill's linter called `unknown type` — none of which any check could see while the contract lived
in prose on both sides.

## 1. Folder map

    docs/
      prd/<prd-slug>.md               the hub note — type: prd
      prd/<prd-slug>.review.md        review findings — type: prd-review
      requirements/<kebab-title>.md   R-001, X-001 — type: requirement
      metrics/<kebab-title>.md        OUT-1 — type: outcome-metric
      questions/<kebab-title>.md      Q-0003 — type: open-question
      backlog/<kebab-title>.md        EPIC-01, FEAT-01, US-01 — type: epic | feature | user-story
      sources/<kebab-name>.md         SRC-0002 — type: source
      decisions/<kebab-title>.md      ADR-0004 — type: decision
      moc/requirements.md  coverage.md  backlog.md
      bases/*.base

A decision goes in `decisions/`, not in `sources/`: it is a thing the project decided, not a thing
the project read. That is also where `anchored-knowledge` keeps it, which is the point — one folder
and one id per note, so the two skills cannot each grow a decision register. The worked example used
to hold `sources/credit-hold-blocks-labelling.md` as `DEC-02` with the same `summary`, the same
`decided` date and the same rejected alternative as that vault's `ADR-0004`: one decision, written
down twice.

Folders are flat and the level lives in `type`, so the whole backlog sits in one folder and a Bases
view groups it. A project that keeps its PRDs elsewhere says so once in its `CLAUDE.md`; the shapes
do not change.

## 2. The hub keeps prose; the citable parts become notes

**A PRD is read cold**, top to bottom, by an agent that has never loaded this skill. That is why the
hub keeps intent, scope, context, agent boundaries, rollout and the agent protocol as prose, and why
it **embeds** rather than merely links the notes a reader must not miss: `![[address-error-rate-on-parcels]]`, `![[carrier-labels-on-the-order-screen]]`,
`![[record-every-label-action]]`. An embed resolves to whatever the note says now, so the hub cannot go stale, and a
reader who scrolls the hub still sees everything
([`../patterns/prd-hub-note.md`](../patterns/prd-hub-note.md)).

What becomes a note is what gets **cited, superseded or covered individually**:

| Note | Why it is not a table row |
|---|---|
| requirement | cited by a criterion, a commit and a test; retired in place; covered on its own |
| open question | has an owner, a date and a lifecycle; blocks specific requirements |
| outcome metric | nine fields, and each one can be unknown and need a question |
| Epic / Feature / Story | published to a tracker; a Feature carries its own coverage lines |
| decision / source | cited by id and locator from whatever rests on it |

## 3. Frontmatter

Closed vocabularies. The check script reads these and nothing else, so a value outside them is an
error rather than a style choice.

```yaml
# a requirement
id: R-001                 # R-NNN, or X-NNN for cross-cutting. Immutable, never reused.
aliases: [R-001]
type: requirement
status: accepted          # draft | accepted | retired
prd: "[[shipping-labels-at-order-processing|PRD-001]]"
feature: "[[create-and-print-a-label|FEAT-01]]"    # omitted on an X- requirement
applies-to: [All]         # X- only: All, or the FEAT ids it changes
priority: P0              # P0 | P1 | P2 | P3
verify: Auto              # Auto | Manual | Eval | Telemetry
source: SRC-0002 @12:04     # SRC-nnnn with a locator | ADR-nnnn | A-nn | PROPOSED
outcomes: ["[[address-error-rate-on-parcels|OUT-1]]"]
coverage: covered         # covered | blocked | skipped-proposed | skipped-p3 | retired
stories: ["[[create-a-label-for-a-confirmed-order|US-01]]"]    # required when coverage is covered
questions: ["[[who-may-void-a-printed-label|Q-0003]]"]   # required when coverage is blocked
superseded-by: "[[notify-on-carrier-outage|R-011]]"  # when status is retired
```

The **statement is the H1**, in one of the five patterns, and appears nowhere else:
`# R-001 — When a clerk confirms an order, the system shall create a carrier label…`. The body is
a sentence of elaboration at most, plus a callout when something is open
([`../patterns/requirement-note.md`](../patterns/requirement-note.md)).

A Feature carries its seven coverage lines as a nested mapping, which is what makes them checkable:

```yaml
checks:
  empty-state: "N/A — a confirmed order always has at least one line."
  loading-state: "[[show-the-label-queue|R-007]]"
  error-state: "[[show-the-carrier-rejection-reason|R-002]], [[reprint-a-damaged-label|R-008]]"
  permissions: "Gap: [[who-may-void-a-printed-label|Q-0003]]"
  bad-input-and-boundaries: "[[cancel-a-queued-label|R-009]]"
  concurrency: "[[export-the-days-labels|R-010]]"
  current-records-and-data-migration: "N/A — labels did not exist before this release."
```

All seven keys, every time, in this order, whatever the Feature does. Three legal values: requirement
links, `N/A` **plus a reason**, or `Gap:` naming a real question note
([`../patterns/coverage-check.md`](../patterns/coverage-check.md)).

## 4. Coverage is derived, never kept

The old coverage table was maintained by hand and could disagree with the requirements it described.
Now each requirement note carries its own `coverage` and `stories`, and
`python3 scripts/prd.py moc <vault>` builds the table from the notes. It cannot drift: there is one
place to change a requirement's coverage, and the table is a view of it
([`../patterns/coverage-moc.md`](../patterns/coverage-moc.md)).

`blocked` and `skipped` are results, not failures. A blocked requirement is a gap that reached the
person who can close it instead of becoming an invented behaviour
([`../principles/a-gap-is-a-question-not-a-guess.md`](../principles/a-gap-is-a-question-not-a-guess.md)).

## 5. The check reads structure, and says so

`python3 scripts/prd.py check <vault>` validates what front matter can prove: id formats and
uniqueness, the five requirement patterns, source format and locators, the closed vocabularies, all
seven coverage lines answered, questions with an owner and a date, metrics with every field, parents
that resolve, stories carrying every label and tagging real requirements, and a story covering only
its own Feature's requirements. Reading frontmatter rather than parsing tables is what made that
list possible.

It still cannot tell whether a citation supports the requirement that cites it, whether a statement
is the behaviour anybody wanted, or whether a criterion tests what it names. Say what it did not
cover ([`../principles/the-check-is-not-a-reviewer.md`](../principles/the-check-is-not-a-reviewer.md)).

## 6. PREVIEW is a gate, not a label

While the PRD is not `accepted`, every story note says `PREVIEW` in its first lines and the check
enforces it. A preview is not published
([`../principles/only-a-person-crosses-a-gate.md`](../principles/only-a-person-crosses-a-gate.md)).
