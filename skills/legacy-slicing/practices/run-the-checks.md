# Run the checks

**When** after writing or editing a survey or a brief, before freezing one, before a flip, and
before reporting anything as done.

**Why.** The script catches the defect class that survives reading. A brief frozen with decisions
still outstanding passes review, because the gate it failed is one line far below the rulings a
reviewer is actually looking at. A ruling citing a behaviour id no survey defines looks exactly like
one that resolves. A changed behaviour with no check behind it reads as finished. None of those is
visible by eye, and all of them are mechanical.

**Steps.**

1. **Run it with the full path**, because the workspace is usually in another folder:

       python3 <skill-folder>/scripts/slice.py check <workspace>
       python3 <skill-folder>/scripts/slice.py signals <workspace>

2. **Treat errors as blocking.** A non-zero exit is not reportable as success, and in particular a
   brief must not be frozen while `check` fails
   ([`../principles/decisions-outstanding-must-read-zero.md`](../principles/decisions-outstanding-must-read-zero.md)).
3. **Treat warnings as a person's to settle.** An absence claim with no exhaustive sweep, a `[told:]`
   tag with no date, four deferrals in one slice, a blast radius with no negatives in it — each is
   either accepted out loud or fixed, never left unread.
4. **Read `signals` at every flip.** Surveys outstanding should trend down and accumulated checks up.
   If neither has moved across several slices, the loop is not running
   ([`flip-a-slice.md`](flip-a-slice.md)).
5. **Never edit to satisfy the script.** Fix the defect it points at, not the text that triggered it.
   Renumbering a behaviour id to silence an unresolved citation is the worst available response: ids
   are cited across files and never reused
   ([`../patterns/survey-note.md`](../patterns/survey-note.md)).
6. **State the four limits by name** in any report. The script cannot judge whether a provenance tag
   is honest, whether a golden master was really recorded from the running system rather than written
   from the survey, whether a slice is a sound slice, or whether a deferral's stated reason is true.
   Those are the four ways this practice actually fails
   ([`../anti-patterns/tests-written-from-the-survey.md`](../anti-patterns/tests-written-from-the-survey.md)).

**Done when** the exit code is reported, every error is fixed, every warning is listed or accepted
out loud, `signals` has been looked at rather than assumed, and the four limits are stated rather
than implied.
