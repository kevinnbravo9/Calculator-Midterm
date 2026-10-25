"""Tests for calculator history management."""

import pandas as pd
import pytest

from app.calculation import Calculation
from app.exceptions import HistoryError
from app.history import History


def test_add_calculation():
    """Test adding a calculation to history."""
    history = History()
    calculation = Calculation("add", 10, 5, 15)

    history.add(calculation)

    assert len(history.get_all()) == 1
    assert history.get_all()[0] == calculation


def test_max_history_size():
    """Test that history respects the maximum size."""
    history = History(max_size=2)

    history.add(Calculation("add", 1, 1, 2))
    history.add(Calculation("add", 2, 2, 4))
    history.add(Calculation("add", 3, 3, 6))

    calculations = history.get_all()

    assert len(calculations) == 2
    assert calculations[0].result == 4
    assert calculations[1].result == 6


def test_clear_history():
    """Test clearing calculation history."""
    history = History()
    history.add(Calculation("multiply", 5, 2, 10))

    history.clear()

    assert history.get_all() == []


def test_save_and_load_history(tmp_path):
    """Test saving and loading calculation history."""
    file_path = tmp_path / "calculator_history.csv"

    history = History()
    history.add(Calculation("add", 10, 5, 15))
    history.add(Calculation("multiply", 4, 5, 20))

    history.save_to_csv(str(file_path))

    new_history = History()
    new_history.load_from_csv(str(file_path))

    calculations = new_history.get_all()

    assert len(calculations) == 2
    assert calculations[0].operation == "add"
    assert calculations[0].operand1 == 10
    assert calculations[0].operand2 == 5
    assert calculations[0].result == 15
    assert calculations[1].operation == "multiply"
    assert calculations[1].result == 20


def test_save_creates_directory(tmp_path):
    """Test that saving creates the history directory."""
    file_path = tmp_path / "history" / "calculator_history.csv"

    history = History()
    history.add(Calculation("subtract", 10, 4, 6))

    history.save_to_csv(str(file_path))

    assert file_path.exists()


def test_load_missing_file(tmp_path):
    """Test loading a history file that does not exist."""
    file_path = tmp_path / "missing.csv"
    history = History()

    with pytest.raises(HistoryError):
        history.load_from_csv(str(file_path))


def test_load_malformed_file(tmp_path):
    """Test loading a malformed history file."""
    file_path = tmp_path / "bad_history.csv"

    dataframe = pd.DataFrame(
        {
            "wrong_column": [1],
            "another_column": [2],
        }
    )
    dataframe.to_csv(file_path, index=False)

    history = History()

    with pytest.raises(HistoryError):
        history.load_from_csv(str(file_path))


def test_load_respects_max_history_size(tmp_path):
    """Test maximum history size when loading from CSV."""
    file_path = tmp_path / "history.csv"

    history = History()
    history.add(Calculation("add", 1, 1, 2))
    history.add(Calculation("add", 2, 2, 4))
    history.add(Calculation("add", 3, 3, 6))
    history.save_to_csv(str(file_path))

    new_history = History(max_size=2)
    new_history.load_from_csv(str(file_path))

    calculations = new_history.get_all()

    assert len(calculations) == 2
    assert calculations[0].result == 4
    assert calculations[1].result == 6