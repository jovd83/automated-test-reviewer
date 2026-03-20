# Workflow: Script Explanation

Use this workflow when the user wants a test script translated into plain language for stakeholders, reviewers, or onboarding.

## Inputs

Required:

- at least one test script file

Optional:

- helper files, fixtures, page objects, or API clients referenced by the script
- business requirement or ticket identifiers

## Steps

1. Read the target script and the minimal set of supporting files required to understand control flow.
2. Break the script into:
   - scope
   - setup and preconditions
   - main actions
   - validations
   - cleanup
   - missing dependencies
3. Identify the business intent of the scenario. If the intent is not explicit, infer it carefully from names, assertions, and data setup, then label it as inferred.
4. Translate the automation into stakeholder language without hiding important technical qualifiers.
5. Call out missing helpers, fixtures, or hidden abstractions that prevent a complete explanation.
6. Use `references/report-contracts.md` and `assets/test_script_explanation.j2` for the report structure.
7. Add concise improvement notes only if they materially improve clarity, maintainability, or observability.

## Guardrails

1. Do not pretend to know what hidden helpers do.
2. Do not rewrite the script unless the user asks for code changes.
3. Keep the explanation faithful to the observed assertions, not the presumed product behavior.
4. If the same file contains multiple tests, explain them separately or explicitly scope the explanation to one test.
