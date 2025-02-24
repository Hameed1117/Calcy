# calculator/plugins/history/__init__.py
from calculator.commands.command import Command
from calculator.calculator import Calculations

class HistoryCommand(Command):
    def execute(self):
        return "\n".join(str(calc) for calc in Calculations.get_history())

def get_command():
    return ("history", HistoryCommand(), 0)
