# One name and one id per level

**Rule.** Four levels, four names, four id formats, no synonyms.

| Level | Id | What it is |
|---|---|---|
| Epic | `EPIC-01` | A business outcome needing one or more Features |
| Feature | `FEAT-01` | One capability: one job for one role |
| User Story | `US-01` | A vertical slice of one Feature: one person builds, tests and demos it in one sprint |
| Acceptance criterion | `AC-1` | One Given/When/Then test; numbering restarts in each story |

A story always takes a `US-01` id, in every mode, because it identifies the work item rather than a
source. **Epic and Feature ids are copied from the source, never created, merged or renamed** — a
person owns those decisions. Where the source has none, leave them out of the tags and name any parent
the user gave in `Details`.

**Why.** "Epic", "feature" and "initiative" mean different things at every company, and the level
decides which tracker item gets created and what gets a parent. Inventing a parent is the costlier
half: it looks like a decision somebody made about how the work is organised, and the tracker then
carries a hierarchy nobody agreed to.

**In the story.**
- Take the next free `US-` number from the current backlog. Never reuse one. If you cannot find the
  current numbers, start at `US-01` and add an Assumption that a person must confirm they are free.
- A tracker number is a separate value and does not replace these ids
  ([`../patterns/tracker-field-map.md`](../patterns/tracker-field-map.md)).
- The level id opens the tracker title, so an item traces back in one lookup
  ([`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)).

**Breaks when.** A parent id is invented or renamed →
[`../anti-patterns/an-invented-parent-id.md`](../anti-patterns/an-invented-parent-id.md).
