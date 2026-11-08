# Renumbered rule ids

**Smell.** `ORDER-4` was deprecated, so `ORDER-5` became `ORDER-4` and the section numbers run
cleanly again. Or a rule inserted at the top of a table took `ORDER-1` and everything below shifted.
The table is tidier than it was.

**Why it is wrong.** The id is the entire value of this base to everything downstream — a story's
source grounding, an acceptance criterion, a test name, a pull request, a tracker tag, another rule's
cross-link. Renumbering re-points every one of those at a different rule, and nothing fails: the test
still passes, against the wrong rule. The damage is also invisible from inside the base, because all
its internal cross-links were updated in the same pass.

**Instead.** Take the next free number in the section, whatever row the rule goes in — position and
number are unrelated. Leave gaps where rules were deprecated; a gap is information. The immutability
is what lets the text be refined aggressively: rewrite the wording freely, because the id is what was
cited, not the sentence
([`../principles/ids-are-immutable.md`](../principles/ids-are-immutable.md),
[`../practices/write-a-business-rule.md`](../practices/write-a-business-rule.md)).
