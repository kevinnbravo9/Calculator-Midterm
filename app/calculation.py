"""Calculation model for the calculator."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Calculation:
    """Represents a single calculator calculation."""

    operation: str
    operand1: float
    operand2: float
    result: float
    timestamp: datetime = field(default_factory=datetime.now)

    def to_dict(self):
        """Convert the calculation to a dictionary."""
        return {
            "operation": self.operation,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "result": self.result,
            "timestamp": self.timestamp.isoformat(),
        }