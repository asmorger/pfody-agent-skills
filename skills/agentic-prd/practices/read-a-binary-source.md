# Read a binary source

**When** a source is `.docx`, `.pdf`, `.vtt` or `.srt` and must be read before it can be cited.

**Why.** A source that cannot be read is a source that gets summarised from its filename. Extraction
also produces the text copy the locator check needs, so the citations in the PRD become verifiable
rather than asserted.

**Steps.**

1. **Extract to a directory**, not to the terminal:

       python <skill-folder>/scripts/extract_text.py <file> --out <dir>

2. **Use the full path to the script.** The PRD and its sources are usually in other folders.
3. **Install the PDF dependency if it is missing.** PDF extraction needs `pypdf` or `pymupdf`;
   everything else is the standard library. If neither can be installed, say so — do not summarise an
   unread PDF.
4. **Read the extracted text whole**, especially a transcript. The reversal of an earlier decision is
   the thing a skim misses, and it is usually the most consequential sentence in the file
   ([`../principles/a-conflict-is-recorded-not-resolved.md`](../principles/a-conflict-is-recorded-not-resolved.md)).
5. **Keep the text copy** and pass it to the check as `--source SRC-xx=<path>`, so the locators are
   verified against real text ([`run-the-checks.md`](run-the-checks.md)).
6. **Register the original**, not the extraction, in the ledger: the link points at the source of
   record ([`cite-a-source.md`](cite-a-source.md)).

**Done when** every binary source is either extracted and read in full, or reported as unread with
the reason, and each extracted text copy is available to the locator check.

**Note.** A folder of meeting transcripts is not a job for this script. Index it with the
`transcript-knowledge-base` skill, which produces cited, deduplicated statements, and draft from the
index.
