# Bounded Task Specification Template

Use this template for a Builder operation. Delete sections that genuinely do not apply. Do not inflate the task merely to fill the template.

## Operation ID

`<SHORT-STABLE-OPERATION-ID>`

## Role

You are `<Codex / Claude Code / other authorized Builder>` acting as the bounded Builder/operator.

The Owner is `<OWNER>`.
The Architect is `<ARCHITECT>`.
You do not independently adjudicate your own substantive result.

## Objective

State the outcome to achieve in one compact paragraph.

## Why this operation exists

State the uncertainty, defect, or deliverable this operation resolves.

## Accepted inputs and identities

List only controlling inputs whose identity matters:

- repository / branch / commit;
- files and hashes;
- environment identity;
- prior receipt or handoff;
- data/artifact roots.

If an identity mismatch is a stop condition, say so explicitly.

## Authority

State exactly what is authorized, for example:

- read-only discovery;
- create one fresh evidence directory;
- edit specified source paths;
- run tests;
- commit to a specified branch;
- push/open a draft PR.

Do not leave write authority implicit.

### Optional delegation / authority expansion

Include this only when relevant. If recursive or sub-agent delegation, expansion of an existing cost, turn, or resource limit, broader tool access, or credential or permission expansion is authorized, define the delegated role, bounded objective and scope, applicable limit, tool, credential, or permission scope, and terminal stop condition. Do not invent a budget where none otherwise exists.

## Builder freedom

Inside the authorized boundary, choose the implementation and investigative mechanics you judge most effective.

Do not treat examples or suggested approaches as mandatory unless they are explicitly labeled requirements.

## Required first output

Before substantive execution, report:

1. rough wall-clock estimate as a range;
2. assumptions;
3. likely bottleneck.

Proceed immediately afterward unless a stop condition applies.

Do not benchmark the estimate, score it afterward, or create evidence about estimation accuracy.

## Required invariants

List state that must remain true, such as:

- protected source/data remains unchanged;
- existing evidence remains immutable;
- no overwrite;
- exact environment remains intact;
- no external communication.

## Prohibited actions

List only meaningful prohibitions. Examples:

- broaden scope;
- merge;
- deploy;
- modify protected inputs;
- remediate outside the authorized target;
- contact external parties;
- rerun a completed operation unless explicitly authorized.

## Stop conditions

Stop and report without repair if:

- required identity mismatches;
- authority is insufficient;
- a protected invariant cannot be preserved;
- required access is unavailable;
- the requested operation cannot be completed without crossing a prohibited boundary.

Add task-specific stop conditions here.

## Acceptance criteria

Define what successful completion means in observable terms.

Prefer behavioral and evidence-backed criteria over prose assertions.

## Evidence to retain

Require only evidence that carries distinct value, such as:

- exact changed files;
- test command and result;
- source/artifact hashes;
- console transcript;
- machine-readable receipt;
- before/after identity where mutation risk matters.

## Return contract

Return one compact report containing:

- reported result: `PASS`, `FAIL CLOSED`, or task-specific equivalent;
- what changed or was created;
- what was inspected/tested;
- evidence paths/identities;
- limitations and unresolved questions;
- explicit mutation/boundary confirmation.

A Builder PASS is an operator-reported result. The Architect adjudicates it from the returned evidence.

## End boundary

State exactly where the Builder must stop.

Do not recommend or execute the next gate unless this task explicitly grants that authority.
