# Selenium Review Guide

## Recognize It

- `org.openqa.selenium.*`
- `selenium.webdriver`
- `WebDriver`, `By`, `WebDriverWait`, `ExpectedConditions`

## Prefer

- explicit waits targeted to a specific condition
- centrally managed driver creation and teardown
- resilient locators and helper abstractions for repeated workflows
- clear separation between interaction helpers and test assertions
- stable data setup outside the UI when the system allows it

## Flag During Review

- `Thread.sleep(...)` for synchronization
- implicit waits mixed with explicit waits
- cached `WebElement` usage across DOM refreshes
- brittle XPath or layout-heavy selectors
- drivers that are not reliably closed
- assertions buried inside page objects or utility classes

## Nuance

- Page objects are common, but screenplay or other patterns can also be valid when they improve maintainability.
- Parallel execution is safe only when driver lifecycle and shared test data are isolated.
- Large Selenium suites often fail because of environment control, not just locator quality.

## Primary References

- https://www.selenium.dev/documentation/
- https://www.selenium.dev/documentation/webdriver/waits/
