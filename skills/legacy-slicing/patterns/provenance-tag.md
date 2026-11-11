# Provenance tag

**Use when** writing any line in a survey. The tag says where the line came from, and therefore how
much of the reader's scepticism it deserves.

**Skeleton.** One tag per observed behaviour, weakest honest tag wins.

```markdown
[code: LabelSvc.cls:112]          read it; the file and line are the proof
[db: trigger tr_label_post]       queried the schema or the object
[logs: 1,308 in 24 months]        measured it in production
[told: ops lead, 2026-10-14]      a person said so; who, and when
[assumed: unverified]             a guess; the sentence says "suspected"

[code: exhaustive sweep of client, reports, stored procedures]
                                  an absence claim, with the corpora named
```

**Notes.**
- The tag governs the verb. `[code:]` lines say *does*; `[assumed:]` lines say *appears to* or
  *suspected*. A confident sentence under a weak tag is the defect this pattern exists to stop.
- `[told:]` without a name and a date is not a tag. "The business said" is unfalsifiable six months
  later, and the person usually remembers something narrower than what was written down.
- `[logs:]` carries its window and its denominator. "Never fires" is a claim about a period.
- An absence claim needs an exhaustive sweep and names what was swept. A ranked search result is
  never an absence
  ([`../principles/absence-needs-an-exhaustive-sweep.md`](../principles/absence-needs-an-exhaustive-sweep.md)).
- Tags only ever get weaker. Finding that a `[code:]` line was actually inferred is a correction to
  make and a finding to file, never a tag to quietly leave in place
  ([`../practices/file-a-finding.md`](../practices/file-a-finding.md)).

**Related.** [`survey-note.md`](survey-note.md),
[`../principles/every-line-carries-its-provenance.md`](../principles/every-line-carries-its-provenance.md),
[`../anti-patterns/tests-written-from-the-survey.md`](../anti-patterns/tests-written-from-the-survey.md).
