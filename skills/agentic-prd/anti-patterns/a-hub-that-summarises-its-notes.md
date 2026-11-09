# A hub that hand-summarises its notes

**Smell.** Section 1 of the PRD restates the outcome metric in a sentence — "we want the address
error rate down to about 1.5%" — beside an `OUT-1` note that holds the baseline, the population, the
denominator and the window. Section 4 lists the requirements in prose. Section 7 has a table of
sources that also exist as notes. Each summary is shorter and reads more easily than the embed would.

**Why it is wrong.** It is the one-home rule broken in the one document everybody reads. The summary
and the note will diverge — the note gets the correction because it is what the check and the
coverage table read, and the hub keeps the old number because nobody re-reads prose they wrote. Then
a cold reader, which is exactly who the hub exists for, takes the number from the hub. The failure is
worse here than anywhere else in the vault precisely because the hub is the entry point: a stale fact
in a requirement note is one wrong requirement, and a stale fact in section 1 is the brief everybody
builds from.

**Instead.** Embed it: `![[address-error-rate-on-parcels]]` — an embed targets the filename and
takes no display text. It resolves to whatever the note says now, so the hub cannot go stale, and a
reader scrolling the hub still sees the whole metric without following a link, which is the cold-read
property the prose was protecting. Keep as prose only what has no note behind it: the narrative, the
scope boundaries, the agent boundaries, the rollout, the protocol. If you find yourself wanting to
summarise a note, that is the signal the note belongs in an embed
([`../patterns/prd-hub-note.md`](../patterns/prd-hub-note.md),
[`../principles/the-prd-owns-why-and-what.md`](../principles/the-prd-owns-why-and-what.md)).

**What this does not forbid.** The failure above is a **hand-written** summary, not summarising as
such — prose nobody re-reads, beside a note that gets the correction. A summary that is *derived* and
*checked* has none of that: every statement carries the link to the note it came from, the whole
thing is regenerated when the notes move, and a check fails it when it goes stale or when a claim
carries no link. That is worth having, because an embed renders **only inside Obsidian** — on GitHub,
in a diff, or to an agent reading the raw file, `![[address-error-rate-on-parcels]]` is a line of
nothing. When the PRD has to be readable outside Obsidian, render it rather than retyping it:
[`../practices/render-a-readable-prd.md`](../practices/render-a-readable-prd.md).
