"""Memento pattern implementation for calculator history."""

from copy import deepcopy


class CalculatorMemento:
    """Store a snapshot of calculator history."""

    def __init__(self, calculations):
        self._calculations = deepcopy(calculations)

    def get_state(self):
        """Return the saved calculator history state."""
        return deepcopy(self._calculations)


class MementoManager:
    """Manage undo and redo history states."""

    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save_state(self, calculations):
        """Save the current state before a new calculation."""
        self._undo_stack.append(
            CalculatorMemento(calculations)
        )
        self._redo_stack.clear()

    def undo(self, current_state):
        """Restore the previous calculator state."""
        if not self._undo_stack:
            return None

        self._redo_stack.append(
            CalculatorMemento(current_state)
        )

        memento = self._undo_stack.pop()
        return memento.get_state()

    def redo(self, current_state):
        """Restore a previously undone calculator state."""
        if not self._redo_stack:
            return None

        self._undo_stack.append(
            CalculatorMemento(current_state)
        )

        memento = self._redo_stack.pop()
        return memento.get_state()

    def clear(self):
        """Clear undo and redo states."""
        self._undo_stack.clear()
        self._redo_stack.clear()