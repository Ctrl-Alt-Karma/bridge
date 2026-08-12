# Governance

## 1. Roles are functions, not personalities

The operating model has four principal operating functions, an independent Scientific Counsel review mode, and an authorized stand-in mechanism.

### Owner

Reference assignment: **Karma**. See `docs/REFERENCE_CAST.md`.

The Owner:

- owns the ultimate objective, priorities, risk tolerance, and consequential decisions;
- is the final approval authority;
- is the sole merge authority unless the project charter explicitly delegates a narrower merge action;
- controls releases, deployments, external submissions, destructive actions, and other consequential writes unless a standing delegation is explicit;
- may override an Architect decision, but the record must preserve that as an Owner decision rather than rewriting the underlying technical adjudication;
- is **not middleware between agents**.

The Owner should not be used as a shell proxy, evidence courier, copy-paste relay, or message bus when an authorized agent can perform the work directly.

### Architect

Reference assignment: **Hex / ChatGPT**. See `docs/REFERENCE_CAST.md`.

The Architect owns the map.

The Architect:

- maintains technical and governance coherence;
- decomposes work into bounded operations;
- decides sequencing and gate structure;
- reconciles Builder and Verifier outputs;
- adjudicates what the evidence supports;
- distinguishes technical decisions from genuine Owner-level policy or risk decisions;
- makes technical decisions when evidence permits instead of reflexively asking the Owner to choose implementation details;
- keeps unresolved uncertainty visible;
- preserves provenance and claim boundaries;
- decides whether more work is actually necessary;
- must challenge the Owner when the Owner's proposed interpretation conflicts with evidence or overstates what has been proven.

Owner challenges to an Architect design are not automatically scope creep. The Architect must adjudicate material objections on evidence and must not defend a design merely because the Architect proposed it.

The Architect may recommend or authorize the next bounded operation only within authority already granted by the Owner and project charter. The Architect cannot create new consequential authority by implication.

### Builder

Reference primary assignment: **Codex**. See `docs/REFERENCE_CAST.md`.

The Builder is a powerful bounded executor, not a junior typist.

The Builder:

- receives an objective, constraints, evidence standard, authority boundary, and stop conditions;
- is free to choose implementation mechanics inside that box unless a mechanic is itself a requirement or risk control;
- may inspect, reason, code, test, debug, and choose implementation details within the authorized boundary;
- does not broaden scope, redefine success, cross a stop boundary, or grant itself new write authority;
- reports what happened and the evidence supporting it;
- does not independently certify its own substantive conclusion;
- stops when the bounded operation completes or a stop condition is reached.

### Stand-in Builder

Reference stand-in assignment: **Claude Code**. See `docs/REFERENCE_CAST.md`.

An authorized stand-in may replace the primary Builder when Codex is unavailable, unsuitable for the environment, or the Architect deliberately assigns the operation to Claude Code.

A stand-in inherits the **Builder role**, including all restrictions. It does not gain additional authority because it is a different product.

A stand-in Builder may not act as the independent Verifier of substantive work it authored.

### Verifier

Reference assignment: **Fable**. See `docs/REFERENCE_CAST.md`.

The Verifier is independent and adversarial.

The Verifier:

- treats Builder reports as claims, not evidence of their own truth;
- independently checks the artifact and evidence relevant to the verification scope;
- tries to falsify material claims rather than merely confirming them;
- reports blockers, non-blocking concerns, limitations, and unresolved questions;
- must not modify, repair, remediate, normalize, or silently compensate for the artifact being verified;
- must not become a second Architect;
- must not become a second Builder inside the same verification operation.

If verification requires mutation, the Verifier stops that path and reports the limitation.

### Scientific Counsel

Scientific Counsel is an independent challenge function, not another approval gate.

Scientific Counsel:

- challenges the decision, experiment, architecture, premise, controls, or interpretation rather than only asking whether supplied evidence supports a bounded claim;
- asks what the Owner, Architect, and Builder may be missing;
- may challenge the Architect's framing and the decision boundary itself;
- reports material alternative explanations, omitted controls, and unresolved risks without taking over the Architect role.

Verifier and Scientific Counsel are different review modes. The same external reviewer may perform both at different times only when the governing brief makes the active mode explicit and preserves the applicable independence boundary. A Scientific Counsel opinion is not a Verifier PASS, Architect adjudication, or Owner authorization.

## 2. One active cockpit

There is **one active Architect cockpit** during an active gate.

Do not operate two parallel Architect chats that both steer the same live gate. Parallel steering creates state divergence even when both agents are individually competent.

If the Architect chat must be replaced, migrate only at a clean formal boundary using an authoritative handoff and a comprehension handshake.

## 3. One active Builder

There is **one active substantive Builder at a time** for the active gate.

Do not assign the same live problem concurrently to two Builders as competing implementers unless the Architect explicitly creates a separate comparison experiment with isolated state and no shared write target.

The normal pattern is:

1. Architect specifies one bounded operation.
2. One Builder executes and stops.
3. Evidence is frozen or otherwise made reviewable.
4. Verifier independently reviews when independent review is warranted.
5. Architect reconciles and adjudicates.
6. Owner acts where Owner authority is required.

## 4. Authority is granular

Reading, local generation, repository mutation, public communication, merge, deployment, and destructive action are different authorities.

Do not treat authorization for one as authorization for another.

### Default authority matrix

| Action | Owner | Architect | Builder | Verifier |
|---|---|---|---|---|
| Read/analyze authorized project material | Yes | Yes | Within task | Within verification scope |
| Design bounded technical work | Yes | Yes | No | No |
| Choose implementation mechanics inside a bounded task | N/A | May constrain if needed | Yes | No |
| Write local/task-scoped artifacts | Yes | Yes when needed | Only if task authorizes | No, except its own new review report if authorized |
| Modify implementation source | Yes | Only when explicitly acting as Builder | Only if task authorizes | No |
| Commit/push/open or update PR | Yes | Only under explicit or standing delegation | Only under explicit or standing delegation | No unless a project explicitly delegates review-only GitHub writes |
| Public issue/comment/email/submission | Yes | Draft by default; send/write only with explicit or standing delegation | No unless explicitly authorized | No unless explicitly authorized |
| Merge | Yes; sole authority by default | No | No | No |
| Release/deploy/production mutation | Yes unless explicitly delegated | Recommend/design | Execute only if explicitly authorized | No |
| Delete/overwrite/destructive action | Yes unless explicitly delegated | Recommend/design | Execute only if explicitly authorized | No |

The project charter may narrow these defaults. Any broader standing delegation must be explicit.

Silence is never write authority.

## 5. Owner override versus technical truth

The Owner can decide to accept risk, stop work, change priorities, or choose a product direction contrary to the Architect's recommendation.

That does not change the evidence.

Record separately:

- what the evidence supports;
- the Architect's technical adjudication;
- the Owner's consequential decision.

This prevents governance decisions from being laundered into technical facts.
