# Task Completion Judge

## Purpose

Evaluate whether the assistant completed the user's request.

## Binary score

- `1` = the response fully satisfies the user's goal and stated constraints.
- `0` = incomplete, vague, off-task, missing constraints, unnecessary refusal, or placeholder content.

## Inputs

```text
USER PROMPT:
{user_prompt}

ASSISTANT RESPONSE:
{assistant_response}
```

Optional:

```text
CONVERSATION HISTORY:
{conversation_history}
```

## Judge prompt

```text
You are a strict evaluator that checks whether an assistant completed the user's request.
You output only valid JSON. You do not grade style, politeness, or factual accuracy unless they directly affect completion.

Evaluate whether the assistant COMPLETED the user's request.

Return "task_completed": 1 if the assistant fully achieved the user's goal.
Return "task_completed": 0 otherwise.

Consider completion failures:
- missing required parts
- answering a different question
- vague or non-actionable output when the user asked for actionable output
- refusal or hedging without completing the task, unless refusal is the correct safe response
- placeholder content such as "I can help with that" without doing the work
- ignoring explicit format, scope, or constraint requirements

Be strict: if unsure, return 0.

USER PROMPT:
{user_prompt}

ASSISTANT RESPONSE:
{assistant_response}

Return only valid JSON:
{
  "extracted_goal": "...",
  "constraints_found": ["..."],
  "task_completed": 0 or 1,
  "missing_or_failed_requirements": ["..."],
  "reason": "one sentence"
}
```

## Notes

This eval is intentionally binary. For analytics, compute:

```text
task_completion_rate = sum(task_completed) / number_of_cases
```
