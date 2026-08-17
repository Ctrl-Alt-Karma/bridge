# Fresh-Architect Comprehension Handshake

A brand-new Architect performs this **read-only** before steering work.

Do not execute project work while completing the handshake.

For continuation-critical claims, check the control record against cited primary evidence where practical. This includes claims that gate the next authorized action, accepted or frozen identities required to continue safely, and claims represented as independently verified or otherwise controlling the active gate. If such a claim is unsupported, contradicted, or cannot be reacquired, leave it unresolved. Repetition in `CURRENT_STATE.md`, a handoff, or prior Architect narrative does not promote a claim.

Keep this check read-only and proportional to the active decision.

For formal Architect succession, the successor writes the reconstruction independently in its own words. The retiring Architect's bootstrap is a source to verify, not text to echo.

## Required restatement

### 1. Mission

What is the project's actual objective?

### 2. Current phase

What gate was last closed, and what gate is active now?

### 3. Authority model

State:

- Owner and final authority;
- Architect role;
- active Builder rule;
- primary and stand-in Builder assignments;
- Verifier role and independence;
- Scientific Counsel role, if active;
- merge/external-write authority;
- whether any standing delegations exist.

### 4. Frozen / accepted state

List only identities required to continue safely.

### 5. What is proven

Separate:

- Builder/operator-reported;
- mechanically verified;
- independently verified;
- Architect-adjudicated.

### 6. What remains unresolved

List genuine unresolved items that can affect the next gate.

### 7. Evidence authority

Identify the authoritative control documents and primary evidence for the current gate.

### 8. Current prohibitions

State the actions presently outside authority.

### 9. Only next authorized action

State exactly one.

### 10. Stop boundary

State where current authority ends.

### 11. Ambiguity and contradiction

Identify any material omission, ambiguity, contradiction, stale detail, unsupported load-bearing claim, or accidental reopening of a settled question.

### 12. Proposed immediate next action

State the next action you would take after authority transfers. Do not execute it during the handshake.

### 13. Architect posture

Confirm that you will:

- maintain one active cockpit;
- make technical decisions when evidence supports them;
- escalate only genuine Owner-level choices;
- preserve claim boundaries;
- challenge the Owner when evidence requires it;
- avoid over-governance and objection theater.

## End marker

For an ordinary fresh-Architect cold start, end with exactly one of:

`HANDOFF COMPREHENSION: PASS`

or

`HANDOFF COMPREHENSION: STOP - <reason>`

A PASS reports successful reconstruction of the repository state. It does not grant operational authority beyond the existing project charter and handoff.

For formal Architect succession, return the reconstruction to the retiring Architect for a bounded backward-pass fidelity check. That check may identify only material omissions, contradictions, authority or scope errors, accidental reopening of settled questions, or incorrect interpretation of the next authorized action. It may not redesign the project, create work, expand scope, or reclaim ongoing Architect authority.

End formal succession with exactly one of:

`PASS_HANDOFF_SUCCESSOR_STATE_RECONSTRUCTION`

or

`HOLD_HANDOFF_SUCCESSOR_STATE_RECONSTRUCTION - <reason>`

A formal succession PASS transfers Architect authority completely. Durable evidence controls any disagreement between retiring and successor Architects.

## Classifying apparently unresolved state

When reconstructing unresolved state, classify each item explicitly as one of:

- `GENUINELY_UNRESOLVED`
- `COMPLETED_WORK_EVIDENCE_LINK_MISSING`
- `ACCESS_LIMITED`
- `HUMAN_FACT_REQUIRES_ATTESTATION`
- `NOT_FOUND_IN_SEARCHED_SCOPE`
- `SETTLED_DURABLY_RECORDED`

Do not infer that work never occurred solely because a closing receipt is absent,
when downstream durable artifacts indicate the upstream operation occurred.

When an inherited item is justified by "no artifact exists", inspect the scope of
that negative claim. If the relevant evidence namespaces were not all searched, do
not inherit global absence as fact; classify it honestly as
`NOT_FOUND_IN_SEARCHED_SCOPE`, `ACCESS_LIMITED`, or
`COMPLETED_WORK_EVIDENCE_LINK_MISSING` as the evidence supports.

Where multiple revisions of an artifact may exist, distinguish authentic artifact
identity from accepted revision status.

If the missing fact is inherently human intent or action and no durable confirmed
attestation exists, ask the responsible actor when available, then serialize and
confirm the bounded attestation. Do not infer motive from timestamps, filenames, or
other weak proxies.

The retiring Architect's bounded backward pass must challenge this class of
omission, asking specifically:

- Does downstream durable state imply an upstream operation occurred?
- Is an inherited absence claim stronger than its documented search scope?
- Is accepted load-bearing work missing a durable evidence pointer?
- Is a human-intent question being treated as a machine-inference problem?
- Is a recovered artifact the accepted revision, or merely an authentic historical
  one?

Succession PASS semantics are unchanged.
