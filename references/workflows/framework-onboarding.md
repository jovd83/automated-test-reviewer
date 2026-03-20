# Workflow: Framework Onboarding

Use this workflow when the automation framework is unknown, mixed, or not covered by a bundled library guide.

## Goal

Collect enough reliable context to analyze the target tests without teaching the skill to self-modify during ordinary runtime use.

## Steps

1. Inspect imports, manifests, file names, and command configuration to infer the toolchain.
2. Normalize common aliases when possible:
   - `pact`, `pact-jvm`, `@pact-foundation/*` -> `pact`
   - `rest-assured`, `io.restassured` -> `restassured`
   - `newman`, `postman collection` -> `postman`
3. Search the target repository for local documentation before going to the web.
4. If online verification is needed, prefer official documentation and primary sources.
5. Build a runtime-only note containing:
   - what the framework is
   - how it synchronizes
   - how assertions work
   - how state is typically managed
   - the most relevant review risks
6. Use that runtime note for the current task.

## Persistence Rules

1. Do not write newly learned framework guidance back into this skill repository automatically.
2. If the user explicitly asks to improve the skill itself, convert the runtime note into a proper library guide as a separate maintenance task.
3. If the current review benefits from a durable local artifact, write a project-local note under `reviews/_supporting/` inside the target repository rather than editing this skill.

## Guardrails

1. Prefer uncertainty over confident guessing.
2. Keep the note short and review-oriented.
3. Cite the official source when the framework behavior materially affects a finding.
