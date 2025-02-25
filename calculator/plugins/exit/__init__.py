"""
Module for the 'exit' command plugin.
"""

import sys
from calculator.commands.command import Command


class ExitCommand(Command):
    """Command to exit the application."""

    def execute(self, *args):
        """
        Execute the exit command.

        Exits the application.
        """
        sys.exit("Exiting...")


def get_command():
    """
    Returns:
        tuple: A tuple containing the command name, an instance of ExitCommand,
        and the expected number of arguments.
    """
    return ("exit", ExitCommand(), 0)
