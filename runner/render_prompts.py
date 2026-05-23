#!/usr/bin/env python3
"""Render LLM-as-judge prompts from Markdown eval templates and JSONL cases.

This script does not call an LLM. It substitutes variables such as
{{human_turn}}, {{agent_turn}}, {{context}}, {{available_tools}}, and
{{tool_trace}} into an eval prompt and writes rendered prompts as JSONL.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_FIELDS = [
    "human_turn",
    "agent_turn",
    "context",
    "available_tools",
    "tool_trace",
]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
    return rows


def render(template: str, case: dict[str, Any]) -> str:
    rendered = template
    for field in DEFAULT_FIELDS:
        rendered = rendered.replace("{{" + field + "}}", str(case.get(field, "")))
    return rendered


def main() -> None:
    parser = argparse.ArgumentParser(description="Render judge prompts from eval templates and cases.")
    parser.add_argument("--eval", required=True, type=Path, help="Path to eval Markdown template")
    parser.add_argument("--cases", required=True, type=Path, help="Path to JSONL cases")
    parser.add_argument("--out", required=True, type=Path, help="Output JSONL path")
    parser.add_argument("--only-matching-eval", action="store_true", help="Only render cases whose eval slug appears in the eval path")
    args = parser.parse_args()

    template = args.eval.read_text(encoding="utf-8")
    cases = load_jsonl(args.cases)

    if args.only_matching_eval:
        eval_key = args.eval.with_suffix("").as_posix()
        cases = [case for case in cases if str(case.get("eval", "")) in eval_key or eval_key.endswith(str(case.get("eval", "")))]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as f:
        for case in cases:
            rendered_prompt = render(template, case)
            output = {
                "id": case.get("id"),
                "eval": case.get("eval"),
                "expected_score": case.get("expected_score"),
                "prompt": rendered_prompt,
            }
            f.write(json.dumps(output, ensure_ascii=False) + "\n")

    print(f"Rendered {len(cases)} prompt(s) to {args.out}")


if __name__ == "__main__":
    main()
