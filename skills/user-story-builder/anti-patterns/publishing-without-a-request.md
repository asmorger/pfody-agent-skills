# Publishing without a request

**Smell.** Tracker items created because the stories were finished and publishing was obviously next.
Or on the strength of "and then put them in Azure DevOps" from before the stories existed. Or a set
published without being shown — just a count, and a `PREVIEW` header that nobody acted on.

**Why it is wrong.** This is the one irreversible step in the skill. Tracker items get assigned,
reported on and worked; a wrong set costs more to unpick than it cost to create, and some of it cannot
be unpicked. An inferred yes is the wrong kind of permission: the user agreed to the idea of
publishing, not to these nineteen items under these parents, which is the thing they would have
caught. Publishing a preview is worse — the source PRD was not accepted, so the behaviour itself is
not agreed.

**Instead.** Treat drafting and publishing as two actions. Require the request in the current
conversation, refuse a `PREVIEW` set outright, show every item with its level, title and parent, and
get a clear yes. Then create parents before children, read the items back and report their ids. With
no adapter for the configured target, hand over the portable markdown and name the missing adapter
rather than improvising
([`../principles/drafting-and-publishing-are-separate.md`](../principles/drafting-and-publishing-are-separate.md),
[`../practices/publish-to-a-tracker.md`](../practices/publish-to-a-tracker.md)).
