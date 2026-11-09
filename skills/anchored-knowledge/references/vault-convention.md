# Vault convention

The output contract for this skill: what a note looks like, what its frontmatter must carry, how
notes link, and how an index note stays true. Every pattern in `patterns/` is one instance of this
contract. A project that already has an Obsidian vault keeps its own conventions and records them in
the config; this file is what the skill proposes when there is nothing to adopt
([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).

## 1. One note, one fact, one id

The record is a graph of small notes, not a set of documents. Each business rule, glossary term,
scope boundary, decision, question, scope-watch item, change and source is **its own note**, named
for what it says, carrying a stable id in its frontmatter.

- **Body budget: 25 lines.** A statement, the links that give it meaning, and a callout when the
  reader must see something. Decision notes may run to 120 lines because the reasoning is the point;
  reference notes are the designated home for long mechanics and are unbounded.
- A note that needs a second `##` heading is two notes, except in a decision or reference note.
- Nothing is copied between notes. A link resolves to whatever the other note says now; a copy goes
  stale silently ([`../principles/one-home-per-fact.md`](../principles/one-home-per-fact.md)).

## 2. Folder map

The vault **is** the record. Open `docs_dir` in Obsidian.

    <repo>/docs/                        the vault — record of source of truth
      anchored-knowledge.config.md      the per-project config
      moc/
        knowledge.md                    the home note; where a newcomer starts
        business-rules.md  glossary.md  scope.md  decisions.md
        open-questions.md  scope-watch.md  changes.md  sources.md
      rules/<kebab-title>.md            business rules, flat, topic as a property
      glossary/<kebab-term>.md
      scope/<kebab-boundary>.md         one note per in/out boundary statement
      decisions/<kebab-title>.md        ADRs
      questions/<kebab-title>.md
      scope-watch/<kebab-title>.md
      changes/<kebab-title>.md
      sources/<kebab-name>.md           one note per registered source, meetings included
      facts/<kebab-title>.md            optional K- notes
      reference/<topic>.md              convention and domain reference notes
      narrative/<topic>.md              derived reading surfaces; they own no facts
      bases/<name>.base                 the Bases definitions the MOCs embed

    <repo>/knowledge-working/           the workbench — never committed, outside the vault
      intake/<date>-<slug>.md
      reconciliations/<date>-<source>.md
      drafts/                           proposed notes, mirroring the vault's folders
      transcript-knowledge/             the transcript index and its state file

Folders are flat on purpose. Topic lives in a property, so a rule that changes topic is one
frontmatter edit rather than a move that rewrites every link to it.

Without a repository, `knowledge_root` is `Knowledge/` and the vault is `Knowledge/Docs/`; the layout
inside it is identical. Keep the workbench outside the vault, or add it to Obsidian's excluded files
so drafts never appear in search or the graph
([`../principles/two-directories-promote-to-commit.md`](../principles/two-directories-promote-to-commit.md)).

`.obsidian/` holds vault settings. Commit `.obsidian/app.json`, `core-plugins.json` and anything the
team shares; gitignore `.obsidian/workspace.json` and `workspace-mobile.json`, which are per-person
window state and conflict on every pull.

## 3. Note naming

| Part | Form | Example |
|---|---|---|
| Filename | kebab-case title, no id | `rules/order-address-frozen-on-confirmation.md` |
| `id` | the immutable citable id | `ORDER-1` |
| `aliases` | the id, for autocomplete and search — **not** for resolving a link | `[ORDER-1]` |
| H1 | `# <ID> — <Title>` | `# ORDER-1 — Order address frozen on confirmation` |

The **id** never changes. The **title and filename may** — rewording a title is an improvement, and
Obsidian rewrites every link to it. That split is the whole reason the id lives in frontmatter rather
than in the filename ([`../principles/ids-are-immutable.md`](../principles/ids-are-immutable.md)).

**Filenames are vault-unique, because the filename is the link target.** Two notes with one
basename — `rules/credit-hold-blocks-labelling.md` and `decisions/credit-hold-blocks-labelling.md` —
make the same link text resolve differently depending on which note it is written in, and under §6
one of the two becomes uncitable outright. The lint reports it.

A project already numbering its files — `adr/0004-credit-hold-blocks-labelling.md` — keeps that form.
The config's file map wins.

## 4. Frontmatter

Properties are the query surface. Bases and the audit read them; the prose does not restate them
([`../principles/properties-are-the-query-surface.md`](../principles/properties-are-the-query-surface.md)).

Every note carries:

```yaml
---
id: ORDER-1                 # omit on MOC and reference notes
aliases: [ORDER-1]          # omit where there is no id
type: business-rule         # closed vocabulary, §5
status: confirmed           # closed vocabulary per type, §5
created: 2026-10-02
updated: 2026-11-08
tags: [rule/orders]         # <type-tag>/<topic>, derived from type and topic
---
```

Wikilinks in a property are Link objects to Obsidian, so they give backlinks and graph edges. Quote
them, or YAML reads `[[` as a nested sequence: `sources: ["[[order-fulfilment-sow-v3]]"]`.

`tags` duplicates `type` and `topic` by design — it is the one sanctioned redundancy, because the tag
pane and `file.hasTag()` are worth it. **The properties are authoritative**; the tag is derived from
them and never carries anything else. Status is never a tag: it changes, and a stale tag beside a
current property is two answers to one question.

### Per-type properties

| type | adds |
|---|---|
| `business-rule` | `topic`, `sources[]`, `authority`, `confirmed`, `pending-on`, `questions[]`, `decisions[]`, `supersedes[]`, `superseded-by` |
| `glossary-term` | `term`, `category`, `governed-by[]`; retired aliases go in `aliases` so old names still resolve |
| `scope-boundary` | `area`, `inclusion` (`included` \| `not-included`), `sources[]`, `authority`, `scope-watch[]` |
| `decision` | `summary`, `decided`, `deciders[]`, `confidence`, `rules[]`, `supersedes[]`, `superseded-by` |
| `open-question` | `owner`, `needed-by`, `blocks[]`, `answered-by[]`, `sources[]` |
| `scope-watch` | `owner`, `baseline[]`, `requested[]`, `affects[]`, `disposition` |
| `knowledge-change` | `change-type`, `identified`, `older[]`, `newer[]`, `affects[]` |
| `source` | `source-type`, `authority`, `provider`, `location`, `source-date`, `citable`; a meeting adds `participants[]` |
| `fact` | `topic`, `applies-to`, `confidence`, `sources[]` |
| `reference` | `topic`, `governs[]` — no `id`, cited as `[[api-conventions]]` |
| `moc` | `snapshot` (§7) — no `id`, no `status` |
| `narrative` | `derived-from[]`, `covers-through`, `input-manifest-sha256` — no `id`; never cited ([`../patterns/narrative-note.md`](../patterns/narrative-note.md)) |

**A source note never lists what it updated.** Each rule names its source; the source note's
backlinks are the list, always current. That is the Source Register's Notes column, replaced by
something that cannot go stale ([`../patterns/source-note.md`](../patterns/source-note.md)).

## 5. Vocabularies

Closed sets. The audit checks membership, so a value outside these is a finding.

    type          business-rule · glossary-term · scope-boundary · decision · open-question
                  scope-watch · knowledge-change · source · fact · reference · moc · narrative
                  intake · reconciliation            (workbench only)

    status        business-rule, fact, scope-boundary
                      draft · confirmed · needs-review · superseded · out-of-scope · rejected
                  decision
                      proposed · accepted · superseded · deprecated · rejected
                  open-question
                      open · partial · answered · blocked · dropped
                  scope-watch
                      watch · clarify · in-scope · deferred · change-request · closed
                  knowledge-change
                      proposed · accepted · needs-review · closed
                  source
                      registered · stale · superseded
                  narrative
                      draft · current · stale

    authority     1-contractual · 2-approved-requirements · 3-client-clarification
                  4-source-artifact · 5-internal-interpretation · 6-unreviewed-intake

    tag prefix    rule/ · term/ · scope/ · decision · question · scope-watch · change
                  source/ · fact/ · reference/ · moc

The authority values are the default ladder, overridable per project
([`../patterns/authority-ladder.md`](../patterns/authority-ladder.md)).

## 6. Links and callouts

**Every reference is a wikilink, and its target is always a filename.** Obsidian resolves a wikilink
against filenames and paths — **never through `aliases`**. A bare `[[ORDER-1]]` therefore resolves
to nothing: clicking it offers to create a new empty note. The `aliases` entry powers autocomplete
and search, and nothing else. (Pick an alias from Obsidian's own autocomplete and watch what it
inserts:
`[[order-address-frozen-on-confirmation|ORDER-1]]`. That is this convention.)

So one citable form, everywhere:

    [[order-address-frozen-on-confirmation|ORDER-1]]        a rule, cited by id
    [[order-address-frozen-on-confirmation|the address freeze]]   when the sentence needs the words
    [[api-conventions]]                                     a reference note, which has no id
    ![[one-label-per-parcel]]                               an embed; it takes no display text
    | [[one-label-per-parcel\|LABEL-1]] |                    inside a table, the pipe is escaped

Never a relative path, never a copied sentence, and never the bare id.

- A wikilink that resolves to nothing is a finding, not a placeholder. The record is cited by builds
  ([`../anti-patterns/a-dangling-citation.md`](../anti-patterns/a-dangling-citation.md)).
- **Display text shaped like an id must be that note's id.** `[[one-label-per-order|LABEL-9]]` opens
  the right note under a wrong name, so the link works and the citation lies. The lint compares them.
- A `#heading` or `#^block` must exist in the target. The lint checks both.
- Every note is reachable from the home note in one or more hops, and has at least one inbound link.
  An unreachable note is knowledge nobody will find
  ([`../anti-patterns/an-orphan-note.md`](../anti-patterns/an-orphan-note.md)).

Status lives in frontmatter. A **callout** appears only when a reader must see something the
statement itself does not say — and never to restate the status property.

    > [!warning] Draft — pending <stakeholder>, as of YYYY-MM-DD
    > What would close it, and the question it waits on.

    > [!todo] Needs review — inherited, source unknown
    > What is being checked and by whom.

    > [!abstract] Superseded by [[one-label-per-consignment|LABEL-5]] — YYYY-MM-DD
    > The earlier understanding, with the anchor it rested on.

    > [!failure] Out of scope — Phase 1
    > What was considered, and where it was deferred to.

    > [!question] Open
    > The part of this statement nobody has settled. See [[who-may-void-a-printed-label|Q-0003]].

    > [!quote] Evidence
    > "the words somebody actually said"
    > — Speaker, [[2026-01-21-order-fulfilment-scope-call]] 00:14:22

A confirmed rule needs no callout at all: `status`, `confirmed` and `sources` already say it. That is
what keeps a rule note twelve lines long
([`../patterns/status-callouts.md`](../patterns/status-callouts.md)).

## 7. MOCs: a live query over a generated snapshot

An index note holds no knowledge. It holds an embedded Bases view, which cannot drift, and beneath it
a generated table, which can be read without Obsidian — by a developer on GitHub, by an agent, in a
diff. Both are derived; the notes are the record.

```markdown
---
type: moc
updated: 2026-11-08
snapshot:
  type: business-rule
  columns: [id, status, topic, sources]
  exclude-status: [superseded, rejected]
  group-by: topic
tags: [moc]
---

# Business Rules

What this system does, as agreed. Rules are notes in `rules/`; this note indexes them.

![[business-rules.base]]

<!-- generated: do not edit · 2026-11-08 -->
### Orders

| ID | Rule | Status | Sources |
|---|---|---|---|
| [[order-address-frozen-on-confirmation|ORDER-1]] | Order address frozen on confirmation | confirmed | [[order-fulfilment-sow-v3]] |
<!-- /generated -->
```

- The `snapshot` property is the generator's input; the markers are its output boundary. Everything
  between them is overwritten, and nothing else in the note is touched
  ([`../practices/regenerate-the-mocs.md`](../practices/regenerate-the-mocs.md)).
- Edit a note to change the table. Editing between the markers is a change that the next
  regeneration silently discards
  ([`../anti-patterns/a-generated-table-edited-by-hand.md`](../anti-patterns/a-generated-table-edited-by-hand.md)).
- Prose above the embed is welcome and is not generated — that is where a MOC earns its place.

The `.base` files live in `bases/` and are embedded, not inlined: `![[name.base]]` is documented
syntax, and one definition serves every note that embeds it. The definitions are in
[`bases.md`](bases.md).

## 8. What this convention does not change

The two layers, the authority ladder, propose-then-apply, deprecate-never-delete, delegation of
transcripts, and every id rule survive intact. The vault changes the **shape** of the record, not its
discipline. A note is still promoted, never drafted in place; a superseded rule still keeps its id
and its note; a transcript is still indexed by `transcript-knowledge-base` rather than read by hand.
