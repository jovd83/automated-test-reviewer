# Rest Assured Review Guide

## Recognize It

- `io.restassured`
- `given().when().then()`
- `RequestSpecification`, `ResponseSpecification`

## Prefer

- reusable request and response specifications for shared headers, auth, and defaults
- assertions on status, headers, and payload semantics instead of status-only checks
- typed payloads or serializers over manual JSON string assembly
- clear setup data creation per test or per fixture
- explicit polling for asynchronous workflows rather than blind sleeps

## Flag During Review

- string-concatenated JSON request bodies
- repeated auth headers or base URIs in every test
- extraction of payload fields without first asserting the response contract
- shared mutable data that makes tests order-dependent
- logs that may expose tokens, secrets, or personal data
- async API tests that rely on fixed delays instead of polling terminal state

## Nuance

- Not every test needs a custom DTO, but repeated complex payloads should not stay as hand-built strings.
- Negative-path coverage matters; a suite full of `200 OK` checks can still be dangerously weak.
- Contract assertions and business assertions often need to coexist for trustworthy API coverage.

## Primary References

- https://rest-assured.io/
