# Postman Review Guide

## Recognize It

- Postman collection JSON
- `pm.test(...)`
- `pm.response`, `pm.environment`, `pm.collectionVariables`
- Newman execution scripts

## Prefer

- environment or collection variables instead of hardcoded URLs and secrets
- explicit `pm.test(...)` assertions for status, body, and negative cases
- small, purposeful collections and folders grouped by feature or workflow
- pre-request scripts only when they add clear value such as auth or deterministic data generation
- versioned collections that can also run in CI through Newman or an equivalent runner

## Flag During Review

- requests with little or no meaningful assertions
- hardcoded tokens, hosts, or environment-specific identifiers
- monolithic collections with unrelated flows bundled together
- hidden request chaining that makes debugging difficult
- error-path scenarios that are never asserted
- tests that depend on untracked local environment state

## Nuance

- Postman can be a valid automation surface, but collections still need the same rigor as code-based tests.
- Folder-level scripts can improve consistency, but they can also hide behavior if overused.
- Request order should be intentional and documented when one request seeds data for another.

## Primary References

- https://learning.postman.com/docs/
- https://learning.postman.com/docs/tests-and-scripts/write-scripts/test-scripts/
