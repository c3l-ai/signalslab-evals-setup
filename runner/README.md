# Runner

This folder contains a small dependency-free prompt renderer.

It prepares LLM-as-judge prompts from Markdown eval templates and JSONL cases.
It does **not** call an LLM, so it can be used with any evaluation platform or judge model.

## Example

```bash
python runner/render_prompts.py   --eval evals/basic_quality/hallucination_factual_accuracy.md   --cases examples/basic_quality_cases.jsonl   --out outputs/rendered_prompts.jsonl
```

Render only cases that match the eval file:

```bash
python runner/render_prompts.py   --eval evals/agent_security/tool_misuse.md   --cases examples/agent_security_cases.jsonl   --out outputs/tool_misuse_prompts.jsonl   --only-matching-eval
```

Each output row includes:

```json
{
  "id": "case-id",
  "eval": "eval-slug",
  "expected_score": 0,
  "prompt": "rendered judge prompt"
}
```
