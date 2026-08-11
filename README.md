# BRIDGE

**Version:** 1.0.0

**A governed multi-agent project operating model for owner-led, architect-directed, independently verified work.**

BRIDGE preserves a reusable way of running difficult technical projects without depending on one chat's memory, one model's confidence, or one person's ability to keep every moving part in their head.

Its core structure is:

- one human **Owner** with final consequential authority;
- one active **Architect cockpit** responsible for the map, sequencing, reconciliation, and adjudication;
- one powerful bounded **Builder** at a time;
- one independent adversarial **Verifier** who does not repair what it reviews;
- explicit evidence and claim boundaries;
- clean phase transitions and durable handoffs;
- executor freedom inside bounded objectives;
- proportional governance: enough control to protect truth and irreversible boundaries, not process for its own sake.

## The governing idea

**The repository is durable memory. Chats are workers.**

A fresh agent should be able to reconstruct the operating model from repository bytes without relying on prior conversation history, hidden custom instructions, or remembered context.

BRIDGE governs **how the team works**. A project overlay governs **what a particular project means**. Domain-specific scientific, legal, engineering, product, or business rules belong in the project overlay and must not silently become BRIDGE rules.

## Reference casting

BRIDGE roles are functions, not brands. The reference implementation that produced this framework uses the following role cast:

- **Owner:** Karma
- **Architect:** Hex / ChatGPT
- **Primary Builder:** Codex
- **Authorized Stand-in Builder:** Claude Code
- **Independent Verifier:** Fable

Those assignments are replaceable. The role boundaries are the invariant. See `docs/REFERENCE_CAST.md`.

## Start here

- Fresh Architect: read `START_HERE.md`.
- New project: read `bootstraps/NEW_PROJECT_SETUP.md` and instantiate `project-template/`.
- Role-specific cold starts are in `bootstraps/`.

## Core canon

- `core/GOVERNANCE.md` — roles, authority, cockpit rules, write/merge/submission boundaries.
- `core/OPERATING_RULES.md` — durable operating rules.
- `core/ROLE_AND_POSTURE.md` — reasoning and communication posture by role.
- `core/EVIDENCE_AND_ADJUDICATION.md` — evidence hierarchy, PASS semantics, reacquisition, verification, and adjudication.
- `templates/TASK_SPEC_TEMPLATE.md` — bounded Builder operation template.
- `templates/HANDOFF_TEMPLATE.md` — clean phase/chat migration template.
- `templates/COMPREHENSION_HANDSHAKE_TEMPLATE.md` — fresh-Architect cold-start gate.

## Design principle

Governance should reduce uncertainty and protect irreversible boundaries. **It should not become the work.**

## License

MIT. See `LICENSE`.
