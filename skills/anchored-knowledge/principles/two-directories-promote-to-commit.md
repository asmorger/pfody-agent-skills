# Two directories; promote to commit

**Rule.** Knowledge is captured and drafted in the workbench, and promoted into the vault when it is
approved. Only the vault is committed. The workbench holds intake, the transcript index, proposals
and anything not yet approved; it is never pushed, and it lives **outside the vault** — a sibling
folder, or inside Obsidian's excluded files.

**Why.** The record is shared: the team reads it, stories cite it, agents build from it. Half-finished
notes in that tree get read as knowledge, so a base with no staging area is a base nobody trusts —
and the usual reaction is to stop writing anything down until it is certain, which is how knowledge
gets lost. Two directories let capture be fast and loose while the record stays clean, and promotion
is the single visible moment where a statement stops being a note and starts being something a build
can rely on.

**In the base.**
- `working_dir` → intake, reconciliations, `drafts/`, the transcript index. `docs_dir` → the vault
  ([`../patterns/the-two-trees.md`](../patterns/the-two-trees.md)).
- **Excluding the workbench from the vault is load-bearing, not tidiness.** A draft inside the vault
  appears in search, the graph and every Bases view, indistinguishable from the record — which is
  exactly the trust the staging area exists to protect.
- Commit the shared parts of `.obsidian/`; gitignore `workspace.json`, which is per-person window
  state and conflicts on every pull.
- The vault may share its folder with unrelated project docs. That is fine, because only promoted
  notes are written there.
- Promotion is one-way: write the note into the vault with its id, `sources` and status, close the
  draft, then commit
  ([`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md)).
- Raw sources and the transcript index stay in the workbench permanently. They are evidence, not
  record.

**Breaks when.** Drafts reach the repository →
[`../anti-patterns/committing-the-working-area.md`](../anti-patterns/committing-the-working-area.md).
