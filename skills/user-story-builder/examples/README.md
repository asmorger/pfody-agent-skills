# Worked example: two story notes

`void-a-printed-label.md` and `export-the-days-labels.md` are the two shapes this skill writes,
side by side: a **Mode A** story grounded in a sourced corpus, and a **Mode C** story built from
nothing but what the user asked for. Drop them in a vault's `backlog/` folder to see them render.

Both are invented — a neutral Order / shipping-label domain, no real client. They share their domain
with `anchored-knowledge` and `agentic-prd`'s example vaults, so the three read as one project: the
Mode A story's `sources` point at rule notes that exist in `anchored-knowledge/examples/vault`.

## What the pair shows

| Look at | To see |
|---|---|
| `void-a-printed-label.md` | Mode A: `source-mode: A`, `sources` as wikilinks, every criterion carrying a rule id |
| `export-the-days-labels.md` | Mode C: `source-mode: C`, `sources: []`, criteria tagged `[Request]`, and a callout that says so |
| both | `tracker-id` empty, `status: draft`, a `review-required` tag — the three things that make "what still needs a person?" a query |

The Mode C note is the honest one to read carefully. Nothing in it is invented beyond what the user
said, every gap went to an Assumption or an Open Question, and the mode is a property rather than a
sentence somebody wrote once and nobody can query
([`../principles/mode-honesty.md`](../principles/mode-honesty.md)).

## What happens on publish

Neither note has a `tracker-id`, so both are unpublished. After a verified create, the publish step
writes `tracker-id`, `tracker-url` and `status: published` back into the note — which is what lets a
later run update rather than duplicate, and lets a reviewer in the tracker get back to the sourced
note ([`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)).

Before anything is sent, the wikilink brackets are stripped — `[[LABEL-2]]` becomes `LABEL-2` — and
then the whole field is normalised to pure ASCII. In that order
([`../principles/tracker-text-is-ascii.md`](../principles/tracker-text-is-ascii.md)).
