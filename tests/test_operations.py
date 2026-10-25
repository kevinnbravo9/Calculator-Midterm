"""Tests for calculator operations."""

import pytest

from app.operations import OperationFactory


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", 10, 5, 15),
        ("subtract", 10, 5, 5),
        ("multiply", 10, 5, 50),
        ("divide", 10, 5, 2),
        ("power", 2, 3, 8),
        ("root", 9, 2, 3),
        ("modulus", 10, 3, 1),
        ("int_divide", 10, 3, 3),
        ("percent", 25, 100, 25),
        ("abs_diff", 5, 10, 5),
    ],
)
def test_operations(operation, a, b, expected):
    """Test calculator operations with different values."""
    calculator_operation = OperationFactory.create_operation(operation)
    assert calculator_operation.execute(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "operation,a,b",
    [
        ("divide", 10, 0),
        ("modulus", 10, 0),
        ("int_divide", 10, 0),
        ("percent", 10, 0),
        ("root", 10, 0),
    ],
)
def test_zero_errors(operation, a, b):
    """Test operations that cannot use zero as the second value."""
    calculator_operation = OperationFactory.create_operation(operation)

    with pytest.raises(ValueError):
        calculator_operation.execute(a, b)


def test_even_root_of_negative_number():
    """Test that an even root of a negative number raises an error."""
    operation = OperationFactory.create_operation("root")

    with pytest.raises(ValueError):
        operation.execute(-16, 2)


def test_odd_root_of_negative_number():
    """Test an odd root of a negative number."""
    operation = OperationFactory.create_operation("root")
    assert operation.execute(-8, 3) == pytest.approx(-2)


def test_invalid_operation():
    """Test that an unknown operation raises an error."""
    with pytest.raises(ValueError):
        OperationFactory.create_operation("unknown")