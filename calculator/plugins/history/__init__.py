"""
Module for the 'history' command plugin.
"""

from calculator.commands.command import Command
from calculator.calculator import Calculations


class HistoryCommand(Command):
    """Command to display the history of calculations."""

    def execute(self, *args):
        """
        Execute the history command.

        Returns:
            str: A newline-separated string of all past calculations.
        """
        return "\n".join(str(calc) for calc in Calculations.get_history())


def get_command():
    """
    Returns:
        tuple: A tuple containing the command name, an instance of HistoryCommand,
        and the expected number of arguments.
    """
    return ("history", HistoryCommand(), 0)
