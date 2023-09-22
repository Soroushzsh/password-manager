import pytest

from utils.custom_validators import *


@pytest.mark.parametrize("input_value, expected_result", [
    ("123", 123),       # Valid integer input
    ("-456", -456),     # Valid negative integer input
    ("0", 0),           # Valid zero input
    ("12.34", False),   # Valid float input (should return False)
    ("abc", False),     # Invalid non-numeric input
    ("123abc", False),  # Invalid mixed input
    ("", False),        # Empty input (should return False)
])
def test_is_int(input_value, expected_result):
    result = is_int(input_value)
    assert result == expected_result


@pytest.mark.parametrize("input_value, expected_result", [
    ('y', True),
    ('n', True),
    ('Y', True),
    ('N', True),
    ('Yes', True),
    ('yes', True),
    ('No', True),
    ('no', True),
    ('Nope', True),
    ('Yup', True),
    ('a', False),
    ('ab', False),
    ('12', False),
    ('ab12', False),
])
def test_yes_or_no(input_value, expected_result):
    result = yes_or_no_validator(input_value)
    assert result == expected_result
