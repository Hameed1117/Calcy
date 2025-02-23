# tests/test_app.py
import sys
import os

# Insert the project root directory into sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from calculator import App
from calculator.calculator import Calculations

# Ensure history is cleared before and after tests.
@pytest.fixture(autouse=True)
def clear_history():
    Calculations.clear_history()
    yield
    Calculations.clear_history()

def run_app_with_inputs(monkeypatch, inputs):
    """
    Helper to run App.start() with simulated inputs.
    'inputs' is a list of strings that simulate successive user inputs.
    """
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(input_iter))
    # Since 'exit' calls sys.exit(), we expect SystemExit.
    with pytest.raises(SystemExit):
        App.start()

def test_greet(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["greet", "exit"])
    captured = capsys.readouterr().out
    assert "Hello there! Welcome to the Advanced Calculator!" in captured

def test_add(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["add 2 3", "exit"])
    captured = capsys.readouterr().out
    # Calculator.add(2,3) returns 5.0 so output should include that
    assert "Result:" in captured
    assert "5.0" in captured

def test_invalid_command(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["foobar", "exit"])
    captured = capsys.readouterr().out
    assert "Unknown command" in captured

def test_invalid_argument_count(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["add 2", "exit"])
    captured = capsys.readouterr().out
    assert "Incorrect number of arguments" in captured

def test_usage(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["usage", "exit"])
    captured = capsys.readouterr().out
    # Check for detailed usage information
    assert "Usage:" in captured
    assert "add: Adds two numbers" in captured
    assert "subtract:" in captured

def test_menu(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["menu", "exit"])
    captured = capsys.readouterr().out
    # Check for each command listed in the menu
    for cmd in ["add", "subtract", "multiply", "divide", "history", "usage", "greet", "joke", "exit", "menu"]:
        assert f" - {cmd}" in captured

def test_history(monkeypatch, capsys):
    # First, perform a calculation so that history is populated.
    run_app_with_inputs(monkeypatch, ["add 2 3", "history", "exit"])
    captured = capsys.readouterr().out
    # The history should show the calculation "2.0 + 3.0 = 5.0"
    assert "2.0 + 3.0 = 5.0" in captured

def test_joke(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["joke", "exit"])
    captured = capsys.readouterr().out
    # Check that one of the predefined jokes is printed.
    jokes = [
        "Why did the math book look sad? Because it had too many problems.",
        "I told a joke about a calculator... It wasn't very calculating.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet."
    ]
    assert any(joke in captured for joke in jokes)

def test_divide_by_zero(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["divide 10 0", "exit"])
    captured = capsys.readouterr().out
    # Division by zero should trigger an error message.
    assert "Error:" in captured
    assert "divide by zero" in captured.lower() or "cannot divide" in captured.lower()

def test_empty_input(monkeypatch, capsys):
    # Test that empty input doesn't crash the app.
    run_app_with_inputs(monkeypatch, ["", "exit"])
    captured = capsys.readouterr().out
    # The welcome message should still be displayed.
    assert "Welcome to the Advanced Calculator!" in captured

def test_invalid_numeric(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["add a b", "exit"])
    captured = capsys.readouterr().out
    # Non-numeric values should trigger an error message.
    assert "Error:" in captured
