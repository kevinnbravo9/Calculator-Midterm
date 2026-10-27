# Advanced Calculator Midterm Project

## Project Description

This project is an advanced calculator application developed in Python. It supports basic and advanced mathematical operations through a command-line REPL. The calculator also includes calculation history, undo and redo, CSV history management, logging, environment configuration, and automated testing.

The project uses Factory, Memento, Observer, Decorator, and Command design patterns.

## Features

- Basic and advanced mathematical operations
- Calculation history
- Undo and redo
- Save and load history using CSV
- Automatic history saving
- Logging
- Input validation and custom exceptions
- Environment-based configuration
- Color-coded terminal output
- Dynamic help menu
- Automated testing and code coverage
- GitHub Actions CI

## Design Patterns

### Factory Pattern

The Factory Pattern is used to create and select calculator operations.

### Memento Pattern

The Memento Pattern is used to save previous states for undo and redo.

### Observer Pattern

The Observer Pattern is used for logging and automatic history saving.

### Decorator Pattern

The Decorator Pattern is used to register commands for the dynamic help menu.

### Command Pattern

The Command Pattern is used to execute calculator operations through command objects.

## Setup

Open the project folder:

```bash
cd calculator_midterm
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

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

Type `help` to see the available commands.

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

### Other Commands

- `history` - Display calculation history
- `clear` - Clear calculation history
- `undo` - Undo the last calculation
- `redo` - Redo the last undone calculation
- `save` - Save calculation history
- `load` - Load calculation history
- `help` - Display available commands
- `exit` - Exit the calculator

## Testing

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=90
```

The project requires at least 90% test coverage.

## Continuous Integration

GitHub Actions automatically runs the tests when changes are pushed to the `main` branch or when a pull request is created. The workflow also checks that coverage remains at or above 90%.

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
│   ├── calculation.py
│   ├── calculator.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── command_decorators.py
│   ├── commands.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── logger.py
│   └── operations.py
├── tests/
├── .github/
│   └── workflows/
├── .env
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```