"""Main calculator class."""

from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento
from app.history import History
from app.operations import OperationFactory


class Calculator:
    """Manage calculations, history, undo/redo, and observers."""

    def __init__(self, max_history_size=100):
        """Initialize the calculator."""
        self.history = History(max_size=max_history_size)
        self.undo_stack = []
        self.redo_stack = []
        self.observers = []

    def add_observer(self, observer):
        """Register an observer."""
        self.observers.append(observer)

    def notify_observers(self, calculation):
        """Notify all registered observers."""
        for observer in self.observers:
            observer.update(calculation)

    def calculate(self, operation_name, operand1, operand2):
        """Perform a calculation and store it in history."""
        self.undo_stack.append(self.create_memento())
        self.redo_stack.clear()

        operation = OperationFactory.create_operation(operation_name)
        result = operation.execute(operand1, operand2)

        calculation = Calculation(
            operation_name,
            operand1,
            operand2,
            result
        )

        self.history.add(calculation)
        self.notify_observers(calculation)

        return result

    def create_memento(self):
        """Create a snapshot of the current history."""
        return CalculatorMemento(self.history.get_all().copy())

    def restore_memento(self, memento):
        """Restore calculator history from a memento."""
        self.history.clear()

        for calculation in memento.get_state():
            self.history.add(calculation)

    def undo(self):
        """Undo the most recent calculation."""
        if not self.undo_stack:
            return False

        self.redo_stack.append(self.create_memento())
        memento = self.undo_stack.pop()
        self.restore_memento(memento)

        return True

    def redo(self):
        """Redo the most recently undone calculation."""
        if not self.redo_stack:
            return False

        self.undo_stack.append(self.create_memento())
        memento = self.redo_stack.pop()
        self.restore_memento(memento)

        return True

    def clear_history(self):
        """Clear the calculation history."""
        self.undo_stack.append(self.create_memento())
        self.redo_stack.clear()
        self.history.clear()

    def get_history(self):
        """Return all calculations in history."""
        return self.history.get_all()