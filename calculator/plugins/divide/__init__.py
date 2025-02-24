# calculator/plugins/divide/__init__.py
from calculator.commands.command import Command
from calculator.calculator import Calculator

class DivideCommand(Command):
    def execute(self, a, b):
        return Calculator.divide(float(a), float(b))

def get_command():
    return ("divide", DivideCommand(), 2)
