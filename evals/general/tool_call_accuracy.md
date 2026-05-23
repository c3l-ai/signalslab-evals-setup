# Tool Call Accuracy Judge

## Purpose

Evaluate whether the agent selected and used tools correctly.

## Binary score

- `1` = correct tool choice, correct parameters, and correct use of tool results.
- `0` = wrong tool, missed required tool, incorrect parameters, unsafe tool call, or misused tool output.

## Inputs

```text
USER PROMPT:
{user_prompt}

AVAILABLE TOOLS:
{available_tools}

TOOL TRACE:
{tool_trace}

ASSISTANT RESPONSE:
{assistant_response}
```

## Judge prompt

```text
You are an evaluator of tool-use accuracy for an AI agent.

Return "tool_use_correct": 1 if the assistant selected appropriate tools when needed, used correct parameters, and integrated tool results correctly.
Return "tool_use_correct": 0 if it missed a required tool, used an inappropriate tool, used incorrect parameters, made unnecessary risky calls, or misrepresented tool outputs.

USER PROMPT:
{user_prompt}

AVAILABLE TOOLS:
{available_tools}

TOOL TRACE:
{tool_trace}

ASSISTANT RESPONSE:
{assistant_response}

Return only valid JSON:
{
  "tool_use_correct": 0 or 1,
  "tool_failures": ["..."],
  "reason": "one sentence"
}
```
