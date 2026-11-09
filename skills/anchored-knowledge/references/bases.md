# Bases definitions

Copy these into `bases/` in the vault, one `.base` file each. A MOC embeds one with
`![[business-rules.base]]`, which is documented Obsidian syntax; an inline fenced block is not, so
the definitions live in files and the MOCs embed them
([`vault-convention.md`](vault-convention.md) §7).

Needs Obsidian 1.9 or later for `table` and `cards`; `list` needs 1.10. A vault on an older version
still works — it shows the generated snapshot and ignores the embed, which is one reason the snapshot
exists.

Schema reminders, because they are easy to get wrong: top-level keys are `filters`, `formulas`,
`properties`, `summaries` and `views`. A frontmatter property is referenced bare (`status`) or as
`note.status`. `file.hasTag("rule")` matches nested tags such as `#rule/orders`. A comparison is a
YAML string — single-quote it when it contains double quotes. **There is no documented `sort` key**;
order columns with `order`, and group with `groupBy`.

## `bases/business-rules.base`

```yaml
filters:
  and:
    - file.hasTag("rule")
    - 'note.status != "superseded"'
    - 'note.status != "rejected"'
properties:
  note.id:
    displayName: ID
  note.status:
    displayName: Status
  note.topic:
    displayName: Topic
  note.sources:
    displayName: Sources
views:
  - type: table
    name: All rules
    order:
      - note.id
      - file.name
      - note.status
      - note.sources
    groupBy:
      property: note.topic
      direction: ASC
  - type: table
    name: Unconfirmed
    filters:
      or:
        - 'note.status == "draft"'
        - 'note.status == "needs-review"'
    order:
      - note.id
      - file.name
      - note.status
      - note.pending-on
      - note.updated
  - type: table
    name: Deprecated and superseded
    filters:
      or:
        - 'note.status == "out-of-scope"'
        - 'note.status == "superseded"'
    order:
      - note.id
      - file.name
      - note.status
      - note.superseded-by
```

The second view is the audit question "what has been pending too long" as a saved query. The third is
what `deprecate-never-delete` buys you: the record of what was considered and dropped, one click away
and out of the way of the live rules.

## `bases/open-questions.base`

```yaml
filters:
  and:
    - file.hasTag("question")
properties:
  note.needed-by:
    displayName: Needed by
views:
  - type: table
    name: Live
    filters:
      or:
        - 'note.status == "open"'
        - 'note.status == "partial"'
        - 'note.status == "blocked"'
    order:
      - note.id
      - file.name
      - note.owner
      - note.needed-by
      - note.blocks
  - type: table
    name: Overdue
    filters:
      and:
        - 'note.status != "answered"'
        - 'note.status != "dropped"'
        - 'note.needed-by < today()'
    order:
      - note.id
      - file.name
      - note.owner
      - note.needed-by
  - type: table
    name: Answered
    filters:
      - 'note.status == "answered"'
    order:
      - note.id
      - file.name
      - note.answered-by
```

An unowned or undated question cannot close, so it appears in `Live` with empty columns — visible as
a gap rather than hidden as a tidy row.

## `bases/sources.base`

```yaml
filters:
  and:
    - file.hasTag("source")
views:
  - type: table
    name: By authority
    order:
      - note.id
      - file.name
      - note.source-type
      - note.source-date
      - note.citable
    groupBy:
      property: note.authority
      direction: ASC
  - type: table
    name: Meetings
    filters:
      - 'note.source-type == "transcript"'
    order:
      - file.name
      - note.source-date
      - note.participants
```

Grouping by authority answers the audit's hardest question at a glance: a record resting mostly on
levels 5 and 6 is a record nobody has confirmed
([`../principles/authority-is-explicit.md`](../principles/authority-is-explicit.md)).

## `bases/decisions.base`

```yaml
filters:
  and:
    - file.hasTag("decision")
views:
  - type: table
    name: All decisions
    order:
      - note.id
      - file.name
      - note.status
      - note.decided
      - note.summary
  - type: table
    name: Up for review
    filters:
      - 'note.status == "accepted"'
    order:
      - note.id
      - file.name
      - note.decided
      - note.review-when
```

## `bases/scope.base`

```yaml
filters:
  and:
    - file.hasTag("scope")
views:
  - type: table
    name: Boundaries
    order:
      - file.name
      - note.inclusion
      - note.sources
      - note.scope-watch
    groupBy:
      property: note.area
      direction: ASC
```

One view, grouped by area, with `inclusion` as a column: that is the assumptions ledger, and it is
quotable in a scope conversation without anybody maintaining an outline
([`../patterns/scope-boundary-note.md`](../patterns/scope-boundary-note.md)).

## `bases/scope-watch.base` and `bases/changes.base`

```yaml
filters:
  and:
    - file.hasTag("scope-watch")
views:
  - type: table
    name: Open watch items
    filters:
      and:
        - 'note.status != "closed"'
        - 'note.status != "in-scope"'
    order:
      - note.id
      - file.name
      - note.status
      - note.owner
      - note.affects
```

```yaml
filters:
  and:
    - file.hasTag("change")
views:
  - type: table
    name: Recent shifts
    order:
      - note.id
      - file.name
      - note.change-type
      - note.identified
      - note.affects
```

## `bases/glossary.base`

```yaml
filters:
  and:
    - file.hasTag("term")
views:
  - type: table
    name: Terms
    order:
      - note.term
      - note.governed-by
      - note.aliases
    groupBy:
      property: note.category
      direction: ASC
```

Showing `aliases` is deliberate: a retired term lives there, so the column is the list of names the
project has used for one concept, which is the terminology drift the glossary exists to kill.

## `bases/orphans.base`

```yaml
filters:
  and:
    - 'file.inFolder("rules") || file.inFolder("questions") || file.inFolder("decisions")'
    - 'file.backlinks.isEmpty()'
views:
  - type: table
    name: Nothing links here
    order:
      - note.id
      - file.name
      - note.type
      - note.updated
```

`file.backlinks` is documented as performance-heavy, so this one is a health check to open during an
audit rather than a view to embed in a MOC
([`../practices/audit-the-base.md`](../practices/audit-the-base.md)).
