# Surveying the whole app first

**Smell.** `survey/` holds forty files and no slice has shipped. The project has a "discovery phase"
with an end date. Somebody is pleased that the tooling made it fast, and there is talk of a
consolidated document so stakeholders can see the whole picture.

**Why it is wrong.** It reassembles the artifact the practice exists to avoid, and the speed is what
makes it tempting rather than what makes it safe. A complete survey is a requirements document that
happens to be derived: every line in it starts decaying the day it is written, the areas surveyed
first are stale by the time they are built, and nobody can tell which of the forty files still
matches the code. The counts go out of date silently, which is worse than the prose, because a stale
number reads exactly like a fresh one.

It also inverts the economics that justified surveying at all. A survey is cheap because it is
regenerated on demand and thrown away; forty of them are a maintenance liability, and the pressure to
hand-patch rather than regenerate becomes irresistible — which is how the next failure arrives
([`a-survey-edited-to-record-a-ruling.md`](a-survey-edited-to-record-a-ruling.md)).

**Instead.** Survey one area ahead of the slice being shaped, and retire each entry at its flip.
Across a project, `survey/` should oscillate between one and three files and trend down, while the
characterisation suite grows — those two signals together are what distinguish a delivery practice
from a documentation practice. If a stakeholder needs the whole picture, that is a derived summary
written deliberately, for that audience, on request, and marked with the date it was true
([`../principles/a-survey-is-derived-and-disposable.md`](../principles/a-survey-is-derived-and-disposable.md),
[`../practices/survey-an-area.md`](../practices/survey-an-area.md)).
