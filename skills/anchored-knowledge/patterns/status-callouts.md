# Status callouts

**Use when** a note's status needs something a property cannot say: what would close it, what it
replaced, what nobody has settled, or the words somebody actually said. The property carries the
state; the callout carries what a reader must see.

**Skeleton.** The closed set. A note carries at most two, and a confirmed rule carries none.

```markdown
> [!warning] Draft — pending operations lead, as of 2026-11-08
> Confirmation expected at the 2026-11-18 review. See [[Q-0003]].

> [!todo] Needs review — inherited, source unknown
> Adopted from the previous base with no anchor. [[Q-0007]] asks where it came from.

> [!abstract] Superseded by [[LABEL-5]] — 2026-11-08
> Earlier understanding: one label per order, anchored at [[order-fulfilment-sow-v3]] §4.2. It held
> because splitting did not exist. See [[CH-0003]].

> [!failure] Out of scope — Phase 1
> Deferred to a future phase. If it returns, it arrives through [[SW-0002]].

> [!question] Open
> Who may void a printed label is unsettled. See [[Q-0003]].

> [!quote] Evidence
> "once it's submitted that address is locked"
> — Dana Lee, [[2026-01-21-order-fulfilment-scope-call]] 00:14:22
```

**Notes.**
- **The callout never restates the status property**, and the property is never omitted because a
  callout is present. `status: draft` plus a `[!warning] Draft` callout is one state said twice, one
  of which will rot ([`../anti-patterns/status-in-two-places.md`](../anti-patterns/status-in-two-places.md)).
- **Every callout carries a date**, and a draft names the stakeholder it waits on. "Pending
  confirmation" with nobody named has no owner, so nothing can close it
  ([`../anti-patterns/a-draft-with-no-date.md`](../anti-patterns/a-draft-with-no-date.md)).
- `[!question] Open` is for a statement that is *partly* settled — the usual case. It attaches the
  open part to the clause it belongs to, which a status property cannot do
  ([`open-question.md`](open-question.md)).
- `[!abstract] Superseded` keeps the previous understanding **and its anchor**. That is what makes
  "did we ever agree to that?" answerable in one read
  ([`../principles/deprecate-never-delete.md`](../principles/deprecate-never-delete.md)).
- `[!quote] Evidence` is the only place verbatim words belong, and it names speaker, meeting note and
  timestamp. More than one quote on a note means the statement is doing two jobs.
- These six and no others. A closed set is checkable; an open one becomes decoration
  ([`../references/vault-convention.md`](../references/vault-convention.md) §6).

**Related.** [`note-frontmatter.md`](note-frontmatter.md),
[`business-rule-note.md`](business-rule-note.md), [`source-note.md`](source-note.md).
