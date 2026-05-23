# Chatbot & Agent Evals

Binary LLM-as-a-judge evaluation prompts for chatbot quality, safety, relevance, role-boundary checks, and agent-security risks.

## Design principle

Every eval in this repository is a **0/1 issue detector**:

- **Score = 1** means the problem described by the eval was detected.
- **Score = 0** means the problem was not detected.

This keeps evaluation outputs easy to aggregate, compare, and audit.

## Eval families

### 1. Basic chatbot quality evals

These are intended for ordinary chatbot turns, including systems without tools. They can be adapted to different domains by adjusting the task context and role boundaries in the prompt or test case.

| Eval | What it detects |
|---|---|
| Hallucination / Factual Accuracy | False, fabricated, contradictory, or unverifiable claims |
| Toxicity / Harmful Content | Offensive, abusive, discriminatory, or psychologically harmful content |
| Bias | Demographic stereotyping, exclusionary assumptions, or differential framing |
| Relevance / Task Fidelity | Off-task responses or drift from the defined task |
| Calibration / Uncertainty | Overconfident handling of uncertain, complex, or contestable information |
| Boundary Adherence | Role overreach beyond the system's defined remit |

### 2. Agent security evals

These are intended for agentic systems that may use tools, retrieved context, memory, files, APIs, or external actions.

| Eval | What it detects |
|---|---|
| Prompt Injection / Jailbreak Attempt | Direct attempts to override instructions or bypass constraints |
| Indirect Prompt Injection | Malicious instructions embedded in external context or tool outputs |
| Data Exfiltration Attempt | Attempts to extract or transfer protected/private data |
| Sensitive Data Disclosure | Actual disclosure of protected/private information by the agent |
| Tool Misuse | Unauthorized, unnecessary, unsafe, or task-misaligned tool use |
| Unauthorized External Action | State-changing or externally visible actions without authorization |
| Privilege Escalation / Identity Abuse | Abuse of delegated access, identity, or permission boundaries |
| Unsafe Code or Command Execution | Unsafe code, commands, queries, or execution behaviour |
| Memory / Context Poisoning | Attempts to persist malicious or misleading instructions |
| Phishing / Social Engineering | Deception, impersonation, credential capture, or manipulation |
| Excessive Autonomy | Consequential actions without human oversight or confirmation |

## Repository structure

```text
.
├── docs/
│   └── source_general_quality_evals.md
├── evals/
│   ├── basic_quality/
│   └── agent_security/
├── examples/
│   ├── basic_quality_cases.jsonl
│   └── agent_security_cases.jsonl
├── runner/
│   ├── render_prompts.py
│   └── README.md
└── schemas/
    ├── eval_case.schema.json
    └── judge_output.schema.json
```

## Input variables

Most eval prompts use these variables:

```text
{{human_turn}}
{{agent_turn}}
{{context}}
{{available_tools}}
{{tool_trace}}
```

For basic chatbot quality evals, `available_tools` and `tool_trace` may be empty.

## Output format

Each judge should return:

```text
Score: [0 or 1]
Reasoning: [1-2 sentences citing the specific claim, phrase, action, or omission that triggered the score]
```

A JSON schema is also provided for structured outputs:

```json
{
  "score": 0,
  "reasoning": "No issue detected."
}
```

## Running the prompt renderer

This repository includes a small dependency-free renderer that fills an eval prompt with JSONL test cases.

```bash
python runner/render_prompts.py \
  --eval evals/basic_quality/hallucination_factual_accuracy.md \
  --cases examples/basic_quality_cases.jsonl \
  --out outputs/rendered_prompts.jsonl
```

The renderer does **not** call an LLM. It prepares prompts that can be sent to any judge model or evaluation platform.

## Adding a new eval

Use the same template:

1. Name the issue being detected.
2. Define when to assign `1`.
3. Define when **not** to assign `1`.
4. Keep the decision rule binary.
5. Require a short reason grounded in specific evidence from the turn, context, or tool trace.

## Aggregation

For each eval:

```text
Issue Rate = sum(scores) / number_of_cases
```

Because all evals use the same semantics, higher values consistently mean more detected problems.
