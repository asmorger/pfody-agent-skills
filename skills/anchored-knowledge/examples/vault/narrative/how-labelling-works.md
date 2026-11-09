---
type: narrative
status: current
audience: internal
derived-from: [rules, scope, decisions, questions]
covers-through: 2026-11-08
input-manifest-sha256: 5e92a4f5e431ea2d837905e834a1456cd86060d8166cb6978ff8b491110ea2b8
aliases: [How labelling works]
tags: [narrative]
---

# How labelling works

> [!warning] Illustrative example only
> The company, the sources, the numbers and the decisions are invented. Do not use them as evidence.

The readable story of order labelling, derived from the notes. **It owns no facts.** Every statement
below is a one-line summary of a note that holds it, with the link to that note; the detail, the
evidence and the status live there. Regenerate it with `vault.py narrative` after the notes move.

## What the system does

- One label per parcel, so a split order gets one label per box
  ([[one-label-per-parcel|LABEL-1]]).
- A confirmed order's shipping address is frozen, so a label cannot be created against an address
  that has since changed ([[order-address-frozen-on-confirmation|ORDER-1]]).
- An order on credit hold cannot be labelled, and the hold is checked at label creation rather than
  at despatch ([[credit-hold-blocks-labelling|ORDER-2]], decided in
  [[enforce-credit-hold-at-label-creation|ADR-0004]]).
- A printed label may be voided, though who may do it is still open
  ([[a-printed-label-may-be-voided|LABEL-2]], [[who-may-void-a-printed-label|Q-0003]]).

## What it deliberately does not do

- Bulk printing across orders is out of scope for this phase
  ([[bulk-printing-excluded|scope]], [[bulk-printing-across-orders|LABEL-3]]).
- Negotiated carrier rates are out of scope
  ([[scope/negotiated-carrier-rates-excluded|negotiated carrier rates]]).

## What could still change the shape

- Splitting a confirmed order across parcels is only a draft understanding, and the rule it would
  replace is already superseded ([[confirmed-order-may-split-across-parcels|ORDER-5]],
  [[one-label-per-parcel-not-per-order|CH-0003]]).
- Partial despatch of a split order is unanswered, and it is what
  [[order-splitting-across-parcels|SW-0002]] is watching
  ([[partial-despatch-of-a-split-order|Q-0004]]).

## Gaps found while deriving

Each line is something this story needed and no note holds. They are listed, never written here.

- Nothing records what happens to a voided label's carrier charge. Belongs in a rule, once somebody
  can answer it — raise it as an open question first.
- No note says who pays for a reprint after a carrier rejection, although
  [[carrier-truncates-address-line-1|K-0001]] records the rejection itself.
