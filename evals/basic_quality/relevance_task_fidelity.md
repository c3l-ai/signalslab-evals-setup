# General Quality Evaluation Prompt
# Educational Chatbot — LLM-as-Judge

---

# Eval 4 — Relevance / Task Fidelity

## Task
Evaluate whether the agent turn stays on its defined pedagogical task. Assign **1** if the response is off-task or irrelevant. Assign **0** if the response is relevant and on-task.

## Definition
Task fidelity requires that the chatbot responds in ways that are relevant to the student's learning task and consistent with its defined educational role. Responses that drift into unrelated topics, provide unnecessary tangents, or fail to address the student's actual question are considered off-task.

## Key Indicators — Assign 1 if present:

**Off-topic Content:**
- Response addresses a topic unrelated to the student's question or learning task
- Significant tangents that do not serve the educational goal

**Failure to Address the Question:**
- Response does not engage with what the student actually asked
- Vague or generic response that could apply to any question

**Misaligned Pedagogical Focus:**
- Response provides information at the wrong level (too advanced, too basic) without acknowledgment
- Response ignores the specific subject matter context

## Do NOT Assign 1 if:
- Brief contextualisation before addressing the question
- Appropriate clarifying questions before responding
- Response addresses adjacent content that is clearly relevant to the learning goal

## Decision Rule
**Assign 1:** Agent turn is substantially off-task, fails to address the student's question, or drifts from the defined educational purpose.
**Assign 0:** Response is relevant and aligned with the pedagogical task.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences explaining what the student asked and how the response diverged or aligned]

---
