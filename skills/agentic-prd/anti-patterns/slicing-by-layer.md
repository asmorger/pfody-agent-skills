# Slicing by layer

**Smell.** A Feature's stories named for the stack: "US-01 Create the label table", "US-02 Add the
carrier API client", "US-03 Build the label screen", "US-04 Wire it together". Each is estimable,
each is clean work, none of them can be demonstrated.

**Why it is wrong.** The sprint's purpose is feedback, and a layer produces none: nothing can be
shown, so nothing can be accepted or refused, and the first time anyone sees the behaviour is after
all four stories land. They also fail together — three of four done means nothing works, where three
of four outcome slices means three things work. The last story is always the integration story, which
is always where the surprises are, which is why it is always late.

**Instead.** Group by outcome: the thinnest path a named role can walk end to end, then the next one.
"Create a label for a confirmed order" touches table, client and screen, and it can be demoed on the
day it is finished. Slice the next story by a different outcome — a failure path, a second role, a
bulk case — not by a different layer
([`../principles/slice-by-outcome-not-by-layer.md`](../principles/slice-by-outcome-not-by-layer.md),
[`../practices/slice-a-feature.md`](../practices/slice-a-feature.md)).
