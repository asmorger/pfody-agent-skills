# Coverage check

**Use when** closing out a Feature. The fixed list of behaviours nobody writes a requirement for and
every agent invents. It lives in the Feature note's frontmatter, as a nested mapping, which is what
makes it checkable.

**Skeleton.** In `backlog/create-and-print-a-label.md`:

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

**Notes.**
- **All seven keys, every time, in this order**, whatever the Feature does. The check reports a
  missing key and a blank value as errors
  ([`../principles/every-coverage-line-is-answered.md`](../principles/every-coverage-line-is-answered.md)).
- Three legal values: requirement wikilinks, `N/A` **plus a reason**, or `Gap:` naming a question
  note. Never blank, never removed.
- `N/A` with no reason is a blank line wearing a label, and the check says so. The reason is the
  record that somebody thought about it
  ([`../anti-patterns/a-blank-coverage-line.md`](../anti-patterns/a-blank-coverage-line.md)).
- `Gap: [[who-may-void-a-printed-label|Q-0003]]` requires the question note to exist with an owner and a needed-by. A dangling gap
  is caught as a dangling wikilink ([`open-question.md`](open-question.md)).
- Filling a line from inference means an `A-xx` source on a new requirement, not a citation
  ([`../principles/implied-is-not-stated.md`](../principles/implied-is-not-stated.md)).
- Two gaps on one Feature is a Feature that is not decomposable yet. Say so rather than slicing
  around it ([`../practices/decompose-a-prd.md`](../practices/decompose-a-prd.md)).

**Related.** [`requirement-note.md`](requirement-note.md), [`coverage-moc.md`](coverage-moc.md),
[`backlog-notes.md`](backlog-notes.md).
