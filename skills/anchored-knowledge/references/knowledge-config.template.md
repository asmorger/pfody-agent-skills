# anchored-knowledge — Project Knowledge Config

```
config_version: 2
```

Saved per project at `Knowledge/anchored-knowledge.config.md` (default) or
`.claude/anchored-knowledge.config.md` (fallback). The skill provisions this file on
first run via discovery-assisted intake — you normally don't create it by hand, but you
can edit it anytime. Everything the `anchored-knowledge` skill needs to adapt to *this*
project lives here, so the skill never has to guess where the knowledge base is, what it
is called, or which ID conventions are in force. To regenerate from scratch, tell the
skill to "reconfigure."

Leave a field blank or `None` when it genuinely does not apply — a blank field changes
behavior (the skill asks, or drops a step), it does not make the skill guess silently.

---

## 1. Knowledge base location
Knowledge lives in **two directories**: a committed source of record (`knowledge_root`, whose
`docs_dir` is the Obsidian vault) and a local workbench (`working_dir`) for knowledge not yet
ready for the repo. **The workbench lives outside the vault** — a sibling folder, or inside
Obsidian's excluded files — because a draft inside the vault appears in search, the graph and
every Bases view, indistinguishable from the record.

- **`docs_dir` — the vault.** Open this folder in Obsidian. It holds every note: the Reference
  Layer (`rules/`, `glossary/`, `scope/`, `decisions/`, `facts/`, `reference/`), the Governance
  Layer (`sources/`, `questions/`, `scope-watch/`, `changes/`), the index notes (`moc/`) and the
  Bases definitions (`bases/`). No repo: `<project>/Knowledge/Docs/`. In a git repo:
  `<repo>/docs/`, the same folder as `knowledge_root`. The layout inside is identical either way.

- **`knowledge_root` — committed source of record.** In a git repo, **`<repo>/docs/`**. Without a
  repo, `<project>/Knowledge/`. This is the only tree that gets committed. `docs/` may also hold
  unrelated files — that is fine, because only *promoted* (confirmed) knowledge is committed here,
  never half-finished notes (those stay in `working_dir`).
- **`working_dir` — the workbench (never committed).** Local staging for intake, reconciliations,
  the transcript index, and drafts that are not yet promoted. Default `<repo>/knowledge-working/`
  (or `<project>/Knowledge/` without a repo). If it sits inside the repo it must be **gitignored**,
  and either way it stays **outside the vault**.

The skill detects whether you are in a git repo — and looks for an existing `.obsidian/` folder,
which is the strongest signal there is — then proposes both defaults and asks the user to confirm
before writing anything.

```
knowledge_root:            # e.g. docs/ (repo, preferred)  |  Knowledge/ (no repo)
docs_dir:                  # e.g. docs/ (repo)  |  Knowledge/Docs/ (no repo); Reference Layer files
working_dir:               # e.g. Knowledge/  — local staging; NEVER committed (gitignore if inside the repo)
storage_mode:  repo-docs | project-knowledge
created_new:  true | false # true if the skill scaffolded it; false if an existing base was adopted

# --- git (fill when knowledge_root is inside a repo) ---
git_managed:  true | false # true => sync via the git-guide skill; never run raw git
git_host:                  # azure-devops | github | none  (from the repo remote)
git_repo_root:             # absolute path from `git rev-parse --show-toplevel`
working_dir_gitignored:  true | false   # true once working_dir is added to .gitignore (when it lives inside the repo)
obsidian_settings_committed:  true | false  # commit .obsidian/app.json etc; always gitignore workspace.json
```

**Promotion:** knowledge is drafted in `working_dir`, and once approved it is *promoted* into
`knowledge_root` and (when `git_managed: true`) committed via the **git-guide** skill — "get the
latest" before editing, "save" then "publish/share" after promoting. `working_dir` is never
pushed.

## 2. Vault layout
Where notes live and how they are written. Folders are flat and topic lives in a property, so a
rule that changes topic is one frontmatter edit rather than a move that rewrites every link to it.
**If a vault already exists, record its real folders, property names and tags here** — the skill
uses them verbatim and renames nothing unless you ask. Renaming a property silently empties every
Bases view and template the team already had.

```
vault:          true | false      # false => the skill asks before converting a document-shaped base
link_style:     wikilink          # wikilink | markdown  (an existing vault's style wins)
query_engine:   bases             # bases (Obsidian 1.9+) | dataview | none
snapshot:       true | false      # generated tables beneath each embed; keep true for non-Obsidian readers
home_note:      moc/knowledge.md

# Folders under docs_dir — the Reference Layer (only these may be cited downstream)
rules:          rules/            # one note per business rule
glossary:       glossary/         # one note per term
scope:          scope/            # one note per in/out boundary statement
decisions:      decisions/        # ADRs, one note each
facts:          facts/            # optional K-NNNN notes
reference:      reference/        # convention and domain notes — the long-mechanics home

# Folders under docs_dir — the Governance Layer (not citable as record)
sources:        sources/          # one note per registered source, meetings included
questions:      questions/
scope_watch:    scope-watch/
changes:        changes/

# Index notes and queries
moc:            moc/              # one MOC per note type, plus the home note
bases:          bases/            # the .base definitions the MOCs embed

# Property names — change only to match an existing vault
prop_id:        id
prop_status:    status
prop_type:      type
prop_sources:   sources
prop_authority: authority

# Working files — under working_dir, NEVER committed, OUTSIDE the vault
intake_dir:     intake/
reconciliations_dir:  reconciliations/
drafts_dir:     drafts/
# transcript_index (working_dir) is set in §5
```

## 3. SOW / scope baseline
The Statement of Work (or equivalent top-authority scope artifact) anchors the whole
authority ladder. **If the skill cannot find it, it asks the user where it is and what it
is called**, then records the answer here. On an internal project with no SOW, set
`sow_present: false` and name whatever serves as the scope baseline instead.

```
sow_present:   true | false
sow_name:                    # exact document title, e.g. "<Client> <Project> SOW v3"
sow_location:                # path or link, e.g. ../SOW/<project>-sow-v3.docx
scope_baseline_note:         # if sow_present is false, what is the top-authority scope source?
```

## 4. ID & ADR conventions
How rules and decisions are referenced. **If existing docs already use IDs, the skill
detects the pattern and records it here; if it cannot reconcile the scheme, it asks the
user to confirm it** before writing any new IDs.

```
rule_id_prefixes:            # per-topic uppercase prefixes, e.g. AUTH, USER, ORDER — or "emerge" to derive per topic; one unique prefix per topic
topics:                      # the topic values, matching the prefixes, e.g. auth, user, orders
note_naming:   title-with-id-alias   # filename is the kebab title; the id lives in frontmatter with a matching alias
adr_convention:  ADR-NNNN    # ID format for decision records
adr_filename:    kebab-title.md      # or NNNN-kebab-title.md where a project already numbers its files
id_rule: "IDs are immutable, never reused, never deleted — deprecate in place, never delete a note. A title may be reworded freely; the ID may not. Any ID cited downstream must resolve to a real note."
```

## 5. Transcript ingestion (delegated)
This skill does **not** parse transcripts itself. Meeting/call transcripts are handled by
the `transcript-knowledge-base` skill, which emits a sourced, incremental index that this
skill treats as a **supplemental source** and reconciles into the Reference Layer.

```
transcripts_present:   true | false
transcripts_folder:                    # folder of raw transcripts handed to transcript-knowledge-base
transcript_index:      transcript-knowledge/transcript-knowledge.md   # (working_dir) output the transcript skill renders — MUST be in the workbench, never in the vault
meeting_notes:         true      # write one source note per meeting in sources/, named YYYY-MM-DD-<kebab>
```

## 6. Authority ladder
Strongest → weakest. Default suits a client-services engagement; adjust for internal
projects. The skill prefers higher authority, records conflicts, and never resolves them
silently.

```
authority_levels:
  1: Contractual baseline (SOW, signed change request)
  2: Approved requirements (accepted requirements / stories / AC)
  3: Client clarification (named stakeholder answer, approved Q&A, meeting decision)
  4: Source artifact (spreadsheet, sample file, export, current-system behavior)
  5: Internal interpretation (team analysis, inferred rule)
  6: Unreviewed intake (draft note, brainstorm, uncited memory)
```

## 7. Review cadence & ownership
```
knowledge_owner:             # person/role accountable for the base
review_cadence:              # e.g. weekly during discovery; on-change during implementation; audit at handoff
```

---

### How the skill uses this file
- No `docs_dir` set ⇒ the skill looks for an existing `.obsidian/` folder first, then for a folder holding knowledge files. If none exists, it proposes `<project>/Knowledge/Docs/` (no repo) or `<repo>/docs/` (repo).
- `query_engine: none` ⇒ the MOCs carry the generated snapshot alone, with no embed. Still readable everywhere, and the snapshot is regenerated by `scripts/vault.py moc`.
- `link_style: markdown` ⇒ relative markdown links instead of wikilinks, for a vault that already writes them. Backlinks and the graph still work; `[[ID]]` shorthand does not.
- `vault: false` ⇒ an adopted base is still document-shaped. The skill proposes the conversion and its shape, and waits — a document-to-notes split is a large diff.
- No `knowledge_root` found ⇒ the skill proposes `<repo>/docs/` in a git repo (or `<project>/Knowledge/` otherwise) and records the confirmed choice. `docs/` may hold other files; only promoted knowledge is committed there.
- `working_dir` ⇒ intake, the transcript index, and drafts live here and are **never committed**; if it's inside the repo it must be gitignored.
- **Promotion** ⇒ approved entries move from `working_dir` into `knowledge_root`; only `knowledge_root` is committed.
- `git_managed: true` ⇒ the skill syncs through the **git-guide** skill (get-latest before editing; save/publish after promoting) and never runs raw git.
- Existing folders, filenames or property names differ from the defaults in §2 ⇒ the recorded names win; nothing is renamed silently, because a renamed property empties every Bases view the team had.
- `sow_present: false` ⇒ the skill never invokes "the SOW"; it uses `scope_baseline_note` as the top authority.
- `rule_id_prefixes` unresolved ⇒ the skill asks the user to confirm the scheme before minting IDs.
- `transcripts_present: true` ⇒ transcript intake is delegated to `transcript-knowledge-base`; its index stays in the workbench, and each **meeting** gets a source note in `sources/` so a rule can cite the meeting it came from.
- Every run ends with `scripts/vault.py lint` and `scripts/vault.py moc`: the lint reports dangling wikilinks, orphans, vocabulary violations, unanchored confirmed notes, oversized notes and duplicate IDs; `moc` refreshes the generated snapshots.
