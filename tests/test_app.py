"""
Test suite for the Advanced Calculator application.
"""
import os
import sys
import importlib
import logging
import pytest

from calculator import App, load_plugins
from calculator.calculator import Calculations

# Insert the project root directory into sys.path so that our packages are found.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture(autouse=True)
def clear_history():
    """Clear calculation history before and after each test."""
    Calculations.clear_history()
    yield
    Calculations.clear_history()

def run_app_with_inputs(monkeypatch, inputs):
    """
    Helper function to simulate user inputs and run the app.

    Args:
        monkeypatch: pytest monkeypatch fixture.
        inputs (list): List of strings to simulate user input.
    """
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(input_iter))
    with pytest.raises(SystemExit):
        App().start()

def test_greet(monkeypatch, capsys):
    """Test that the greet command returns the proper greeting."""
    run_app_with_inputs(monkeypatch, ["greet", "exit"])
    captured = capsys.readouterr().out
    assert "Hello there! Welcome to the Advanced Calculator!" in captured

def test_add(monkeypatch, capsys):
    """Test the add command."""
    run_app_with_inputs(monkeypatch, ["add 2 3", "exit"])
    captured = capsys.readouterr().out
    assert "Result:" in captured
    assert "5.0" in captured

def test_subtract(monkeypatch, capsys):
    """Test the subtract command."""
    run_app_with_inputs(monkeypatch, ["subtract 5 3", "exit"])
    captured = capsys.readouterr().out
    assert "Result:" in captured
    assert "2.0" in captured or "2" in captured

def test_multiply(monkeypatch, capsys):
    """Test the multiply command."""
    run_app_with_inputs(monkeypatch, ["multiply 2 3", "exit"])
    captured = capsys.readouterr().out
    assert "Result:" in captured
    assert "6.0" in captured

def test_divide(monkeypatch, capsys):
    """Test the divide command."""
    run_app_with_inputs(monkeypatch, ["divide 10 2", "exit"])
    captured = capsys.readouterr().out
    assert "Result:" in captured
    assert "5.0" in captured

def test_invalid_command(monkeypatch, capsys):
    """Test handling of an invalid command."""
    run_app_with_inputs(monkeypatch, ["foobar", "exit"])
    captured = capsys.readouterr().out
    assert "No such command:" in captured

def test_invalid_argument_count(monkeypatch, capsys):
    """Test command execution with invalid argument count."""
    run_app_with_inputs(monkeypatch, ["add 2", "exit"])
    captured = capsys.readouterr().out
    assert "Incorrect number of arguments." in captured

def test_usage(monkeypatch, capsys):
    """Test the usage command."""
    run_app_with_inputs(monkeypatch, ["usage", "exit"])
    captured = capsys.readouterr().out
    assert "Usage:" in captured
    assert "add: Adds two numbers" in captured

def test_menu(monkeypatch, capsys):
    """Test the menu command."""
    run_app_with_inputs(monkeypatch, ["menu", "exit"])
    captured = capsys.readouterr().out
    for cmd in ["add", "subtract", "multiply", "divide", "history", "usage", "greet", "joke", "exit", "menu"]:
        assert f" - {cmd}" in captured

def test_history(monkeypatch, capsys):
    """Test the history command after an addition."""
    run_app_with_inputs(monkeypatch, ["add 2 3", "history", "exit"])
    captured = capsys.readouterr().out
    assert "2.0 + 3.0 = 5.0" in captured

def test_joke(monkeypatch, capsys):
    """Test the joke command."""
    run_app_with_inputs(monkeypatch, ["joke", "exit"])
    captured = capsys.readouterr().out
    jokes = [
        "Why did the math book look sad? Because it had too many problems.",
        "I told a joke about a calculator... It wasn't very calculating.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet."
    ]
    assert any(joke in captured for joke in jokes)

def test_divide_by_zero(monkeypatch, capsys):
    """Test division by zero error handling."""
    run_app_with_inputs(monkeypatch, ["divide 10 0", "exit"])
    captured = capsys.readouterr().out
    assert "Error:" in captured
    assert "divide by zero" in captured.lower() or "cannot divide" in captured.lower()

def test_empty_input(monkeypatch, capsys):
    """Test behavior when input is empty."""
    run_app_with_inputs(monkeypatch, ["", "exit"])
    captured = capsys.readouterr().out
    assert "Welcome to the Advanced Calculator!" in captured

def test_invalid_numeric(monkeypatch, capsys):
    """Test command execution with non-numeric input."""
    run_app_with_inputs(monkeypatch, ["add a b", "exit"])
    captured = capsys.readouterr().out
    assert "Error:" in captured

def test_plugin_load_failure(monkeypatch, caplog):
    """Test plugin load failure scenario."""
    def failing_import_module(name, package=None):
        raise ImportError("Forced failure")
    monkeypatch.setattr(importlib, "import_module", failing_import_module)
    with caplog.at_level(logging.ERROR):
        plugins = load_plugins()
        assert not plugins
        # Check that our log messages contain the error text
        assert "Failed to load plugin" in caplog.text
