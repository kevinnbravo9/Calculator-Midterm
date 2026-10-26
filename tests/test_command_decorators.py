"""Tests for calculator command decorators."""

from app.command_decorators import (
    COMMAND_REGISTRY,
    get_registered_commands,
    register_command,
)


def test_register_command():
    """Test that the decorator registers a command."""
    original_registry = COMMAND_REGISTRY.copy()

    try:
        @register_command("test", "Test command")
        def test_command():
            return "executed"

        commands = get_registered_commands()

        assert "test" in commands
        assert commands["test"]["description"] == "Test command"
        assert commands["test"]["function"]() == "executed"
    finally:
        COMMAND_REGISTRY.clear()
        COMMAND_REGISTRY.update(original_registry)


def test_get_registered_commands():
    """Test retrieving the command registry."""
    commands = get_registered_commands()

    assert commands is COMMAND_REGISTRY