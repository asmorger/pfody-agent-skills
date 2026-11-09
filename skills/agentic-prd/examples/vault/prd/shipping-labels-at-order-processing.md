---
id: PRD-001
aliases: [PRD-001]
type: prd
status: Accepted
size: Standard
owner: Example TPO
approvers: [Example Operations Lead, Example Architect, Example QA Lead]
version: 1.0
epics: ["[[carrier-labels-on-the-order-screen|EPIC-01]]"]
outcomes: ["[[address-error-rate-on-parcels|OUT-1]]"]
created: 2026-10-02
updated: 2026-11-05
tags: [prd]
---

# PRD-001 — Shipping Labels at Order Processing

> [!warning] Illustrative example only
> The company, the sources, the numbers and the decisions are invented. Do not use them as evidence.

This PRD is the source of record for **why** and **what**; the tracker is the source of record for
**state**. Each requirement, question and metric is its own note, linked from here — so a
requirement can be cited, superseded and covered on its own, and this note stays readable top to
bottom by an agent that has never loaded the skill.

**Work item levels.** One id format per level. `EPIC-01` → `FEAT-01` → `US-01`; `R-001` is a
behaviour, not a tracker item; `AC-1` numbers restart in each story.

## 1. Intent

**Narrative.** Warehouse clerks create a carrier label from the order screen. They do not enter the
address again. Parcels leave faster and with fewer address errors.

**Problem.** Clerks copy each address from the order system to the carrier website. The step is slow
and causes address errors. Evidence: [[discovery-call-with-the-operations-lead|SRC-01]] @12:04.

**Users.** Warehouse clerk — creates and prints a label during order processing, primary user.
Warehouse supervisor — voids a label when an order changes.

**Outcomes.** ![[address-error-rate-on-parcels]]

## 2. Scope

**In scope.** Creating, printing and voiding a carrier label from the order screen.

**Non-goals.** Bulk printing across orders — not priced in this phase; revisit when the carrier
exposes a batch endpoint ([[print-labels-in-one-job|R-014]] carries the behaviour at P3). Negotiated carrier rates — no
source addresses them.

## 3. Context

Labels are created by hand on the carrier's website today. Constraint: the carrier truncates address
line 1 at 35 characters. Dependency: the finance system's credit-hold flag must be readable
synchronously ([[credit-hold-blocks-labelling|DEC-02]]).

## 4. Epics, Features and requirements

![[carrier-labels-on-the-order-screen]]

Requirements live in `requirements/` and are indexed by [[requirements|the requirements MOC]]; the
coverage table is [[coverage]]. The two Features are [[create-and-print-a-label|FEAT-01]] and [[void-a-label|FEAT-02]], and each carries
its own seven coverage lines in frontmatter.

## 5. Cross-cutting requirements

![[record-every-label-action]]

## 6. Agent boundaries

**Always.** Cite a requirement id in every commit that implements one. Run the project's tests
before reporting done.

**Ask first.** Any change to a requirement's wording. Any new dependency. Any schema change.

**Never.** Invent a behaviour no requirement states. Resolve a conflict between two sources. Mark a
gate crossed.

**Stop conditions.** A requirement whose coverage is `blocked`. A coverage line reading `Gap:`. A
`PROPOSED` source.

## 7. Knowledge ledger

Sources are notes in `sources/`, each cited by id and locator from the requirement that rests on it.
Open questions are notes in `questions/` — [[who-may-void-a-printed-label|Q-03]] is the one still open. Decisions are `DEC-nn`.

## 8. Rollout and measurement

Flag `labels.order-screen`, off by default. Phase 1 is one warehouse. Rollback is the flag.
Telemetry feeds [[address-error-rate-on-parcels|OUT-1]] from the carrier returns report.

## Agent protocol

Kept verbatim in every PRD. Read sections 1, 2 and 6 before writing any code. Cite the requirement
id you are implementing. If a requirement is ambiguous, stop and raise it as a question rather than
choosing — a guess is indistinguishable from a requirement once it is on the page.
