# Cypress Review Guide

## Recognize It

- `cypress.config.*`
- `*.cy.*`
- `cy.get`, `cy.intercept`, `cy.session`, `Cypress.Commands`

## Prefer

- stable selectors such as `data-*` attributes or accessible queries
- built-in retry behavior through `should(...)` and deterministic command chains
- network aliases and explicit application signals instead of timed waits
- programmatic state setup through APIs, tasks, fixtures, or app-supported shortcuts
- `cy.session()` when it clearly reduces repeated login cost without hiding state leaks

## Flag During Review

- `cy.wait(<number>)` for synchronization
- selectors tied to styling or DOM shape instead of user-facing intent
- conditional branching on unstable DOM state
- shared state between tests or assumptions about previous test execution
- `click({ force: true })` or similar overrides without a justified actionability reason
- tests that make state-changing requests but never assert the resulting user-visible outcome

## Nuance

- Page objects can help repeated UI flows, but simple tests do not need ceremony.
- Heavy custom commands can hide intent if they become wrappers around full scenarios.
- Network stubbing is useful for isolating external dependencies, but overuse can erase real integration risk.

## Primary References

- https://docs.cypress.io/app/core-concepts/best-practices
- https://docs.cypress.io/app/core-concepts/retry-ability
- https://docs.cypress.io/api/commands/intercept
