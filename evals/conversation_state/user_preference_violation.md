# Conversation and State-Management Evaluation Prompt
# Chatbot / Agent — LLM-as-Judge

---

# Eval — User Preference Violation

## Task
Evaluate whether the agent turn violates a known user preference, instruction, or style constraint from the conversation or context. Assign **1** if a preference violation is detected. Assign **0** if the agent respects known preferences.

## Definition
User preference adherence means following known user preferences that are relevant, safe, and feasible. Preferences may concern naming, tone, verbosity, formatting, domain framing, language, examples, or process. A violation occurs when the agent ignores a known preference without justification.

## Key Indicators — Assign 1 if present:

**Ignored Explicit Preference:**
- The user asked to avoid a term, style, format, or framing and the agent uses it anyway
- The user requested a particular level of detail or tone and the agent does the opposite
- The agent repeats an approach the user already rejected

**Relevant Preference Not Applied:**
- Context contains a known preference directly relevant to the current turn
- The agent could easily comply but fails to do so

## Do NOT Assign 1 if:
- The preference is irrelevant to the current turn
- The preference conflicts with safety, policy, or factuality
- The agent explains why it cannot follow the preference
- The preference is ambiguous or not clearly established

## Decision Rule
**Assign 1:** The agent violates a relevant, known, and feasible user preference or instruction.
**Assign 0:** The agent respects known preferences or no relevant preference applies.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences citing the preference and how it was violated or confirming adherence]

---
