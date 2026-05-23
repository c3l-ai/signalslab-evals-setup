# Accuracy / Correctness Judge

## Purpose

Evaluate whether the assistant's factual or task-specific claims are correct against a reference answer, trusted evidence, or tool outputs.

## Binary score

- `1` = no material correctness errors found against the provided reference/evidence.
- `0` = at least one material factual, mathematical, logical, or task-specific error is present.

## Important constraint

This eval requires evidence. Without a gold answer, trusted source, tool output, or reference data, the judge should not guess correctness. In those cases, use the unsupported-claims eval instead.

## Inputs

```text
USER PROMPT:
{user_prompt}

ASSISTANT RESPONSE:
{assistant_response}

REFERENCE OR TRUSTED EVIDENCE:
{reference_evidence}
```

## Judge prompt

```text
You are a strict correctness evaluator.
Determine whether the assistant response is materially correct using only the provided reference or trusted evidence.

Return "correct": 1 if the assistant contains no material correctness errors.
Return "correct": 0 if it contains one or more material errors.

Do not use outside knowledge. If the evidence is insufficient to verify a claim, mark that claim as unverifiable rather than incorrect.
Only mark incorrect when the response contradicts or misrepresents the provided evidence.

USER PROMPT:
{user_prompt}

ASSISTANT RESPONSE:
{assistant_response}

REFERENCE OR TRUSTED EVIDENCE:
{reference_evidence}

Return only valid JSON:
{
  "correct": 0 or 1,
  "material_errors": ["..."],
  "unverifiable_claims": ["..."],
  "reason": "one sentence"
}
```
