# Workflow: Script Quality Review

Use this workflow for a findings-first review of automated test quality, reliability, and maintainability.

## Inputs

Required:

- one or more automated test files or directories

Optional:

- supporting helpers, fixtures, or page objects
- target project root
- local testing rules in `.test-guidelines.md`

## Steps

1. Read the target tests and enough supporting files to understand setup, actions, assertions, and hidden abstractions.
2. Read the matching framework guide from `references/libraries/<framework>/knowledge.md`.
3. Apply rule precedence:
   - nearest component `.test-guidelines.md`
   - project-root `.test-guidelines.md`
   - `references/guidelines/organization.md`
   - framework guidance
4. Run deterministic checks only when they are already available in the target project or obviously safe to execute. Prefer:
   - existing lint commands
   - static analysis commands already defined in the repo
   - narrow test-file checks rather than full suites
5. Review the automation across these areas:
   - readability and structure
   - reliability and synchronization
   - assertion strength
   - data and state control
   - maintainability and reuse
   - traceability and rule compliance
6. When the script uses unfamiliar or borderline API surface, verify behavior with official docs before making strong claims.
7. Write the report using `references/report-contracts.md` and `assets/test_script_review.j2`.

## Guardrails

1. Findings come first. Do not bury critical issues under a long summary.
2. Back every finding with code evidence, tool output, or a clearly cited rule.
3. Do not label a pattern as wrong just because it differs from your preference.
4. Distinguish product risk from style preference.
5. Do not mutate this skill repository during routine review work.
6. If the user later asks for fixes, use the report as the starting point rather than silently switching from review to implementation.
