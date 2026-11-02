"""Tests for calculator operations."""

import pytest

from app.exceptions import OperationError
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

    with pytest.raises(OperationError):
        calculator_operation.execute(a, b)


def test_even_root_of_negative_number():
    """Test that an even root of a negative number raises an error."""
    operation = OperationFactory.create_operation("root")

    with pytest.raises(OperationError):
        operation.execute(-16, 2)


def test_odd_root_of_negative_number():
    """Test an odd root of a negative number."""
    operation = OperationFactory.create_operation("root")
    assert operation.execute(-8, 3) == pytest.approx(-2)


def test_invalid_operation():
    """Test that an unknown operation raises an error."""
    with pytest.raises(ValueError):
        OperationFactory.create_operation("unknown")

@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", -10, 5, -5),
        ("subtract", 5, 10, -5),
        ("multiply", -4, 5, -20),
        ("multiply", -4, -5, 20),
        ("divide", -10, 2, -5),
        ("divide", 0, 5, 0),
        ("power", 2, -2, 0.25),
        ("power", 5, 0, 1),
        ("root", 16, 4, 2),
        ("modulus", -10, 3, 2),
        ("int_divide", -10, 3, -4),
        ("percent", 0, 100, 0),
        ("abs_diff", -5, 5, 10),
        ("add", 2.5, 1.5, 4),
    ],
)
def test_operation_edge_cases(operation, a, b, expected):
    """Test arithmetic operations with edge-case values."""
    calculator_operation = OperationFactory.create_operation(operation)

    assert calculator_operation.execute(a, b) == pytest.approx(expected)

def test_get_operations():
    """Test that the factory returns all available operations."""
    operations = OperationFactory.get_operations()

    assert "add" in operations
    assert "subtract" in operations
    assert "multiply" in operations
    assert "divide" in operations
    assert "power" in operations
    assert "root" in operations
    assert "modulus" in operations
    assert "int_divide" in operations
    assert "percent" in operations
    assert "abs_diff" in operations