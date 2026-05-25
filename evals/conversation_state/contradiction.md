# Conversation and State-Management Evaluation Prompt
# Chatbot / Agent — LLM-as-Judge

---

# Eval — Contradiction

## Task
Evaluate whether the agent turn contradicts itself, contradicts the human turn, or contradicts established context from the conversation. Assign **1** if a contradiction is detected. Assign **0** if no material contradiction is detected.

## Definition
A contradiction occurs when the agent asserts two incompatible claims, reverses an earlier established position without explanation, or conflicts with facts provided by the user or context. This eval focuses on internal and conversational consistency, not external factual accuracy.

## Key Indicators — Assign 1 if present:

**Self-Contradiction:**
- The response makes two claims that cannot both be true
- The response gives inconsistent instructions or conclusions

**Contradiction of User/Context:**
- The agent states something that directly conflicts with the human turn or provided context
- The agent reverses an earlier agreed decision or constraint without acknowledging the change

**Unexplained Reversal:**
- The agent changes its recommendation or framing without new evidence or explanation
- The agent says something is both required and optional in the same context

## Do NOT Assign 1 if:
- The agent explicitly acknowledges new information and revises its position
- Differences are minor wording shifts rather than substantive contradictions
- The apparent conflict is resolved by context or qualification

## Decision Rule
**Assign 1:** The response contains a material contradiction within itself or relative to the established conversation/context.
**Assign 0:** No material contradiction is present.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences identifying the contradiction or confirming consistency]

---
