from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class EvalCase:
    id: str
    eval: str
    user_prompt: str
    assistant_response: str = ""
    context: str = ""
    tool_trace: str = ""
    state_changes: str = ""
    expected: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EvalResult:
    eval_name: str
    score: int
    reason: str
    evidence: List[str] = field(default_factory=list)
    categories: List[str] = field(default_factory=list)
    raw: Dict[str, Any] = field(default_factory=dict)
