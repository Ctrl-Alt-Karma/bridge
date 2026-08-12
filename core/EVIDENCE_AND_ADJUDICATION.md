# Evidence and Adjudication

## 1. Evidence hierarchy

Prefer evidence in roughly this order, subject to the domain:

1. directly inspectable primary source bytes or authoritative external records;
2. executed falsifying or acceptance tests tied to exact source/artifact identity;
3. immutable run artifacts, logs, hashes, receipts, and manifests;
4. independent Verifier findings grounded in the above;
5. Builder implementation reports;
6. Architect summaries and handoffs;
7. chat recollection, PR descriptions, or unsupported narrative.

Higher narrative confidence does not increase evidence strength.

## 2. Portable identity

When identity matters, record enough information for another agent to reacquire the same object, such as:

- repository + commit + path + source lines;
- exact file path + SHA-256;
- artifact ID + hash + size;
- test command + exact source identity + result;
- external record + stable reference + relevant excerpt.

Use the smallest identity set that makes the claim reproducible.

## 3. Reacquisition

After context loss, a fresh agent should reacquire authoritative state rather than asking the Owner to remember it.

A reacquisition task is normally read-only and should answer only what the Architect needs to make the next decision.

A reacquisition package should be lean. Default to:

- one report;
- source hashes or identity record where material;
- worktree/artifact identity record where material;
- command/access transcript where needed to demonstrate read-only behavior.

Do not copy authoritative documents into the package unless transport or distinct evidentiary value requires it. Quote the controlling sections with exact paths/locations instead.

## 4. Claim states are different dimensions

Use these labels conceptually even if the project uses different exact field names.

### OPERATOR_REPORTED

A Builder or operator says the operation behaved a certain way.

This is a claim backed by the Builder's evidence, not independent certification.

### MECHANICALLY_VERIFIED

A deterministic check independently confirms a narrow property, for example a SHA-256 match, schema validation, test result, or exact byte comparison.

Mechanical verification proves only the property checked.

### INDEPENDENTLY_VERIFIED

A separate Verifier inspected the relevant evidence under an independent role boundary and issued a verdict on a stated scope.

### ARCHITECT_ADJUDICATED

The Architect reconciled the available evidence, formal results, limitations, and conflicts into a technical disposition.

Architect adjudication may explain or supersede the practical meaning of an older result without rewriting the immutable historical result.

### OWNER_AUTHORIZED

The Owner approved a consequential decision or action.

Owner authorization is authority, not technical evidence.

## 5. PASS semantics

### Builder PASS

A Builder PASS reports successful completion of the bounded task under the Builder-visible protocol.

Preferred wording for a bounded reacquisition operation:

> A PASS reports that the requested evidence was reacquired completely and read-only. The Architect adjudicates that claim from the returned evidence.

For implementation operations, adapt the first sentence to the task while preserving the second principle.

### Verifier PASS

A Verifier PASS means the stated verification scope is supported by evidence independently inspected by the Verifier.

It does not authorize the next operation.

### Architect gate decision

The Architect decides what the Builder and Verifier evidence means for project progression within already granted authority.

Do not call the Architect decision an independent verification unless the Architect actually performed an independent verification under the required access model.

### Owner authorization

The Owner decides whether a consequential action may occur.

Do not call Owner approval a technical PASS.

## 6. Formal result versus substantive meaning

Never rewrite history for tidiness.

Example pattern:

- immutable run result: `FAIL CLOSED`;
- later evidence proves the failure was a harness defect, not a product defect;
- Architect records an additive adjudication stating what is now technically qualified;
- the original `FAIL CLOSED` remains the original run result.

This preserves both chronology and truth.

## 7. Proportional evidence

Evidence should answer the claim.

Do not create a ceremony-sized package for a receipt-sized question.

Add a file, manifest, screenshot, rerun, or independent review only when it carries distinct evidentiary value or controls a material risk.

## 8. Falsification

Where practical, prefer tests that can disprove the claim:

- fail on the buggy or rejected state;
- pass on the intended state;
- bind to exact identities;
- avoid vacuous success.

When a deterministic test or check directly resolves a claimed property, prefer it as the primary gate for that property rather than asking an LLM to manually reconfirm the same deterministic fact. The check proves only the property it actually tests.

The Verifier remains responsible for challenging whether the correct property was tested, whether the test is bound to the intended target and source identity, whether its scope and design are adequate and non-vacuous, and whether important failure modes remain outside the oracle.

Agreement between models is weak evidence compared with a resolving oracle such as executable behavior or authoritative source bytes.

## 9. Verifier challenge and report preservation

When a gate already warrants independent verification, the Verifier may challenge whether a material Architect interpretation follows from evidence within the verification scope. This does not make the Verifier a second Architect, an approval authority over the Architect, or a mandatory second adjudicator, and it must not create a recursive review loop.

The original Verifier report must remain preserved verbatim and directly accessible in the project's evidence or control record. Architect commentary and adjudication are additive; they must not replace or rewrite the Verifier's report.

## 10. Review identity binding

When source or artifact identity can materially affect a substantive conclusion, Builder, Verifier, and Architect review or adjudication reports must identify the exact identity actually reviewed. Use a repository and commit, file hash, artifact ID and hash, or another stable identity proportionate to the claim.

Do not require hashes for casual discussion or for analysis where identity cannot materially affect the conclusion. A report must not imply that it reviewed a later or different artifact merely because the project moved after the review occurred.

## 11. High-risk gate design

When post-hoc judgment could materially alter a high-risk conclusion, design the gate before observing result-bearing evidence:

- predeclare the acceptance or decision criteria;
- include meaningful negative controls where practical;
- when the claim materially depends on both intended source semantics and actual execution, require evidence for both.

Apply this proportionally. Predeclaration does not eliminate judgment, negative controls need not be ceremonial, and source inspection does not substitute for runtime evidence when execution behavior is part of the claim.
