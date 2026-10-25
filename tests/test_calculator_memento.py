"""Tests for the calculator Memento pattern."""

from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento, MementoManager


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


def test_undo():
    """Test restoring the previous state."""
    manager = MementoManager()

    first_state = [
        Calculation("add", 1, 1, 2),
    ]

    manager.save_state([])
    restored_state = manager.undo(first_state)

    assert restored_state == []


def test_redo():
    """Test restoring an undone state."""
    manager = MementoManager()

    current_state = [
        Calculation("add", 1, 1, 2),
    ]

    manager.save_state([])
    undone_state = manager.undo(current_state)
    redone_state = manager.redo(undone_state)

    assert len(redone_state) == 1
    assert redone_state[0].result == 2


def test_undo_without_saved_state():
    """Test undo when there is nothing to undo."""
    manager = MementoManager()

    assert manager.undo([]) is None


def test_redo_without_saved_state():
    """Test redo when there is nothing to redo."""
    manager = MementoManager()

    assert manager.redo([]) is None


def test_new_state_clears_redo():
    """Test that a new calculation clears redo history."""
    manager = MementoManager()

    manager.save_state([])
    manager.undo([Calculation("add", 1, 1, 2)])

    manager.save_state(
        [Calculation("multiply", 2, 2, 4)]
    )

    assert manager.redo([]) is None


def test_clear_memento_history():
    """Test clearing undo and redo states."""
    manager = MementoManager()

    manager.save_state([])
    manager.clear()

    assert manager.undo([]) is None
    assert manager.redo([]) is None