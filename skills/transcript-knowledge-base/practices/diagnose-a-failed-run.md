# Diagnose a failed run

**When** a run errors, skips something unexpectedly, or produces an index that looks wrong.

**Why.** Most of these have one cause and one fix, and the wrong instinct in every case is to work
around the tool by writing output by hand.

**Steps.** Match the symptom:

    a file shows `error` in the manifest
        malformed or unsupported. Other files still process. Report it; do not
        fill in its items by hand.

    the re-run reprocessed everything
        the file content changed, so the hash differs — or the state file was
        missing, moved, or not passed. Check --state first.

    the same file reprocesses every single run
        its hash never reached processed_files. Copy it from the manifest,
        verbatim → ../principles/the-content-hash-is-the-unit-of-work.md

    two similar rules did not merge
        dedup is lexical. Lower dedup_threshold, or align the statements, and
        re-merge → ../practices/curate-a-large-corpus.md

    ids changed between runs, or a topic has two prefixes
        the taxonomy is emergent, or a category name was not reused exactly
        → ../practices/seed-the-taxonomy.md

    a `.docx` will not parse
        confirm it is a real Word file — a zip containing word/document.xml.

    citations have no speaker
        the export carries no speaker labels (newer Copilot -en-US files among
        them). Meeting and date is the correct citation. Do not infer a speaker.

    merge reported dropped items
        they had no provenance. Cite them from the brief or delete them
        → ../principles/every-item-carries-a-source.md

    this base's index was overwritten
        the default output paths collided with the caller's
        → ../anti-patterns/overwriting-a-sibling-index.md

**Then.** Re-run the deterministic steps rather than patching their output; all three are idempotent
([`../principles/the-tool-does-the-mechanics.md`](../principles/the-tool-does-the-mechanics.md)). The
tests in `tests/` state the guaranteed behaviour, and `python examples/demo.py` proves a working
end-to-end cycle on the sample data when you need to tell a tool problem from a data problem.

**Done when** the symptom is matched to its cause, the fix is applied by re-running rather than by
editing output, and anything genuinely unprocessable is reported to the user instead of filled in.
