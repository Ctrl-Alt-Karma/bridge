# Handoff Template

A handoff is a compact phase delta. It should let a fresh Architect reconstruct the live cockpit without replaying the whole project.

## 1. Handoff ID

`HANDOFF-<DATE>-<FROM>-TO-<TO>`

State whether this is the live pointer and whether a dated immutable checkpoint also exists.

## 2. Mission

One paragraph describing the project mission relevant to this workstream.

## 3. Last closed gate

- gate name;
- formal result;
- Architect adjudication if different from formal result;
- independent verification status;
- key evidence identity.

## 4. Active gate

State exactly what is active now.

If nothing is authorized yet, say so.

## 5. Role assignments

- Owner;
- Architect;
- active Builder, if any;
- Verifier;
- any stand-in assignment.

## 6. Current authority

State what each active agent may do now.

Do not assume old authorization survives a phase change unless the project explicitly made it standing authority.

## 7. Accepted state and identities

Only the identifiers needed to continue safely:

- repositories/commits;
- artifacts/hashes;
- environments;
- protected inputs;
- current branches/PRs if material.

## 8. Authoritative evidence

List the smallest set of sources that control the current state.

Distinguish primary evidence from summaries.

## 9. Settled decisions

Record decisions that should not be reopened without new evidence.

## 10. Unresolved items

List genuine unresolved questions, not every future idea.

## 11. Access and capability limits

Record material limits for Architect, Builder, and Verifier.

## 12. Known limitations / claim boundaries

State what has **not** been proven.

Distinguish Builder-reported, independently verified, and Architect-adjudicated claims where material.

## 13. Only next authorized action

Exactly one action or one bounded operation.

If the next step requires Owner approval first, say so instead of authorizing it implicitly.

## 14. Stop boundary

State what must not happen after the next action.

## 15. Communication posture

Only include project-specific deviations from `core/ROLE_AND_POSTURE.md`. Do not duplicate the whole style guide.
