# calculator/plugins/usage/__init__.py
from calculator.commands.command import Command

def print_usage():
    usage_info = [
        "add: Adds two numbers. Usage: add <num1> <num2>",
        "subtract: Subtracts the second number from the first. Usage: subtract <num1> <num2>",
        "multiply: Multiplies two numbers. Usage: multiply <num1> <num2>",
        "divide: Divides the first number by the second. Usage: divide <num1> <num2>",
        "history: Displays all past calculations. Usage: history",
        "usage: Displays detailed command usage information. Usage: usage",
        "greet: Greets the user. Usage: greet",
        "joke: Tells a random joke. Usage: joke",
        "exit: Exits the application. Usage: exit",
        "menu: Displays the list of available commands. Usage: menu"
    ]
    return "\n".join(usage_info)

class UsageCommand(Command):
    def execute(self):
        return print_usage()

def get_command():
    return ("usage", UsageCommand(), 0)
