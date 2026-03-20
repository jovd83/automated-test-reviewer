# Rule Resolution

Use this folder for human-authored testing rules that override generic framework guidance.

## Precedence

Resolve rules from highest to lowest priority:

1. Component-level `.test-guidelines.md` nearest to the reviewed tests
2. Project-level `.test-guidelines.md` at the repository root
3. Skill-local guidance in this folder
4. Framework guidance in `references/libraries/`
5. General engineering judgment

If two rules conflict, apply the highest-precedence rule and document the conflict in the report.

## Recommended Storage Locations

### In the target repository

Use these when the rules should travel with the code under review:

- Project-wide rules: `<repo-root>/.test-guidelines.md`
- Component-specific rules: `<component-path>/.test-guidelines.md`

### In this skill repository

Use these when the same rules must be reusable across many reviewed projects:

- Project family rules: `references/guidelines/projects/<project-name>.md`
- Component family rules: `references/guidelines/components/<component-name>.md`

## Authoring Guidance

Good rules are:

- concrete
- testable
- scoped
- stable over time

Avoid vague policy such as "write cleaner tests." Prefer explicit expectations such as "all state-changing UI flows must assert the resulting user-visible confirmation."
