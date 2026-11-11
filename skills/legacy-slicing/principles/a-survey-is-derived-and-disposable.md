# A survey is derived and disposable

**Rule.** A survey is regenerated, never corrected by hand, and never edited to record a decision. It
is deleted at the flip, not archived. Its `status` moves `surveyed` → `reviewed` → `sliced` →
`replaced`, and `replaced` means the file is gone.

**Why.** Two things break the moment a ruling is typed into a survey. Observation and intention stop
being distinguishable, so every provenance tag in the file becomes a claim nobody can check — the
reader can no longer tell which lines were read out of the system and which were wished into it. And
the survey starts competing with the brief as the record of what was decided, which is how two
records of one decision drift apart.

Deleting it at the flip is the same argument one step later. By then its content lives in the
characterisation suite, in a form that fails when it goes stale. Keeping a prose copy beside an
executable one guarantees they will disagree, and guarantees nobody will know which to believe.

**In the slice.**
- A wrong line is regenerated, not patched. If regeneration is expensive, that is a tooling problem,
  not a reason to hand-edit.
- Rulings live in the brief's keep/change/drop table, which cites the survey's behaviour ids
  ([`../patterns/slice-brief.md`](../patterns/slice-brief.md)).
- `survey/` should be shrinking across a project. An area is surveyed one slice ahead, and retired
  one slice later ([`../anti-patterns/surveying-the-whole-app-first.md`](../anti-patterns/surveying-the-whole-app-first.md)).
- A survey is `citable: false` in the registry on purpose. A story, spec or test cites the ruling,
  never the observation
  ([`../references/vault-taxonomy.json`](../references/vault-taxonomy.json)).

**Breaks when.** A decision is recorded in the file that was supposed to be thrown away →
[`../anti-patterns/a-survey-edited-to-record-a-ruling.md`](../anti-patterns/a-survey-edited-to-record-a-ruling.md).
