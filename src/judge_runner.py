"""Minimal scaffold for running binary LLM-as-a-judge evals.

This file intentionally avoids binding to a specific LLM provider.
Replace `call_judge_model` with your preferred API client.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, Dict, Iterable, List

from models import EvalCase, EvalResult


ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evals"


def load_jsonl(path: str | Path) -> Iterable[EvalCase]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield EvalCase(**json.loads(line))


def load_eval_prompt(eval_name: str) -> str:
    matches = list(EVAL_DIR.glob(f"**/{eval_name}.md"))
    if not matches:
        raise FileNotFoundError(f"No eval prompt found for {eval_name}")
    return matches[0].read_text(encoding="utf-8")


def render_prompt(template: str, case: EvalCase) -> str:
    return template.format(
        user_prompt=case.user_prompt,
        assistant_response=case.assistant_response,
        context=case.context,
        tool_trace=case.tool_trace,
        state_changes=case.state_changes,
        tools=case.metadata.get("tools", ""),
        reference_evidence=case.metadata.get("reference_evidence", ""),
        metrics=case.metadata.get("metrics", ""),
    )


def run_cases(
    cases: Iterable[EvalCase],
    call_judge_model: Callable[[str], Dict],
) -> List[EvalResult]:
    results: List[EvalResult] = []
    for case in cases:
        eval_prompt = load_eval_prompt(case.eval)
        rendered = render_prompt(eval_prompt, case)
        raw = call_judge_model(rendered)

        # Normalise common binary field names into `score`.
        score = raw.get("score")
        if score is None:
            for key, value in raw.items():
                if isinstance(value, int) and value in (0, 1):
                    score = value
                    break
        if score not in (0, 1):
            raise ValueError(f"Judge did not return binary score for case {case.id}: {raw}")

        results.append(
            EvalResult(
                eval_name=case.eval,
                score=score,
                reason=raw.get("reason", ""),
                evidence=raw.get("evidence", []),
                categories=raw.get("categories", raw.get("attack_categories", [])),
                raw=raw,
            )
        )
    return results


def call_judge_model(prompt: str) -> Dict:
    """Placeholder.

    Replace with a real LLM call. The model should return parsed JSON.
    """
    raise NotImplementedError("Connect this to your LLM provider of choice.")


if __name__ == "__main__":
    print("This is a scaffold. Import run_cases and provide call_judge_model.")
