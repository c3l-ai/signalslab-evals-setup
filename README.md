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

These evals are based on the idea that a chatbot response can fail even when it is fluent and superficially helpful. The basic quality family therefore focuses on core response risks: factual reliability, harm, fairness, task alignment, uncertainty handling, and role boundaries. These are intentionally broad checks that can be used for ordinary chatbot turns before considering more specialized agentic behaviour such as tools or memory.

The evals draw on several related ideas:

- **Factual reliability and faithfulness:** generated responses can contain fluent but unsupported or false content. Hallucination / Factual Accuracy detects fabricated, contradictory, or unverifiable claims relative to the user turn, available context, or established knowledge.
- **Safe and non-harmful language:** chatbots can generate content that is toxic, abusive, discriminatory, or psychologically harmful. Toxicity / Harmful Content detects language or advice that could harm, demean, threaten, or distress users.
- **Fairness and representational harms:** generated language can reproduce stereotypes, exclusionary assumptions, or differential treatment of demographic groups. Bias detects these demographic or social-assumption failures.
- **Task alignment:** useful responses should remain relevant to the user's actual request and the chatbot's defined task. Relevance / Task Fidelity detects off-topic drift, generic non-answers, or misalignment with the requested task.
- **Calibration and uncertainty:** systems should avoid presenting uncertain, context-dependent, or contested claims with unwarranted confidence. Calibration / Uncertainty detects overconfident or falsely certain responses.
- **Role and scope boundaries:** a chatbot should not assume roles outside its intended remit, such as therapist, legal advisor, medical advisor, or general delegated decision-maker, unless explicitly designed and governed for that role. Boundary Adherence detects role overreach.

### 2. Helpfulness and usability evals

These are general response-quality checks. They are not domain-specific and are intended to detect whether a response is useful, understandable, appropriately scoped, and practically helpful.

| Eval | What it detects |
|---|---|
| Completeness | Missing important parts of the user's request |
| Actionability | Vague, abstract, or non-operational guidance |
| Clarity / Coherence | Confusing wording, poor structure, or unclear reasoning flow |
| Conciseness | Unnecessary verbosity, repetition, or scope creep |


These evals are based on the idea that usefulness is not only about factual correctness. A response may be safe and accurate but still fail if it omits necessary information, is too abstract to apply, is difficult to understand, or is unnecessarily long. The helpfulness and usability family therefore focuses on whether the response helps the user achieve their goal with an appropriate level of detail, practical next steps, clear structure, and minimal unnecessary burden.

The evals draw on several related ideas:

- **Usability as goal achievement:** usability is commonly framed around whether specified users can achieve specified goals effectively, efficiently, and satisfactorily in a given context. Completeness and actionability help detect failures of effectiveness, while conciseness and clarity help detect avoidable inefficiency.
- **Cooperative communication:** conversational contributions should be appropriately informative, relevant, clear, orderly, and not more verbose than needed. This supports the completeness, clarity/coherence, and conciseness evals.
- **Plain-language and scannable communication:** usable responses should be easy to scan, written in plain language, and organized around the user's likely next action. This supports the clarity/coherence and actionability evals.
- **Heuristic evaluation:** usability inspection methods often identify barriers that make systems harder to use. These evals apply the same idea to generated responses: they detect response-level barriers such as missing information, vague guidance, confusing structure, or avoidable verbosity.

### 3. Conversation and state-management evals

These are intended for multi-turn interactions where the agent needs to remember prior context, respect known preferences, and maintain continuity.

| Eval | What it detects |
|---|---|
| Context Retention Failure | Failure to use relevant prior conversation or provided context |
| Contradiction | Internal contradiction or conflict with established conversation/context |
| User Preference Violation | Ignoring known user preferences, constraints, or prior instructions |
| Unnecessary Clarification | Asking for clarification when enough information was available to proceed |

### 4. Agent security evals

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

These evals are based on the idea that agentic systems expand the risk surface beyond ordinary chatbot response quality. Once a system can use tools, read external content, access files, maintain memory, or take externally visible actions, failures can involve not only bad answers but also unauthorized actions, data exposure, poisoned state, or misuse of delegated permissions.

The evals draw on several related ideas:

- **Instruction hierarchy and prompt injection:** agents may encounter instructions from users, tools, webpages, emails, files, or retrieved documents. Prompt Injection / Jailbreak Attempt and Indirect Prompt Injection detect attempts to make untrusted content override higher-priority instructions or the user's actual goal.
- **Data boundary protection:** agents may have access to private context, files, credentials, account data, or internal prompts. Data Exfiltration Attempt detects attempts to extract protected information, while Sensitive Data Disclosure detects whether the agent actually revealed it.
- **Tool and action governance:** tool-using agents can perform searches, read files, send messages, modify records, or execute code. Tool Misuse, Unauthorized External Action, Unsafe Code or Command Execution, and Excessive Autonomy detect cases where tools or actions are unsafe, unnecessary, unauthorized, or insufficiently supervised.
- **Permission and identity boundaries:** agents often operate with delegated user permissions. Privilege Escalation / Identity Abuse detects attempts to exploit the agent's access, impersonate others, or bypass permissions.
- **Persistent state integrity:** agents with memory or long-running context can be manipulated through stored instructions or poisoned state. Memory / Context Poisoning detects attempts to persist malicious or misleading instructions.
- **Social-engineering risk:** agents can generate or amplify deceptive communication. Phishing / Social Engineering detects impersonation, credential capture, fraud, or manipulative communication.

## Repository structure

```text
.
├── docs/
│   └── source_general_quality_evals.md
├── evals/
│   ├── basic_quality/
│   ├── helpfulness_usability/
│   ├── conversation_state/
│   └── agent_security/
├── examples/
│   ├── basic_quality_cases.jsonl
│   ├── helpfulness_usability_cases.jsonl
│   ├── conversation_state_cases.jsonl
│   └── agent_security_cases.jsonl
├── runner/
│   ├── render_prompts.py
│   └── README.md
└── schemas/
    ├── eval_case.schema.json
    └── judge_output.schema.json
```

## Input variables

Most eval prompts use some or all of the following variables. For ordinary chatbot turns, only `human_turn`, `agent_turn`, and sometimes `context` are needed. For agentic systems, `available_tools` and `tool_trace` help the judge evaluate tool use and security behaviour.

| Variable | Meaning | Typical use | Example |
|---|---|---|---|
| `{{human_turn}}` | The user's message for the turn being evaluated. | Used by all evals to understand what the user asked for, what constraints were given, and whether the response was relevant. | `Can you summarize this article in three bullet points?` |
| `{{agent_turn}}` | The chatbot or agent response being evaluated. | Used by all evals as the primary object of judgment. | `Here are three key points: ...` |
| `{{context}}` | Any additional information available to the agent or judge, such as retrieved passages, uploaded-document excerpts, prior conversation, system role description, task instructions, or reference material. | Used for hallucination, groundedness, relevance, calibration, boundary adherence, and indirect prompt-injection checks. Leave empty if no extra context was provided. | `Retrieved passage: The report states that enrolments increased by 12% in 2024.` |
| `{{available_tools}}` | The tools the agent was allowed to use in this turn, including each tool's name and purpose. | Used for agent and security evals to determine whether tool use was available, necessary, appropriate, or risky. Leave empty for non-tool chatbot evals. | `search_web: Search the public web; read_file: Read uploaded files; send_email: Send email from the user's account.` |
| `{{tool_trace}}` | The tools the agent actually called, including inputs, outputs, and any externally visible or state-changing actions. | Used for tool misuse, unauthorized action, data disclosure, excessive autonomy, and other security evals. Leave empty if no tools were called. | `Tool call: send_email(to=external@example.com, subject=Notes); Result: email sent.` |

### Notes

- `context` can include trusted material, untrusted material, or both. For security evals, clearly label untrusted content such as webpages, emails, retrieved documents, or tool outputs.
- `available_tools` describes what the agent *could* have used.
- `tool_trace` describes what the agent *actually* used.
- If a variable is not relevant to a case, set it to an empty string, `None`, or another explicit placeholder supported by your runner.
- Do not include private or sensitive data in eval cases unless the eval is explicitly designed to test handling of that data.

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


## References and background resources

These resources informed the terminology and structure used in the eval set. They are background references only; the eval prompts are intentionally kept self-contained so they can be adapted to different chatbot and agent contexts.

### LLM-as-a-judge and evaluation design

- Zheng et al. (2023), **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena**: foundational work on using LLMs as evaluators, including known issues such as position bias, verbosity bias, self-preference bias, and the need for calibration.  
  https://arxiv.org/abs/2306.05685
- DeepEval documentation: examples of LLM-as-a-judge metrics such as hallucination, answer relevancy, task completion, and faithfulness-style checks.  
  https://deepeval.com/docs/metrics-hallucination
- Ragas documentation: RAG-oriented evaluation concepts such as faithfulness, answer relevancy, context precision, and context recall.  
  https://docs.ragas.io/en/v0.1.21/concepts/metrics/

### Basic chatbot quality, safety, and reliability

- Ji et al. (2023), **Survey of Hallucination in Natural Language Generation**: surveys hallucination in NLG and LLM settings, motivating checks for fabricated, contradictory, or unsupported content.
  https://dl.acm.org/doi/10.1145/3571730
- Maynez et al. (2020), **On Faithfulness and Factuality in Abstractive Summarization**: shows that generated summaries can be fluent while unfaithful to source content, supporting factuality and faithfulness-style evals.
  https://aclanthology.org/2020.acl-main.173/
- Gehman et al. (2020), **RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models**: introduces a benchmark for evaluating toxic language generation, motivating toxicity and harmful-content checks.
  https://aclanthology.org/2020.findings-emnlp.301/
- Blodgett et al. (2020), **Language (Technology) is Power: A Critical Survey of “Bias” in NLP**: argues that bias evaluation requires explicit attention to social harms, affected groups, and normative assumptions.
  https://aclanthology.org/2020.acl-main.485/
- Sheng et al. (2019), **The Woman Worked as a Babysitter: On Biases in Language Generation**: studies demographic bias in generated text, supporting evals for stereotypes, differential framing, and representational harms.
  https://aclanthology.org/D19-1339/
- Guo et al. (2017), **On Calibration of Modern Neural Networks**: defines confidence calibration as whether confidence estimates correspond to correctness likelihood, motivating uncertainty and overconfidence checks.
  https://proceedings.mlr.press/v70/guo17a.html
- Amershi et al. (2019), **Guidelines for Human-AI Interaction**: provides design guidance for human-AI systems, including setting expectations, communicating uncertainty, and supporting appropriate reliance.
  https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/
- Weidinger et al. (2022), **Taxonomy of Risks posed by Language Models**: classifies harms from language models, including discrimination, information hazards, misinformation, malicious uses, and human-computer interaction harms.
  https://dl.acm.org/doi/10.1145/3531146.3533088

### Helpfulness, usability, and response design

- ISO 9241-11:2018, **Ergonomics of human-system interaction — Part 11: Usability**: defines usability in terms of users achieving specified goals with effectiveness, efficiency, and satisfaction in a specified context of use. This motivates treating completeness, actionability, clarity, and conciseness as usability-related response qualities.
  https://www.iso.org/obp/ui
- Grice (1975), **Logic and Conversation**: introduces the Cooperative Principle and conversational maxims of quantity, quality, relation, and manner. These motivate response-level expectations such as being sufficiently informative, relevant, clear, orderly, and not unnecessarily verbose.
  https://web.stanford.edu/class/psych205/papers/Grice-1975.pdf
- Nielsen Norman Group, **Concise, Scannable, and Objective: How to Write for the Web**: reports that concise, scannable, and objective writing improves measured usability, supporting the conciseness and clarity/coherence evals.
  https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/
- Nielsen Norman Group, **Writing for the Web**: practical guidance on concise, scannable, plain-language communication for digital interfaces, relevant to response clarity, actionability, and usability.
  https://www.nngroup.com/topic/writing-web/
- Nielsen Norman Group, **10 Usability Heuristics for User Interface Design**: general heuristic-evaluation principles for identifying usability problems. While designed for interfaces, the same inspection logic can be adapted to generated responses by detecting barriers that prevent users from understanding or acting on an answer.
  https://www.nngroup.com/articles/ten-usability-heuristics/

### Conversation state, dialogue management, and personalization

- Clark & Brennan (1991), **Grounding in Communication**: introduces grounding and common ground as the process through which participants establish shared understanding during interaction.
  https://web.stanford.edu/~clark/1990s/Clark%2C%20H.H.%20_%20Brennan%2C%20S.E.%20_Grounding%20in%20communication_%201991.pdf
- Grice (1975), **Logic and Conversation**: introduces the Cooperative Principle and conversational maxims, which motivate coherence, relevance, appropriate informativeness, and avoiding unnecessary conversational burden.
  https://web.stanford.edu/class/psych205/papers/Grice-1975.pdf
- Jacqmin, Rojas-Barahona & Favre (2022), **Do you follow me? A Survey of Recent Approaches in Dialogue State Tracking**: surveys dialogue state tracking as the process of maintaining user needs and dialogue state across turns in task-oriented systems.
  https://arxiv.org/abs/2207.14627
- OpenAI Cookbook, **Context Engineering for Personalization**: practical guidance on managing session context, fixed attributes, inferred attributes, and user preferences for personalized agents.
  https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization
- OpenAI Agents SDK, **Agent memory**: describes memory summaries, progressive disclosure, and using stored preferences or prior work to support continuity across agent interactions.
  https://openai.github.io/openai-agents-js/guides/sandbox-agents/memory/

### Agent security and prompt-injection risks

- OWASP, **AI Agent Security Cheat Sheet**: agent-specific risks including prompt injection, tool abuse, memory poisoning, goal hijacking, excessive autonomy, and high-impact action abuse.  
  https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- OWASP, **Top 10 for Large Language Model Applications 2025**: application-level LLM risks, including prompt injection and sensitive information disclosure.  
  https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OWASP, **LLM01: Prompt Injection**: direct and indirect prompt-injection patterns and consequences such as unauthorized function access, sensitive information disclosure, and output manipulation.  
  https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- OpenAI, **Understanding prompt injections**: explains prompt injection as a social-engineering attack against AI systems, especially when third-party content enters the conversation context.  
  https://openai.com/safety/prompt-injections/
- MITRE ATLAS: knowledge base of adversary tactics and techniques for AI-enabled systems.  
  https://atlas.mitre.org/

### AI risk-management context

- NIST, **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile**: broader risk-management framing for generative AI systems.  
  https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

## Aggregation

For each eval:

```text
Issue Rate = sum(scores) / number_of_cases
```

Because all evals use the same semantics, higher values consistently mean more detected problems.
