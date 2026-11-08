# Raw git in the knowledge base

**Smell.** `git add docs/ && git commit -m "update knowledge"`. A promotion committed without getting
the latest first. A `git push` to the shared branch. An auto-commit after an approval, because the
approval obviously implied it.

**Why it is wrong.** The record is shared, and the person who owns the knowledge is often not the
person who is comfortable with git — that is frequently why the knowledge was in scattered notes to
begin with. Raw git in that situation produces exactly the failures that stop people contributing: an
edit committed on a stale copy that clobbers a teammate's rule, the working area pushed to the team, a
branch state nobody present can unpick. Reconciling against a stale rule set is the subtler harm — the
audit comes out wrong in both directions and looks authoritative.

**Instead.** Go through the `git-guide` skill. Get the latest before reading or ingesting; save as a
private checkpoint after promoting, naming the exact rule ids; publish to open a review. Record
`git_managed: true` and the host in the config. Never auto-commit, and never commit the working area
([`../principles/git-goes-through-git-guide.md`](../principles/git-goes-through-git-guide.md),
[`../practices/promote-to-the-record.md`](../practices/promote-to-the-record.md)).
