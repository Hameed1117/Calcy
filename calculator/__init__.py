# calculator/__init__.py
import sys
import random
from . import calculator

def print_menu(command_map):
    """Print available commands vertically."""
    print("Available commands:")
    for cmd in command_map:
        print(f" - {cmd}")

def print_usage():
    """Print detailed usage information for each command."""
    usage_info = [
        "add: Adds two numbers. Usage: add <num1> <num2>",
        "subtract: Subtracts the second number from the first. Usage: subtract <num1> <num2>",
        "multiply: Multiplies two numbers. Usage: multiply <num1> <num2>",
        "divide: Divides the first number by the second. Usage: divide <num1> <num2>",
        "history: Displays all past calculations. Usage: history",
        "menu: Displays the list of available commands. Usage: menu",
        "usage: Displays detailed command usage information. Usage: usage",
        "greet: Greets the user. Usage: greet",
        "joke: Tells a random joke. Usage: joke",
        "exit: Exits the application. Usage: exit"
    ]
    print("\n".join(usage_info))

# Abstract Command class
class Command:
    def execute(self, *args):
        raise NotImplementedError("Subclasses must implement this method.")

# Command implementations
class AddCommand(Command):
    def execute(self, a, b):
        return calculator.Calculator.add(float(a), float(b))

class SubtractCommand(Command):
    def execute(self, a, b):
        return calculator.Calculator.subtract(float(a), float(b))

class MultiplyCommand(Command):
    def execute(self, a, b):
        return calculator.Calculator.multiply(float(a), float(b))

class DivideCommand(Command):
    def execute(self, a, b):
        return calculator.Calculator.divide(float(a), float(b))

class HistoryCommand(Command):
    def execute(self):
        print("\n".join(str(calc) for calc in calculator.Calculations.get_history()))

class UsageCommand(Command):
    def execute(self):
        print_usage()

class GreetCommand(Command):
    def execute(self):
        print("Hello there! Welcome to the Advanced Calculator!")

class JokeCommand(Command):
    def __init__(self):
        self.jokes = [
            "Why did the math book look sad? Because it had too many problems.",
            "I told a joke about a calculator... It wasn't very calculating.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet."
        ]
    def execute(self):
        print(random.choice(self.jokes))

class ExitCommand(Command):
    def execute(self):
        sys.exit(print("Exiting..."))

class MenuCommand(Command):
    def __init__(self, command_map):
        self.command_map = command_map
    def execute(self):
        print_menu(self.command_map)

# The App class remains the entry point.
class App:
    @staticmethod
    def start() -> None:
        # Build the command mapping: command name -> (Command instance, expected number of arguments)
        command_map = {
            'add': (AddCommand(), 2),
            'subtract': (SubtractCommand(), 2),
            'multiply': (MultiplyCommand(), 2),
            'divide': (DivideCommand(), 2),
            'history': (HistoryCommand(), 0),
            'usage': (UsageCommand(), 0),
            'greet': (GreetCommand(), 0),
            'joke': (JokeCommand(), 0),
            'exit': (ExitCommand(), 0)
        }
        # Menu command depends on the command_map, so add it afterward.
        command_map['menu'] = (MenuCommand(command_map), 0)
        
        print("Welcome to the Advanced Calculator!")
        print("Type 'menu' to display available commands.")
        
        while True:
            try:
                user_input = input(">>> ").strip()
                if not user_input:
                    continue
                parts = user_input.split()
                cmd = parts[0]
                args = parts[1:]
                # Look up the command; this follows EAFP style.
                command, expected_args = command_map[cmd]
                if len(args) != expected_args:
                    raise TypeError("Incorrect number of arguments.")
                result = command.execute(*args)
                if result is not None:
                    print("Result:", result)
            except KeyError:
                print("Unknown command. Type 'menu' for available commands.")
            except TypeError:
                print("Incorrect number of arguments. Please check the command usage.")
            except Exception as e:
                print("Error:", e)
