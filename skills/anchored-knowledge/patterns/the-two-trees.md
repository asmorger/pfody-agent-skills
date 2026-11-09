# The two trees

**Use when** standing up a base, or working out where a note belongs. One committed vault, one local
workbench. The full folder map is in
[`../references/vault-convention.md`](../references/vault-convention.md) §2.

**Skeleton.** In a git repository, `knowledge_root` and `docs_dir` are both `<repo>/docs/`, and that
folder **is** the Obsidian vault:

    <repo>/docs/                     = the vault; open this in Obsidian
      anchored-knowledge.config.md
      moc/           knowledge.md (home) + one MOC per note type
      rules/         one note per business rule
      glossary/      one note per term
      scope/         one note per in/out boundary
      decisions/     ADRs
      questions/  scope-watch/  changes/  sources/  facts/
      reference/     convention and domain notes — the long-mechanics home
      bases/         the .base definitions the MOCs embed
      .obsidian/     vault settings; gitignore workspace.json

    <repo>/knowledge-working/        = the workbench; never committed
      intake/            fast capture before triage
      reconciliations/   proposals awaiting approval
      drafts/            proposed notes, mirroring the vault's folders
      transcript-knowledge/   the index from transcript-knowledge-base, and its state

Without a repository, `knowledge_root` is `<project>/Knowledge/` and the vault is
`Knowledge/Docs/`. The layout inside the vault is identical either way, so a project workspace
mirrors a development repository.

**Notes.**
- Folders are flat and topic lives in a property. A rule that changes topic is one frontmatter edit,
  not a move that rewrites every link to it
  ([`note-frontmatter.md`](note-frontmatter.md)).
- **Keep the workbench out of the vault** — a sibling folder, or inside Obsidian's excluded files —
  so drafts never surface in search, the graph or a Bases view. A draft that looks like a note is
  worse than no draft ([`../principles/two-directories-promote-to-commit.md`](../principles/two-directories-promote-to-commit.md)).
- Only *promoted* notes are written to the vault, which is why sharing `docs/` with the repo's other
  files is harmless ([`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md)).
- Commit the shared parts of `.obsidian/` — `app.json`, `core-plugins.json`, the Bases settings — so
  the team opens the same vault. Gitignore `workspace.json` and `workspace-mobile.json`: they are
  per-person window state and conflict on every pull.
- All filenames kebab-case, and the config's file map wins wherever an existing vault differs
  ([`../principles/match-the-projects-voice.md`](../principles/match-the-projects-voice.md)).

**Related.** [`knowledge-config.md`](knowledge-config.md), [`start-note.md`](start-note.md),
[`../practices/bootstrap-a-base.md`](../practices/bootstrap-a-base.md).
