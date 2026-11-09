---
type: moc
updated: 2026-11-08
snapshot:
  type: user-story
  columns: [id, title, parent, source-mode, status, testing-complexity, tracker-id]
generator: story.py moc
generated: 2026-11-09
input-paths: [backlog/]
input-manifest-sha256: fcc41d0297e0a9e956aba40b602c1b8e57996d8a74eda6d9c441cf2abb9dffbe
managed-block-sha256: 35ddede251ee71254bfe30ca0579a5545e5d0f9de8940a05b1ee67291f6145a9
---

# Backlog

> [!warning] Illustrative example only
> The stories, the sources and the roles are invented. Do not use them as evidence.

One note per story in `backlog/`, each carrying the mode it was built in. A Mode A story cites the
record vault's rule and decision ids; a Mode C story cites nothing, because nothing was there to
cite, and says so in `source-mode` rather than in a sentence somebody wrote once.

`tracker-id` is empty until a publish returns one, which is what makes "what is still unpublished?"
a query rather than a reading exercise.

![[backlog.base]]

<!-- generated: do not edit -->
| ID | Title | Parent | Source mode | Status | Testing complexity | Tracker id |
|---|---|---|---|---|---|---|
| [[void-a-printed-label-story\|US-03]] | Void a printed label | [[void-a-label\|FEAT-02]] | A | draft | Medium | — |
| [[export-the-days-labels\|US-07]] | Export the day's labels as a CSV | — | C | draft | Low | — |
<!-- /generated -->
