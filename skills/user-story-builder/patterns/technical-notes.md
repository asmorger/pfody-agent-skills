# Technical Notes

**Use when** there are implementation-shaping facts that do not belong in business-facing prose.
Terse bullets, never paragraphs, and never a restatement of `Details` or the criteria.

**Skeleton.**

```markdown
**Technical Notes**
- **Permission**: Void label
- **Feature flag**: labels.void
- **Design assets**: None
- **Resource-scoped authorization**: only the clerk who printed the label may void it (LABEL-4).
- **Validation highlights**: the carrier truncates address line 1 at 35 characters.
```

The three header bullets are always present, even as `None`. Everything below them appears only when
a source explicitly addresses it.

**Notes.**
- **Permission**: the conceptual capability gating the work — "Void label", "View labels". Use the
  config's `permission_model` source verbatim where it names one; otherwise state the capability
  conceptually. `None` only when no auth gate applies.
- **Feature flag**: the flag name, `None`, or `To be determined by engineering`.
- **Design assets**: links from the config's `design_asset_source`, or `None`. Never a placeholder
  link.
- Optional bullets — entity base, tenant scoping, resource-scoped authorization, validation
  highlights, out of scope — appear **only** when sourced. Silence means "Not specified in source" or
  omission ([`../principles/pattern-matching-is-not-a-source.md`](../principles/pattern-matching-is-not-a-source.md)).
- Do not infer entity behaviour, tenancy or ownership from a feature's name. Where the config lists
  `entity_base_options`, engineering chooses — describe the need, assert nothing.
- Omit tenancy entirely when the config's `tenancy_term` is `None`
  ([`../principles/vocabulary-comes-from-the-config.md`](../principles/vocabulary-comes-from-the-config.md)).
- Out-of-scope callouts are the exception, not the habit: state one only when a prior version
  included the capability, a stakeholder asked for it to be visible, or it resolves a real ambiguity
  ([`../anti-patterns/a-gratuitous-out-of-scope-callout.md`](../anti-patterns/a-gratuitous-out-of-scope-callout.md)).

**Related.** [`user-story.md`](user-story.md), [`knowledge-config.md`](knowledge-config.md).
