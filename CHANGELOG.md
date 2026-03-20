# Changelog

All notable changes to the `automated-test-reviewer` repository will be documented in this file.

The format is based on Keep a Changelog and uses `Added`, `Changed`, `Removed`, and `Fixed` sections where useful.

## [Unreleased]

## [2.0.0] - 2026-03-18

### Added
- `agents/openai.yaml` metadata for better agent-platform discoverability.
- `scripts/validate_skill.py` to validate frontmatter, links, ASCII safety, metadata, and eval fixtures.
- `evals/smoke-prompts.json` with representative routing and output expectations.
- `references/report-contracts.md` to define consistent output structure, severity labels, and coverage states.
- `references/workflows/framework-onboarding.md` as a safe fallback for unknown or mixed frameworks.

### Changed
- Rewrote `SKILL.md` to be standards-aligned, findings-first, and explicit about memory boundaries.
- Reworked workflow docs to clarify inputs, output contracts, ambiguity handling, and escalation rules.
- Replaced weak or speculative framework notes with more consistent review-oriented guidance.
- Rebuilt report templates into clean ASCII Markdown structures suitable for enterprise reporting.
- Refreshed the README to clearly document scope, installation, operating model, validation, and contribution expectations.

### Removed
- Runtime self-modification behavior that instructed the agent to mutate the skill repository during ordinary use.
- Non-standard `SKILL.md` frontmatter fields that reduced compatibility with Agent Skills tooling.

## [1.0.0] - 2026-03-17

### Added
- Initial release of the Automated Test Reviewer skill.
- Core workflows for Script Explanation, Functional Case Mapping, and Script Quality Review.
- Self-improvement capabilities for learning new testing frameworks dynamically.
- Support for multiple frameworks including Cypress, Playwright, Selenium, and Postman.
