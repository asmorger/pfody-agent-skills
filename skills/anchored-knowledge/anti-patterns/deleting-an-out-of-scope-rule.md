# Deleting an out-of-scope rule

**Smell.** Bulk printing was deferred, so `LABEL-3` was removed and the table closed up. A superseded
assumption edited into the new version. An ADR rewritten in place when the decision reversed.

**Why it is wrong.** "Did we ever agree to that?" is the question this base is most often asked, and a
deleted rule cannot answer it. The anchor goes with it: the rule existed because a source said
something, and that source still says it. So six weeks later the behaviour is re-proposed as new,
re-argued from scratch, and nobody can show it was considered and dropped — which is a commercial
loss, not just an untidy one. An overwritten ADR is worse, because the reasoning that would have
settled it is the part that was replaced.

**Instead.** Deprecate in place. Keep the id, rewrite the rule to say what is now true — "**not in
Phase 1 scope**. Deferred to a future phase." — and leave it where it sits. Preserve superseded
assumptions with their anchors. Supersede an ADR with a new one that names it, and change the old
one's status rather than its body
([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md),
[`../patterns/inline-status-markers.md`](../patterns/inline-status-markers.md)).
