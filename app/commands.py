"""Command pattern implementation for calculator actions."""

from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract base class for calculator commands."""

    @abstractmethod
    def execute(self):
        """Execute the command."""


class CalculatorCommand(Command):
    """Command that executes a calculator operation."""

    def __init__(self, calculator, operation, operand1, operand2):
        """Initialize a calculator command."""
        self.calculator = calculator
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self):
        """Execute the calculator operation."""
        return self.calculator.calculate(
            self.operation,
            self.operand1,
            self.operand2,
        )