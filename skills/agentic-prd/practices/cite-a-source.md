# Cite a source

**When** writing any citation, and when checking one you or someone else wrote.

**Why.** The locator is what makes a requirement cheap to disagree with. Without one, checking a
single sentence means re-reading a whole transcript, so nobody checks — and an unchecked requirement
is indistinguishable from an invented one.

**Steps.**

1. **Register the source first.** A row in the ledger with its id, name, type (`Verified` or
   `Stakeholder`), link and date ([`../patterns/knowledge-ledger.md`](../patterns/knowledge-ledger.md)).
   Link to where it lives; copy nothing out of it.
2. **Write the locator by looking at it.** A time `SRC-07 @1:13:06`, a page `SRC-02 p.4`, a line
   `SRC-03 L12`. Open the source, find the sentence, then write the locator — never from memory and
   never estimated from position.
3. **Quote the sentence to yourself.** If you cannot, the source does not state it: mark it
   `PROPOSED` or raise a question
   ([`../principles/implied-is-not-stated.md`](../principles/implied-is-not-stated.md)).
4. **Pick the right kind of citation.** A `DEC-xx` for something a decision settled, with no locator.
   An `A-xx` for an inference, with its basis and what would falsify it. `PROPOSED` when there is no
   source at all.
5. **Record a date as the source gives it.** "Next quarter" does not become a date.
6. **Verify the locators mechanically** where you can: `check_prd.py --source SRC-07=<text copy>`
   confirms the time or line exists in the text ([`run-the-checks.md`](run-the-checks.md)).
7. **Flag internal-only sources** in the report, before the PRD leaves the team
   ([`../principles/link-the-source-never-copy-it.md`](../principles/link-the-source-never-copy-it.md)).

**Done when** every requirement's Source column holds one of the four legal values, every `SRC-xx`
has a locator and a ledger row, each locator was compared against the source as it was written, and
the person has been told which citations only the team can open.
