# A frozen brief is appended, never rewritten

**Rule.** When building starts the brief's `status` becomes `frozen` and everything above the freeze
line stops changing. New learning goes into an `## Amendments` section as a dated entry naming who
decided. A second amendment on one slice is a signal to stop and reshape, not to write a third.

**Why.** The amendment log is the only evidence anybody will ever have about how often the premises
were wrong, and that number is what tells you whether slices are sized right. Editing the brief in
place produces a document that was always correct, about a project that kept being surprised, and
destroys the one measurement that would have improved the next ten slices.

It also protects the rulings. A keep/change/drop row carries a person's name and a date because
somebody will ask in six months why the system behaves this way. A row that was silently rewritten
answers that question wrongly, with full confidence, in that person's name.

**In the slice.**
- `shaping` → `frozen` → `flipped`. The freeze is an event with a date in front matter, not a mood
  ([`../patterns/slice-brief.md`](../patterns/slice-brief.md)).
- An amendment states what was learned, what changed, who decided and when. One line each is enough.
- Scope that arrives after the freeze is usually a new slice, not an amendment. Amend when the slice
  cannot ship without it; otherwise add it to the backlog and keep going.
- A shipped brief is never retro-edited. If something dropped turns out to be needed, that is a new
  slice ([`../practices/file-a-finding.md`](../practices/file-a-finding.md)).

**Breaks when.** The record is smoothed so the plan appears to have been right all along →
[`../anti-patterns/a-deferral-with-no-reason.md`](../anti-patterns/a-deferral-with-no-reason.md).
