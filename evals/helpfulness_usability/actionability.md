# Helpfulness and Usability Evaluation Prompt
# Chatbot / Agent — LLM-as-Judge

---

# Eval — Actionability

## Task
Evaluate whether the agent turn is too vague, abstract, or non-operational to help the user act. Assign **1** if the response lacks actionable value. Assign **0** if the response gives usable guidance, output, or next steps.

## Definition
Actionability means the response provides concrete, usable information appropriate to the user's request. A response may be factually correct and relevant but still not actionable if it consists mostly of generalities, platitudes, or high-level advice without practical detail.

## Key Indicators — Assign 1 if present:

**Vague Guidance:**
- Uses broad statements such as "consider your goals" without explaining how
- Gives generic advice that could apply to almost any situation
- Avoids making a needed recommendation or decision when enough information is available

**Missing Operational Detail:**
- Fails to provide steps, examples, criteria, template content, or implementation details when requested
- Describes a concept but not how to use it
- Leaves the user without a clear next action

**Non-Deliverable Response:**
- Says it can help but does not produce the requested artifact
- Provides meta-commentary about the task instead of a usable answer

## Do NOT Assign 1 if:
- The user asked for a conceptual explanation rather than practical steps
- The response appropriately gives a high-level summary because the user requested brevity
- The response includes at least one clear and relevant action, example, or decision path

## Decision Rule
**Assign 1:** The response is too vague or abstract to be practically useful for the user's task.
**Assign 0:** The response provides concrete, usable guidance or output.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences citing the vague or non-actionable content, or confirming the response is usable]

---
