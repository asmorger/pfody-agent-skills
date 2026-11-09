# Criteria padded to a count

**Smell.** Every story with exactly five criteria. The fourth and fifth restate the first in other
words, or test the framework — "Given the page, when it loads, then the page displays". Or a
criterion covering an edge case no source mentions, added to round out the coverage.

**Why it is wrong.** Padding makes coverage unreadable. A reviewer can no longer tell which criteria
are the behaviour and which are filler, so they check none, and the genuine gap — an edge case nobody
specified — hides among four restatements. Each padded criterion also becomes a test somebody writes
and maintains. The invented edge case is the worse half: it is an unsourced requirement that has
entered the build wearing a criterion's formatting.

**Instead.** Write what the source supports — typically three to seven, and fewer is correct when the
source specifies fewer. Order from the primary output outward to the edges and stop. Include criteria
for validation, errors or permissions **only** where a named source specifies behaviour for them;
silence means an Open Question or omission. If the story feels under-tested, it is under-specified,
and that is a gap to surface rather than fill
([`../principles/factuality-over-completeness.md`](../principles/factuality-over-completeness.md),
[`../patterns/acceptance-criterion.md`](../patterns/acceptance-criterion.md)).
