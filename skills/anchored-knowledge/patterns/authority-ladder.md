# Authority ladder

**Use when** two sources disagree, or when registering a source. Strongest to weakest; prefer higher,
record the conflict, never resolve it silently.

**Skeleton.** The default ladder, suited to a client-services engagement:

    1  Contractual baseline        SOW, signed change request
    2  Approved requirements       accepted requirements, stories, acceptance criteria
    3  Client clarification        named stakeholder answer, approved Q&A, meeting decision
    4  Source artifact             spreadsheet, sample file, export, current-system behaviour
    5  Internal interpretation     team analysis, an inferred rule
    6  Unreviewed intake           draft note, brainstorm, uncited memory

Recorded on each source note as `authority: 3-client-clarification`, and on every note that cites
it, so a conflict can be weighed without opening the source.

**Notes.**
- Overridable per project in the config. An internal project with no SOW names what serves as its
  scope baseline instead, and the rest of the ladder shifts up
  ([`knowledge-config.md`](knowledge-config.md)).
- Level 4 is evidence of what the system *does*, which is not the same as what it *should* do. It
  loses to levels 1–3 on intent and beats them on current behaviour.
- A higher level winning does not make the lower statement disappear. It is recorded as the previous
  understanding ([`knowledge-change-entry.md`](knowledge-change-entry.md)).
- Equal levels do not settle anything. Two level-3 clarifications that disagree are an open question
  ([`open-question.md`](open-question.md)).
- A record resting mostly on levels 5 and 6 is a record nobody has confirmed. The sources MOC groups
  by `authority`, so this is visible rather than a judgement you have to make
  ([`../principles/authority-is-explicit.md`](../principles/authority-is-explicit.md)).

**Related.** [`source-note.md`](source-note.md), [`scope-watch-item.md`](scope-watch-item.md),
[`../principles/conflicts-are-recorded-not-resolved.md`](../principles/conflicts-are-recorded-not-resolved.md).
