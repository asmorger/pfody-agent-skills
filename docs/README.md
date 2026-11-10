# docs

Standing documents that belong to no skill, plus the worked example they refer to. Each page is one
self-contained HTML file: open it in a browser, or publish it as a Claude artifact from the same file.

## Pages

| File | Audience | What it carries |
| --- | --- | --- |
| [`survey-slice-suite.html`](survey-slice-suite.html) | engineers, tech leads | The three artifacts and their lifespans, field templates for both written documents, the four correction loops, and the routing table that gives every kind of wrongness one destination. |
| [`one-hour-per-slice.html`](one-hour-per-slice.html) | PM / PO | The same practice from the product side: what we read out of the old system ourselves, the three short decisions needed per slice, and how a switch is made safe. |
| [`the-identity-seam.html`](the-identity-seam.html) | both | A worked example on user management. Why identity is sliced by population rather than by workflow, the authentication/authorization seam that defers the hardest question, and the survey's twenty questions sorted by who can answer each one. |

## The practice

All three describe one way of modernising a legacy desktop application with agents while keeping
XP's actual commitments rather than its artifacts. A **survey** is derived from the old code and
deleted at the flip; a **slice brief** is decided, frozen at build start, and superseded at the
flip; a **characterization suite** is the only artifact allowed to outlive a slice, and the only
one that can fail. The pages are a set and change together.

## Worked example

```
examples/
  survey/user-management.md            derived, disposition: surveyed
  slices/012-internal-signin-entra.md  decided, frozen 2026-11-13
```

These are the artifacts in the formats the practice specifies, as a template to copy. The numbers,
file paths and table names in them are plausible but invented: they are a worked example, not a
record of a real system. Regenerate a survey against real code before trusting a line of it.

The slice is numbered 012 deliberately. Identity wants a schema change and a shared-code change,
both of which the blast-radius rule excludes, so it should not be anyone's first area.

## Published copies, all private

- `survey-slice-suite` &mdash; <https://claude.ai/artifact/5kC2QPDpawMYhNxAm2ydu1>
- `one-hour-per-slice` &mdash; <https://claude.ai/artifact/AU9eJBeecmAs38MB8fd3pA>
- `the-identity-seam` &mdash; <https://claude.ai/artifact/2en6SWFSsC1BDonYpxreGo>

## Before editing a page

They are artifact sources, so they carry no `<!doctype>`, `<head>` or `<body>` of their own &mdash;
the Artifact publisher supplies that skeleton, and adding one by hand breaks the publish.

They are also deliberately pure ASCII (`&middot;` as an entity, the `\00d7` CSS escape), so they
render the same published or opened straight from disk, where nothing declares a charset. The
markdown under `examples/` is ordinary UTF-8 and carries literal `·`; that constraint applies only
to the HTML.
