# New Project Setup

This operating system is intentionally separate from any one project's domain rules.

## Recommended setup

Create a dedicated control repository for the project. Choose public or private visibility according to the project's data, security, and collaboration needs.

Copy the contents of `project-template/` into its root, then complete the placeholders.

Keep this BRIDGE repository as the governing reference, or copy the `core/`, `templates/`, and `bootstraps/` directories into the project control repository if the environment requires a self-contained package.

Before assigning project work, record the governing BRIDGE identity in `PROJECT_CHARTER.md`: the BRIDGE version, source repository or distribution identity, and commit SHA or equivalent immutable identity where one applies. If no immutable identity is available, record the available version or distribution identity and that limitation honestly.

## Bootstrap sequence

1. **Owner defines the charter.**
   Fill `PROJECT_CHARTER.md` with mission, role assignments, risk/authority rules, protected assets, and any standing delegations.

2. **Record current state.**
   Fill `CURRENT_STATE.md` from primary evidence. Do not import old project assumptions.

3. **Separate domain from governance.**
   Put project-specific scientific, legal, engineering, product, or business constraints in `DOMAIN_RULES.md` and `ACCEPTANCE_CRITERIA.md`.

4. **Start the Architect.**
   Give the fresh Architect `bootstraps/ARCHITECT_COLD_START.md` and repository access.

5. **Require the comprehension handshake.**
   The Architect reconstructs state read-only and the Owner accepts or corrects it.

6. **Architect creates the first bounded task.**
   Use `templates/TASK_SPEC_TEMPLATE.md`.

7. **Assign exactly one Builder.**
   Choose one Primary Builder and, optionally, one authorized Stand-in Builder. The BRIDGE reference casting uses Codex as Primary Builder and Claude Code as Stand-in Builder.

8. **Freeze a reviewable result.**
   When independent review is warranted, stop the Builder and give the Verifier a frozen or read-only review target.

9. **Architect reconciles.**
   Keep Builder report, independent verification, Architect adjudication, and Owner authorization distinct.

10. **Handoff only at a clean boundary.**
    Use `templates/HANDOFF_TEMPLATE.md` when migrating the Architect cockpit or closing a meaningful phase.

## Do not inherit prior domain rules

A new project must not inherit any earlier project's domain-specific technical rules merely because they were used successfully before.

Reusable governance lives here. Domain truth belongs to the active project.
