# Diagnose a failed run

**When** intake repeats, citations vanish, or a publish fails or writes something wrong.

**Why.** Most of these have one cause and one fix, and the wrong instinct in every case is to work
around the symptom — hand-mapping a field, or filling a gap the source left.

**Steps.** Match the symptom:

    intake runs again on every invocation
        the config was not saved to a detected path, or config_version mismatches.
        Confirm Knowledge/user-story-builder.config.md exists and check the stamp
        → ../principles/detect-confirm-save.md

    stories cite nothing, or the mode dropped unexpectedly
        authoritative_sources is empty, or the paths moved. Validate on load and
        update the config's paths → ../practices/load-or-provision-the-config.md

    a cited id resolves to nothing
        Mode A requires every id to resolve. Fix the citation or drop to a
        name-and-section citation → ../patterns/source-tag.md

    the tracker shows markdown instead of formatted text
        the rich-text field was sent as markdown. The adapter converts first; if a
        NEW story reports `markdown` in multilineFieldsFormat, stop and report it
        per the adapter's phase 2.

    `az boards` not found
        the DevOps extension is missing: `az extension add --name azure-devops`.

    401 or permission errors on publish
        not authenticated, or the token lacks Work Items write. `az login` /
        `az devops login`, with Work Items (Read & Write).

    the field prompt appears on every publish
        fields_resolved did not persist, or the org/project changed. Check that
        phase 1c wrote back and that fields_resolved_for matches the current target
        → ../practices/resolve-the-tracker-fields.md

    a custom field errors
        it does not exist in this project. Let resolution mark it `unavailable`;
        do not hand-map it → ../patterns/tracker-field-map.md

    characters are mangled in a tracker field
        rich text went out unnormalised → ../principles/tracker-text-is-ascii.md

**Then.** Fix the cause and re-run, rather than patching the output. Report anything that genuinely
cannot be resolved — a source you have no access to, a tracker field that does not exist — to the
user instead of working around it.

**Done when** the symptom is matched to its cause, the fix is applied at the cause, and anything
unresolvable is reported rather than papered over.
