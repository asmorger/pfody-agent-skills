# The generated index shipped as finished

**Smell.** Forty transcripts in, one render out, and a message that says "here is the knowledge
index" with a count. No mention of status items that survived, no mention that one topic has three
overlapping notes, no mention that dedup is lexical — and no mention that none of it is citable yet.

**Why it is wrong.** Both limits at that scale are structural. Dedup is Jaccard over keywords, so the
same rule phrased differently in two meetings sometimes does not merge and a topic sprawls.
Extraction over-reaches on status-heavy meetings because a standup sentence is grammatically identical
to a rule. Presenting the output as finished transfers confidence it has not earned, and the reader
who acts on it will act on a duplicate or a stale assignment. The irony is that the honest framing is
*more* valuable: a sourced superset is worth a great deal, because every line in it can be checked,
which is the expensive part.

**Instead.** Say what it is — a fully-sourced superset to curate, and **evidence rather than
record** — and name the two jobs left: prune the status items, merge the near-duplicates. Report the
counts: items, meetings, files written and removed, unsourced drops. Every note carries
`citable: false` and the MOC opens with the warning, but neither is a substitute for saying it in the
report. Then offer the curation pass as its own run
([`../principles/a-large-corpus-is-a-superset.md`](../principles/a-large-corpus-is-a-superset.md),
[`../practices/curate-a-large-corpus.md`](../practices/curate-a-large-corpus.md)).
