# JUnit 5 Review Guide

## Recognize It

- `org.junit.jupiter`
- `@Test`, `@BeforeEach`, `@AfterEach`, `@ParameterizedTest`
- `Assertions.*`

## Prefer

- isolated tests with explicit setup and teardown
- `assertThrows`, `assertAll`, and parameterized tests where they improve clarity
- narrow test scope with one behavior under test per method
- tagging and clear naming for execution control
- helper methods or fixtures that reduce duplication without hiding business intent

## Flag During Review

- order-dependent tests
- exceptions caught and ignored without assertions
- `Thread.sleep(...)` used to wait for async behavior
- disabled tests without an owner or reason
- large tests that verify many unrelated behaviors at once
- setup performed in a way that leaks shared mutable state across tests

## Nuance

- Fluent assertion libraries can improve readability, but consistency matters more than chasing style trends.
- Integration-heavy tests may need broader fixtures, but they still need clear isolation boundaries.
- Parameterization is valuable only when the data table remains readable and intention-revealing.

## Primary References

- https://junit.org/junit5/docs/current/user-guide/
