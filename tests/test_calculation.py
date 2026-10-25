"""Tests for the Calculation class."""

from datetime import datetime

from app.calculation import Calculation


def test_create_calculation():
    """Test creating a calculation."""
    calculation = Calculation("add", 10, 5, 15)

    assert calculation.operation == "add"
    assert calculation.operand1 == 10
    assert calculation.operand2 == 5
    assert calculation.result == 15
    assert isinstance(calculation.timestamp, datetime)


def test_calculation_to_dict():
    """Test converting a calculation to a dictionary."""
    calculation = Calculation("multiply", 4, 5, 20)

    data = calculation.to_dict()

    assert data["operation"] == "multiply"
    assert data["operand1"] == 4
    assert data["operand2"] == 5
    assert data["result"] == 20
    assert "timestamp" in data