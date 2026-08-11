# Project Charter

## Project ID

`<PROJECT-ID>`

## Mission

Describe the actual outcome this project exists to achieve.

## Governing BRIDGE identity

- Version: `<BRIDGE-VERSION>`
- Source repository or distribution: `<BRIDGE-SOURCE>`
- Commit SHA or equivalent immutable identity, where applicable: `<BRIDGE-IMMUTABLE-IDENTITY-OR-NOT-AVAILABLE>`
- Identity limitation, if any: `<LIMITATION-OR-NONE>`

Record the exact BRIDGE source governing this project. Do not fabricate an immutable identity when the available source or distribution does not provide one.

## Non-goals

State nearby work that is explicitly outside this project.

## Role assignments

- Owner: `<OWNER>`
- Architect: `<ARCHITECT>`
- Primary Builder: `<PRIMARY-BUILDER>`
- Authorized Stand-in Builder: `<STANDIN-BUILDER>`
- Independent Verifier: `<VERIFIER>`

Role separation from BRIDGE remains in force.

## Authority and standing delegations

State any project-specific standing authority for:

- implementation writes;
- commit/push;
- PR creation/update;
- external communication/submission;
- release/deployment;
- destructive actions.

If omitted, no additional standing write authority is implied. BRIDGE core authority rules apply.

## Material boundary enforcement map

Record only consequential authority boundaries whose enforcement matters to project risk.

| Boundary | Mechanical control, if suitable and proportionate | Residual procedural trust |
|---|---|---|
| `<MATERIAL-BOUNDARY>` | `<CONTROL-OR-NOT-AVAILABLE/UNSUITABLE/DISPROPORTIONATE>` | `<EXPLICIT-RESIDUAL-TRUST>` |

Do not expand this into a general compliance matrix.

## Protected assets / irreversible boundaries

List production systems, data, repositories, customer/public channels, secrets, regulated material, or other assets requiring special control.

## Repository / system map

List the repositories, systems, services, environments, and major data roots that comprise the project.

## Definition of success

State the project-level finish line. Gate-level criteria belong in `ACCEPTANCE_CRITERIA.md` and task specs.

## Domain boundary

Domain-specific rules belong in `DOMAIN_RULES.md`. They do not modify the reusable operating system unless the Owner explicitly adopts a documented exception here.
