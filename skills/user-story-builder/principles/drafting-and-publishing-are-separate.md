# Drafting and publishing are separate

**Rule.** Never publish without an explicit request in the current conversation. Writing a story and
pushing it to a tracker are two actions, and the second needs its own yes — plus a configured
publishing target and an adapter that matches it.

**Why.** Publishing is the one irreversible step here. Tracker items get assigned, reported on and
worked, and a wrong set costs more to unpick than it cost to create. An inferred yes is also the wrong
kind of permission: the user agreed to the idea of publishing, not to these nineteen items under these
parents, which is the thing they would have caught. Keeping the actions separate is what makes drafting
safe to iterate on.

**In the story.**
- No adapter for the configured target → emit the portable markdown and name the missing adapter. Do
  not improvise an import ([`../practices/add-a-tracker-adapter.md`](../practices/add-a-tracker-adapter.md)).
- Where the source PRD is not `Accepted`, write `PREVIEW` at the top and do not publish it at all
  ([`../practices/build-from-a-prd.md`](../practices/build-from-a-prd.md)).
- Show the item set — level, title, parent — and get a clear yes before creating anything
  ([`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)).
- Never guess a parent's tracker id. Find it in the PRD's work item map, or ask
  ([`one-name-and-one-id-per-level.md`](one-name-and-one-id-per-level.md)).
- Read created items back and report their ids. An unverified create is a claim, not a fact.

**Breaks when.** Items appear in a tracker nobody asked for →
[`../anti-patterns/publishing-without-a-request.md`](../anti-patterns/publishing-without-a-request.md).
