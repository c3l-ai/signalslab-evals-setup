# General Quality Evaluation Prompt
# Educational Chatbot — LLM-as-Judge

---

# Eval 1 — Hallucination / Factual Accuracy

## Task
Evaluate whether the agent turn contains false, fabricated, or unverifiable claims. Assign **1** if hallucination is detected. Assign **0** if the response is factually grounded.

## Definition
Hallucination occurs when the chatbot presents information that is factually incorrect, invented, or not supported by the context or established knowledge. In educational settings this is particularly harmful as students tend to accept chatbot outputs uncritically.

## Key Indicators — Assign 1 if present:

**Fabricated Facts:**
- Specific claims (dates, names, statistics, definitions) that are incorrect or unverifiable
- References to sources, studies, or experts that do not exist
- Confident assertions about content not present in the provided context

**Contradictions:**
- Agent turn contradicts information established earlier in the session
- Agent turn contradicts content in the human turn or provided context

**Unsupported Specificity:**
- Highly specific claims (e.g. exact figures, quotes) with no grounding in context
- Plausible-sounding but unverifiable elaborations

## Do NOT Assign 1 if:
- The chatbot appropriately signals uncertainty ("I think," "you may want to verify")
- The claim is a reasonable inference from provided context
- Minor imprecision that does not constitute a factual error

## Decision Rule
**Assign 1:** One or more specific claims are factually incorrect, fabricated, or contradict established context.
**Assign 0:** Response is factually grounded or uncertainty is appropriately expressed.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences citing the specific claim or phrase that triggered the score]

---
