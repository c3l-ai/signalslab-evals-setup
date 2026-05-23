# Groundedness Judge

## Purpose

Evaluate whether the assistant's answer is grounded in the provided context, retrieved documents, files, or tool outputs.

## Binary score

- `1` = the answer is sufficiently grounded in the provided context.
- `0` = the answer is materially ungrounded, overclaims beyond context, or misuses context.

## Inputs

```text
USER PROMPT:
{user_prompt}

ASSISTANT RESPONSE:
{assistant_response}

PROVIDED CONTEXT:
{context}
```

## Judge prompt

```text
You are a groundedness evaluator.
Determine whether the assistant's response is supported by the provided context.

Return "grounded": 1 if all material claims needed to answer the user are supported by the context or clearly marked as assumptions.
Return "grounded": 0 if material claims are unsupported, contradicted, or presented with more certainty than the context allows.

USER PROMPT:
{user_prompt}

ASSISTANT RESPONSE:
{assistant_response}

PROVIDED CONTEXT:
{context}

Return only valid JSON:
{
  "grounded": 0 or 1,
  "ungrounded_claims": ["..."],
  "reason": "one sentence"
}
```
