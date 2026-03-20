# Workflow: Functional Case Mapping

Use this workflow to compare manual, functional, or acceptance test assets against the available automation and show what is covered, partially covered, missing, or unverifiable.

## Inputs

Required:

- one or more functional or manual test case sources
- one or more automated test files or directories

Optional:

- helper files, page objects, fixtures, or requirement documents

## Steps

1. Normalize the manual or functional cases into a common shape:
   - case ID
   - title
   - preconditions
   - actions
   - expected results
2. Inspect the automation and supporting files needed to confirm setup, behavior, and assertions.
3. Map each case element to automation evidence using the status labels from `references/report-contracts.md`:
   - `matched`
   - `partial`
   - `missing`
   - `unverifiable`
4. Record the exact automation evidence used for each mapping decision.
5. Generate:
   - a per-case report using `assets/test_case_mapping_report.j2`
   - a summary table using `assets/mapping_summary_table.j2`
   - an automation-to-case traceability view using `assets/script_to_testcase_trace.j2`
6. Highlight the highest-risk gaps first, especially:
   - missing assertions
   - setup-only flows
   - unverified negative paths
   - requirements with no reliable automation coverage

## Guardrails

1. Do not count navigation or setup alone as full coverage.
2. Do not mark a case as covered if the expected result has no observable assertion.
3. Prefer `unverifiable` over optimistic matching when helper indirection prevents confirmation.
4. If the user asks for interactive mapping, keep the same evidence standards and report shape.
