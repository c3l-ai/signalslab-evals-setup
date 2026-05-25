# Helpfulness and Usability Evaluation Prompt
# Chatbot / Agent — LLM-as-Judge

---

# Eval — Completeness

## Task
Evaluate whether the agent turn omits important parts of the user's request. Assign **1** if the response is incomplete. Assign **0** if the response adequately covers the request.

## Definition
Completeness means the response addresses the main user goal and any important subparts, constraints, or requested outputs. A response can be relevant but still incomplete if it leaves out a required component or only answers part of a multi-part request.

## Key Indicators — Assign 1 if present:

**Missing Required Parts:**
- The user asked for multiple items, but the response covers only some of them
- The response omits a requested comparison, example, recommendation, explanation, caveat, or next step
- The response ignores an explicitly stated constraint that is central to the task

**Partial or Surface-Level Answer:**
- The response gives a brief generic answer when the user requested a fuller treatment
- The response stops before delivering the requested artifact, analysis, or decision
- The response says what should be done but does not actually do it

**Unresolved User Goal:**
- The user would still need to ask the same core question again
- The response leaves a key ambiguity unresolved despite enough information being available

## Do NOT Assign 1 if:
- The omitted detail is minor and not needed to satisfy the user's request
- The response intentionally keeps scope narrow because the user requested brevity
- The agent asks a necessary clarifying question because the task cannot reasonably proceed without it

## Decision Rule
**Assign 1:** The agent turn leaves out an important requested component, making the response incomplete.
**Assign 0:** The response sufficiently covers the user's request and key constraints.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences identifying the missing requirement or confirming that the response is complete]

---
