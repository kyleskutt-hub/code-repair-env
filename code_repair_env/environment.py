"""Code Repair Environment for Prime Intellect verifiers."""

from __future__ import annotations
import random
from typing import Any
import verifiers as vf
from datasets import Dataset
from .bugs import BUG_TEMPLATES

def _make_dataset(num_examples: int = 100, seed: int = 42) -> Dataset:
    random.seed(seed)
    rows = []
    for _ in range(num_examples):
        bug = random.choice(BUG_TEMPLATES)
        prompt = (
            "Fix the bug in this Python function.\n"
            "Return ONLY the corrected code (no markdown, no explanation).\n\n"
            f"Buggy code:\n{bug['buggy']}\n\n"
            f"Test that should pass:\n{bug['test']}\n"
        )
        rows.append({
            "prompt": prompt,
            "answer": bug["fixed"],
            "info": {"test": bug["test"], "bug_type": bug["bug_type"]},
        })
    return Dataset.from_list(rows)

def _extract_text(completion) -> str:
    if isinstance(completion, str):
        return completion.strip()
    if completion and isinstance(completion, list):
        return (completion[-1].get("content") or "").strip()
    return ""

def _strip_code_fences(text: str) -> str:
    t = text.strip()
    if "`" not in t:
        return t
    parts = t.split("`")
    if len(parts) >= 3:
        return parts[1].replace("python", "", 1).strip()
    return t.replace("`", "").strip()

def score_code_fix(completion, answer: str = "", info: dict = None, **_: Any) -> float:
    info = info or {}
    test_code = info.get("test", "")
    code = _strip_code_fences(_extract_text(completion))
    full_code = f"{code}\n{test_code}\n"
    try:
        exec(full_code, {"__builtins__": __builtins__}, {})
        return 1.0
    except Exception:
        return 0.0

def load_environment(num_examples: int = 100, seed: int = 42, **kwargs):
    dataset = _make_dataset(num_examples=num_examples, seed=seed)
    rubric = vf.Rubric(funcs=[score_code_fix], weights=[1.0])
    return vf.SingleTurnEnv(
        dataset=dataset,
        system_prompt="You are a precise code repair assistant.",
        rubric=rubric,
        **kwargs,
    )
