# A statement is not a quote

**Rule.** The `statement` is written like a line from a rules document: present tense, declarative,
self-contained, third person. Synthesise the rule; leave the speaker's words in the source's `quote`.

**Why.** The two have different jobs. The statement has to be readable by someone who was not in the
room and testable by someone building from it, which a quote almost never is — it depends on the
previous sentence, it hedges, it names people instead of roles. The quote has to be exactly what was
said, which a cleaned-up statement is not. Keeping them in separate fields means the index gets both
properties instead of a compromise, and it is why the rendered document can read like a hand-written
spec while every line stays checkable.

**In the index.**
- Good: "A label is created for the order's shipping address when a clerk requests it."
- Good: "A voided label cannot be reused; a new label must be created."
- Bad: "Dana said they'd probably do labels per parcel I think." Bad: "Per parcel, not per order."
- Self-contained means no "this", "that one" or "as above". The statement will be read on its own, in
  a table row ([`../patterns/rendered-index.md`](../patterns/rendered-index.md)).
- Use roles, not names, in the statement. Names belong in the source's speaker field.
- Present tense even for a future decision: the index describes the system as agreed, not the meeting.

**Breaks when.** Dialogue is pasted into the statement →
[`../anti-patterns/a-quote-as-a-statement.md`](../anti-patterns/a-quote-as-a-statement.md).
