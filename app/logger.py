"""Logging and observer classes for the calculator."""

import logging
import os


class CalculatorLogger:
    """Configure and manage calculator logging."""

    def __init__(self, log_file, encoding="utf-8"):
        directory = os.path.dirname(log_file)

        if directory:
            os.makedirs(directory, exist_ok=True)

        self.logger = logging.getLogger(
            f"calculator.{os.path.abspath(log_file)}"
        )
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        handler = logging.FileHandler(
            log_file,
            encoding=encoding,
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message):
        """Log an informational message."""
        self.logger.info(message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(message)


class LoggingObserver:
    """Observer that logs new calculations."""

    def __init__(self, calculator_logger):
        self.calculator_logger = calculator_logger

    def update(self, calculation):
        """Log calculation details."""
        self.calculator_logger.info(
            f"{calculation.operation}: "
            f"{calculation.operand1}, "
            f"{calculation.operand2} = "
            f"{calculation.result}"
        )


class AutoSaveObserver:
    """Observer that automatically saves calculator history."""

    def __init__(self, history, file_path):
        self.history = history
        self.file_path = file_path

    def update(self, calculation):
        """Save history when a new calculation occurs."""
        self.history.save_to_csv(self.file_path)