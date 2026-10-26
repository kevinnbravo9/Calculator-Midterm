"""Command-line interface for the calculator."""

from colorama import Fore, Style, init

from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
from app.commands import CalculatorCommand
from app.command_decorators import get_registered_commands, register_command
from app.input_validators import validate_number
from app.logger import AutoSaveObserver, CalculatorLogger, LoggingObserver


init(autoreset=True)


OPERATIONS = {
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "root",
    "modulus",
    "int_divide",
    "percent",
    "abs_diff",
}

@register_command("add", "Add two numbers")
@register_command("subtract", "Subtract two numbers")
@register_command("multiply", "Multiply two numbers")
@register_command("divide", "Divide two numbers")
@register_command("power", "Raise one number to the power of another")
@register_command("root", "Calculate the nth root of a number")
@register_command("modulus", "Calculate the remainder of division")
@register_command("int_divide", "Perform integer division")
@register_command("percent", "Calculate percentage")
@register_command("abs_diff", "Calculate absolute difference")
@register_command("history", "Display calculation history")
@register_command("clear", "Clear calculation history")
@register_command("undo", "Undo the last calculation")
@register_command("redo", "Redo the last undone calculation")
@register_command("save", "Save calculation history")
@register_command("load", "Load calculation history")
@register_command("help", "Display available commands")
@register_command("exit", "Exit the calculator")
def register_repl_commands():
    """Register REPL commands for the dynamic help menu."""

def display_help():
    """Display the dynamically registered calculator commands."""
    print(Fore.CYAN + "\nAvailable Commands:")

    commands = get_registered_commands()

    for name, command_data in reversed(commands.items()):
        print(f"{name:<12} - {command_data['description']}")


def display_history(calculator):
    """Display calculation history."""
    history = calculator.get_history()

    if not history:
        print(Fore.YELLOW + "History is empty.")
        return

    print(Fore.CYAN + "\nCalculation History:")

    for calculation in history:
        print(
            f"{calculation.operation}: "
            f"{calculation.operand1} "
            f"{calculation.operand2} = "
            f"{calculation.result}"
        )


def create_calculator(config):
    """Create and configure the calculator."""
    calculator = Calculator(
        max_history_size=config.max_history_size
    )

    calculator_logger = CalculatorLogger(
        config.log_path,
        config.default_encoding,
    )

    calculator.add_observer(
        LoggingObserver(calculator_logger)
    )

    if config.auto_save:
        calculator.add_observer(
            AutoSaveObserver(
                calculator.history,
                config.history_path,
            )
        )

    return calculator


def run_repl():
    """Run the calculator REPL."""
    config = CalculatorConfig()
    calculator = create_calculator(config)

    print(Fore.GREEN + "Advanced Calculator")
    print("Type 'help' to see available commands.")

    while True:
        try:
            command = input("\nEnter command: ").lower().strip()

            if command == "exit":
                print(Fore.GREEN + "Goodbye!")
                break

            if command == "help":
                display_help()
                continue

            if command == "history":
                display_history(calculator)
                continue

            if command == "clear":
                calculator.clear_history()
                print(Fore.GREEN + "History cleared.")
                continue

            if command == "undo":
                if calculator.undo():
                    print(Fore.GREEN + "Last calculation undone.")
                else:
                    print(Fore.YELLOW + "Nothing to undo.")
                continue

            if command == "redo":
                if calculator.redo():
                    print(Fore.GREEN + "Calculation restored.")
                else:
                    print(Fore.YELLOW + "Nothing to redo.")
                continue

            if command == "save":
                calculator.history.save_to_csv(
                    config.history_path
                )
                print(Fore.GREEN + "History saved.")
                continue

            if command == "load":
                calculator.history.load_from_csv(
                    config.history_path
                )
                print(Fore.GREEN + "History loaded.")
                continue

            if command not in OPERATIONS:
                print(Fore.RED + f"Unknown command: {command}")
                continue

            first_value = input("Enter first number: ")
            second_value = input("Enter second number: ")

            operand1 = validate_number(
                first_value,
                config.max_input_value,
            )
            operand2 = validate_number(
                second_value,
                config.max_input_value,
            )

            calculation_command = CalculatorCommand(
             calculator,
             command,
             operand1,
             operand2,
            )

            result = calculation_command.execute()

            result = round(result, config.precision)

            print(
                Fore.GREEN
                + f"Result: {result}"
                + Style.RESET_ALL
            )

        except Exception as error:
            print(Fore.RED + f"Error: {error}")


if __name__ == "__main__":
    run_repl()