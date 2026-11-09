# Anchored Knowledge Templates

Copy-paste note templates for the vault. One note per statement, named for what it says, with the id
in frontmatter. The contract these instance is
[`vault-convention.md`](vault-convention.md); the Bases definitions the MOCs embed are in
[`bases.md`](bases.md). Adapt folders, property names and prefixes to the project and record any
deviation in `anchored-knowledge.config.md` — an existing vault's conventions win.

Every note carries `type`, `status`, `created`, `updated` and `tags`, plus `id` and `aliases`
wherever there is an id. Quote wikilinks in properties: `sources: ["[[note name]]"]`.

---

# Reference Layer — the source of record

## Business rule — `rules/<kebab-title>.md`

```markdown
---
id: PREFIX-N
aliases: [PREFIX-N]
type: business-rule
status: draft | confirmed | needs-review | superseded | out-of-scope | rejected
topic: <topic, matching the tag's second segment>
authority: 1-contractual | 2-approved-requirements | 3-client-clarification | 4-source-artifact | 5-internal-interpretation | 6-unreviewed-intake
sources: ["[[source-note]]"]
confirmed: YYYY-MM-DD          # when status is confirmed
pending-on: <stakeholder>      # when status is draft
questions: ["[[<kebab-question>|Q-NNNN]]"]
decisions: ["[[<kebab-decision>|ADR-NNNN]]"]
supersedes: []
superseded-by:                 # a wikilink, when status is superseded
scope-watch: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [rule/<topic>]
---

# PREFIX-N — <Title: what the rule says>

One self-contained, testable sentence. Field and entity names in backticks
(`EntityName.fieldName`), cross-references as wikilinks ([[<other-note>|PREFIX-M]]).

**Also** [[<other-note>|PREFIX-M]] <why a reader of this rule wants it next> · [[term]]
```

A callout is added **only** when the property cannot say it. One of:

```markdown
> [!warning] Draft — pending <stakeholder>, as of YYYY-MM-DD
> What would close it, and the question it waits on: [[<kebab-question>|Q-NNNN]].

> [!todo] Needs review — inherited, source unknown
> What is being checked, and by whom.

> [!abstract] Superseded by [[<other-note>|PREFIX-M]] — YYYY-MM-DD
> The earlier understanding, with the anchor it rested on. See [[<kebab-change>|CH-NNNN]].

> [!failure] Out of scope — Phase N
> Deferred to a future phase. If it returns, it arrives through [[<kebab-watch-item>|SW-NNNN]].

> [!question] Open
> The part of this statement nobody has settled. See [[<kebab-question>|Q-NNNN]].

> [!quote] Evidence
> "the words somebody actually said"
> — Speaker, [[YYYY-MM-DD-meeting-note]] HH:MM:SS
```

## Glossary term — `glossary/<kebab-term>.md`

```markdown
---
type: glossary-term
term: <Term, as the project capitalises it>
aliases: [<Term>, <RetiredName>]
category: <core-concepts | systems-integration | roles | …>
status: confirmed
governed-by: ["[[<kebab-title>|PREFIX-N]]"]
sources: ["[[source-note]]"]
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [term/<category>]
---

# <Term>

Precise definition for someone new to the domain. Link the governing rule; never restate it.
```

Retired names go in `aliases` so autocomplete and search still find the note under the old word,
with a `[!abstract] Retired name` callout giving the date and the change note that renamed it. An
alias does **not** make `[[OldName]]` resolve. Renaming the file is what fixes the existing links —
Obsidian rewrites every one of them — and if a name has to keep resolving from outside the vault,
leave a one-line stub note at the old filename pointing here.

## Scope boundary — `scope/<kebab-boundary>.md`

```markdown
---
type: scope-boundary
status: confirmed
area: <feature area>
inclusion: included | not-included
authority: 1-contractual
sources: ["[[source-note]]"]
rules: ["[[<kebab-title>|PREFIX-N]]"]
scope-watch: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [scope/<area>]
---

# <Behaviour> is [not] included

One boundary, the source that decided it, and where it goes if it comes back. "No source addresses
them" is an honest entry — write it with `authority: 5-internal-interpretation`.
```

## Decision — `decisions/<kebab-title>.md`

The one note type that may run long. Up to 120 lines; the reasoning is the point.

```markdown
---
id: ADR-NNNN
aliases: [ADR-NNNN]
type: decision
status: proposed | accepted | superseded | deprecated | rejected
summary: One sentence. The decisions MOC reads it from here, so it is written once.
decided: YYYY-MM-DD
deciders: []
confidence: low | medium | high
rules: ["[[<kebab-title>|PREFIX-N]]"]
sources: ["[[source-note]]"]
supersedes: []
superseded-by:
review-when: <the event or date that triggers a review>
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [decision]
---

# ADR-NNNN — <Decision title>

## Context
Why the decision is needed. The problem and the constraints.

## Decision
What was decided, and where it is enforced ([[<kebab-title>|PREFIX-N]]).

## Consequences
**Easier.** What this buys.
**Harder.** Costs, risks, limitations, follow-up work.

## Alternatives
**<Name>.** Rejected: **how it fails** — not that it lost.

## Assumptions
Conditions that must stay true for this decision to hold.

## Related
[[<kebab-title>|PREFIX-N]] · [[term]] · [[source-note]]
```

A reversal is a **new** note naming what it supersedes; the old one takes `status: superseded`,
`superseded-by`, and a `[!abstract]` callout. A refinement that reverses nothing gets a dated
`[!info]` addendum on the existing note.

## Fact — `facts/<kebab-title>.md`, optional

```markdown
---
id: K-NNNN
aliases: [K-NNNN]
type: fact
status: confirmed
topic: <topic>
applies-to: <area, feature, workflow, integration>
confidence: low | medium | high
authority: 4-source-artifact
sources: ["[[source-note]]"]
rules: ["[[<kebab-title>|PREFIX-N]]"]
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [fact/<topic>]
---

# K-NNNN — <The fact>

One durable statement about the world that rules depend on.

**So.** The delivery, design, testing or risk consequence — and which rule exists because of it.
```

## Reference / convention note — `reference/<topic>.md`

No id, cited by name, no size budget. The home for mechanics a rule must not carry.

```markdown
---
type: reference
topic: <api | integration | build | sql | test | …>
status: confirmed
governs: ["[[<kebab-title>|PREFIX-N]]"]
sources: ["[[source-note]]"]
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [reference/<topic>]
---

# <Topic> Conventions

The purpose, in one sentence.

## <Section>
Rules, naming patterns, field maps, state machines, message contracts, examples. Link the decision
that set the convention ([[<kebab-decision>|ADR-NNNN]]).
```

---

# Governance Layer — sourcing and change control

## Source note — `sources/<kebab-name>.md`

```markdown
---
id: SRC-NNNN
aliases: [SRC-NNNN]
type: source
status: registered | stale | superseded
source-type: sow | requirements | stakeholder-answer | email | transcript | sample-file | vendor-doc
authority: 1-contractual
provider: <client | team | vendor | named role>
source-date: YYYY-MM-DD
location: <path, URL, or system-of-record link — the original, never an extraction>
citable: false
participants: []               # transcripts and meetings only
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [source/<source-type>]
---

# <Source name>

What it is and what authority it carries, in a line or two.

**Does not cover** <the gaps>. A statement about any of those does not come from here.
```

**Never list what the source updated.** Each rule names its own source, so this note's backlinks are
that list, always current. A meeting note is a source note with `source-type: transcript`, named for
its date — `sources/YYYY-MM-DD-<kebab-meeting>.md` — and may carry one `[!quote] Evidence` callout.

## Open question — `questions/<kebab-title>.md`

```markdown
---
id: Q-NNNN
aliases: [Q-NNNN]
type: open-question
status: open | partial | answered | blocked | dropped
owner: <name or role>          # mandatory
needed-by: YYYY-MM-DD          # mandatory
blocks: ["[[<kebab-title>|PREFIX-N]]"]
answered-by: []                # the rule or decision that now holds the answer
sources: ["[[source-note]]"]
scope-watch: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [question]
---

# Q-NNNN — <The question?>

The unresolved question, in one sentence.

**Best answer so far.** What is known, including evidence that does not settle it, labelled as not
settling it.

**Next.** Who will ask or decide, and which note the answer becomes.
```

Answered, it keeps **no** answer: `status: answered`, `answered-by` pointing at the rule or decision,
and one line saying who answered and when.

## Scope watch — `scope-watch/<kebab-title>.md`

```markdown
---
id: SW-NNNN
aliases: [SW-NNNN]
type: scope-watch
status: watch | clarify | in-scope | deferred | change-request | closed
owner: <name or role>
baseline: ["[[baseline-source]]"]
requested: ["[[newer-source]]"]
affects: ["[[<kebab-title>|PREFIX-N]]"]
questions: []
disposition:                   # filled by a person: outcome, date, source
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [scope-watch]
---

# SW-NNNN — <Watch item>

**Agreed.** What the baseline scopes, and where.

**Asked for.** What is now being requested, and by whom.

**Why it may cost more.** The surfaces it changes that the baseline priced as one.

**Recommendation.** In scope · clarify · defer · route to change control.
```

## Knowledge change — `changes/<kebab-title>.md`

```markdown
---
id: CH-NNNN
aliases: [CH-NNNN]
type: knowledge-change
status: proposed | accepted | needs-review | closed
change-type: contradiction | scope-refinement | terminology-shift | decision-update | requirement-update | source-correction
identified: YYYY-MM-DD
older: ["[[older-source]]", "[[<kebab-title>|PREFIX-N]]"]
newer: ["[[newer-source]]"]
affects: ["[[<kebab-title>|PREFIX-N]]"]
owner: <name or role>
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [change]
---

# CH-NNNN — <What changed>

**Previously.** What the team believed, and the anchor it rested on.

**Now.** What changed, and which newer source supports it.

**Interpretation.** Contradiction · refinement · terminology shift · correction — and why. This line
is what stops a refinement being logged as a reversal.

**Done.** The notes updated, superseded, added or opened, each as a wikilink.
```

Both anchor sets are mandatory. Every note in `affects` gets its own dated callout.

---

# Index notes

## MOC — `moc/<type>.md`

```markdown
---
type: moc
updated: YYYY-MM-DD
snapshot:
  type: business-rule
  columns: [id, title, status, sources]
  exclude-status: [superseded, rejected]
  group-by: topic
tags: [moc]
---

# <Title>

A few lines of prose: the baseline, what a reader may cite, what the views are for. Not generated.

![[<name>.base]]

<!-- generated: do not edit -->
<!-- /generated -->
```

Leave the markers empty and run `python3 scripts/vault.py moc <vault>` to fill them. Everything
between them is overwritten on every run; nothing else in the note is touched.

## Home note — `moc/knowledge.md`

```markdown
---
type: moc
updated: YYYY-MM-DD
review-cadence: <discovery / build / handoff cadence>
owner: <role>
tags: [moc]
---

# Knowledge

## What you may cite
The **record** is this vault: [[business-rules|Business Rules]], [[glossary|Glossary]],
[[scope|Scope]], [[decisions|Decisions]] and the notes in `reference/`. **Governance** —
[[sources|Sources]], [[open-questions|Open Questions]], [[scope-watch|Scope Watch]],
[[changes|Changes]] — is not citable as record. The **workbench** holds intake, drafts and the
transcript index: evidence, not record.

## Baseline
Contract, approved requirements, delivery baseline.

## Now
Questions needing answers, scope watch, decisions in flight, ingestion backlog.

## Recently changed
- YYYY-MM-DD — [[<kebab-change>|CH-NNNN]] <what changed>
```

`Now` and `Recently changed` are judgement, not a query, which is why they are the only tables in
the vault a person writes by hand.

---

# Workbench — never committed, never inside the vault

## Intake — `<working_dir>/intake/YYYY-MM-DD-<kebab-slug>.md`

```markdown
---
type: intake
status: untriaged | converted | archived
captured-by: <role or agent>
captured: YYYY-MM-DD
source: <meeting, email, file, chat, stakeholder>
---

# Intake — <short title>

Raw notes:
-

Triage destination:
- Record: <new rule / glossary / boundary / decision>
- Question: · Scope watch: · Change: · Source:
```

Plain markdown, no wikilinks to notes that do not exist yet. Raw notes stay raw.

## Reconciliation — `<working_dir>/reconciliations/YYYY-MM-DD-<source>.md`

Grouped into conflicts, refinements and new rules, each row giving the id, the **quoted** current
text, the incoming item and the recommendation — plus *also opening* and *already covered*. Tables
are right here and wrong in the record: this document is read once, by a person, as a diff
([`../patterns/reconciliation-audit.md`](../patterns/reconciliation-audit.md)).

## Transcripts — delegated, no template here

This skill does **not** hand-write meeting notes. Run the **`transcript-knowledge-base`** skill on
the transcripts folder, overriding its output paths into the workbench; it produces a sourced,
incremental index with per-turn citations. Write a source note per **meeting**, reconcile the items
into the record, and carry each verbatim quote onto the rule it anchors as a `[!quote] Evidence`
callout ([`../practices/ingest-transcripts.md`](../practices/ingest-transcripts.md)).
