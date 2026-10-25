"""Command-line interface for the calculator."""

from colorama import Fore, Style, init

from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
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


def display_help():
    """Display available calculator commands."""
    print(Fore.CYAN + "\nAvailable Commands:")
    print("add, subtract, multiply, divide")
    print("power, root, modulus, int_divide")
    print("percent, abs_diff")
    print("history - Display calculation history")
    print("clear   - Clear calculation history")
    print("undo    - Undo the last calculation")
    print("redo    - Redo the last undone calculation")
    print("save    - Save calculation history")
    print("load    - Load calculation history")
    print("help    - Display available commands")
    print("exit    - Exit the calculator")


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

            result = calculator.calculate(
                command,
                operand1,
                operand2,
            )

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