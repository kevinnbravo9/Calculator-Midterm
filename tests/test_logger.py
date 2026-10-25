"""Tests for calculator logging and observers."""

from app.calculation import Calculation
from app.history import History
from app.logger import (
    AutoSaveObserver,
    CalculatorLogger,
    LoggingObserver,
)


def test_calculator_logger(tmp_path):
    """Test calculator logging methods."""
    log_file = tmp_path / "calculator.log"
    calculator_logger = CalculatorLogger(str(log_file))

    calculator_logger.info("Information message")
    calculator_logger.warning("Warning message")
    calculator_logger.error("Error message")

    for handler in calculator_logger.logger.handlers:
        handler.flush()

    assert log_file.exists()

    content = log_file.read_text(encoding="utf-8")

    assert "Information message" in content
    assert "Warning message" in content
    assert "Error message" in content


def test_logging_observer(tmp_path):
    """Test that LoggingObserver logs a calculation."""
    log_file = tmp_path / "observer.log"
    calculator_logger = CalculatorLogger(str(log_file))

    observer = LoggingObserver(calculator_logger)
    calculation = Calculation("add", 10, 5, 15)

    observer.update(calculation)

    for handler in calculator_logger.logger.handlers:
        handler.flush()

    content = log_file.read_text(encoding="utf-8")

    assert "add" in content
    assert "10" in content
    assert "5" in content
    assert "15" in content


def test_auto_save_observer(tmp_path):
    """Test that AutoSaveObserver saves history to CSV."""
    history_file = tmp_path / "calculator_history.csv"

    history = History()
    calculation = Calculation("multiply", 4, 5, 20)
    history.add(calculation)

    observer = AutoSaveObserver(
        history,
        str(history_file),
    )

    observer.update(calculation)

    assert history_file.exists()

    content = history_file.read_text(encoding="utf-8")

    assert "multiply" in content
    assert "20" in content