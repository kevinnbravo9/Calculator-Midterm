# Advanced Calculator Midterm Project

## Project Description

This project is an advanced calculator application developed in Python. The calculator provides basic and advanced mathematical operations through a command-line REPL interface. It also includes calculation history, undo and redo functionality, CSV history management, logging, configuration using environment variables, and automated testing.

The project uses several software design patterns, including Factory, Memento, Observer, Decorator, and Command. Colorama is also used to provide color-coded output in the command-line interface. The Decorator Pattern is used to support a dynamic help menu, while the Command Pattern encapsulates calculator operations as command objects.

## Features

- Interactive REPL command-line interface
- Addition
- Subtraction
- Multiplication
- Division
- Power
- Root
- Modulus
- Integer division
- Percentage calculation
- Absolute difference
- Calculation history
- Undo and redo
- Clear history
- Save history to CSV
- Load history from CSV
- Automatic history saving
- Application logging
- Input validation
- Custom exception handling
- Environment-based configuration
- Color-coded terminal output
- Dynamic help menu using the Decorator Pattern
- Calculator commands using the Command Pattern
- Automated testing with Pytest
- Code coverage with pytest-cov
- GitHub Actions CI workflow

## Design Patterns

### Factory Pattern

The Factory Pattern is used to create and select calculator operations. This makes it easier to organize the different mathematical operations and add new operations in the future.

### Memento Pattern

The Memento Pattern is used to support undo and redo functionality. It stores previous states of the calculation history so that the calculator can restore an earlier state when needed.

### Observer Pattern

The Observer Pattern is used for logging and automatic history saving. The `LoggingObserver` records calculator activity, while the `AutoSaveObserver` automatically saves the calculation history.

### Decorator Pattern

The Decorator Pattern is used to register calculator commands for the dynamic help menu. Each command and its description are registered using a decorator, allowing the help menu to display the available commands dynamically.

### Command Pattern

The Command Pattern is used to encapsulate calculator operations as command objects. The `CalculatorCommand` class stores the calculator, operation, and operands, and executes the requested calculation through its `execute()` method.

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd calculator_midterm
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment on macOS/Linux:

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

The calculator uses a `.env` file for configuration.

```env
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_LOG_FILE=calculator.log
CALCULATOR_HISTORY_FILE=calculator_history.csv
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8
```

## Running the Calculator

Run the calculator with:

```bash
python3 main.py
```

The calculator will display a prompt where commands can be entered.

## Available Commands

### Mathematical Operations

- `add`
- `subtract`
- `multiply`
- `divide`
- `power`
- `root`
- `modulus`
- `int_divide`
- `percent`
- `abs_diff`

### History and Application Commands

- `history` - Display calculation history
- `clear` - Clear calculation history
- `undo` - Undo the last calculation
- `redo` - Redo the last undone calculation
- `save` - Save calculation history
- `load` - Load calculation history
- `help` - Display available commands
- `exit` - Exit the calculator

## Example

```text
Advanced Calculator
Type 'help' to see available commands.

Enter command: add
Enter first number: 10
Enter second number: 5
Result: 15.0
```

## Color-Coded Output

The calculator uses Colorama to provide color-coded terminal output. Successful operations, errors, warnings, help information, and history messages are displayed using different colors to make the REPL easier to use.

## Testing

Run all tests with:

```bash
pytest
```

Run the tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=90
```

The project is configured to require at least 90% test coverage.

## Continuous Integration

GitHub Actions is configured to automatically install the project dependencies and run the test suite whenever changes are pushed to the `main` branch or a pull request is created.

The CI workflow also verifies that total test coverage remains at or above 90%.

## Technologies Used

- Python
- Pandas
- python-dotenv
- Pytest
- pytest-cov
- Colorama
- Git
- GitHub Actions

## Project Structure

```text
calculator_midterm/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── command_decorators.py
│   ├── commands.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── operations.py
│   └── logger.py
├── tests/
│   ├── test_command_decorators.py
│   ├── test_commands.py
├── .github/
│   └── workflows/
│       └── python-app.yml
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```