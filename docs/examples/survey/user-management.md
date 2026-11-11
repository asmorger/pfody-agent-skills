---
area:        User management (LoginForm, frmUserMaint, frmUserGroups)
entry:       LoginForm.vb:1-640; frmUserMaint.vb:1-1880;
             frmUserGroups.vb:1-410; UserSvc.cls:1-920; usp_AuthenticateUser
generated:   2026-11-10 from legacy@a3f91c2
disposition: surveyed        # not yet reviewed with the business
---

> DERIVED. Regenerate this file; never hand-edit it to record a decision.
> Every behavior line carries where it came from. `[code:]` means we read it
> and it is verified. `[db:]` means we queried it. `[logs:]` means we measured
> it. `[told:]` means a person said so and we have not checked. `[assumed:]`
> means we are guessing and the reader should trust us least here.

## Observed behaviors

### Sign-in

B01  Username is the login key. Globally unique, compared case-insensitively,
     stored as typed.                        [code: usp_AuthenticateUser:22]
B02  Passwords are unsalted SHA-1 in USERS.PWD_HASH. No per-user salt, no
     work factor, no algorithm column.       [code: UserSvc.cls:210]
B03  No account lockout. USERS.FAIL_CNT is incremented on a bad password and
     read by nothing.                        [code: 1 writer, 0 readers]
B04  Password complexity and 90-day expiry are enforced in the client form.
     usp_AuthenticateUser accepts any hash it is handed, so any client that
     calls the proc directly bypasses both.  [code: frmUserMaint.vb:742]
B05  An admin reset writes a new hash directly. No must-change flag, no
     notification, no record of who reset it. [code: frmUserMaint.vb:1104]

### Population and account type

B06  Internal versus external is not stored anywhere. It is inferred at
     runtime from whether the user maps to org 1 ("HQ").
                                             [code: UserSvc.cls:488]
B07  12 accounts have no interactive sign-in in 24 months yet appear as
     ACTOR_ID on rows written last week. These are integrations
     authenticating with a stored username and password.
                                             [logs + db]
B08  4 accounts show overlapping concurrent sessions from the warehouse
     subnet throughout each shift: shared shift logins, one credential per
     station rather than per person.          [logs]

### Tenancy

B09  USER_ORG is many-to-many. 23 of 412 accounts map to more than one org.
                                             [db]
B10  A multi-org user picks one org from a dropdown at sign-in and sees that
     org for the session. The choice is remembered in USERS.LAST_ORG.
                                             [code: LoginForm.vb:402]
B11  Three reports ignore the session org and aggregate across every org the
     user maps to.                            [code: rptAging.vb:88, +2]

### Security groups

B12  USER_GROUP is many-to-many. 41 distinct groups exist in the table.
                                             [db]
B13  There is no permission table. A "security group" is a name that code
     compares against: `If IsInGroup("WHSE_SUPER")`. 9 distinct group names
     appear as string literals across 31 call sites. Nothing maps a group to
     a capability; the mapping is the 31 call sites.
                                             [code: exhaustive grep IsInGroup]
B14  31 of the 41 groups are referenced nowhere: not in client code, not in
     reports, not in stored procedures. 142 users hold at least one of them.
                                             [code: exhaustive grep + db]
B15  87 accounts belong to zero groups, can sign in, and can reach every
     screen. Groups are checked only on write actions, so a user in no group
     has full read access to their org.       [code + db]
B16  Any member of ADMIN can grant any group, including ADMIN. The grant is
     not audited.                             [code: frmUserGroups.vb:233]

### Deletion

B17  Soft delete sets USERS.DELETED=1. usp_AuthenticateUser does not filter
     on that column, so a soft-deleted account can still sign in.
                                             [code: usp_AuthenticateUser:22]
B18  A soft-deleted username is never released. Re-hiring a person requires
     a new username.                          [code: frmUserMaint.vb:612]
B19  USERS.USER_ID is a foreign key on 34 tables as CREATED_BY, MODIFIED_BY
     or ACTOR_ID. No user row can ever be hard deleted, in the legacy app or
     its replacement.                         [db: exhaustive]

## Data touched

USERS, USER_ORG, USER_GROUP, ORGS, AUDIT_LOGIN
usp_AuthenticateUser, usp_SetUserPassword, tr_user_audit

## Usage (prod logs and database, 24 months)

sign-ins 184,002 · accounts 412 · interactive in last 90d 298
accounts by population: HQ admin 6 · internal staff 250 · warehouse 90
                        · external 54 · integration 12
multi-org accounts 23 · zero-group accounts 87
groups defined 41 · groups referenced in code 9
soft-deleted accounts 61 · sign-ins by soft-deleted accounts 0
suspected integration accounts 12 · suspected shared station logins 4
admin password resets 318 · self-service resets 0 (no such feature)

## Questions for the business

Q01 (B17) A soft-deleted account can still sign in. It has never happened in
    24 months. Fix it, or has someone been relying on it?
Q02 (B14) 31 of the 41 groups are referenced nowhere in the software. Do they
    mean something to you outside the app, or can they be retired?
Q03 (B15) 87 people are in no group at all and can read everything in their
    org. Intended, or an accident nobody noticed?
Q04 (B09) 23 people belong to more than one organization. Is that a real need
    or years of data entry? The answer changes the tenancy model.
Q05 (B11) Three reports show data across all of a user's organizations
    regardless of which one they picked at sign-in. Correct, or a leak?
Q06 (B08) Four warehouse stations appear to share a login. After this work,
    does every warehouse worker need their own identity, or do station
    accounts stay? This is a licensing and audit question, not a technical one.
Q07 (B01) Entra makes the work email the sign-in identity. Legacy usernames
    are printed on pick tickets and appear in 24 months of audit rows. Must
    the old username survive as a visible field?
Q08 (B06) Internal versus external is currently inferred from org 1
    membership. We need the policy, not the current behavior: what must an
    external user never be able to see?
Q09 Are the third-party users people, or systems? If any are systems they
    need API credentials, not user identities, and they leave this project
    entirely.
Q10 (B02) No password can be migrated. Unsalted SHA-1 cannot be handed to any
    identity provider, so all 412 accounts re-enroll. That is a cutover and
    communications plan for internal staff and external customers. Who owns it?
Q11 Do customer administrators need to manage their own users? Delegated
    administration is a product decision and it constrains the external
    identity provider more than any technical consideration will.
Q12 (B16) Anyone in ADMIN can grant ADMIN, unaudited. Acceptable to carry
    forward, or does it get fixed on the way through?
Q13 External identity is licensed per monthly active user. At the current
    external count that is a recurring cost. Has it been priced against the
    directive?

## Questions for a named specialist

S01 (B19) 34 tables name a user as the actor on a row. Is there a regulatory
    or audit requirement that those always resolve to a named person?
    → controller or compliance
S02 (B13) What does each of the 9 live group names actually gate, in business
    terms? We can read the 31 call sites; we cannot tell you which of them
    matter. → the longest-tenured warehouse supervisor
S03 (B07) Which of the 12 integration accounts belong to systems we still run,
    and where are their credentials stored? → integrations owner

## Still ours to verify (not questions for anyone)

V01 Whether the client caches the resolved permission set after sign-in, which
    determines if a group change takes effect immediately or at next login.
V02 Whether any stored procedure or report reads USER_GROUP directly, which
    would make the 31 call sites an undercount.
V03 Whether the three cross-org reports (B11) are reachable by external users.
V04 Whether usp_AuthenticateUser is called by anything other than the desktop
    client.
