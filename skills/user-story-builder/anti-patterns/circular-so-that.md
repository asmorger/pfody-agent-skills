# Circular "so that"

**Smell.** "…I want to void a printed label, so that I can void the label." "…so that it is in
scope." "…so that I can see the detail page." The clause is present, grammatical, and says nothing.

**Why it is wrong.** The *so that* is the only place the story records why the work is worth doing,
and it is what a product owner uses to decide whether to cut it. Restated, the story has no business
rationale at all — so when the sprint is over-committed, nobody can compare this story against
another, and the decision gets made on size instead of value. It also hides a real question: if the
business reason cannot be stated, it may be that nobody has one.

**Instead.** Apply the swap test: if the *so that* could be moved into the *I want to* and still make
sense, it is circular — rewrite it. Name the consequence outside the system: "so that a cancelled
order is not collected by the carrier", "so that I can challenge the carrier's invoice". Where no
source gives you a reason and you cannot infer one honestly, that is an Open Question, not a filled
clause ([`../patterns/as-a-i-want-so-that.md`](../patterns/as-a-i-want-so-that.md),
[`../practices/review-an-existing-story.md`](../practices/review-an-existing-story.md)).
