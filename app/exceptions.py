"""Custom exceptions for the calculator."""


class CalculatorError(Exception):
    """Base exception for calculator errors."""


class OperationError(CalculatorError):
    """Raised when a calculator operation cannot be completed."""


class ValidationError(CalculatorError):
    """Raised when user input is invalid."""


class HistoryError(CalculatorError):
    """Raised when a history operation cannot be completed."""