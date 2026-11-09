# Worked example: a backlog vault

`vault/` is a backlog you can open in Obsidian: two story notes, the index that queries them, and
the Bases definition the index embeds.

    vault/backlog/void-a-printed-label-story.md   Mode A — grounded in a sourced corpus
    vault/backlog/export-the-days-labels.md       Mode C — built from nothing but the request
    vault/moc/backlog.md                          the index; its table is generated
    vault/bases/backlog.base                      Backlog · Unpublished · Still needs a person

Everything is invented — a neutral Order / shipping-label domain, no real client. It shares that
domain with `anchored-knowledge` and `agentic-prd`'s example vaults, so the three read as one
project: the Mode A story's `sources` point at rule and decision notes that exist in
`anchored-knowledge/examples/vault`.

## What the pair shows

| Look at | To see |
|---|---|
| `void-a-printed-label-story.md` | Mode A: `source-mode: A`, `sources` as wikilinks, every criterion carrying a rule id |
| `export-the-days-labels.md` | Mode C: `source-mode: C`, `sources: []`, criteria tagged `[Request]`, and a callout that says so |
| both | `tracker-id` empty, `status: draft`, `review-required: true` — the three things that make "what still needs a person?" a query |
| the file name | `-story`, because `requirements/void-a-printed-label.md` has the plain name in a combined vault. The file name is the link target, so two notes cannot share one |

The Mode C note is the honest one to read carefully. Nothing in it is invented beyond what the user
said, every gap went to an Assumption or an Open Question, and the mode is a property rather than a
sentence somebody wrote once and nobody can query
([`../principles/mode-honesty.md`](../principles/mode-honesty.md)).

## Checking it

    cd examples/vault
    python3 ../../scripts/story.py check . --knowledge ../../../anchored-knowledge/examples/vault
    python3 ../../scripts/story.py moc   . --check

Without `--knowledge` the same run reports ten **warnings** and no errors: the Mode A story cites
the record vault, and a backlog on its own cannot tell a missing note from a knowledge base it was
not given. With it, both are silent — which is the half that shows the two vaults really do form
one ([`../practices/run-the-checks.md`](../practices/run-the-checks.md)).

## What happens on publish

Neither note has a `tracker-id`, so both are unpublished. After a verified create, the publish step
writes `tracker-id`, `tracker-url` and `status: published` back into the note — which is what lets a
later run update rather than duplicate, and lets a reviewer in the tracker get back to the sourced
note ([`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)). `story.py
check` reports a `tracker-id` on a note that does not say `published`, and a `published` note with
no `tracker-id`: either way the next run would create a second item instead of updating the first.

Before anything is sent, the wikilink brackets are stripped — `[[a-printed-label-may-be-voided|LABEL-2]]` becomes `LABEL-2` — and
then the whole field is normalised to pure ASCII. In that order
([`../principles/tracker-text-is-ascii.md`](../principles/tracker-text-is-ascii.md)).
