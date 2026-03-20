# Report Contracts

Use these contracts to keep outputs consistent across explanation, mapping, and quality-review workflows.

## Shared Rules

1. Use valid Markdown only.
2. Keep the tone professional, plain, and audit-friendly.
3. Cite evidence using file paths and concise snippets when possible.
4. Separate observed facts from inference and uncertainty.
5. Keep generated artifacts in the target repository's `reviews/` directory unless the user asks for inline-only output.

## Quality Review Contract

Required sections:

1. `Scope`
2. `Executive Summary`
3. `Findings`
4. `Strengths`
5. `Deterministic Checks`
6. `Rule Resolution`
7. `Suggested Remediations`
8. `Assumptions and Gaps`

### Severity Labels

- `critical`: likely to hide failures, create false confidence, or block trustworthy execution
- `high`: meaningful reliability, maintainability, or coverage risk
- `medium`: clear issue with moderate impact or compounding maintenance cost
- `low`: improvement opportunity with limited immediate risk

### Finding Shape

Each finding should include:

- severity
- title
- evidence
- impact
- recommendation
- confidence (`high`, `medium`, or `low`)

## Script Explanation Contract

Required sections:

1. `Scope`
2. `Business Intent`
3. `Setup and Preconditions`
4. `Test Flow`
5. `Validations`
6. `Missing Context`
7. `Risks and Assumptions`
8. `Glossary`

The explanation should translate automation behavior into stakeholder language without flattening important technical caveats.

## Functional Coverage Mapping Contract

Required sections:

1. `Scope`
2. `Coverage Summary`
3. `Per-Case Analysis`
4. `Automation-to-Case Traceability`
5. `Coverage Gaps`
6. `Assumptions and Unverifiable Areas`

### Mapping Status Labels

- `matched`: the automation clearly covers the intent and assertion
- `partial`: some intent is present, but setup, action, or assertion coverage is incomplete
- `missing`: no credible coverage found
- `unverifiable`: coverage may exist, but helper indirection or missing files prevented confirmation

### Coverage Guidance

1. Calculate coverage from observable evidence, not optimistic assumptions.
2. Treat setup-only automation without assertions as at most `partial`.
3. If a manual case depends on data or helpers you cannot inspect, prefer `unverifiable` over `matched`.

## File Naming Guidance

Recommended output names:

- `reviews/<subject>-script-explanation.md`
- `reviews/<subject>-quality-review.md`
- `reviews/<subject>-coverage-mapping.md`
- `reviews/<subject>-traceability.md`

Use lowercase kebab-case filenames where practical.
