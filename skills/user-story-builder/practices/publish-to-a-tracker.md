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
6. **Normalise all rich text to pure ASCII**, then convert the markdown to the tracker's markup. The
   adapter defines both steps and the order matters
   ([`../principles/tracker-text-is-ascii.md`](../principles/tracker-text-is-ascii.md)).
7. **Open each title with its level id** — `US-01 Void a printed label` — and apply the config's
   required tags.
8. **Link the parent.** Find the Feature's tracker id in the PRD's work item map or ask for it.
   **Never guess it.**
9. **Read every created item back** and report its tracker id. An unverified create is a claim.
10. **Respect the adapter's batch discipline** rather than firing every create at once.

**Done when** every shown item exists with its parent, each title opens with its level id, every
rich-text field is ASCII, the created ids are reported, and nothing was created that the user did not
see first.
