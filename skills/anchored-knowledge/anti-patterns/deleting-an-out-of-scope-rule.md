# Deleting an out-of-scope rule

**Smell.** Bulk printing was deferred, so the `LABEL-3` note was deleted and the MOC regenerated
without it. A superseded scope boundary edited into the new one. A decision note rewritten in place
when the decision reversed.

**Why it is wrong.** "Did we ever agree to that?" is the question this base is most often asked, and a
deleted rule cannot answer it. The anchor goes with it: the rule existed because a source said
something, and that source still says it. So six weeks later the behaviour is re-proposed as new,
re-argued from scratch, and nobody can show it was considered and dropped — which is a commercial
loss, not just an untidy one. In a vault it costs more again: every wikilink that cited `[[LABEL-3]]`
— from other notes, from stories, from code comments — now resolves to nothing, and the ones outside
the vault will never be found. An overwritten decision is worse still, because the reasoning that
would have settled it is the part that was replaced.

**Instead.** Deprecate in place. Keep the note and its id, set `status: out-of-scope`, add a
`[!failure]` callout naming the phase and the scope-watch note that would bring it back. Preserve a
superseded boundary as its own note. Supersede a decision with a new one that names it, and change
the old one's `status` rather than its body. Deprecated notes stay out of the way without leaving the
record: the MOC's snapshot excludes them and a Bases view collects them
([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md),
[`../patterns/status-callouts.md`](../patterns/status-callouts.md)).
