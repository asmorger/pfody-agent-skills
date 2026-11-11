# Absence needs an exhaustive sweep

**Rule.** A claim that something is referenced nowhere, used by nobody or dead needs a complete sweep
of every corpus it could hide in, and the tag says so: `[code: exhaustive sweep of client, reports,
stored procedures]`. A ranked or semantic search cannot support a negative, however good its top
results are.

**Why.** The most valuable findings a survey produces are negatives. "Thirty-one of the forty-one
groups are referenced nowhere" retires a feature, answers a question the business could not answer
about itself, and costs one sweep. It is also the single easiest claim to get wrong, because a search
that returns nothing looks identical whether the thing is absent or merely phrased differently three
files away.

The asymmetry is what matters. A false positive is caught the moment someone opens the file. A false
negative deletes a behaviour that twelve people depended on, and is discovered in production.

**In the slice.**
- Name the corpora swept, not just the tool. Client code, reports, stored procedures, scheduled jobs
  and integration configuration are five different places, and a sweep of one is not a sweep.
- Where the thing is a string compared at runtime, sweep for the literal, not for the concept. A
  group name tested as `"WHSE_SUPER"` is invisible to a search for permissions.
- Pair every absence claim with a count from the other direction: how many rows still hold the thing
  nobody reads. Those two numbers together are what makes a `DROP` ruling safe.
- A behaviour that is merely *unreachable from the screens* is not absent. Say which, and tag the
  rest `[assumed:]` ([`every-line-carries-its-provenance.md`](every-line-carries-its-provenance.md)).

**Breaks when.** A top-k result is written down as an absence, and a `DROP` ruling is taken against
it → [`../anti-patterns/a-deferral-with-no-reason.md`](../anti-patterns/a-deferral-with-no-reason.md).
