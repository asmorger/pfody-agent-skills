# Verify the quotes

**When** step 4 has written the vault, before you report a run as finished, and again after any
re-extraction. Every run, not only the ones you doubt — an extraction that looks right is exactly
the one worth checking ([`../principles/a-quote-is-checked-not-trusted.md`](../principles/a-quote-is-checked-not-trusted.md)).

**Why.** Steps 1–4 guarantee that the vault is well formed. They guarantee nothing about whether the
words in it were said. This is the step that reads the transcripts again and compares.

**Steps.**

1. Run it against the same folder the vault was built from:

       python -m tkb.cli verify --vault <vault-dir> --folder <transcript-dir> --state <state.json>

   Exit status 1 means there are problems. The JSON carries `quotes_checked`, `problems` and
   `unchecked`.

2. **Read each problem as a statement about the extraction, not about the tool.**

   | Problem | What it means | Fix |
   |---|---|---|
   | `cue … is not in` | the timestamp was copied wrong, or from the wrong brief | re-extract that item from the right turn |
   | `is <name>, but the note cites <other>` | the turn belongs to someone else | take the speaker from the brief's turn header, never from nearby prose |
   | `not in … at <cue>` | the words are not in that turn — a paraphrase, a smoothing, or an invention | copy the words from the brief verbatim, or drop the item |
   | `cites [[…]], which is not an indexed meeting` | the item names a meeting no transcript produced | fix the `meeting`/`date` pair so it matches the ingested file |
   | `cannot read the transcript` | the file moved, or its format has no parser | point `--folder` at the real folder |
   | `register:` | a bracketed correction has no row, or a registered correction is missing from a quote | [`../patterns/errata-register.md`](../patterns/errata-register.md) |

3. **Fix by re-extracting**, never by editing the note: every note is regenerated, so an edit is
   discarded on the next render
   ([`../anti-patterns/editing-a-generated-note.md`](../anti-patterns/editing-a-generated-note.md)).
   Correct `items.json`, re-run `merge` and `render`, then verify again.

4. **Report `unchecked` honestly.** These are quotations with no cue to check them against. They are
   not failures and not passes; they are the part of the output nothing verified. Say the number.

**Done when** `verify` exits 0, every problem was fixed by re-extraction rather than by editing
output or loosening a quote, and your report gives `quotes_checked` and the `unchecked` count beside
the item and meeting counts.
