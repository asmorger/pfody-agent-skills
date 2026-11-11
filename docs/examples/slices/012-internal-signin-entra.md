---
slice:    012-internal-signin-entra
demo:     An HQ administrator signs in with their Entra work account and
          lands on the same screens with the same rights they have today,
          while everyone else still signs in with a username and password.
appetite: 14 judgment-hours · ~2 wks wall clock · tokens order 10^1 USD
toggle:   auth.entra.internal   (per-user allow-list; legacy sign-in stays hot)
blast:    one additive nullable column (USERS.ENTRA_OID); no data migration;
          no change to USER_GROUP or its semantics; no change to any screen's
          permission check; no change to external sign-in; no password touched
frozen:   2026-11-13       # amend below, never rewrite above
---

> DECIDED. Frozen at build start. New learning is appended under Amendments
> with a date and a decider. Nothing above the freeze line is rewritten.

## Population

Six named HQ administrators, by allow-list. Not all internal users. Not the
warehouse. Not external users. Not the 12 integration accounts.

Identity cannot be sliced by workflow, because every workflow depends on it.
So it is sliced by **population**, smallest and most tolerant first. These six
can be told in person what is changing and can fall back to the old sign-in
the same minute.

## Keep / change / drop

B01  username as identifier    KEEP    stays visible on screens and reports;
                                       stops being the credential for these 6
                                       [survey B01 · PM 11-11]
B02  SHA-1 password check      KEEP    unchanged for the other 406 accounts
                                       [survey B02 · PM 11-11]
B12  group-based authorization KEEP    unchanged; rights still resolve from
B13                                    USER_GROUP for every population
                                       [survey B13 · PM 11-11]
B17  soft-deleted can sign in  CHANGE  both sign-in paths reject DELETED=1
                                       [survey B17 · PM 11-11]
B14  31 unreferenced groups    DEFER   retiring them is its own slice
                                       [survey B14 · PM 11-11]
B06  internal/external by org  DEFER   not touched; an explicit allow-list
                                       makes the inference unnecessary here
                                       [survey B06 · PM 11-11]
B16  unaudited ADMIN grants    DEFER   real problem, wrong slice; filed as a
                                       finding             [survey B16 · PM 11-11]
B08  shared station logins     DEFER   warehouse is out of this population
                                       [survey B08 · no owner yet]

## What this slice deliberately does not decide

What "security group" should become. Entra supplies **identity only**. The
permission set still resolves from USER_GROUP through the same 31 call sites.

This is the seam that lets the slice ship: the open question from the survey
(Q02, S02) does not need an answer for another three slices, because nothing
on the authorization side of the seam changes.

## Checks

char/auth_resolves_permission_set.approved
    Golden master: for all 412 accounts, the permission set resolved from
    USER_GROUP, recorded by driving the legacy domain layer. Must not change.
    Covers the whole population even though the slice covers six, because it
    costs nothing extra and protects everything the slice could break.
char/auth_rejects_known_cases.approved
    Existing rejections unchanged: bad password, unknown username, locked org.
new/entra_signin_resolves_same_rights
    For each allow-listed admin, rights resolved via ENTRA_OID equal rights
    resolved via username.
new/soft_deleted_is_rejected_on_both_paths
parallel-run
    5 working days. Every Entra sign-in also resolves the legacy path in
    shadow and logs a diff. Flip requires 0 diffs and at least 3 sign-ins per
    allow-listed admin.

## No-gos

Touching USER_GROUP or its semantics. Migrating or rehashing any password.
External users. Warehouse station logins. Retiring any group. Changing any
screen's permission check. Any non-additive schema change. Any change to
usp_AuthenticateUser's signature.

## Open

The 12 integration accounts (survey B07) are not on the allow-list and are
unaffected by this slice. They will break in the slice that moves all internal
users, because they authenticate with a stored password. Finding filed; they
need their own slice with API credentials before that one starts.

## Decisions outstanding: 0

## Amendments

(none yet)
