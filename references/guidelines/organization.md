# Organization Rules Template

Use this file for company-wide testing rules that should apply unless a higher-precedence component or project rule overrides them.

Suggested sections:

## Traceability

- Example: every automated test must reference a requirement, ticket, or case ID

## Naming

- Example: test names must describe the expected behavior and state under test

## Prohibited Patterns

- Example: hard waits are not allowed in UI automation
- Example: stateful test ordering is not allowed in any suite

## Evidence Expectations

- Example: every state-changing test must assert visible user feedback or API side effects

## Exceptions

- Example: temporary exceptions must include an owner and expiration note

Replace the examples with your actual organizational rules. Keep them specific enough that a reviewer can confirm compliance from repository evidence.
