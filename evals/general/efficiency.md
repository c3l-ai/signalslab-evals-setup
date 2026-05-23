# Efficiency Eval

## Purpose

Evaluate whether the agent used resources appropriately.

## Binary score

- `1` = efficient enough for the task.
- `0` = inefficient because of unnecessary verbosity, unnecessary tool calls, avoidable latency, or excessive token/cost use.

## Recommended implementation

Use computed metrics first:

- latency
- prompt tokens
- completion tokens
- total cost
- number of tool calls

Then use an LLM judge only for qualitative efficiency: unnecessary rambling, redundant reasoning, or avoidable tool use.

## Inputs

```text
USER PROMPT:
{user_prompt}

ASSISTANT RESPONSE:
{assistant_response}

TOOL TRACE:
{tool_trace}

METRICS:
latency_ms={latency_ms}
prompt_tokens={prompt_tokens}
completion_tokens={completion_tokens}
total_cost={total_cost}
```

## Judge prompt

```text
You are an evaluator of agent efficiency.
Determine whether the assistant used a reasonable amount of text, tools, and effort for the user's request.

Return "efficient": 1 if the response and tool behavior are reasonably efficient.
Return "efficient": 0 if there is clear unnecessary verbosity, unnecessary tool use, repeated work, or disproportionate cost/latency for the task.

Do not penalize necessary tool use or necessary detail for complex tasks.

USER PROMPT:
{user_prompt}

ASSISTANT RESPONSE:
{assistant_response}

TOOL TRACE:
{tool_trace}

METRICS:
{metrics}

Return only valid JSON:
{
  "efficient": 0 or 1,
  "inefficiencies": ["..."],
  "reason": "one sentence"
}
```
