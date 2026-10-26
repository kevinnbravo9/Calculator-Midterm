"""Tests for the calculator Memento pattern."""

from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento


def test_memento_stores_state():
    """Test that a memento stores calculator history."""
    calculations = [
        Calculation("add", 10, 5, 15),
    ]

    memento = CalculatorMemento(calculations)
    state = memento.get_state()

    assert len(state) == 1
    assert state[0].operation == "add"
    assert state[0].result == 15


def test_memento_uses_copy():
    """Test that the memento keeps an independent copy."""
    calculations = [
        Calculation("add", 1, 2, 3),
    ]

    memento = CalculatorMemento(calculations)
    calculations.clear()

    state = memento.get_state()

    assert len(state) == 1
    assert state[0].result == 3