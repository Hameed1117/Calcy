"""
Module for the 'subtract' command plugin.
"""

from calculator.commands.command import Command
from calculator.calculator import Calculator


class SubtractCommand(Command):
    """Command to perform subtraction using the Calculator."""

    def execute(self, *args):
        """
        Execute the subtract command.

        Args:
            *args: Two arguments representing the numbers to subtract.

        Returns:
            float: The result of subtracting the second argument from the first.

        Raises:
            ValueError: If the number of arguments is not exactly two.
        """
        if len(args) != 2:
            raise ValueError("SubtractCommand requires exactly 2 arguments.")
        a, b = args
        return Calculator.subtract(float(a), float(b))


def get_command():
    """
    Returns:
        tuple: A tuple containing the command name, an instance of SubtractCommand,
        and the expected number of arguments.
    """
    return ("subtract", SubtractCommand(), 2)
