# Pact Review Guide

## Recognize It

- `@pact-foundation/*`
- `au.com.dius.pact`
- consumer-driven contract files and broker publishing

## Prefer

- consumer-driven contracts that describe the interface the consumer actually needs
- flexible matchers for dynamic values instead of exact-value lock-in
- explicit provider states for setup during provider verification
- versioned contract publication and verification in CI
- a clear boundary between contract coverage and functional coverage

## Flag During Review

- exact matching of timestamps, IDs, or other dynamic fields when a semantic matcher is sufficient
- use of Pact as a substitute for full functional or end-to-end testing
- contracts written from the provider perspective instead of the consumer need
- assertions about business rules that belong in service or integration tests
- brokerless workflows that make compatibility hard to reason about

## Nuance

- Contract tests should be fast and focused on interface expectations, not complete scenario simulation.
- Provider states are part of the test design. Weak or vague state setup often leads to brittle verification.
- Consumer and provider teams both benefit when contracts stay minimal and intention-revealing.

## Primary References

- https://docs.pact.io/
