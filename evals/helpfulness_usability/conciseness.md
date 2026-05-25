# Helpfulness and Usability Evaluation Prompt
# Chatbot / Agent — LLM-as-Judge

---

# Eval — Conciseness

## Task
Evaluate whether the agent turn is unnecessarily verbose, repetitive, or bloated relative to the user's request. Assign **1** if conciseness problems are detected. Assign **0** if the response is appropriately concise.

## Definition
Conciseness means the response gives enough information to satisfy the request without unnecessary repetition, excessive background, irrelevant detail, or over-explanation. This eval does not penalize longer responses when the task genuinely requires detail.

## Key Indicators — Assign 1 if present:

**Unnecessary Length:**
- Provides extensive background when the user asked for a brief answer
- Includes multiple sections that do not help answer the request
- Over-explains obvious points or repeats the same idea several times

**Repetition:**
- Restates the same recommendation, caveat, or explanation without adding value
- Uses filler phrases or redundant summaries

**Poor Scope Control:**
- Adds tangential information not requested and not useful
- Expands into adjacent topics that distract from the user's goal

## Do NOT Assign 1 if:
- The user asked for a detailed explanation, plan, or analysis
- The response is long because the task has multiple parts
- The additional detail materially improves usefulness or safety

## Decision Rule
**Assign 1:** The response is longer, more repetitive, or more bloated than the task requires.
**Assign 0:** The response is appropriately concise for the user's request.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences explaining the verbosity/repetition issue or confirming appropriate conciseness]

---
