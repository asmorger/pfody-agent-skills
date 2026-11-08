# Slice by outcome, not by layer

**Rule.** A User Story is a vertical slice of one Feature: one person builds, tests and demos it
inside one sprint, and what they demo is something a named role can do. A story that delivers a
table, an endpoint, a service or a screen with nothing behind it is not a story.

**Why.** A layer cannot be demonstrated, so it cannot be accepted, so it cannot be refused — the
feedback the sprint exists to produce never arrives. Layer slices also fail together: three of four
done means nothing works, where three of four outcome slices means three things work. The one-person
test is deliberate. It bounds the slice by what can be held in one head and finished, which is also
what makes an estimate possible without the PRD carrying one.

**In the PRD.**
- A valid story produces a workflow, persisted data, enforcement, permission behaviour, integration
  behaviour or a reporting output
  ([`../practices/slice-a-feature.md`](../practices/slice-a-feature.md)).
- A specific role, never "user". A need, never a screen. The *so that* clause gives a business
  reason and does not restate the need.
- Keep a failure path with its main path when one person can build and demo both; split it when its
  complexity is separate. This is judgement, and no check tests it.
- `P0` and `P1` requirements may share a story, tagged with the highest. A `P2` goes in its own story
  tagged `Stretch`. `P3` is not sliced at all.

**Breaks when.** Stories come out named for the stack →
[`../anti-patterns/slicing-by-layer.md`](../anti-patterns/slicing-by-layer.md).
