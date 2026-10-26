"""Tests for calculator input validation."""

import pytest

from app.exceptions import ValidationError
from app.input_validators import validate_number


@pytest.mark.parametrize(
    "value,expected",
    [
        ("10", 10.0),
        ("-5", -5.0),
        ("3.5", 3.5),
        (20, 20.0),
        ("100", 100.0),
        ("-100", -100.0),
    ],
)
def test_validate_number(value, expected):
    """Test valid numerical inputs."""
    assert validate_number(value, 100) == expected


@pytest.mark.parametrize(
    "value",
    [
        "hello",
        None,
        "",
    ],
)
def test_validate_invalid_number(value):
    """Test invalid numerical inputs."""
    with pytest.raises(ValidationError):
        validate_number(value, 100)


def test_number_above_maximum():
    """Test a number above the configured maximum."""
    with pytest.raises(ValidationError):
        validate_number(101, 100)


def test_number_below_minimum():
    """Test a number below the configured minimum."""
    with pytest.raises(ValidationError):
        validate_number(-101, 100)
