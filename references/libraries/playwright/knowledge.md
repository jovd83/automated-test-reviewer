# Playwright Review Guide

## Recognize It

- `@playwright/test`
- `playwright.config.*`
- `test`, `expect`, `page`, `locator`, `request`

## Prefer

- role-based, label-based, or test-id locators over deep CSS chains
- web-first assertions such as `await expect(locator)...` instead of manual polling
- deterministic state setup through fixtures, API calls, or `storageState`
- centralized configuration for base URL, timeouts, devices, and retries
- reusable helpers or page objects when flows are repeated across tests

## Flag During Review

- `page.waitForTimeout(...)` or other hard waits
- brittle selectors tied to layout structure
- reading DOM state manually and then using plain assertions where retrying assertions are available
- shared state between tests or dependence on execution order
- `force: true` without a documented reason
- tests that drive slow UI setup for every scenario when faster setup paths already exist

## Nuance

- Page objects are helpful for repeated workflows but are not mandatory for very small suites.
- `networkidle` is not a universal readiness signal. Prefer assertions tied to the user-visible state.
- Screenshot assertions can be powerful, but only when baselines and tolerances are intentionally managed.

## Primary References

- https://playwright.dev/docs/intro
- https://playwright.dev/docs/actionability
- https://playwright.dev/docs/test-assertions
