import pytest

def validate_task(payload):
    if not payload.get("title"):
        raise ValueError("title required")
    if payload.get("priority", "normal") not in {"low", "normal", "high"}:
        raise ValueError("invalid priority")
    return True

def test_valid_task():
    assert validate_task({"title": "Release", "priority": "high"})

# Gaps: None payload, whitespace title, invalid status, unexpected fields,
# state transitions and boundary values.
