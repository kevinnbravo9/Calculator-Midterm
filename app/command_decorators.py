"""Decorators for registering calculator commands."""

COMMAND_REGISTRY = {}


def register_command(name, description):
    """Register a command and its description for the dynamic help menu."""
    def decorator(func):
        COMMAND_REGISTRY[name] = {
            "function": func,
            "description": description,
        }
        return func

    return decorator


def get_registered_commands():
    """Return all registered calculator commands."""
    return COMMAND_REGISTRY