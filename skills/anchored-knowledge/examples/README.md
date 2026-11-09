# Worked example: an Order Fulfilment vault

`vault/` is a small, complete, internally consistent knowledge record in the shape this skill
writes. **Open `vault/` in Obsidian** and start at `moc/knowledge.md`.

It is invented — a neutral Order / shipping-label domain, no real client — and it is the fixture the
bundled script is tested against.

## What to look at

| Look at | To see |
|---|---|
| `moc/knowledge.md` | the home note: what may be cited, the baseline, what is open now |
| `moc/business-rules.md` | a MOC: prose, an embedded Bases view, and a generated snapshot |
| `rules/order-address-frozen-on-confirmation.md` | a confirmed rule — twelve lines, no callout needed |
| `rules/confirmed-order-may-split-across-parcels.md` | a draft, with the stakeholder and date that can close it |
| `rules/one-label-per-order.md` | a superseded rule, deprecated in place, keeping its id |
| `rules/bulk-printing-across-orders.md` | out of scope, and still answering "did we agree to that?" |
| `glossary/parcel.md` | a retired term kept as an alias, so `[[Shipment]]` still resolves |
| `sources/order-fulfilment-sow-v3.md` | a source note whose **backlinks** are what it anchored |
| `sources/2026-11-08-operations-review.md` | a meeting note with the verbatim quote behind a rule |
| `decisions/credit-hold-blocks-labelling.md` | the one long note type: reasoning and rejected alternatives |

The graph view is worth a look: rules cluster by topic, every rule reaches a source, and the two
meeting notes sit where the evidence does.

## Try the script

    cd vault
    python3 ../../scripts/vault.py lint .    # → ok
    python3 ../../scripts/vault.py moc  .    # → silent; the snapshots already match the notes

Then break something and watch it get caught — change a `status` to a value outside the vocabulary,
point a link at `[[ORDER-99]]`, or empty a confirmed rule's `sources`:

    python3 ../../scripts/vault.py lint .
    3 findings
      rules/order-address-frozen-on-confirmation.md: dangling wikilink [[ORDER-99]]
      rules/order-address-frozen-on-confirmation.md: status 'agreed' is not valid for type 'business-rule'
      rules/credit-hold-blocks-labelling.md: status confirmed with no sources

To see the snapshots regenerate, edit a rule's `status` and run `moc` again. The diff is the whole
point: it shows what moved, and nothing else in the note is touched.

## What is deliberately imperfect

`scope/negotiated-carrier-rates-excluded.md` rests on nothing but internal interpretation and says so
with a `[!todo] Needs review` callout — an honest level-5 boundary is a real thing a record holds, and
the `sources` MOC grouped by authority is where you would notice it. `Q-0004` is `blocked` rather than
open, because the question behind it cannot be asked until `SW-0002` is settled.

There is no `.obsidian/` folder here, so Obsidian will create its own on first open.
