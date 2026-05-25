# Helpfulness and Usability Evaluation Prompt
# Chatbot / Agent — LLM-as-Judge

---

# Eval — Clarity / Coherence

## Task
Evaluate whether the agent turn is confusing, poorly structured, internally disorganized, or difficult to follow. Assign **1** if clarity or coherence problems are detected. Assign **0** if the response is understandable and logically organized.

## Definition
Clarity and coherence refer to whether the response can be easily understood by the intended user. Problems include unclear wording, confusing structure, unexplained jumps, inconsistent framing, or writing that makes the answer harder to use.

## Key Indicators — Assign 1 if present:

**Confusing Wording:**
- Ambiguous phrasing makes the meaning hard to determine
- Uses unexplained jargon where simpler wording is needed
- Sentences are grammatically or semantically difficult to parse

**Poor Organization:**
- Ideas are presented in a confusing order
- The response lacks signposting when the task requires structure
- Important points are buried or mixed with unrelated material

**Logical Incoherence:**
- The response jumps between ideas without clear links
- The answer contains statements that do not fit together
- The structure obscures the main answer or conclusion

## Do NOT Assign 1 if:
- The response is brief but still understandable
- The topic is inherently complex but the response explains it reasonably
- Minor style issues do not prevent comprehension

## Decision Rule
**Assign 1:** The response has clarity, structure, or coherence problems that materially reduce understandability.
**Assign 0:** The response is clear enough for the user to understand and use.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences identifying the clarity/coherence issue or confirming the response is understandable]

---
