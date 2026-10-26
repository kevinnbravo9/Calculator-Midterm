"""Tests for the main Calculator class."""

from app.calculator import Calculator


class DummyObserver:
    """Simple observer used for testing."""

    def __init__(self):
        self.calculations = []

    def update(self, calculation):
        self.calculations.append(calculation)


def test_calculator_performs_calculation():
    """Test performing a calculation."""
    calculator = Calculator()

    result = calculator.calculate("add", 10, 5)

    assert result == 15
    assert len(calculator.get_history()) == 1
    assert calculator.get_history()[0].operation == "add"


def test_calculator_notifies_observer():
    """Test that registered observers are notified."""
    calculator = Calculator()
    observer = DummyObserver()

    calculator.add_observer(observer)
    calculator.calculate("multiply", 4, 5)

    assert len(observer.calculations) == 1
    assert observer.calculations[0].result == 20


def test_calculator_undo():
    """Test undoing a calculation."""
    calculator = Calculator()

    calculator.calculate("add", 10, 5)
    calculator.calculate("multiply", 2, 3)

    assert calculator.undo() is True
    assert len(calculator.get_history()) == 1
    assert calculator.get_history()[0].result == 15


def test_calculator_redo():
    """Test redoing an undone calculation."""
    calculator = Calculator()

    calculator.calculate("add", 10, 5)
    calculator.calculate("multiply", 2, 3)

    calculator.undo()

    assert calculator.redo() is True
    assert len(calculator.get_history()) == 2
    assert calculator.get_history()[1].result == 6


def test_undo_without_history():
    """Test undo when there is nothing to undo."""
    calculator = Calculator()

    assert calculator.undo() is False

def test_redo_without_undo():
    """Test redo when there is nothing to redo."""
    calculator = Calculator()

    assert calculator.redo() is False

def test_new_calculation_clears_redo():
    """Test that a new calculation clears redo history."""
    calculator = Calculator()

    calculator.calculate("add", 10, 5)
    calculator.undo()

    calculator.calculate("multiply", 2, 3)

    assert calculator.redo() is False


def test_clear_history():
    """Test clearing calculator history."""
    calculator = Calculator()

    calculator.calculate("add", 1, 2)
    calculator.calculate("subtract", 10, 5)

    calculator.clear_history()

    assert calculator.get_history() == []


def test_maximum_history_size():
    """Test calculator maximum history size."""
    calculator = Calculator(max_history_size=2)

    calculator.calculate("add", 1, 1)
    calculator.calculate("add", 2, 2)
    calculator.calculate("add", 3, 3)

    history = calculator.get_history()

    assert len(history) == 2
    assert history[0].result == 4
    assert history[1].result == 6