# calculator/plugins/subtract/__init__.py
from calculator.commands.command import Command
from calculator.calculator import Calculator

class SubtractCommand(Command):
    def execute(self, a, b):
        return Calculator.subtract(float(a), float(b))

def get_command():
    return ("subtract", SubtractCommand(), 2)
