#!/usr/bin/env python3
"""Validate the Automated Test Reviewer skill package."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEXT_SUFFIXES = {".md", ".j2", ".yaml", ".json", ".py"}
REQUIRED_FILES = [
    Path("SKILL.md"),
    Path("README.md"),
    Path("CHANGELOG.md"),
    Path("agents/openai.yaml"),
    Path("references/report-contracts.md"),
    Path("references/workflows/script-explanation.md"),
    Path("references/workflows/functional-case-mapping.md"),
    Path("references/workflows/script-quality-review.md"),
    Path("references/workflows/framework-onboarding.md"),
    Path("scripts/validate_skill.py"),
    Path("evals/smoke-prompts.json"),
]
FRAMEWORK_GUIDES = [
    Path("references/libraries/cypress/knowledge.md"),
    Path("references/libraries/junit5/knowledge.md"),
    Path("references/libraries/pact/knowledge.md"),
    Path("references/libraries/playwright/knowledge.md"),
    Path("references/libraries/postman/knowledge.md"),
    Path("references/libraries/restassured/knowledge.md"),
    Path("references/libraries/selenium/knowledge.md"),
]
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate skill metadata, linked files, text safety, and eval fixtures."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of plain text.",
    )
    return parser.parse_args()


def collect_frontmatter(skill_path: Path) -> tuple[dict[str, object], list[str]]:
    errors: list[str] = []
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, ["SKILL.md must start with YAML frontmatter delimited by ---"]
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}, ["SKILL.md frontmatter block is incomplete"]
    raw = parts[1].strip().splitlines()
    data: dict[str, object] = {}
    current_block: str | None = None
    for line in raw:
        if line.startswith("  "):
            if current_block is None:
                errors.append(f"Unexpected nested frontmatter line: {line!r}")
                continue
            stripped = line.strip()
            if ":" not in stripped:
                errors.append(f"Invalid nested frontmatter line: {line!r}")
                continue
            key, value = stripped.split(":", 1)
            nested = data.setdefault(current_block, {})
            if not isinstance(nested, dict):
                errors.append(f"Frontmatter block {current_block!r} must be a mapping")
                continue
            nested[key.strip()] = value.strip()
            continue
        if ":" not in line:
            errors.append(f"Invalid frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        normalized_key = key.strip()
        normalized_value = value.strip()
        if normalized_value:
            data[normalized_key] = normalized_value
            current_block = None
        else:
            data[normalized_key] = {}
            current_block = normalized_key
    allowed_keys = {"name", "description", "metadata"}
    extra = sorted(set(data) - allowed_keys)
    missing = sorted(allowed_keys - set(data))
    if "metadata" in missing:
        missing.remove("metadata")
    if missing:
        errors.append(f"Missing frontmatter keys: {', '.join(missing)}")
    if extra:
        errors.append(f"Unexpected frontmatter keys: {', '.join(extra)}")
    metadata = data.get("metadata")
    if metadata is not None:
        if not isinstance(metadata, dict):
            errors.append("metadata must be a mapping")
        else:
            allowed_metadata_keys = {"author", "version"}
            metadata_extra = sorted(set(metadata) - allowed_metadata_keys)
            metadata_missing = sorted(allowed_metadata_keys - set(metadata))
            if metadata_missing:
                errors.append(
                    f"metadata is missing keys: {', '.join(metadata_missing)}"
                )
            if metadata_extra:
                errors.append(
                    f"metadata has unexpected keys: {', '.join(metadata_extra)}"
                )
    return data, errors


def is_ascii_clean(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    return all(ord(ch) < 128 for ch in text)


def validate_markdown_links(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for raw_link in MARKDOWN_LINK_RE.findall(text):
        if raw_link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = raw_link.split("#", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            rel = path.relative_to(ROOT)
            errors.append(f"Broken local link in {rel}: {raw_link}")
    return errors


def validate_openai_yaml(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    required_snippets = [
        "interface:",
        "display_name:",
        "short_description:",
        "default_prompt:",
    ]
    for snippet in required_snippets:
        if snippet not in text:
            errors.append(f"agents/openai.yaml is missing {snippet}")
    return errors


def validate_eval_fixture(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"Invalid JSON in {path.relative_to(ROOT)}: {exc}"]
    if not isinstance(payload, list) or not payload:
        return ["evals/smoke-prompts.json must contain a non-empty JSON array"]
    required_keys = {"id", "prompt", "expected_workflow", "expected_artifacts"}
    for index, item in enumerate(payload):
        if not isinstance(item, dict):
            errors.append(f"Eval item {index} must be an object")
            continue
        missing = sorted(required_keys - set(item))
        if missing:
            errors.append(
                f"Eval item {index} is missing keys: {', '.join(missing)}"
            )
        artifacts = item.get("expected_artifacts")
        if artifacts is not None and not isinstance(artifacts, list):
            errors.append(f"Eval item {index} expected_artifacts must be a list")
    return errors


def main() -> int:
    args = parse_args()
    errors: list[str] = []

    for relative in REQUIRED_FILES + FRAMEWORK_GUIDES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required file: {relative.as_posix()}")

    skill_data, frontmatter_errors = collect_frontmatter(ROOT / "SKILL.md")
    errors.extend(frontmatter_errors)

    if skill_data.get("name") != "automated-test-reviewer":
        errors.append("SKILL.md frontmatter name must be automated-test-reviewer")

    errors.extend(validate_openai_yaml(ROOT / "agents/openai.yaml"))
    errors.extend(validate_eval_fixture(ROOT / "evals/smoke-prompts.json"))

    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        if not is_ascii_clean(path):
            errors.append(f"Non-ASCII text detected in {path.relative_to(ROOT)}")
        if path.suffix == ".md":
            errors.extend(validate_markdown_links(path))

    if args.json:
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2))
    else:
        if errors:
            print("Validation failed:")
            for error in errors:
                print(f"- {error}")
        else:
            print("Validation passed.")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
