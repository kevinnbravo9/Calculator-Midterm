"""Arithmetic operations for the calculator."""

from abc import ABC, abstractmethod
from app.exceptions import OperationError


class Operation(ABC):
    """Base class for all calculator operations."""

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Execute an operation using two numbers."""


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Root degree cannot be zero.")
        if a < 0 and b % 2 == 0:
            raise OperationError(
                "Cannot calculate an even root of a negative number."
            )
        if a < 0:
            return -((-a) ** (1 / b))
        return a ** (1 / b)


class Modulus(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot perform modulus by zero.")
        return a % b


class IntegerDivide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a // b


class Percent(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError(
                "Cannot calculate percentage with zero as the second value."
            )
        return (a / b) * 100


class AbsoluteDifference(Operation):
    def execute(self, a, b):
        return abs(a - b)


class OperationFactory:
    """Factory for creating calculator operations."""

    _operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntegerDivide,
        "percent": Percent,
        "abs_diff": AbsoluteDifference,
    }

    @classmethod
    def create_operation(cls, operation_name: str) -> Operation:
        """Create an operation based on its command name."""
        operation = cls._operations.get(operation_name.lower())

        if operation is None:
            raise ValueError(f"Unknown operation: {operation_name}")

        return operation()