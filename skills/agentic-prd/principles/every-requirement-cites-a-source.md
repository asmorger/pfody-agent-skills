# Every requirement cites a source

**Rule.** Each requirement row carries exactly one value in its Source column: a `SRC-xx` with a
locator, a `DEC-xx`, an `A-xx`, or `PROPOSED`. A `SRC-xx` without a locator — a time, a page, a line
— is not a citation. Compare the locator against the source at the moment you write it.

**Why.** The citation is what lets a reader disagree with a requirement cheaply. Without a locator a
reader must re-read the whole source to check one sentence, so nobody checks, and an unchecked
requirement is indistinguishable from an invented one. The locator is also what the check script can
verify mechanically ([`../practices/run-the-checks.md`](../practices/run-the-checks.md)) — the one
part of citation discipline that does not depend on anyone's diligence.

**In the PRD.**
- A time in a transcript: `SRC-07 @1:13:06`. A page in a document: `SRC-02 p.4`. A line in plain
  notes: `SRC-03 L12`.
- Every `SRC-xx` has a row in the knowledge ledger with its type, link and date
  ([`../patterns/knowledge-ledger.md`](../patterns/knowledge-ledger.md)).
- `DEC-xx` needs no locator: the decision row cites its own source.
- `A-xx` names an assumption or inference the approver accepts the risk on.
- `PROPOSED` means nobody has sourced it yet. An Accepted PRD contains none
  ([`../anti-patterns/accepted-with-proposed-left-in.md`](../anti-patterns/accepted-with-proposed-left-in.md)).

**Breaks when.** A behaviour a source only implies is written as sourced →
[`../anti-patterns/implied-behaviour-as-sourced.md`](../anti-patterns/implied-behaviour-as-sourced.md).
