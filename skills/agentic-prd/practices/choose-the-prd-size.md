# Choose the PRD size

**When** starting a PRD, or when a document feels heavier than the work it describes. Pick the
smallest size that removes guesswork.

**Why.** A PRD costs the person's attention, and attention spent on sections the work does not need
is attention not spent on the requirements. The opposite failure is worse but rarer: a half-page
brief for a cross-release programme leaves agents to invent the parts nobody wrote.

**Steps.**

1. **Count the Epics and the releases.** One clear behaviour, no Epic → no PRD. One Feature under one
   Epic → `Small`. One Epic in one release → `Standard`. Several Epics, or work spanning releases →
   `Large`.
2. **Take the sections that size requires**, and no others:

       No PRD     none — write one User Story
       Small      1, 2, 4, 6, 7 — constraints at the end of section 2
       Standard   1 to 8
       Large      1 to 8, plus the optional modules that apply

3. **Split a Large rather than grow it.** An Epic that can ship alone gets its own PRD. Two PRDs that
   each cover a release beat one nobody finishes reading.
4. **Add a module only when it applies**: M1 when the product itself contains a model or an agent —
   its behaviours become requirements with `Verify: Eval` — and M2 when existing records must move.
5. **Record the size in the front matter**, so a reviewer judges the document against the right
   checklist.
6. **Re-size when the work does.** A `Small` that grows a second Epic becomes a `Standard`; say so
   rather than bending the sections.

**Done when** the front matter names a size, every section that size requires is present and filled,
and no section is present only because the template had it.

**Related.** [`../patterns/prd-document.md`](../patterns/prd-document.md),
[`draft-a-prd.md`](draft-a-prd.md).
