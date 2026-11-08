# The two trees

**Use when** standing up a base, or working out where a file belongs. One committed record, one local
working area.

**Skeleton.** Without a repository — `knowledge_root` is `Knowledge/`, `docs_dir` is `Knowledge/Docs/`:

    Knowledge/                       = knowledge_root   (governance layer + config)
      anchored-knowledge.config.md
      knowledge-index.md
      source-register.md
      open-questions.md
      scope-watch.md
      knowledge-change-log.md
      Docs/                          = docs_dir   (Reference Layer; mirrors a repo's docs/)
        business-rules.md
        glossary.md
        assumptions.md
        <topic>-conventions.md       api / build / sql / test, as needed
        <topic>.md                   auth, data mapping, environments, as needed
        adr/
          INDEX.md
          0001-<kebab-title>.md
        <supporting-folder>/         optional, supplemental only (meetings/, examples/)

In a git repository, `knowledge_root` and `docs_dir` are both `<repo>/docs/` and the same files sit
together there, beside whatever else the repo keeps in `docs/`.

    <working_dir>/                   local, uncommitted, gitignored if inside the repo
      knowledge-intake.md            fast capture before triage
      transcript-knowledge.md        the index from transcript-knowledge-base
      drafts/                        proposed rules, ADRs and entries pending approval

**Notes.**
- The Docs folder has the same layout either way, so a project workspace's `Knowledge/Docs/` mirrors a
  development repository's `docs/`.
- Only *promoted* knowledge is written to the record, which is why sharing `docs/` with unrelated
  files is harmless ([`../principles/two-directories-promote-to-commit.md`](../principles/two-directories-promote-to-commit.md)).
- Without a repository the working area may be the same folder as the record; keep drafts in
  `drafts/`.
- All filenames kebab-case, and the config's file map wins wherever an existing base differs.

**Related.** [`knowledge-config.md`](knowledge-config.md),
[`../practices/bootstrap-a-base.md`](../practices/bootstrap-a-base.md),
[`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md).
