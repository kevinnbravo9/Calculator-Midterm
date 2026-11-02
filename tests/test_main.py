"""Tests for the calculator REPL."""

from app.operations import OperationFactory

from unittest.mock import patch

from main import run_repl


def test_repl_addition(capsys):
    """Test an addition through the actual REPL."""
    user_inputs = [
        "add",
        "2",
        "3",
        "exit",
    ]

    with patch("builtins.input", side_effect=user_inputs):
        run_repl()

    output = capsys.readouterr().out

    assert "Result: 5" in output
    assert "Goodbye!" in output


def test_repl_invalid_command(capsys):
    """Test an invalid command through the actual REPL."""
    user_inputs = [
        "invalid",
        "exit",
    ]

    with patch("builtins.input", side_effect=user_inputs):
        run_repl()

    output = capsys.readouterr().out

    assert "Unknown command: invalid" in output


def test_repl_divide_by_zero(capsys):
    """Test REPL error handling for division by zero."""
    user_inputs = [
        "divide",
        "10",
        "0",
        "exit",
    ]

    with patch("builtins.input", side_effect=user_inputs):
        run_repl()

    output = capsys.readouterr().out

    assert "Cannot divide by zero." in output
    assert "Goodbye!" in output


def test_repl_help(capsys):
    """Test the help command through the actual REPL."""
    user_inputs = [
        "help",
        "exit",
    ]

    with patch("builtins.input", side_effect=user_inputs):
        run_repl()

    output = capsys.readouterr().out

    assert "Available Commands:" in output
    assert "add" in output
    assert "undo" in output
    assert "redo" in output
    assert "save" in output
    assert "load" in output

def test_help_uses_factory_operations(capsys):
    """Test that help automatically displays factory operations."""
    from main import display_help

    display_help()

    output = capsys.readouterr().out

    for operation in OperationFactory.get_operations():
        assert operation in output

def test_repl_uses_color_for_result(capsys):
    """Test that calculation results use Colorama output."""
    user_inputs = [
        "add",
        "2",
        "3",
        "exit",
    ]

    with patch("builtins.input", side_effect=user_inputs):
        with patch("main.Fore.GREEN", "[GREEN]"):
            run_repl()

    output = capsys.readouterr().out

    assert "[GREEN]Result: 5" in output