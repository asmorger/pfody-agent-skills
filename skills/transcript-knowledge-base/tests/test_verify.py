"""Tests for the quote verifier: the one check in this skill that reads meaning, not shape.

Every test here plants a defect that passes `render` and every other check, because that is the
class of failure the verifier exists for: a citation that looks exactly like a good one.
"""

import os
import unittest

from helpers import ROOT, temp_dir, write  # noqa: F401

from tkb.index import KnowledgeIndex, Source
from tkb.vault import render_vault
from tkb.verify import verify

TRANSCRIPT = """# Atlas Kickoff
Date: 2026-01-05
Participants: Maya, Devin

[00:00:05] Maya: Welcome everyone. The goal today is to align on the launch scope.
[00:00:30] Devin: We decided to target the EU region first because that is where demand is highest.
[00:01:10] Maya: I am concerned about the data residency risk without the new storage layer.
"""


def build(tmp, quote, speaker="Devin", ts="00:00:30"):
    """Render a one-item vault that cites the kickoff transcript, and verify it."""
    folder = os.path.join(tmp, "transcripts")
    path = write(folder, "2026-01-05_kickoff.txt", TRANSCRIPT)
    idx = KnowledgeIndex()
    idx.merge_item("Scope", "A statement under test", [Source(
        meeting="Atlas Kickoff", date="2026-01-05", speaker=speaker,
        timestamp=ts, quote=quote, file=path)])
    idx.mark_ingested(path, "hash0", "Atlas Kickoff", "2026-01-05")
    vault = os.path.join(tmp, "vault")
    render_vault(idx, vault)
    return vault, folder


class TestQuoteVerification(unittest.TestCase):
    def test_a_real_quote_passes(self):
        vault, folder = build(temp_dir(),
                              "We decided to target the EU region first")
        result = verify(vault, folder)
        self.assertEqual([str(p) for p in result.problems], [])
        self.assertEqual(result.checked, 1)

    def test_punctuation_and_case_are_the_services_not_the_speakers(self):
        vault, folder = build(temp_dir(),
                              "we decided TO TARGET the EU region, first!")
        self.assertTrue(verify(vault, folder).ok)

    def test_an_ellipsis_may_hide_words_but_not_reorder_them(self):
        vault, folder = build(temp_dir(),
                              "We decided to target the EU region ... demand is highest")
        self.assertTrue(verify(vault, folder).ok)

        vault, folder = build(temp_dir(),
                              "demand is highest ... We decided to target")
        self.assertFalse(verify(vault, folder).ok)

    def test_an_invented_quote_is_caught(self):
        vault, folder = build(temp_dir(),
                              "We decided to target the APAC region first")
        problems = [str(p) for p in verify(vault, folder).problems]
        self.assertTrue(any("not in" in p for p in problems), problems)

    def test_a_quote_in_the_wrong_mouth_is_caught(self):
        vault, folder = build(temp_dir(),
                              "We decided to target the EU region first", speaker="Maya")
        problems = [str(p) for p in verify(vault, folder).problems]
        self.assertTrue(any("but the note cites Maya" in p for p in problems), problems)

    def test_a_quote_at_a_cue_nobody_spoke_at_is_caught(self):
        vault, folder = build(temp_dir(),
                              "We decided to target the EU region first", ts="04:00:00")
        problems = [str(p) for p in verify(vault, folder).problems]
        self.assertTrue(any("is not in" in p for p in problems), problems)

    def test_a_quote_may_run_past_a_turn_boundary(self):
        vault, folder = build(
            temp_dir(),
            "where demand is highest ... concerned about the data residency risk")
        self.assertTrue(verify(vault, folder).ok)


class TestErrataRegister(unittest.TestCase):
    """A mishearing is corrected in a register, never by editing the transcript."""

    REGISTER = """---
type: errata
---

| Transcript | Cue | Speaker | Transcript says | Correction | State | Evidence |
|---|---|---|---|---|---|---|
| 2026-01-05-atlas-kickoff | 00:00:30 | Devin | the EU | European Union | candidate | first use |
"""

    def test_a_bracket_without_a_row_is_a_problem(self):
        vault, folder = build(temp_dir(),
                              "We decided to target the EU [European Union] region first")
        problems = [str(p) for p in verify(vault, folder).problems]
        self.assertTrue(any("has no errata row" in p for p in problems), problems)

    def test_a_bracket_with_a_row_is_accepted(self):
        tmp = temp_dir()
        vault, folder = build(tmp, "We decided to target the EU [European Union] region first")
        write(vault, "errata.md", self.REGISTER)
        self.assertTrue(verify(vault, folder).ok, [str(p) for p in verify(vault, folder).problems])

    def test_a_registered_correction_must_travel_with_every_quote_of_it(self):
        tmp = temp_dir()
        vault, folder = build(tmp, "We decided to target the EU region first")
        write(vault, "errata.md", self.REGISTER)
        problems = [str(p) for p in verify(vault, folder).problems]
        self.assertTrue(any("the annotation is missing" in p for p in problems), problems)


class TestUncheckedQuotes(unittest.TestCase):
    def test_a_quote_with_no_cue_is_reported_as_unchecked_not_as_passing(self):
        tmp = temp_dir()
        vault, folder = build(tmp, "We decided to target the EU region first")
        write(os.path.join(vault, "items"), "hand-written.md", """---
id: HAND-1
type: transcript-item
---

# HAND-1 — Somebody added this by hand

> [!quote] Evidence
> "this was never checked against anything"
> — Devin, [[2026-01-05-atlas-kickoff]]
""")
        result = verify(vault, folder)
        self.assertTrue(result.ok, [str(p) for p in result.problems])
        self.assertEqual(len(result.unchecked), 1, result.unchecked)
        self.assertIn("no checkable citation", str(result.unchecked[0]))


if __name__ == "__main__":
    unittest.main()
