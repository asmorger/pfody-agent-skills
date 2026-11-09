---
type: reference
topic: integration
status: confirmed
governs: ["[[one-label-per-parcel|LABEL-1]]", "[[carrier-truncates-address-line-1|K-0001]]"]
sources: ["[[carrier-api-reference]]"]
created: 2026-11-08
updated: 2026-11-08
---

# Order Data Mapping

How order fields map to the carrier's label request. The rules that depend on this are [[one-label-per-parcel|LABEL-1]]
and the constraint [[carrier-truncates-address-line-1|K-0001]].

## Field map

| Order field | Carrier field | Notes |
| --- | --- | --- |
| `order.shipTo.line1` | `AddressLine1` | Truncated at 35 characters by the carrier ([[carrier-truncates-address-line-1\|K-0001]]); validate before sending. |
| `order.shipTo.postcode` | `PostCode` | Uppercased, spaces removed. |
| `parcel.weightGrams` | `WeightKg` | Divided by 1000, rounded up to 2 decimal places. |
| `parcel.id` | `ClientReference` | One label per parcel, so this is the idempotency anchor. |

## Not mapped

`order.customerNotes` is not sent. The carrier has no field for it and it may contain customer
personal data.
