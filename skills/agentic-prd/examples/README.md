# Worked example: a shipping-labels PRD vault

`vault/` is a small, complete, internally consistent PRD in the shape this skill writes. **Open
`vault/` in Obsidian** and start at `prd/shipping-labels-at-order-processing.md`.

Everything in it is invented — a neutral Order / shipping-label domain, no real client, no real
numbers — and it is the fixture the bundled script is tested against. It shares its domain with
`anchored-knowledge`'s example vault, so the two read as one project.

## What to look at

| Look at | To see |
|---|---|
| `prd/shipping-labels-at-order-processing.md` | the hub: prose for intent, scope and agent boundaries, `![[OUT-1]]` and `![[EPIC-01]]` embedded rather than summarised |
| `requirements/create-a-label-on-order-confirmation.md` | a requirement note — the statement is the H1, everything else is a property |
| `requirements/void-a-printed-label.md` | `coverage: blocked`, with the question that blocks it |
| `requirements/one-label-per-order.md` | retired in place: the id and the note stay forever |
| `requirements/record-every-label-action.md` | a cross-cutting `X-` requirement, with `applies-to` instead of a feature |
| `backlog/create-and-print-a-label.md` | a Feature carrying its seven coverage lines as `checks` |
| `backlog/void-a-label.md` | two of those lines as `Gap:` — the Feature is not decomposable yet |
| `moc/coverage.md` | the coverage table, generated from the requirement notes |
| `questions/who-may-void-a-printed-label.md` | the same note shape `anchored-knowledge` uses, with a `prd` property |

In the graph, every requirement reaches a source and a story, and the two blocked ones reach `Q-03`.

## Run the script

    cd vault
    python3 ../../scripts/prd.py check .      # → 0 errors, 0 warnings, 140 checks
    python3 ../../scripts/prd.py moc  .       # → no changes; the snapshots match the notes

Confirm a locator actually exists in its source:

    python3 ../../scripts/prd.py check . --source SRC-01=path/to/transcript.txt

Then break something and watch it get caught. Set a `priority` to `High`, point a criterion at
`R-777`, blank a `checks` line, empty a question's `owner`, or move a story's `parent` to the wrong
Feature:

    python3 ../../scripts/prd.py check .
    ERROR   R-002: priority 'High' is not one of ('P0', 'P1', 'P2', 'P3')
    ERROR   US-01: a criterion cites unknown requirement R-777
    ERROR   FEAT-01: coverage line 'error-state' is blank
    ERROR   Q-03: a question with no owner cannot close
    ERROR   US-01: covers R-001, which belongs to FEAT-01, not to its parent FEAT-02

To see coverage regenerate, change a requirement's `coverage` and run `moc` again. The diff is the
point: it shows what moved, and the table can never disagree with the notes.

## What is deliberately imperfect

`FEAT-02` has two `Gap:` coverage lines pending `Q-03`, and `R-012` is `blocked` rather than covered.
That is the skill working: a gap that reached the person who can close it, instead of becoming an
invented behaviour. `R-014` is `skipped-p3` — a result, not an omission. There is no `.obsidian/`
folder, so Obsidian will create its own on first open.
