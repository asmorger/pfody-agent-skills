# Locate the base

**When** at the start of every run, before anything is read, drafted or written. There is no run that
skips this.

**Why.** Every path, filename and id scheme in this skill differs per project, and a wrong guess
writes a second knowledge base beside the real one — two rule files, two id schemes, no source of
record.

**Steps.**

1. **Look for the config**, first found wins: `docs/anchored-knowledge.config.md`, then
   `Knowledge/…`, then `.claude/…`. Found → validate (step 6) and go straight to the requested
   operation.
2. **No config: discover the base.** Look for an existing vault first — a `.obsidian/` folder is the
   strongest signal there is, and its location decides everything downstream. Otherwise scan for a
   `Knowledge/Docs/`, `docs/` or `Knowledge/` folder and for files named like `business-rules*.md`,
   `open-questions*.md`, `decisions*.md` or `adr/`, `source-register*.md`, `glossary*.md`,
   `assumptions*.md`, `*-conventions.md`, `bits of knowledge*.md`.
3. **Propose both locations and let the user confirm.** In a git repository (`git rev-parse
   --show-toplevel`): `knowledge_root` and `docs_dir` are both `<repo>/docs/`, which becomes the
   vault, and `working_dir` is `<repo>/knowledge-working/`, outside it. Without one:
   `<project>/Knowledge/` with `Knowledge/Docs/` as the vault, and the workbench alongside
   ([`../patterns/the-two-trees.md`](../patterns/the-two-trees.md)). **Never guess silently.**
   Where a vault already exists, its root wins and the workbench goes outside it.
4. **If git-managed**, record `git_managed: true` and the host, and do all git through the `git-guide`
   skill from here on
   ([`../principles/git-goes-through-git-guide.md`](../principles/git-goes-through-git-guide.md)).
   Get the latest before reading.
5. **Provision the config** from
   [`../references/knowledge-config.template.md`](../references/knowledge-config.template.md), filling
   in what you discovered. Ask about what discovery cannot settle: the location, the SOW's name and
   location, the id and ADR conventions, the transcripts folder, and — for a vault — whether Bases is
   available and which link style the project writes
   ([`../references/vault-convention.md`](../references/vault-convention.md)).
6. **Validate on load.** Check that the paths the config names still exist. A renamed or moved folder
   is flagged to the user — offer to update the config — never silently cited as nothing.
7. **Adopt existing names** into the file map, verbatim
   ([`adopt-an-existing-base.md`](adopt-an-existing-base.md)).
8. **Continue with the original request in the same turn.** Intake is a means, not the deliverable.

**Done when** the config exists, its paths resolve, the user confirmed any location you proposed, and
the thing they actually asked for is underway.
