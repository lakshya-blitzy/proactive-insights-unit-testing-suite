import re
import pytest

def is_valid_email(value):
    return bool(re.match(r"^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$", value or ""))

def discount(total, percent):
    if total < 0 or not 0 <= percent <= 100:
        raise ValueError("invalid discount")
    return round(total * percent / 100, 2)

def test_valid_email():
    assert is_valid_email("qa@example.com")

def test_standard_discount():
    assert discount(200, 10) == 20

# Gaps: malformed/unicode/empty email, None, numeric boundaries,
# invalid percentage, whitespace-only values and exception branches.
