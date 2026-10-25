"""Configuration management for the calculator."""

import os

from dotenv import load_dotenv

from app.exceptions import ValidationError


load_dotenv()


class CalculatorConfig:
    """Load and validate calculator configuration settings."""

    def __init__(self):
        self.log_dir = os.getenv("CALCULATOR_LOG_DIR", "logs")
        self.history_dir = os.getenv("CALCULATOR_HISTORY_DIR", "history")

        self.log_file = os.getenv(
            "CALCULATOR_LOG_FILE",
            "calculator.log",
        )
        self.history_file = os.getenv(
            "CALCULATOR_HISTORY_FILE",
            "calculator_history.csv",
        )

        try:
            self.max_history_size = int(
                os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100")
            )
            self.precision = int(
                os.getenv("CALCULATOR_PRECISION", "2")
            )
            self.max_input_value = float(
                os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000")
            )
        except ValueError as exc:
            raise ValidationError(
                "Invalid numeric configuration value."
            ) from exc

        self.auto_save = (
            os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
        )

        self.default_encoding = os.getenv(
            "CALCULATOR_DEFAULT_ENCODING",
            "utf-8",
        )

        self._validate()

    def _validate(self):
        """Validate configuration values."""
        if self.max_history_size <= 0:
            raise ValidationError(
                "Maximum history size must be greater than zero."
            )

        if self.precision < 0:
            raise ValidationError(
                "Precision cannot be negative."
            )

        if self.max_input_value <= 0:
            raise ValidationError(
                "Maximum input value must be greater than zero."
            )

    @property
    def log_path(self):
        """Return the complete log file path."""
        return os.path.join(self.log_dir, self.log_file)

    @property
    def history_path(self):
        """Return the complete history file path."""
        return os.path.join(
            self.history_dir,
            self.history_file,
        )