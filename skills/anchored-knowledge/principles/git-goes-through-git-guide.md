# Git goes through git-guide

**Rule.** When the record is git-managed, every git operation goes through the `git-guide` skill: get
the latest before reading or editing, save after promoting, publish to open a review. Never run raw
git against a knowledge base, and never commit the workbench.

**Why.** The record is shared, and the person who owns the knowledge is often not the person who is
comfortable with git — that is why the knowledge was in scattered notes to begin with. Raw git in
that situation produces the failures that make people stop contributing: an edit on a stale copy that
clobbers a teammate's rule, a working draft pushed to the team, a branch nobody can unpick. Getting
the latest first is the half that matters most: reconciling an incoming source against a stale rule
set produces an audit that is wrong in both directions.

**In the base.**
- Before reading or ingesting: get the latest, so you reconcile against the team's current record
  ([`../practices/ingest-a-source.md`](../practices/ingest-a-source.md)).
- After promoting: save as a private checkpoint, then publish for review. Name the exact rule ids you
  promoted in the save message
  ([`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md)).
- Record `git_managed: true`, the host and the repository root in the config. Detect the root with
  `git rev-parse --show-toplevel`.
- Add the workbench to `.gitignore` when it sits inside the repository, and record that it was
  done ([`two-directories-promote-to-commit.md`](two-directories-promote-to-commit.md)).
- Never auto-commit. Promotion is approved first, then saved.

**Breaks when.** Raw git is run against the record →
[`../anti-patterns/raw-git-in-the-knowledge-base.md`](../anti-patterns/raw-git-in-the-knowledge-base.md).
