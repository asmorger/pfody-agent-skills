"""Tests for the knowledge index: id assignment, dedup/merge, provenance, vault render."""

import os
import unittest

from helpers import ROOT, temp_dir  # noqa: F401

from tkb.index import KnowledgeIndex, Source, derive_prefix
from tkb.vault import render_vault


def src(meeting="Kickoff", date="2026-01-05", speaker="Maya", ts="0:12", quote="...", turn="t0001"):
    return Source(meeting=meeting, date=date, speaker=speaker, timestamp=ts, quote=quote, turn_id=turn)


class TestIndexMerge(unittest.TestCase):
    def test_ids_assigned_per_category(self):
        idx = KnowledgeIndex()
        i1, new1 = idx.merge_item("Bidding", "Bids must be whole dollars.", [src()])
        i2, new2 = idx.merge_item("Bidding", "All bidding is blind to other bidders.", [src()])
        i3, _ = idx.merge_item("Authentication & Access", "Users authenticate via SSO.", [src()])
        self.assertEqual((i1, i2), ("BID-1", "BID-2"))
        self.assertTrue(i3.startswith("AA"))  # derived prefix from two words
        self.assertTrue(new1 and new2)

    def test_near_duplicate_merges_and_keeps_all_sources(self):
        idx = KnowledgeIndex()
        a, _ = idx.merge_item("Bidding", "Bid amounts must be a positive multiple of the minimum bid.",
                              [src(meeting="Scope Discussion", quote="multiple of the minimum")])
        b, created = idx.merge_item("Bidding", "Bids must be a positive multiple of the minimum bid amount.",
                                    [src(meeting="Standup", date="2026-01-28", quote="multiple of minimum bid")])
        self.assertEqual(a, b)            # folded into the same item
        self.assertFalse(created)
        item = idx.items[a]
        self.assertEqual(len(item.sources), 2)   # both meetings retained as evidence
        meetings = {s.meeting for s in item.sources}
        self.assertEqual(meetings, {"Scope Discussion", "Standup"})

    def test_unrelated_statements_do_not_merge(self):
        idx = KnowledgeIndex()
        idx.merge_item("Bidding", "All bidding is blind to other bidders.", [src()])
        _id, created = idx.merge_item("Bidding", "Pickup penalties apply after a grace period.", [src()])
        self.assertTrue(created)
        self.assertEqual(len(idx.items), 2)

    def test_supersession_marks_referenced_item(self):
        idx = KnowledgeIndex()
        old, _ = idx.merge_item("Auction", "Auctions launch in March.", [src(date="2026-01-05")],
                                status="tentative")
        new, _ = idx.merge_item("Auction", "Auctions launch in April per revised plan.",
                                [src(date="2026-02-02")], status="confirmed", supersedes=[old])
        # The newer item explicitly supersedes the older; the old one is marked,
        # but its evidence is preserved (not deleted).
        self.assertEqual(idx.items[old].status, "superseded")
        self.assertEqual(idx.items[new].status, "confirmed")
        self.assertTrue(idx.items[old].sources)

    def test_provenance_is_mandatory(self):
        idx = KnowledgeIndex()
        item = idx.items.get(idx.merge_item("X", "A rule.", [src()])[0])
        self.assertEqual(item.validate(), [])
        item.sources = []
        self.assertIn("no provenance (sources empty)", item.validate())


class TestVaultRender(unittest.TestCase):
    def _idx(self):
        idx = KnowledgeIndex(title="Acme Rules", intro="Rules from discovery.")
        idx.merge_item("Authentication & Access", "Users authenticate via SSO through Acme ID.",
                       [src(meeting="Alignment", date="2026-01-15", speaker="Jason",
                            ts="0:12:04", quote="we go through Acme ID for sign on", turn="t0042")],
                       prefix="AUTH")
        idx.merge_item("Bidding", "All bidding is blind; bidders cannot see other bids.",
                       [src(meeting="Scope", date="2026-01-21", quote="bidding is blind")],
                       prefix="BID", status="confirmed")
        return idx

    def _render(self, idx=None):
        d = temp_dir()
        summary = render_vault(idx or self._idx(), d)
        return d, summary

    def read(self, d, rel):
        with open(os.path.join(d, rel), encoding="utf-8") as fh:
            return fh.read()

    def test_one_note_per_item_and_per_meeting(self):
        d, summary = self._render()
        self.assertEqual(summary["items"], 2)
        self.assertEqual(summary["meetings"], 2)
        self.assertEqual(sorted(os.listdir(os.path.join(d, "items"))),
                         ["all-bidding-is-blind-bidders-cannot-see-other-bids.md",
                          "users-authenticate-via-sso-through-acme-id.md"])
        self.assertEqual(sorted(os.listdir(os.path.join(d, "meetings"))),
                         ["2026-01-15-alignment.md", "2026-01-21-scope.md"])

    def test_item_note_shape(self):
        d, _ = self._render()
        note = self.read(d, "items/users-authenticate-via-sso-through-acme-id.md")
        self.assertTrue(note.startswith("---\n"))
        self.assertIn("id: AUTH-1", note)
        self.assertIn("aliases: [AUTH-1]", note)
        self.assertIn("type: transcript-item", note)
        self.assertIn("status: confirmed", note)
        self.assertIn("citable: false", note)
        # No `tags`: `type` and `category` already carry what the tag encoded, and a hand-kept
        # third copy of two fields is free to disagree with both.
        self.assertNotIn("tags:", note)
        self.assertIn('category: "Authentication & Access"', note)
        # the source is a quoted wikilink to the meeting note, so Obsidian reads it as a link
        self.assertIn('sources: ["[[2026-01-15-alignment]]"]', note)
        self.assertIn("# AUTH-1 — Users authenticate via SSO through Acme ID.", note)

    def test_verbatim_quote_is_on_the_note(self):
        """The quote moved out of the state file and onto the statement it anchors."""
        d, _ = self._render()
        note = self.read(d, "items/users-authenticate-via-sso-through-acme-id.md")
        self.assertIn("> [!quote] Evidence", note)
        self.assertIn('> "we go through Acme ID for sign on"', note)
        self.assertIn("> — Jason, [[2026-01-15-alignment]] 0:12:04", note)

    def test_quote_also_survives_in_the_state_cache(self):
        d, _ = self._render()
        idx = self._idx()
        state = os.path.join(temp_dir(), "s.json")
        idx.save(state)
        reloaded = KnowledgeIndex.load(state)
        s = reloaded.items["AUTH-1"].sources[0]
        self.assertEqual(s.quote, "we go through Acme ID for sign on")
        self.assertEqual(s.timestamp, "0:12:04")

    def test_moc_has_embed_and_generated_snapshot(self):
        d, summary = self._render()
        moc = self.read(d, summary["moc"])
        self.assertIn("type: moc", moc)
        self.assertIn("![[acme-rules.base]]", moc)
        self.assertIn("<!-- generated: do not edit", moc)
        self.assertIn("<!-- /generated -->", moc)
        self.assertIn("### Authentication & Access", moc)
        self.assertIn("| [[users-authenticate-via-sso-through-acme-id\\|AUTH-1]] |", moc)
        self.assertNotIn("| [[AUTH-1]] |", moc)
        self.assertIn("[[2026-01-15-alignment]]", moc)
        self.assertTrue(os.path.exists(os.path.join(d, "bases/acme-rules.base")))

    def test_status_is_a_property_and_a_callout_not_prose(self):
        idx = KnowledgeIndex()
        idx.merge_item("Scope", "Buy Now is deferred to a future phase.",
                       [src(quote="buy now later")], status="deferred", note="not Phase 1")
        d, _ = self._render(idx)
        note = self.read(d, "items/buy-now-is-deferred-to-a-future-phase.md")
        self.assertIn("status: deferred", note)
        self.assertIn("> [!failure] Deferred", note)
        self.assertIn("> not Phase 1", note)
        # the statement itself stays clean
        self.assertIn("# SCO-1 — Buy Now is deferred to a future phase.", note)

    def test_pipe_escaped_in_the_moc_table_only(self):
        idx = KnowledgeIndex()
        idx.merge_item("X", "A rule with a | pipe.", [src()])
        d, summary = self._render(idx)
        self.assertIn("\\|", self.read(d, summary["moc"]))
        # the note's own heading needs no escaping, because it is not a table
        self.assertIn("# X-1 — A rule with a | pipe.", self.read(d, "items/a-rule-with-a-pipe.md"))

    def test_rerun_is_idempotent_and_preserves_created(self):
        d, _ = self._render()
        rel = "items/users-authenticate-via-sso-through-acme-id.md"
        before = self.read(d, rel)
        with open(os.path.join(d, rel), "w", encoding="utf-8") as fh:
            fh.write(before.replace("created: " + before.split("created: ")[1].split("\n")[0],
                                    "created: 2020-01-01"))
        render_vault(self._idx(), d)
        after = self.read(d, rel)
        self.assertIn("created: 2020-01-01", after)   # original creation date kept
        render_vault(self._idx(), d)
        self.assertEqual(after, self.read(d, rel))    # second re-run changes nothing

    def test_a_renamed_statement_removes_its_old_note(self):
        d, _ = self._render()
        idx = KnowledgeIndex(title="Acme Rules")
        idx.merge_item("Bidding", "All bidding is blind; bidders cannot see other bids.",
                       [src(meeting="Scope", date="2026-01-21", quote="bidding is blind")],
                       prefix="BID")
        summary = render_vault(idx, d)
        self.assertFalse(os.path.exists(
            os.path.join(d, "items/users-authenticate-via-sso-through-acme-id.md")))
        self.assertGreaterEqual(summary["files_removed"], 1)

    def test_a_hand_added_note_is_never_deleted(self):
        d, _ = self._render()
        mine = os.path.join(d, "items", "my-own-note.md")
        with open(mine, "w", encoding="utf-8") as fh:
            fh.write("---\ntype: note\n---\n\n# Mine\n")
        render_vault(KnowledgeIndex(title="Acme Rules"), d)
        self.assertTrue(os.path.exists(mine))

    def test_long_statement_is_truncated_at_a_word_boundary(self):
        idx = KnowledgeIndex()
        idx.merge_item("X", "A very long canonical statement that keeps going well past any "
                            "reasonable filename length and must be cut somewhere sensible.",
                       [src()])
        d, _ = self._render(idx)
        names = os.listdir(os.path.join(d, "items"))
        self.assertEqual(len(names), 1)
        stem = names[0][:-3]
        self.assertLessEqual(len(stem), 72)
        self.assertFalse(stem.endswith("-"))


class TestPrefix(unittest.TestCase):
    def test_derive_prefix(self):
        self.assertEqual(derive_prefix("Bidding"), "BID")
        self.assertEqual(derive_prefix("Authentication & Access"), "AA")
        self.assertEqual(derive_prefix("Terms & Conditions"), "TC")


if __name__ == "__main__":
    unittest.main()
