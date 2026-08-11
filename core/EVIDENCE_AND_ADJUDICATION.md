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

Agreement between models is weak evidence compared with a resolving oracle such as executable behavior or authoritative source bytes.
