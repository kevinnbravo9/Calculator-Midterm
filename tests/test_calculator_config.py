"""Tests for calculator configuration."""

import pytest

from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError


def test_default_configuration(monkeypatch):
    """Test configuration default values."""
    variables = [
        "CALCULATOR_LOG_DIR",
        "CALCULATOR_HISTORY_DIR",
        "CALCULATOR_LOG_FILE",
        "CALCULATOR_HISTORY_FILE",
        "CALCULATOR_MAX_HISTORY_SIZE",
        "CALCULATOR_AUTO_SAVE",
        "CALCULATOR_PRECISION",
        "CALCULATOR_MAX_INPUT_VALUE",
        "CALCULATOR_DEFAULT_ENCODING",
    ]

    for variable in variables:
        monkeypatch.delenv(variable, raising=False)

    config = CalculatorConfig()

    assert config.log_dir == "logs"
    assert config.history_dir == "history"
    assert config.log_file == "calculator.log"
    assert config.history_file == "calculator_history.csv"
    assert config.max_history_size == 100
    assert config.auto_save is True
    assert config.precision == 2
    assert config.max_input_value == 1000000
    assert config.default_encoding == "utf-8"


def test_custom_configuration(monkeypatch):
    """Test custom configuration values."""
    monkeypatch.setenv("CALCULATOR_LOG_DIR", "custom_logs")
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", "custom_history")
    monkeypatch.setenv("CALCULATOR_LOG_FILE", "custom.log")
    monkeypatch.setenv("CALCULATOR_HISTORY_FILE", "custom.csv")
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "50")
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "false")
    monkeypatch.setenv("CALCULATOR_PRECISION", "4")
    monkeypatch.setenv("CALCULATOR_MAX_INPUT_VALUE", "5000")
    monkeypatch.setenv("CALCULATOR_DEFAULT_ENCODING", "ascii")

    config = CalculatorConfig()

    assert config.log_dir == "custom_logs"
    assert config.history_dir == "custom_history"
    assert config.log_file == "custom.log"
    assert config.history_file == "custom.csv"
    assert config.max_history_size == 50
    assert config.auto_save is False
    assert config.precision == 4
    assert config.max_input_value == 5000
    assert config.default_encoding == "ascii"


def test_configuration_paths(monkeypatch):
    """Test generated log and history paths."""
    monkeypatch.setenv("CALCULATOR_LOG_DIR", "logs")
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", "history")
    monkeypatch.setenv("CALCULATOR_LOG_FILE", "calculator.log")
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        "calculator_history.csv",
    )

    config = CalculatorConfig()

    assert config.log_path == "logs/calculator.log"
    assert config.history_path == "history/calculator_history.csv"


@pytest.mark.parametrize(
    "variable,value",
    [
        ("CALCULATOR_MAX_HISTORY_SIZE", "0"),
        ("CALCULATOR_MAX_HISTORY_SIZE", "-1"),
        ("CALCULATOR_PRECISION", "-1"),
        ("CALCULATOR_MAX_INPUT_VALUE", "0"),
        ("CALCULATOR_MAX_INPUT_VALUE", "-100"),
    ],
)
def test_invalid_configuration(monkeypatch, variable, value):
    """Test invalid configuration values."""
    monkeypatch.setenv(variable, value)

    with pytest.raises(ValidationError):
        CalculatorConfig()


def test_invalid_numeric_configuration(monkeypatch):
    """Test a non-numeric configuration value."""
    monkeypatch.setenv(
        "CALCULATOR_MAX_HISTORY_SIZE",
        "invalid",
    )

    with pytest.raises(ValidationError):
        CalculatorConfig()