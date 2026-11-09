# Faking the output when Python is missing

**Smell.** No interpreter on PATH, or one at 3.8, and a `knowledge-index.md` produced anyway — read
from the transcripts and written by hand, with citations that look right. Sometimes a state file
invented alongside it so the next run "works".

**Why it is wrong.** It is the worst version of hand-writing the index, because the user asked for a
sourced document and received something that only resembles one. The citations cannot have been copied
from briefs that were never generated, so they were composed, which makes them unverifiable at exactly
the moment they look most authoritative. An invented state file is worse again: the next real run
trusts its hashes and skips files that were never ingested, so the fabrication becomes permanent and
invisible.

**Instead.** Stop and say so. Offer the install path for the platform — `winget install
Python.Python.3.12`, `brew install python@3.12`, the distribution's package manager — and wait. No
`pip install` is needed, which removes the usual excuse. One message of friction against a document
nobody can trust is not a close call
([`../principles/never-fake-the-output.md`](../principles/never-fake-the-output.md),
[`../practices/confirm-python.md`](../practices/confirm-python.md)).
