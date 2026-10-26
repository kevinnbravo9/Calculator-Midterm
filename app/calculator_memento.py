"""Memento pattern implementation for calculator history."""

from copy import deepcopy


class CalculatorMemento:
    """Store a snapshot of calculator history."""

    def __init__(self, calculations):
        self._calculations = deepcopy(calculations)

    def get_state(self):
        """Return the saved calculator history state."""
        return deepcopy(self._calculations)
