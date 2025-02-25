"""
Module for the 'greet' command plugin.
"""

from calculator.commands.command import Command


class GreetCommand(Command):
    """Command to greet the user."""

    def execute(self, *args):
        """
        Execute the greet command.

        Returns:
            str: Greeting message.
        """
        return "Hello there! Welcome to the Advanced Calculator!"


def get_command():
    """
    Returns:
        tuple: A tuple containing the command name, an instance of GreetCommand,
        and the expected number of arguments.
    """
    return ("greet", GreetCommand(), 0)
