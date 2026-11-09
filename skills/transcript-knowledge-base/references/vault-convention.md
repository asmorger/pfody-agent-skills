# Vault convention

What this skill writes. Everything in the output folder is **generated**: a re-run overwrites it, and
a note that is no longer generated is deleted. That is the opposite of the record vault that
`anchored-knowledge` keeps, where notes are hand-written and promoted — and the difference is the
whole reason this output is evidence rather than record.

If you have `anchored-knowledge` installed, its `references/vault-convention.md` is the canonical
contract for the shared parts: frontmatter as the query surface, wikilinks as the structure, the
callout vocabulary, the MOC's `<!-- generated -->` markers. This file is the part specific to a
transcript index.

## 1. The folder

    <vault_path>/                     default `transcript-knowledge/`
      moc/<title-slug>.md             the index: prose, a Bases embed, a generated table
      items/<statement-slug>.md       one note per knowledge item
      meetings/<date>-<name>.md       one note per meeting that produced a statement
      bases/<title-slug>.base         the Bases definition the MOC embeds
      .tkb-manifest.json              the files this renderer wrote

**Put it in the workbench, never in a record vault.** Point `--out` at a folder that belongs to this
skill. A record vault's notes are hand-written and promoted; this renderer deletes what it no longer
generates, and it cannot tell the difference
([`../anti-patterns/overwriting-a-sibling-index.md`](../anti-patterns/overwriting-a-sibling-index.md)).

Two things make a re-run safe. A note's `created` date is read back from the existing file and kept,
so only `updated` moves. And only files named in `.tkb-manifest.json` are ever deleted — a note you
dropped into the folder yourself survives.

## 2. The item note

Filename is a slug of the statement, truncated at 72 characters on a word boundary. The id lives in
frontmatter with a matching alias, so `[[AUTH-1]]` resolves however the statement is later reworded.

```markdown
---
id: AUTH-1
aliases: [AUTH-1]
type: transcript-item
status: confirmed
category: Authentication
sources: ["[[2026-01-15-alignment]]", "[[2026-02-02-review]]"]
supersedes: []
related: []
citable: false
created: 2026-01-16
updated: 2026-11-08
tags: [transcript-item/authentication]
---

# AUTH-1 — Users authenticate via SSO through Acme ID.

> [!quote] Evidence
> "we go through Acme ID for sign on"
> — Jason, [[2026-01-15-alignment]] 0:12:04

> [!quote] Evidence
> "users authenticate via SSO"
> — Priya, [[2026-02-02-review]] 0:05:11
```

- **`type: transcript-item`, not `business-rule`.** A statement here is what somebody said in a
  meeting, not what the project has agreed. The type is what stops it being cited as record
  ([`../principles/precision-over-volume.md`](../principles/precision-over-volume.md)).
- `citable: false` on every note, for the same reason.
- **The statement is the H1 and appears nowhere else.** The note is frontmatter, one heading and its
  evidence — usually under fifteen lines.
- **Two evidence callouts is the output working**, not a duplicate: one statement, cited to two
  meetings months apart
  ([`../principles/evidence-is-never-discarded.md`](../principles/evidence-is-never-discarded.md)).
- `status` is a property, and anything other than `confirmed` also gets one callout — `[!abstract]`
  for superseded, `[!failure]` for deferred, `[!warning]` otherwise. The statement itself stays clean
  ([`../principles/status-is-a-field-not-a-sentence.md`](../principles/status-is-a-field-not-a-sentence.md)).
- Statuses are this skill's six: `confirmed` · `tentative` · `draft` · `pending` · `deferred` ·
  `superseded`. They are not the record vault's vocabulary; `anchored-knowledge` maps them when it
  reconciles.

## 3. The meeting note

Named for its date, so the folder sorts chronologically: `meetings/2026-01-15-alignment.md`. No id —
`anchored-knowledge` assigns `SRC-NNNN` if and when it promotes the note into the record.

```markdown
---
type: meeting
status: ingested
meeting-date: 2026-01-15
participants: [Jason, Priya]
transcript: transcripts/2026-01-15-alignment.docx
content-hash: 9f2a1c4e7b0d8a63
citable: false
created: 2026-01-16
updated: 2026-11-08
tags: [meeting]
---

# Alignment — 2026-01-15
```

**A meeting note never lists what it produced.** Every statement links to it, so its backlinks are
that list, always current. A meeting gets a note when it produced a statement; a transcript that
yielded nothing is recorded in the state file and needs no note.

## 4. The MOC

Prose, then `![[<title-slug>.base]]`, then a table between `<!-- generated: … -->` and
`<!-- /generated -->`. The whole note is regenerated each run, so the markers are a convention shared
with `anchored-knowledge` rather than a boundary this renderer needs
([`../patterns/vault-notes.md`](../patterns/vault-notes.md)).

The MOC leads with what the index *is*: a supplemental source, not a record. That warning is the most
important line in the output, because everything downstream depends on somebody reading it
([`../principles/a-large-corpus-is-a-superset.md`](../principles/a-large-corpus-is-a-superset.md)).

## 5. The state file is not a second home

`knowledge-index.state.json` holds the items, their sources, the quotes, the timestamps and the
content hashes. The quotes are on the notes *and* in the state, which looks like duplication and is
not: the state is the **merge cache** that makes an incremental run possible, it is regenerable, and
nobody reads it as knowledge. Delete it and the next run reprocesses every transcript
([`../patterns/state-file.md`](../patterns/state-file.md)).
