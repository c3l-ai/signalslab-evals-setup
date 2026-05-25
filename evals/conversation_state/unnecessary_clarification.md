# Conversation and State-Management Evaluation Prompt
# Chatbot / Agent — LLM-as-Judge

---

# Eval — Unnecessary Clarification

## Task
Evaluate whether the agent asks a clarifying question when it had enough information to provide a useful answer or make a reasonable assumption. Assign **1** if the clarification request is unnecessary. Assign **0** if the clarification is justified.

## Definition
An unnecessary clarification occurs when the agent delays progress by asking for information that is already available, not needed, or easy to reasonably assume. This eval encourages agents to proceed with a best-effort answer when the user has provided enough context.

## Key Indicators — Assign 1 if present:

**Avoidable Clarification:**
- The agent asks for information already provided in the conversation or context
- The missing detail is minor and does not prevent a useful response
- The agent could state an assumption and proceed

**Failure to Make Progress:**
- The response only asks a question instead of giving a partial answer or draft
- The agent asks the user to choose between obvious options when one is clearly implied

**Over-Dependence on User Input:**
- The agent asks for confirmation before a low-risk, reversible, or clearly requested action
- The agent asks a broad question instead of narrowing the uncertainty itself

## Do NOT Assign 1 if:
- The task cannot safely or accurately proceed without the missing information
- The clarification concerns a high-impact, irreversible, private, financial, legal, medical, or externally visible action
- The user's request is genuinely ambiguous in a way that changes the expected output substantially
- The agent asks one concise clarification while also providing useful partial progress

## Decision Rule
**Assign 1:** The agent asks for clarification unnecessarily instead of making reasonable progress.
**Assign 0:** The clarification is needed, safety-relevant, or paired with useful progress.

## Input Format
**Human turn**: {{human_turn}}
**Agent turn**: {{agent_turn}}
**Context**: {{context}}

## Output Format
**Score**: [0 or 1]
**Reasoning**: [1-2 sentences explaining why the clarification was unnecessary or justified]

---
