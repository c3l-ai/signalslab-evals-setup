# Conversation and State-Management Evaluation Prompt
# Chatbot / Agent — LLM-as-Judge

---

# Eval — Context Retention Failure

## Task
Evaluate whether the agent turn fails to use relevant information already available in the conversation or provided context. Assign **1** if a context-retention failure is detected. Assign **0** if the agent appropriately uses the relevant prior context.

## Definition
Context retention means maintaining continuity with previous turns, known constraints, user-provided details, and current-session context. A failure occurs when the agent forgets, ignores, or asks again for information that is already available and relevant.

## Key Indicators — Assign 1 if present:

**Forgetting Provided Information:**
- Asks the user to provide information that is already in the conversation or context
- Gives an answer that ignores a relevant prior constraint, preference, or decision
- Treats an established fact as unknown without reason

**Loss of Continuity:**
- Fails to connect the current answer to the previous turn when the user clearly refers back to it
- Repeats earlier exploration instead of building on the established direction
- Misidentifies what "this," "that," "those," or similar references refer to when context makes it clear

## Do NOT Assign 1 if:
- The prior context is genuinely ambiguous or insufficient
- The agent asks a necessary clarification because multiple interpretations remain plausible
- The ignored context is irrelevant to the current turn

## Decision Rule
**Assign 1:** The agent fails to use relevant prior context that was available and should have shaped the response.
**Assign 0:** The agent maintains appropriate continuity with the conversation or context.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences citing the prior context that was ignored or confirming continuity]

---
