# An invented citation

**Smell.** A source whose `turn_id` is plausible but not in the brief. A timestamp estimated from
where the topic seemed to be. A quote tidied into grammatical English. A speaker attributed because
they were the one who usually said that kind of thing — in a file that carries no speaker labels at
all.

**Why it is wrong.** The citation is the entire difference between this document and a summary. An
invented one makes an unverifiable statement look verified, which is strictly worse than leaving it
out, and the place it gets discovered is a commercial conversation: someone opens the transcript at
`0:17:11` and finds nothing. The tool enforces the floor — `validate()` rejects an item with no
sources and `merge` drops unsourced items and counts them — so a fabricated source is the only route
by which an uncited statement reaches the index.

**Instead.** Copy the `turn_id` and the quote from the brief line, as they are. Keep the quote short
and verbatim, hedges included. Where the export carries no speaker, leave the field empty and let the
citation be meeting plus date. And where you cannot find a line that says it, drop the item — a rule
you believe but cannot cite belongs in the conversation with the user, not in the index
([`../principles/every-item-carries-a-source.md`](../principles/every-item-carries-a-source.md),
[`../patterns/transcript-brief.md`](../patterns/transcript-brief.md)).
