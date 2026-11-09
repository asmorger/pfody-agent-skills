# Status recorded as a rule

**Smell.** "The label service is assigned to the integrations team." "Bulk printing is behind a
feature flag." "Carrier work starts in sprint 14." "The address parser is nearly done." Sixty items
out of a standup, each properly cited.

**Why it is wrong.** This is the dominant failure of the whole skill, and it conceals itself: a long
index looks thorough. What it does is bury the dozen real rules among fifty progress notes, so the
reader who needs the rule cannot find it and the reader who finds a status line treats it as a
requirement. Status is also the fastest-decaying content in any transcript — the assignment changes,
the flag is removed, the sprint slips — so a status-heavy index is stale on the day it is rendered,
while still carrying citations that make it look current.

**Instead.** Apply the test: could this sentence be written into a specification? "Users authenticate
via SSO" passes; "SSO is assigned to Priya" does not. Expect three to fifteen items from an hour, and
expect **few or none** from a standup — that is a correct result, not a failed extraction. Never
extract to a count ([`../principles/precision-over-volume.md`](../principles/precision-over-volume.md),
[`../practices/curate-a-large-corpus.md`](../practices/curate-a-large-corpus.md)).
