"""
Module for the 'joke' command plugin.
"""

import random
from calculator.commands.command import Command


class JokeCommand(Command):
    """Command to return a random joke."""

    def __init__(self):
        """Initialize JokeCommand with a list of jokes."""
        self.jokes = [
            "Why did the math book look sad? Because it had too many problems.",
            "I told a joke about a calculator... It wasn't very calculating.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet."
        ]

    def execute(self, *args):
        """
        Execute the joke command.

        Returns:
            str: A random joke.
        """
        return random.choice(self.jokes)


def get_command():
    """
    Returns:
        tuple: A tuple containing the command name, an instance of JokeCommand,
        and the expected number of arguments.
    """
    return ("joke", JokeCommand(), 0)
