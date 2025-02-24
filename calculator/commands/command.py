# calculator/commands/command.py
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        # Dictionary mapping command name -> (command_instance, expected_args)
        self.commands = {}

    def register_command(self, command_name: str, command: Command, expected_args: int):
        self.commands[command_name] = (command, expected_args)

    def execute_command(self, command_name: str, *args):
        try:
            command, expected_args = self.commands[command_name]
            if len(args) != expected_args:
                raise TypeError("Incorrect number of arguments.")
            return command.execute(*args)
        except KeyError:
            print(f"No such command: {command_name}")
