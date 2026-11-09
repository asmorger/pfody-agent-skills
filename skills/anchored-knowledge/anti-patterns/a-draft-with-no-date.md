# A draft with no date

**Smell.** `status: draft` and nothing else. A `> [!warning] Draft` callout with no date and no name.
`status: needs-review` on a note whose `updated` is the day it was written. All correct about the
state and silent about when — and often about who.

**Why it is wrong.** An undated marker cannot be closed. Nobody can tell whether it is a week old or
from the previous phase, so nobody chases it, and after a few months it becomes decoration: readers
learn that the markers mean nothing and start treating drafts as confirmed. The missing stakeholder
compounds it — "pending confirmation" with nobody named has no owner, so there is no one to ask. Both
omissions turn a live flag into permanent furniture.

**Instead.** A draft carries `pending-on` and a dated callout naming the stakeholder:
`> [!warning] Draft — pending operations lead, as of 2026-11-08`. A confirmed note carries
`confirmed: 2026-10-02`. A supersession carries its date and its replacement. Then the `Unconfirmed`
Bases view lists what has been pending too long, which is the only reason the state exists
([`../patterns/status-callouts.md`](../patterns/status-callouts.md),
[`../practices/audit-the-base.md`](../practices/audit-the-base.md)).
