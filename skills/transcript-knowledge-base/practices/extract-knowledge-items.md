# Extract knowledge items

**When** the briefs exist and you are turning them into items. Step 2 — the only step that is yours,
and the only one that can invent something.

**Why.** This is where the index's quality comes from and where every failure mode lives. The tool
cannot judge whether a sentence is a durable rule, and it cannot tell a real citation from a
plausible one.

**Steps.**

1. **Read the brief whole**, before writing anything. The rule is often spread across several turns,
   and a later turn frequently reverses an earlier one
   ([`../patterns/transcript-brief.md`](../patterns/transcript-brief.md)).
2. **Follow the contract** in
   [`../prompts/index_extraction_prompt.md`](../prompts/index_extraction_prompt.md). It is the same
   rules in fillable form.
3. **Hold the precision bar.** Three to fifteen items from an hour. Skip greetings, scheduling, status,
   tangents and opinions in passing. If you could not write it into a specification, it is not an item
   ([`../principles/precision-over-volume.md`](../principles/precision-over-volume.md)).
4. **Write each statement as a rule** — declarative, present tense, self-contained, role-based — and
   leave the speaker's words in the quote
   ([`../principles/a-statement-is-not-a-quote.md`](../principles/a-statement-is-not-a-quote.md)).
5. **Keep statements atomic.** Split anything joining two behaviours with "and"
   ([`../principles/one-rule-per-item.md`](../principles/one-rule-per-item.md)).
6. **Cite every item** with a real `turn_id` and a short quote copied from the brief. Cannot cite it →
   drop it ([`../principles/every-item-carries-a-source.md`](../principles/every-item-carries-a-source.md)).
7. **Set `status` and a short `note`** rather than hedging inside the statement
   ([`../principles/status-is-a-field-not-a-sentence.md`](../principles/status-is-a-field-not-a-sentence.md)).
8. **Reuse existing category names exactly**, so a restated rule merges instead of starting a second
   section ([`../patterns/category-taxonomy.md`](../patterns/category-taxonomy.md)).
9. **Write `items.json`** with the hashes copied from the manifest
   ([`../patterns/items-json.md`](../patterns/items-json.md)).

**Done when** every item is one atomic rule written as a rule, carries a citation copied rather than
composed, has a status, and sits in an existing category name — and every file you read is in
`processed_files` with its hash, including any that yielded nothing.
