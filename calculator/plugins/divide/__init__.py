"""
Module for the 'divide' command plugin.
"""

from calculator.commands.command import Command
from calculator.calculator import Calculator


class DivideCommand(Command):
    """Command to perform division using the Calculator."""

    def execute(self, *args):
        """
        Execute the divide command.

        Args:
            *args: Two arguments representing the dividend and divisor.

        Returns:
            float: The result of dividing the first argument by the second.

        Raises:
            ValueError: If the number of arguments is not exactly two.
        """
        if len(args) != 2:
            raise ValueError("DivideCommand requires exactly 2 arguments.")
        a, b = args
        return Calculator.divide(float(a), float(b))


def get_command():
    """
    Returns:
        tuple: A tuple containing the command name, an instance of DivideCommand,
        and the expected number of arguments.
    """
    return ("divide", DivideCommand(), 2)
