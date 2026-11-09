# Category taxonomy

**Use when** deciding how items are grouped and how their ids are formed. Two ways: seed it, or let
it emerge. Seed it on any domain you already understand.

**Skeleton.** Seeded, in the config — ordered, each with its prefix:

```yaml
categories:
  - {name: "Orders",        prefix: "ORDER"}
  - {name: "Labels",        prefix: "LABEL"}
  - {name: "Carrier",       prefix: "CARR"}
  - {name: "Scope & Phasing", prefix: "SCOPE"}
```

Emergent: omit `categories` and put a sensible `category` on each item. The tool derives a prefix and
orders the sections by first appearance.

**Notes.**
- Seeding keeps ids and section order stable across runs, which is what makes them citable from
  outside ([`../principles/ids-are-stable-across-runs.md`](../principles/ids-are-stable-across-runs.md)).
- It is also how the output is made to mirror an existing rules document: same sections, same
  prefixes, so the two read side by side
  ([`../practices/seed-the-taxonomy.md`](../practices/seed-the-taxonomy.md)).
- **Reuse an existing item's category name exactly.** "Labels" and "Labelling" are two sections with
  two prefixes for one topic, and the dedup will not merge across them.
- Emergent is right for a one-off exploration of a domain you do not know yet — and only then.
- Ids are per category, so a category added later does not disturb the numbering of the others.

**Related.** [`tool-config.md`](tool-config.md), [`rendered-index.md`](rendered-index.md).
