# Prepare the briefs

**When** at the start of every run — the first one and every one after. Step 1.

**Why.** `prepare` is the incremental engine. It is what makes re-running cheap, which is what makes
the index stay current rather than being a one-off document that ages.

**Steps.**

1. **Run it against the transcripts folder:**

       python -m tkb.cli prepare --folder "<transcripts folder>" --state knowledge-index.state.json

2. **Read what it printed**: the list of new or changed transcripts to process, and the path to the
   manifest. Unchanged files are skipped — that is the incremental behaviour, and it is why this same
   command is both initial and incremental
   ([`run-an-incremental-update.md`](run-an-incremental-update.md)).
3. **Note the manifest path.** Its `files[]` carries each file's `hash`, name, meeting and date, and
   you will copy those into `items.json`
   ([`../principles/the-content-hash-is-the-unit-of-work.md`](../principles/the-content-hash-is-the-unit-of-work.md)).
4. **Pass `--config` if the paths are not the defaults.** A run driven by another skill always needs
   this ([`../patterns/tool-config.md`](../patterns/tool-config.md)).
5. **Check for files marked `error`** in the manifest. Malformed or unsupported files are reported and
   the rest still process; do not fill in an errored file's items
   ([`diagnose-a-failed-run.md`](diagnose-a-failed-run.md)).
6. **Nothing to process** is a valid result. It means every transcript is already in the index; say so
   rather than re-extracting.

**Done when** the briefs exist in the work directory, you have the manifest path and the list of files
to process, and any errored file has been reported rather than worked around.

**Related.** [`../patterns/transcript-brief.md`](../patterns/transcript-brief.md).
