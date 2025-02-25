"""
Module for the 'multiply' command plugin.
"""

from calculator.commands.command import Command
from calculator.calculator import Calculator


class MultiplyCommand(Command):
    """Command to perform multiplication using the Calculator."""

    def execute(self, *args):
        """
        Execute the multiply command.

        Args:
            *args: Two arguments representing the numbers to multiply.

        Returns:
            float: The product of the two numbers.

        Raises:
            ValueError: If the number of arguments is not exactly two.
        """
        if len(args) != 2:
            raise ValueError("MultiplyCommand requires exactly 2 arguments.")
        a, b = args
        return Calculator.multiply(float(a), float(b))


def get_command():
    """
    Returns:
        tuple: A tuple containing the command name, an instance of MultiplyCommand,
        and the expected number of arguments.
    """
    return ("multiply", MultiplyCommand(), 2)
