"""Tests for the calculator Command design pattern."""

from app.calculator import Calculator
from app.commands import CalculatorCommand


def test_calculator_command_add():
    """Test executing an addition through CalculatorCommand."""
    calculator = Calculator()

    command = CalculatorCommand(
        calculator,
        "add",
        10,
        5,
    )

    assert command.execute() == 15


def test_calculator_command_power():
    """Test executing a power operation through CalculatorCommand."""
    calculator = Calculator()

    command = CalculatorCommand(
        calculator,
        "power",
        2,
        3,
    )

    assert command.execute() == 8


def test_calculator_command_stores_request_data():
    """Test that CalculatorCommand encapsulates its request data."""
    calculator = Calculator()

    command = CalculatorCommand(
        calculator,
        "multiply",
        4,
        5,
    )

    assert command.calculator is calculator
    assert command.operation == "multiply"
    assert command.operand1 == 4
    assert command.operand2 == 5