# Hand-parsing a transcript

**Smell.** A transcript read in this skill and turned into rules directly. A `.vtt` extracted, skimmed
and summarised into intake. Twelve meeting files read in one pass with a paragraph of findings each.

**Why it is wrong.** Reading produces a summary, and a summary is plausible, uncited and quietly lossy
in a specific place: the reversal buried at minute 73, which is almost always the most consequential
sentence in the file. There is no way to tell afterwards which statements were quoted and which were
compressed. The second cost is incrementality — a hand pass has no content hashes, so the next
transcript means re-reading everything or guessing what is new, and in practice the base stops being
updated.

**Instead.** Delegate to `transcript-knowledge-base`, which change-detects by content hash, parses the
formats, and renders per-turn citations with the quote behind every statement. Then do the part a
parser cannot: reconcile each item against the existing rules. The division is the point — mechanical
work mechanised, judgement kept
([`../principles/transcripts-are-delegated.md`](../principles/transcripts-are-delegated.md),
[`../practices/ingest-transcripts.md`](../practices/ingest-transcripts.md)).
