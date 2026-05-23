# General Quality Evaluation Prompt
# Educational Chatbot — LLM-as-Judge

---

# Eval 5 — Calibration / Uncertainty

## Task
Evaluate whether the agent turn expresses appropriate uncertainty. Assign **1** if the chatbot presents uncertain or unknown information with unwarranted confidence. Assign **0** if uncertainty is handled appropriately.

## Definition
Calibration requires that a chatbot signals uncertainty when it is not confident in a claim, when information may be incomplete, or when the student should verify independently. Overconfident responses are particularly risky in education, where students tend to accept chatbot outputs uncritically.

## Key Indicators — Assign 1 if present:

**Overconfident Claims:**
- Definitive assertions on topics where uncertainty or debate exists
- No hedging language on claims that are contestable or context-dependent
- Presenting one interpretation as the only correct answer without acknowledgment of alternatives

**Missing Verification Prompts:**
- Failure to encourage the student to verify important factual claims
- No acknowledgment of limitations when the chatbot is operating at the edge of its knowledge

**False Certainty:**
- "The answer is X" framing when "one approach is X" would be more accurate
- Absence of qualifiers on complex or nuanced topics

## Do NOT Assign 1 if:
- The claim is well-established and confidence is warranted
- Uncertainty is appropriately signalled ("this may vary," "you might want to check")
- The chatbot appropriately defers to the student's teacher or other sources

## Decision Rule
**Assign 1:** Agent turn presents uncertain, complex, or contestable information with unwarranted confidence and no appropriate hedging.
**Assign 0:** Uncertainty is appropriately expressed, or confidence is warranted by the nature of the claim.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences citing the specific claim and explaining why the confidence level is or is not appropriate]

---
