"""End-to-end CLI test: prepare -> merge -> render a vault, including incremental re-run."""

import io
import json
import os
import unittest
from contextlib import redirect_stdout

from helpers import ROOT, temp_dir, write  # noqa: F401

from tkb import cli

KICKOFF = (
    "Title: Project Kickoff\nDate: 2026-01-05\n\n"
    "[00:00:05] Maya: We decided to authenticate users via SSO through the IN portal.\n"
    "[00:00:30] Devin: Bids must be a positive multiple of the minimum bid amount.\n"
)
REVIEW = (
    "Title: Review\nDate: 2026-02-02\n\n"
    "[00:00:05] Priya: Confirming again, users authenticate via SSO through the IN portal.\n"
    "[00:00:30] Devin: All bidding is blind to other bidders.\n"
)


def _read(vault, rel):
    with open(os.path.join(vault, rel), encoding="utf-8") as fh:
        return fh.read()


def run(argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        cli.main(argv)
    return json.loads(buf.getvalue())


class TestCliEndToEnd(unittest.TestCase):
    def setUp(self):
        self.d = temp_dir()
        self.folder = os.path.join(self.d, "transcripts")
        os.makedirs(self.folder)
        self.state = os.path.join(self.d, "state.json")
        self.work = os.path.join(self.d, "work")
        self.vault = os.path.join(self.d, "transcript-knowledge")

    def _merge_from_manifest(self, manifest_path, items):
        """Helper: build an items.json the way the agent would, then merge."""
        manifest = json.load(open(manifest_path, encoding="utf-8"))
        by_name = {f["name"]: f for f in manifest["files"]}
        payload = {
            "processed_files": [
                {"path": f["path"], "name": f["name"], "hash": f["hash"],
                 "meeting": f["meeting"], "date": f["date"]}
                for f in manifest["files"] if "hash" in f
            ],
            "items": items,
        }
        items_path = os.path.join(self.d, "items.json")
        json.dump(payload, open(items_path, "w", encoding="utf-8"), ensure_ascii=False)
        return run(["merge", "--items", items_path, "--state", self.state])

    def test_full_lifecycle_and_incremental(self):
        write(self.folder, "kickoff.txt", KICKOFF)

        # 1. prepare
        prep = run(["prepare", "--folder", self.folder, "--state", self.state, "--workdir", self.work])
        self.assertEqual(prep["counts"]["to_process"], 1)
        manifest_path = os.path.join(self.work, "_manifest.json")

        # 2+3. extract (simulated) + merge
        res = self._merge_from_manifest(manifest_path, [
            {"category": "Authentication", "statement": "Users authenticate via SSO through the IN portal.",
             "sources": [{"meeting": "Project Kickoff", "date": "2026-01-05", "speaker": "Maya",
                          "timestamp": "00:00:05", "quote": "authenticate users via SSO", "turn_id": "t0000"}]},
            {"category": "Bidding", "statement": "Bids must be a positive multiple of the minimum bid amount.",
             "sources": [{"meeting": "Project Kickoff", "date": "2026-01-05", "speaker": "Devin",
                          "timestamp": "00:00:30", "quote": "positive multiple of the minimum bid", "turn_id": "t0001"}]},
        ])
        self.assertEqual(res["created"], 2)

        # 4. render the vault
        rnd = run(["render", "--out", self.vault, "--state", self.state])
        self.assertEqual(rnd["items"], 2)
        self.assertEqual(rnd["meetings"], 1)
        note = _read(self.vault, "items/users-authenticate-via-sso-through-the-in-portal.md")
        self.assertIn("id: AUT-1", note)
        self.assertIn('sources: ["[[2026-01-05-project-kickoff]]"]', note)
        self.assertIn("> — Maya, [[2026-01-05-project-kickoff]] 00:00:05", note)
        moc = _read(self.vault, rnd["moc"])
        # The citable form: filename as target, id as display text, pipe escaped for the cell.
        # A bare [[AUT-1]] would resolve to nothing, because Obsidian never matches an alias.
        self.assertIn("| [[users-authenticate-via-sso-through-the-in-portal\\|AUT-1]] |", moc)
        self.assertNotIn("[[AUT-1]]", moc)

        # --- Incremental: add a second transcript, re-run ---
        write(self.folder, "review.txt", REVIEW)
        prep2 = run(["prepare", "--folder", self.folder, "--state", self.state, "--workdir", self.work])
        self.assertEqual(prep2["to_process"], ["review.txt"])      # only the new file
        self.assertEqual(prep2["unchanged"], ["kickoff.txt"])

        self._merge_from_manifest(os.path.join(self.work, "_manifest.json"), [
            # A restatement of AUTH-1 -> should fold in as a second source, not a new id.
            {"category": "Authentication", "statement": "Users authenticate via SSO through the IN portal.",
             "sources": [{"meeting": "Review", "date": "2026-02-02", "speaker": "Priya",
                          "timestamp": "00:00:05", "quote": "users authenticate via SSO", "turn_id": "t0000"}]},
            # A genuinely new rule.
            {"category": "Bidding", "statement": "All bidding is blind to other bidders.",
             "sources": [{"meeting": "Review", "date": "2026-02-02", "speaker": "Devin",
                          "timestamp": "00:00:30", "quote": "bidding is blind", "turn_id": "t0001"}]},
        ])
        status = run(["status", "--state", self.state])
        self.assertEqual(status["items"], 3)                       # AUTH-1 merged, not duplicated
        self.assertEqual(status["categories"]["Authentication"], 1)
        self.assertEqual(status["categories"]["Bidding"], 2)

        # AUTH-1 now has two sources from two meetings.
        from tkb.index import KnowledgeIndex
        idx = KnowledgeIndex.load(self.state)
        self.assertEqual(len(idx.items["AUT-1"].sources), 2)

        # Re-rendering folds the second meeting in: one note per meeting, and the merged
        # statement's note now cites both — which is the whole point of the incremental run.
        rnd2 = run(["render", "--out", self.vault, "--state", self.state])
        self.assertEqual((rnd2["items"], rnd2["meetings"]), (3, 2))
        note = _read(self.vault, "items/users-authenticate-via-sso-through-the-in-portal.md")
        self.assertIn('sources: ["[[2026-01-05-project-kickoff]]", "[[2026-02-02-review]]"]', note)
        self.assertEqual(note.count("> [!quote] Evidence"), 2)

    def test_merge_drops_items_without_provenance(self):
        write(self.folder, "kickoff.txt", KICKOFF)
        run(["prepare", "--folder", self.folder, "--state", self.state, "--workdir", self.work])
        items_path = os.path.join(self.d, "items.json")
        json.dump({"processed_files": [], "items": [
            {"category": "X", "statement": "An unsourced claim.", "sources": []},
        ]}, open(items_path, "w", encoding="utf-8"))
        res = run(["merge", "--items", items_path, "--state", self.state])
        self.assertEqual(res["dropped_no_provenance"], 1)
        self.assertEqual(res["total_items"], 0)


if __name__ == "__main__":
    unittest.main()
