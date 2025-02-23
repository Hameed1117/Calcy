# calculator/__init__.py
import sys
import random
from . import calculator  # Use relative import to access calculator.py

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

class App:
    @staticmethod
    def start() -> None:
        # A list of jokes for the 'joke' command
        jokes = [
            "Why did the math book look sad? Because it had too many problems.",
            "I told a joke about a calculator... It wasn't very calculating.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet."
        ]
        
        # Define the command mapping: command name -> (callable, expected argument count)
        command_map = {
            'add': (lambda a, b: calculator.Calculator.add(float(a), float(b)), 2),
            'subtract': (lambda a, b: calculator.Calculator.subtract(float(a), float(b)), 2),
            'multiply': (lambda a, b: calculator.Calculator.multiply(float(a), float(b)), 2),
            'divide': (lambda a, b: calculator.Calculator.divide(float(a), float(b)), 2),
            'history': (lambda: print("\n".join(str(calc) for calc in calculator.Calculations.get_history())), 0),
            'usage': (lambda: print_usage(), 0),
            'greet': (lambda: print("Hello there! Welcome to the Advanced Calculator!"), 0),
            'joke': (lambda: print(random.choice(jokes)), 0),
            'exit': (lambda: sys.exit(print("Exiting...")), 0)
        }
        # Add the "menu" command to print commands vertically.
        command_map['menu'] = (lambda: print_menu(command_map), 0)
        
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
                func, expected_args = command_map[cmd]
                if len(args) != expected_args:
                    raise TypeError
                result = func(*args)
                if result is not None:
                    print("Result:", result)
            except KeyError:
                print("Unknown command. Type 'menu' for available commands.")
            except TypeError:
                print("Incorrect number of arguments. Please check the command usage.")
            except Exception as e:
                print("Error:", e)
