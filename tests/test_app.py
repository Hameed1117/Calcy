import sys
import os
import pytest
import importlib  # needed for our monkeypatch in the new test

# Insert the project root directory into sys.path so that our packages are found.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import App, load_plugins
from calculator.calculator import Calculations

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
    with pytest.raises(SystemExit):
        App().start()

def test_greet(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["greet", "exit"])
    captured = capsys.readouterr().out
    assert "Hello there! Welcome to the Advanced Calculator!" in captured

def test_add(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["add 2 3", "exit"])
    captured = capsys.readouterr().out
    assert "Result:" in captured
    assert "5.0" in captured

def test_subtract(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["subtract 5 3", "exit"])
    captured = capsys.readouterr().out
    assert "Result:" in captured
    assert "2.0" in captured or "2" in captured

def test_multiply(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["multiply 2 3", "exit"])
    captured = capsys.readouterr().out
    assert "Result:" in captured
    assert "6.0" in captured

def test_divide(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["divide 10 2", "exit"])
    captured = capsys.readouterr().out
    assert "Result:" in captured
    assert "5.0" in captured

def test_invalid_command(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["foobar", "exit"])
    captured = capsys.readouterr().out
    assert "No such command:" in captured

def test_invalid_argument_count(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["add 2", "exit"])
    captured = capsys.readouterr().out
    assert "Incorrect number of arguments." in captured

def test_usage(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["usage", "exit"])
    captured = capsys.readouterr().out
    assert "Usage:" in captured
    assert "add: Adds two numbers" in captured
    assert "subtract:" in captured

def test_menu(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["menu", "exit"])
    captured = capsys.readouterr().out
    for cmd in ["add", "subtract", "multiply", "divide", "history", "usage", "greet", "joke", "exit", "menu"]:
        assert f" - {cmd}" in captured

def test_history(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["add 2 3", "history", "exit"])
    captured = capsys.readouterr().out
    assert "2.0 + 3.0 = 5.0" in captured

def test_joke(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["joke", "exit"])
    captured = capsys.readouterr().out
    jokes = [
        "Why did the math book look sad? Because it had too many problems.",
        "I told a joke about a calculator... It wasn't very calculating.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet."
    ]
    assert any(joke in captured for joke in jokes)

def test_divide_by_zero(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["divide 10 0", "exit"])
    captured = capsys.readouterr().out
    assert "Error:" in captured
    assert "divide by zero" in captured.lower() or "cannot divide" in captured.lower()

def test_empty_input(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["", "exit"])
    captured = capsys.readouterr().out
    assert "Welcome to the Advanced Calculator!" in captured

def test_invalid_numeric(monkeypatch, capsys):
    run_app_with_inputs(monkeypatch, ["add a b", "exit"])
    captured = capsys.readouterr().out
    assert "Error:" in captured

def test_plugin_load_failure(monkeypatch, capsys):
    # Force import_module to always fail to load a plugin.
    def failing_import_module(name, package=None):
        raise Exception("Forced failure")
    monkeypatch.setattr(importlib, "import_module", failing_import_module)
    from calculator import load_plugins
    plugins = load_plugins()
    assert plugins == {}
    output = capsys.readouterr().out
    assert "Failed to load plugin" in output
