# calculator/plugins/exit/__init__.py
import sys
from calculator.commands.command import Command

class ExitCommand(Command):
    def execute(self):
        sys.exit("Exiting...")

def get_command():
    return ("exit", ExitCommand(), 0)
