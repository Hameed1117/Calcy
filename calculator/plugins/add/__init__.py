"""
Module for the 'add' command plugin.
"""

from calculator.commands.command import Command
from calculator.calculator import Calculator


class AddCommand(Command):
    """Command to perform addition using the Calculator."""

    def execute(self, *args):
        """
        Execute the add command.

        Args:
            *args: Two arguments representing the numbers to add.

        Returns:
            float: The result of adding the two numbers.

        Raises:
            ValueError: If the number of arguments is not exactly two.
        """
        if len(args) != 2:
            raise ValueError("AddCommand requires exactly 2 arguments.")
        a, b = args
        return Calculator.add(float(a), float(b))


def get_command():
    """
    Returns:
        tuple: A tuple containing the command name, an instance of AddCommand,
        and the expected number of arguments.
    """
    return ("add", AddCommand(), 2)
