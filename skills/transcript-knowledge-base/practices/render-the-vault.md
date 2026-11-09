# Render the vault

**When** the merge is done. Step 4 — it writes the deliverable.

**Why.** Render is pure output: it reads the state and writes the notes. Keeping it separate is why a
bad extraction can be fixed and re-rendered without touching a note by hand.

**Steps.**

1. **Run it:**

       python -m tkb.cli render --out ./transcript-knowledge --state knowledge-index.state.json

2. **Point `--out` at a folder that belongs to this skill**, in the workbench. Every note in it is
   generated, and a note that is no longer generated is deleted on the next run — so a record vault
   is the one place it must never point
   ([`../anti-patterns/overwriting-a-sibling-index.md`](../anti-patterns/overwriting-a-sibling-index.md)).
3. **Pass `--config`** when the paths, title, intro or category order are not the defaults
   ([`../patterns/tool-config.md`](../patterns/tool-config.md)).
4. **Read the result.** `items/` one note per statement with its evidence callouts, `meetings/` one
   note per meeting that produced something, `moc/` the index with its Bases embed and generated
   table ([`../patterns/vault-notes.md`](../patterns/vault-notes.md)).
5. **Read the counts the command prints**: items, meetings, files written, files removed. A removal
   count above zero on a run that added nothing means a statement was reworded and its old note was
   cleaned up — expected, and worth saying.
6. **Check the state file sits where the config says.** It holds the content hashes that make the
   next run incremental, and it is what the notes are regenerated from
   ([`../patterns/state-file.md`](../patterns/state-file.md)).
7. **Say what it is.** On a small corpus it is a usable index. On a large one it is a sourced superset
   to curate, and that must be said rather than implied
   ([`../principles/a-large-corpus-is-a-superset.md`](../principles/a-large-corpus-is-a-superset.md)).
8. **Say that it is not record.** Nothing here may be cited by a story, a spec or a test until it has
   been reconciled into the project's knowledge base. The MOC says so; say it in the report too
   ([`../anti-patterns/the-generated-index-shipped-as-finished.md`](../anti-patterns/the-generated-index-shipped-as-finished.md)).
9. **Re-render freely.** It is idempotent — a second run with no changes writes nothing — so a
   wording or config change is one command, never an edit to a note
   ([`../anti-patterns/editing-a-generated-note.md`](../anti-patterns/editing-a-generated-note.md)).

**Done when** the vault exists at the configured path with its state file, the counts are reported,
and the user has been told both whether they are holding a finished index or a superset to curate,
and that it is evidence rather than record.
