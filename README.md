# Automated Test Reviewer

[![Validate Skills](https://github.com/jovd83/automated-test-reviewer/actions/workflows/validate.yml/badge.svg)](https://github.com/jovd83/automated-test-reviewer/actions/workflows/validate.yml)
[![version](https://img.shields.io/badge/version-2.0.0-blue)](CHANGELOG.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)

Explain, assess, and map automated tests with evidence-first Markdown reports.

This Agent Skill helps another agent do three high-value jobs well:

1. Explain a test script in plain business language.
2. Review automation quality with findings-first output and actionable recommendations.
3. Map manual or functional test cases to existing automation and show real coverage gaps.

The repository is designed for practical agent use, not as a vague prompt dump. It includes workflow instructions, framework-specific review guides, report contracts, output templates, and lightweight validation artifacts.

## What This Skill Is Responsible For

- Turning test automation into stakeholder-friendly explanations.
- Reviewing UI, API, and contract tests for reliability, maintainability, assertion quality, and traceability.
- Producing coverage-mapping reports between manual or functional cases and automated scripts.
- Writing artifacts into the target project under `reviews/`, not into the skill repository.

## What This Skill Is Not Responsible For

- Acting as a generic refactoring assistant for unrelated application code.
- Storing persistent cross-agent memory inside the skill repository.
- Auto-mutating its own framework knowledge during normal runtime execution.
- Replacing framework documentation or full framework tutorials.

## Supported Review Surfaces

- Playwright
- Cypress
- Selenium WebDriver
- Rest Assured
- Postman / Newman collections
- Pact
- JUnit 5-based test suites
- Unknown or mixed frameworks through the fallback onboarding workflow

## How It Works

1. The agent classifies the request as explanation, coverage mapping, or quality review.
2. It detects the framework from imports, manifests, naming conventions, and repository structure.
3. It loads only the relevant workflow and framework reference material.
4. It produces a structured Markdown artifact using the bundled report contracts and templates.
5. It writes the result into the target repository's `reviews/` directory unless the user asks for inline-only output.

## Memory Model

- Runtime memory: temporary reasoning and extracted notes for the current task only.
- Project-local persistent memory: generated reports and optional supporting notes written into the reviewed repository.
- Shared memory: intentionally out of scope for this skill. If durable cross-agent reuse is needed, integrate an external shared-memory skill instead of expanding this repository into shared infrastructure.

## Installation

Clone or copy the folder into a local skills directory that your agent runtime can discover:

```bash
git clone https://github.com/jovd83/automated-test-reviewer.git
```

Common local skill locations:

- `~/.agents/skills/`
- `~/.cursor/skills/`
- Tool-specific local skill directories supported by your agent platform

## Quick Start

Example prompts:

- `Use $automated-test-reviewer to explain tests/e2e/login.spec.ts for a product manager.`
- `Use $automated-test-reviewer to review cypress/e2e/checkout.cy.ts and highlight flaky patterns.`
- `Use $automated-test-reviewer to map docs/manual-cases/checkout.csv against tests/e2e/checkout/.`

## Repository Layout

```text
SKILL.md
agents/
  openai.yaml
assets/
  mapping_summary_table.j2
  script_to_testcase_trace.j2
  test_case_mapping_report.j2
  test_script_explanation.j2
  test_script_review.j2
evals/
  smoke-prompts.json
references/
  guidelines/
  libraries/
  report-contracts.md
  workflows/
scripts/
  validate_skill.py
CHANGELOG.md
README.md
```

## Validation and Maintenance

Run the repository validator before publishing changes:

```bash
python scripts/validate_skill.py
```

The validator checks:

- `SKILL.md` frontmatter compliance
- required repository files
- local Markdown link integrity
- ASCII safety for text artifacts
- `agents/openai.yaml` shape
- eval fixture structure

## Evaluation Strategy

The repository includes `evals/smoke-prompts.json`, a lightweight prompt suite for manual or automated forward-testing. Each case defines the expected workflow and artifact shape so maintainers can verify that future edits still route correctly and preserve output quality.

## Contribution Notes

Keep changes small, auditable, and aligned with the skill's scope:

1. Tighten instructions before adding more files.
2. Prefer explicit report contracts over vague prose.
3. Do not add self-modifying behavior.
4. Keep framework guidance review-oriented and grounded in official documentation.
5. Run `python scripts/validate_skill.py` after substantive changes.

## Publishability Notes

This repository is intentionally focused on the skill package itself. Optional future additions such as CI workflows, release automation, or a formal open-source license can be added by the repository owner without changing the skill contract.
