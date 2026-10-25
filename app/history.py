"""Calculation history management using pandas."""

import os
from datetime import datetime

import pandas as pd

from app.calculation import Calculation
from app.exceptions import HistoryError


class History:
    """Manage calculator history and CSV persistence."""

    def __init__(self, max_size=100):
        self.calculations = []
        self.max_size = max_size

    def add(self, calculation):
        """Add a calculation to history."""
        self.calculations.append(calculation)

        if len(self.calculations) > self.max_size:
            self.calculations.pop(0)

    def clear(self):
        """Clear all calculation history."""
        self.calculations.clear()

    def get_all(self):
        """Return all calculations."""
        return self.calculations.copy()

    def save_to_csv(self, file_path):
        """Save calculation history to a CSV file."""
        try:
            directory = os.path.dirname(file_path)

            if directory:
                os.makedirs(directory, exist_ok=True)

            data = [
                calculation.to_dict()
                for calculation in self.calculations
            ]

            dataframe = pd.DataFrame(
                data,
                columns=[
                    "operation",
                    "operand1",
                    "operand2",
                    "result",
                    "timestamp",
                ],
            )

            dataframe.to_csv(file_path, index=False)

        except (OSError, ValueError, pd.errors.ParserError) as exc:
            raise HistoryError(
                f"Unable to save calculation history: {exc}"
            ) from exc

    def load_from_csv(self, file_path):
        """Load calculation history from a CSV file."""
        if not os.path.exists(file_path):
            raise HistoryError("History file does not exist.")

        try:
            dataframe = pd.read_csv(file_path)

            required_columns = {
                "operation",
                "operand1",
                "operand2",
                "result",
                "timestamp",
            }

            if not required_columns.issubset(dataframe.columns):
                raise HistoryError("History file is malformed.")

            loaded_calculations = []

            for _, row in dataframe.iterrows():
                calculation = Calculation(
                    operation=row["operation"],
                    operand1=float(row["operand1"]),
                    operand2=float(row["operand2"]),
                    result=float(row["result"]),
                    timestamp=datetime.fromisoformat(
                        str(row["timestamp"])
                    ),
                )
                loaded_calculations.append(calculation)

            self.calculations = loaded_calculations[-self.max_size:]

        except HistoryError:
            raise
        except (
            OSError,
            ValueError,
            TypeError,
            pd.errors.ParserError,
        ) as exc:
            raise HistoryError(
                f"Unable to load calculation history: {exc}"
            ) from exc