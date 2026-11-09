# Publish to a tracker

**When** the user asks for stories to be pushed to a tracker, and the config names a publishing
target. Step 5.

**Why.** The one irreversible step in the skill. Tracker items get assigned, reported on and worked;
a wrong set costs more to unpick than it cost to create.

**Steps.**

1. **Check it was asked for, in this conversation.** Drafting and publishing are separate actions, and
   an earlier "and then put them in the tracker" from before the stories existed is not this request
   ([`../principles/drafting-and-publishing-are-separate.md`](../principles/drafting-and-publishing-are-separate.md)).
2. **Refuse a preview.** A story set marked `PREVIEW`, because its source PRD is not `Accepted`, is
   not publishable ([`build-from-a-prd.md`](build-from-a-prd.md)).
3. **Load the adapter** for the configured target from `../references/adapters/`, e.g.
   [`../references/adapters/azure-devops.md`](../references/adapters/azure-devops.md). No adapter
   matches → emit the portable markdown and tell the user which adapter is missing
   ([`add-a-tracker-adapter.md`](add-a-tracker-adapter.md)).
4. **Resolve the fields** if `fields_resolved` is false, or the org or project changed
   ([`resolve-the-tracker-fields.md`](resolve-the-tracker-fields.md)).
5. **Show the item set** — every item with its level, title and parent — and get a clear yes.
6. **Strip the wikilink brackets first**: `[[LABEL-2]]` → `LABEL-2`, `[[ORDER-1|the freeze]]` → `the
   freeze`. A tracker renders `[[…]]` literally, so an un-stripped link shows a reader a reference
   that goes nowhere ([`../references/vault-convention.md`](../references/vault-convention.md)).
7. **Normalise all rich text to pure ASCII**, then convert the markdown to the tracker's markup. The
   adapter defines both steps and the order matters — brackets, then ASCII, then markup
   ([`../principles/tracker-text-is-ascii.md`](../principles/tracker-text-is-ascii.md)).
8. **Open each title with its level id** — `US-01 Void a printed label` — and apply the config's
   required tags.
9. **Link the parent.** Find the Feature's tracker id in the note's `tracker-id`, or ask for it.
   **Never guess it.**
10. **Read every created item back**, then **write the id into the note**: `tracker-id`,
    `tracker-url` and `status: published`. That is what makes the link bidirectional, and an
    unverified create is a claim rather than a publish
    ([`../patterns/user-story.md`](../patterns/user-story.md)).
11. **Respect the adapter's batch discipline** rather than firing every create at once.

**Done when** every shown item exists with its parent, each title opens with its level id, every
rich-text field is bracket-free ASCII, each note carries the tracker id it was given, and nothing was
created that the user did not see first.
