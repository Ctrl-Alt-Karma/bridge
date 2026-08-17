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
- Scientific Counsel, if assigned;
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

Record material limits for Architect, Builder, Verifier, and Scientific Counsel where assigned.

## 12. Retiring-chat condition

For formal Architect succession, disclose proportionally:

- context condition: light, moderate, or heavy;
- confidence that the active state is internally coherent;
- known dependence on compressed or summarized history;
- potentially stale or ambiguous details;
- facts the successor must reacquire from durable evidence before using them load-bearingly.

This is diagnostic disclosure, not proof that the state is correct or incorrect. For an ordinary non-succession phase handoff, mark this section not applicable.

## 13. Known limitations / claim boundaries

State what has **not** been proven.

Distinguish Builder-reported, independently verified, and Architect-adjudicated claims where material.

## 14. Only next authorized action

Exactly one action or one bounded operation.

If the next step requires Owner approval first, say so instead of authorizing it implicitly.

Do not preload a large stack of fully authored future Builder prompts. After a successful succession handshake, the successor Architect authors the next substantive Builder operation from canonical governance and durable project state.

## 15. Canon synchronization

For formal Architect retirement, record:

- the retirement canon-flush disposition for each candidate reusable change;
- the resulting canonical repository and commit;
- any held `AMBIGUOUS` candidate;
- confirmation that project-only rules were not promoted.

For an ordinary non-retirement handoff, mark this section not applicable.

## 16. Stop boundary

State what must not happen after the next action.

## 17. Communication posture

Only include project-specific deviations from `core/ROLE_AND_POSTURE.md`. Do not duplicate the whole style guide.

## 18. Succession status

For formal Architect succession, record the successor's reconstruction disposition and the retiring Architect's bounded backward-pass result. Authority transfers only on:

`PASS_HANDOFF_SUCCESSOR_STATE_RECONSTRUCTION`

Otherwise record:

`HOLD_HANDOFF_SUCCESSOR_STATE_RECONSTRUCTION`

## Continuity reconciliation (formal Architect retirement only)

A compact completeness check, not an autobiography. Proportional to load-bearing
work.

- Load-bearing work completed since the last durable checkpoint.
- Exact durable artifact or evidence identity for each material item.
- Accepted revision or version where more than one may exist.
- Material local-only evidence, with path and stable identity as far as known.
- Any `COMPLETED_WORK_EVIDENCE_LINK_MISSING` item, with scope for recovery.
- Any material human or actor fact that requires durable attestation.
- Confirmation that downstream artifacts were checked for evidence that apparently
  missing upstream work actually occurred, before calling it unresolved.
- All material evidence namespaces used by the retiring cockpit.
- For each namespace: durably indexed, searched during retirement, inaccessible, or
  no longer relevant.
- The search-scope basis for any claim that an artifact does not exist.
