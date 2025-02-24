# calculator/plugins/multiply/__init__.py
from calculator.commands.command import Command
from calculator.calculator import Calculator

class MultiplyCommand(Command):
    def execute(self, a, b):
        return Calculator.multiply(float(a), float(b))

def get_command():
    return ("multiply", MultiplyCommand(), 2)
