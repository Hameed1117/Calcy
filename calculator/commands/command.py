"""
Module defining the abstract Command interface and a CommandHandler.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract base class for commands."""

    @abstractmethod
    def execute(self, *args):
        """Execute the command with the given arguments."""
        raise NotImplementedError


class CommandHandler:
    """
    Handles registration and execution of commands.
    
    Attributes:
        commands (dict): Mapping from command name to a tuple of (command instance, expected_args).
    """

    def __init__(self):
        # Dictionary mapping command name -> (command_instance, expected_args)
        self.commands = {}

    def register_command(self, command_name: str, command: Command, expected_args: int):
        """
        Register a command with its name and expected argument count.
        """
        self.commands[command_name] = (command, expected_args)

    def execute_command(self, command_name: str, *args):
        """
        Execute the command with the given name and arguments.
        
        Returns:
            The result of command execution if the command exists and arguments match;
            Otherwise, returns None.
        """
        try:
            command, expected_args = self.commands[command_name]
            if len(args) != expected_args:
                raise TypeError("Incorrect number of arguments.")
            return command.execute(*args)
        except KeyError:
            print(f"No such command: {command_name}")
            return None
