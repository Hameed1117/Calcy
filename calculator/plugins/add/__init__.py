# calculator/plugins/add/__init__.py
from calculator.commands.command import Command
from calculator.calculator import Calculator

class AddCommand(Command):
    def execute(self, a, b):
        return Calculator.add(float(a), float(b))

def get_command():
    # (command_name, command_instance, expected_args)
    return ("add", AddCommand(), 2)
