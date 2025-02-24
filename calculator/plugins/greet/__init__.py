# calculator/plugins/greet/__init__.py
from calculator.commands.command import Command

class GreetCommand(Command):
    def execute(self):
        return "Hello there! Welcome to the Advanced Calculator!"

def get_command():
    return ("greet", GreetCommand(), 0)
