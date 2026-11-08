# An unanchored rule

**Smell.** A rule row that reads like settled fact and names no source, carries no date and wears no
marker. "An order on credit hold cannot be labelled." True, probably. From where, nobody knows.

**Why it is wrong.** A knowledge base is read by people who will not check it — that is the whole
point of having one — so an unanchored rule is believed exactly as strongly as an anchored one. The
cost lands on whoever builds from it, and it compounds: the next source arrives, contradicts the rule,
and reconciliation cannot weigh the conflict because one side has no authority level. The rule also
cannot be defended commercially. "We never agreed to that" has no answer.

**Instead.** Anchor it or flag it. Anchored means the inline date points at a Source Register row that
names this rule id. Flagged means a dated `Draft` marker naming the stakeholder it is pending on, or
`Needs Review` when it was inherited and nobody knows. Both take one clause. Backfilling an adopted
base means adding markers and questions, never inventing the source that would have justified it
([`../principles/anchor-or-flag.md`](../principles/anchor-or-flag.md),
[`../patterns/source-register-row.md`](../patterns/source-register-row.md)).
