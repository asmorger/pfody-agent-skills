# Worked example

**The content here is invented.** There is no such legacy application, no such tables and no such
commit. The file paths, counts and dates are plausible fabrications in the neutral `Order` /
shipping-label domain the skills share, so the pair can be read end to end without a real codebase.
Regenerate a survey against real code before trusting a line of anything shaped like this.

One area, caught at the moment just before the flip:

    survey/label-printing.md        the derived note, at `status: sliced`
    slices/reprint-a-label.md       the decided brief, at `status: frozen`

The pair is shown pre-flip on purpose, because it is the only state in which both files legitimately
exist. One step later the brief becomes `flipped` and the survey is deleted, which is why a surviving
survey beside a flipped brief is one of the defects the checker reports.

Read them in that order. What the pair is meant to show:

- **Six behaviours, five different provenance tags.** The `[told:]` and `[assumed:]` lines are the
  ones the review actually spends its time on, which is the point of tagging at all.
- **An absence claim done properly** — B07 names the corpora swept, and is paired with a count of
  rows that still hold the thing nobody reads. That pairing is what makes the `DROP` safe.
- **Three question lists, split by who can answer.** Only the first went to the product owner.
- **A seam.** The slice changes reprint behaviour and deliberately leaves the void-reason vocabulary
  alone, which is how an open question (Q02) stays open without blocking the work.
- **`Decisions outstanding: 0` with two questions still unanswered**, because both became `DEFER`
  rows with reasons rather than dependencies.
- **An amendment**, appended after the freeze rather than edited into the body, recording that one
  survey line was wrong and what happened as a result.

Note what the brief is *not*: there is no narrative, no justification section, and nothing a reader
could mistake for a specification of the finished system. That lives in the characterisation suite,
which is the only artifact of the three that survives the flip.
