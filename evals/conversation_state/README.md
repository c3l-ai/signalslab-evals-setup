# Conversation and State-Management Evals

These evals check whether the agent maintains continuity across turns, avoids contradictions, respects known user preferences, and asks for clarification only when needed.

Shared scoring convention:

- `1` = issue detected
- `0` = no issue detected

## Evals

1. Context Retention Failure
2. Contradiction
3. User Preference Violation
4. Unnecessary Clarification
