# Vague requirement

**Smell.** "The system shall respond quickly." "Labels shall be easy to reprint." "The screen shall
behave appropriately when the carrier is unavailable." "Performance shall be robust." An adjective
where a threshold belongs, with no number anywhere in the row.

**Why it is wrong.** The requirement cannot be given a verify method, so it cannot be tested,
accepted or refused — it will be marked done by whoever implements it, against their own reading. It
also hides the question that was actually open: "quickly" always meant a number somebody knows or
nobody has decided, and the vague wording is what stopped that being asked while it was cheap.

**Instead.** Put the threshold in the requirement, with its condition: "When a clerk requests a
label, the system shall return the label or an error within 3 seconds at the 95th percentile." If
nobody has given you the number, that is an open question and the requirement is `PROPOSED` until it
is answered — never a word standing in for a number
([`../principles/one-behaviour-per-requirement.md`](../principles/one-behaviour-per-requirement.md),
[`../patterns/requirement-row.md`](../patterns/requirement-row.md)).
