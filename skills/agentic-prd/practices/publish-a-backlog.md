# Publish a backlog

**When** a person asks for an approved backlog to be put into a work tracker. Mode `PUBLISH`.

**Why.** This is the one irreversible step in the skill. Tracker items get assigned, reported on and
worked; unpicking a wrong set costs more than creating it did, and some of it cannot be unpicked at
all.

**Steps.**

1. **Check all three preconditions**: the person asked in this conversation, the PRD status is
   `accepted`, and a person approved the backlog at Gate 3. Any one missing → stop and say which
   ([`../principles/only-a-person-crosses-a-gate.md`](../principles/only-a-person-crosses-a-gate.md)).
2. **Find the tracker tools.** None available → hand over the backlog file and stop. Do not improvise
   an export.
3. **Show exactly what you will create** — every item, with its level, title and parent — and get a
   clear yes. Not an inferred yes from an earlier message
   ([`../anti-patterns/publishing-without-a-yes.md`](../anti-patterns/publishing-without-a-yes.md)).
4. **Read the target from the tool's own configuration.** `az devops configure -l` for Azure DevOps.
   Never assume an organisation or a project.
5. **Create parents before children**: Epic, then Feature, then User Story
   ([`../patterns/tracker-item.md`](../patterns/tracker-item.md)).
6. **Open each title with its level id** and tag each item with the `PRD-NNN` id, so any item traces
   back in one lookup.
7. **Normalise every field to plain ASCII** before sending: straight quotes, `-` for dashes, `->` for
   arrows, "Section" for `§`. On Windows the hops between the CLI and the tracker corrupt the rest
   silently, and the corruption is only visible in the tracker afterwards.
8. **Read the created items back** and record their ids in the PRD's work item map.

**Done when** every item in the shown set exists in the tracker with its parent, each title opens
with its level id and carries the `PRD-NNN` tag, the ids are recorded in the PRD, and nothing was
created that the person did not see first.
