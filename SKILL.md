---
name: automated-test-reviewer
description: Use when Codex needs to explain automated test scripts in business language, review test automation quality with findings-first output, or map functional/manual test cases to automated coverage across UI, API, and contract-testing frameworks.
metadata:
  dispatcher-layer: feedback
  dispatcher-lifecycle: active
  dispatcher-category: testing
  dispatcher-capabilities: automated-test-review, functional-case-mapping, test-script-explanation, automation-quality-review
  dispatcher-accepted-intents: review_automation_quality, map_functional_cases_to_automation, explain_automated_test_script
  dispatcher-input-artifacts: automated_test_suite, manual_test_cases, functional_requirements, repo_context
  dispatcher-output-artifacts: quality_review_report, coverage_mapping_report, script_explanation, review_artifact
  dispatcher-stack-tags: testing, review, framework-agnostic
  dispatcher-risk: low
  dispatcher-writes-files: true

---

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --model <model_name> --reason <reason>` (or `./log-dispatch.sh` on Linux)

# Automated Test Reviewer

> **Author:** jovd83 | **Version:** 2.1.1


Use this skill to turn automated tests and manual or functional test assets into clear review artifacts. Default to evidence-based analysis, not code modification. Write reports into the target project, never back into this skill repository.

## 1. Start

1. Classify the request into one primary workflow:
   - `script-explanation`
   - `functional-case-mapping`
   - `script-quality-review`
2. If the user asks for multiple outcomes, choose the primary workflow first and list the secondary artifacts you will also produce.
3. Confirm the target inputs:
   - test script files or directories
   - functional or manual test case files when mapping is requested
   - target project root for report output
4. If a required path is missing and you cannot infer it safely, ask one focused question. Do not ask broad discovery questions.
5. Refuse requests that are unrelated to automated test analysis, documentation, coverage mapping, or automation quality review.

## 2. Respect the Memory Boundary

1. Use runtime memory for temporary reasoning, extracted notes, and intermediate classifications.
2. Use project-local persistent memory only for artifacts created in the target repository, normally under `reviews/`.
3. Do not write back into this skill's `references/`, `assets/`, or other skill files during normal execution.
4. Do not promote runtime findings into shared memory automatically.
5. If long-term cross-agent reuse is requested, integrate with an external shared-memory skill or another explicit persistence mechanism instead of inventing one inside this repository.

## 2a. Dispatcher Integration

Use `skill-dispatcher` as the preferred cross-skill routing layer when another skill needs a review or mapping step from this package.

1. Accept dispatcher-led handoffs for intents such as `review_automation_quality`, `map_functional_cases_to_automation`, and `explain_automated_test_script`.
2. Keep this skill review-first. Do not turn a review request into unsolicited test implementation or framework migration work.
3. Treat direct references from sibling skills as a compatibility fallback, not the preferred integration contract.
4. Keep shared-memory usage limited to stable policy or conventions supplied externally, never task-local review state.

## 3. Detect Context Before Analyzing

1. Inspect the test files, nearby manifests, and imports before choosing framework guidance.
2. Recognize common frameworks from imports and conventions such as:
   - Playwright: `@playwright/test`, `playwright.config.*`
   - Cypress: `cypress.config.*`, `*.cy.*`
   - Selenium: `org.openqa.selenium`, `selenium.webdriver`
   - Rest Assured: `io.restassured`
   - Postman/Newman: Collection JSON, `pm.test`, `newman`
   - Pact: `au.com.dius.pact`, `@pact-foundation`
   - JUnit 5: `org.junit.jupiter`
3. Read the matching library guide from `references/libraries/<framework>/knowledge.md` when one exists.
4. If the framework is missing or ambiguous, use `references/workflows/framework-onboarding.md`.

## 4. Apply the Workflow

1. For script explanation, read `references/workflows/script-explanation.md`.
2. For functional or manual coverage mapping, read `references/workflows/functional-case-mapping.md`.
3. For findings-first automation review, read `references/workflows/script-quality-review.md`.
4. Use `references/report-contracts.md` to keep output structure, severity, coverage labels, and evidence style consistent.

## 5. Non-Negotiable Analysis Rules

1. Ground every conclusion in repository evidence, deterministic tool output, or explicitly cited documentation.
2. Distinguish clearly between:
   - observed behavior
   - reasonable inference
   - missing or unverifiable information
3. Prefer official documentation when checking unfamiliar APIs, recent deprecations, or framework-specific edge cases.
4. Do not claim coverage for helpers, fixtures, or service behavior that you could not inspect.
5. Do not invent line numbers, requirements, or business intent.
6. If you run linting or deterministic checks, use existing project commands where possible and avoid installing new dependencies unless the user asks.
7. Treat organization, project, and component rules as higher priority than generic framework guidance.
8. If local enterprise rules conflict across layers, document the conflict and apply the highest-precedence rule.

## 6. Output Rules

1. Write review artifacts into `<target-project>/reviews/`.
2. Use descriptive filenames such as:
   - `reviews/login-script-explanation.md`
   - `reviews/checkout-coverage-mapping.md`
   - `reviews/order-api-quality-review.md`
3. Keep the chat response concise:
   - what you reviewed
   - what you produced
   - the highest-value findings or coverage gaps
4. When possible, include file paths, evidence snippets, and confidence notes inside the report, not only in chat.
5. If the user does not want files written, provide the same report content inline and say that file creation was skipped.

## 7. Enterprise Rule Resolution

Apply rule precedence in this order:

1. Component-level `.test-guidelines.md` closest to the reviewed tests
2. Project-level `.test-guidelines.md` at the repository root
3. Skill-local guidance under `references/guidelines/`
4. Framework guidance under `references/libraries/`
5. General engineering judgment

Use `references/guidelines/README.md` for the lookup model.

## 8. Useful Bundled Files

1. `references/report-contracts.md`
   Use for output shape, severity definitions, coverage labels, and evidence requirements.
2. `references/workflows/script-explanation.md`
   Use for stakeholder-friendly narrative explanations of test intent and behavior.
3. `references/workflows/functional-case-mapping.md`
   Use for traceability and gap analysis between test cases and automation.
4. `references/workflows/script-quality-review.md`
   Use for findings-first quality reviews with prioritized remediation guidance.
5. `references/workflows/framework-onboarding.md`
   Use when the framework is unknown, mixed, or unsupported by the bundled library guides.
6. `assets/*.j2`
   Use as report shape references when drafting the final Markdown artifacts.

## 9. Example Requests

1. `Explain tests/auth/login.spec.ts for a product manager.`
2. `Map docs/test-cases/checkout.csv against tests/e2e/checkout/ and show the missing coverage.`
3. `Review these Cypress specs for flakiness and weak assertions.`
4. `Compare our Postman collection to the documented smoke cases and show what is still manual.`

## 10. Troubleshooting

1. Problem: The request mixes explanation, quality review, and refactoring.
   Fix: Perform the requested analysis first, summarize findings, and only propose implementation follow-up unless the user explicitly asks for code changes.
2. Problem: The scripts rely on helpers or fixtures you cannot locate.
   Fix: Mark the affected areas as `unverifiable`, list the missing files, and continue with the evidence you do have.
3. Problem: The framework is not covered by a bundled knowledge file.
   Fix: Use `references/workflows/framework-onboarding.md` and keep any new framework notes project-local unless the user explicitly asks to evolve the skill.
4. Problem: The user wants broad product refactoring or non-testing architecture work.
   Fix: Decline or redirect because this skill is for automated test understanding, coverage mapping, and quality review.

## 11. Gotchas

1. **Context Constraints on Mass Review**: Providing an entire test suite or a massive manual test CSV (hundreds of rows) at once can degrade analysis depth. Recommend performing coverage mapping or reviews feature by feature.
2. **Semantic Divergence in Mapping**: When tracing manual steps to automated code, differing terminology (e.g., a manual step saying "Submit Order" vs code doing `.click('#checkout')`) can cause false negatives in coverage mapping.
3. **Hidden State and Dynamic Data**: The reviewer analyzes scripts statically. Tests heavily reliant on dynamic setup, database state, or implicit external fixtures may be misunderstood since the runtime behavior is invisible.
4. **Report Output Path Constraints**: Reports are written directly to `<target-project>/reviews/`. Ensure the target repository allows these files or manually specify an alternate directory if this conflicts with `.gitignore` configurations.