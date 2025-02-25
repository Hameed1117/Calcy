"""
Module for initializing the Advanced Calculator application,
loading plugins, and running the interactive command loop.
"""

import os
import pkgutil
import importlib
from .commands.command import CommandHandler


def load_plugins():
    """
    Load all command plugins from the 'plugins' directory.
    Each plugin should be in its own subfolder (with an __init__.py)
    and define a get_command() function that returns:
        (command_name, command_instance, expected_args)

    Returns:
        dict: A mapping of command names to (command_instance, expected_args).
    """
    command_map = {}
    base_path = os.path.dirname(__file__)
    plugins_path = os.path.join(base_path, "plugins")
    if not os.path.isdir(plugins_path):
        return command_map
    for _, plugin_name, ispkg in pkgutil.iter_modules([plugins_path]):
        if ispkg:
            try:
                module = importlib.import_module(f"calculator.plugins.{plugin_name}")
                if hasattr(module, "get_command"):
                    cmd_tuple = module.get_command()  # (name, instance, expected_args)
                    command_name, command_instance, expected_args = cmd_tuple
                    command_map[command_name] = (command_instance, expected_args)
            except Exception as e:  # pylint: disable=broad-exception-caught
                print(f"Failed to load plugin {plugin_name}: {e}")
    return command_map


def print_menu(command_map):
    """
    Print available commands vertically.

    Args:
        command_map (dict): Mapping of command names to command details.
    """
    print("Available commands:")
    for cmd in command_map:
        print(f" - {cmd}")


class App:
    """Application class for the Advanced Calculator."""

    def __init__(self):
        """Initialize the App by loading and registering plugins."""
        self.command_handler = CommandHandler()
        # Load plugins and register each command with its expected argument count.
        plugins = load_plugins()  # returns dict mapping command name -> (command_instance, expected_args)
        for name, (cmd_instance, expected_args) in plugins.items():
            self.command_handler.register_command(name, cmd_instance, expected_args)

    def start(self):
        """
        Start the interactive command loop.
        
        Continuously reads user input and executes corresponding commands.
        """
        print("Welcome to the Advanced Calculator!")
        print("Type 'menu' to display available commands.")
        # If no plugin provides a 'menu' command, register a built-in one.
        if "menu" not in self.command_handler.commands:
            class MenuCommand:
                """Built-in command to display the menu of available commands."""

                def __init__(self, command_map):
                    """
                    Initialize the MenuCommand.
                    
                    Args:
                        command_map (dict): Mapping of command names to command details.
                    """
                    self.command_map = command_map

                def execute(self, *args):
                    """Execute the command to print the available commands."""
                    print_menu(self.command_map)

            self.command_handler.register_command("menu", MenuCommand(self.command_handler.commands), 0)
        while True:
            try:
                user_input = input(">>> ").strip()
                if not user_input:
                    continue
                parts = user_input.split()
                cmd = parts[0]
                args = parts[1:]
                result = self.command_handler.execute_command(cmd, *args)
                if result is not None:
                    print("Result:", result)
            except Exception as e:  # pylint: disable=broad-exception-caught
                print("Error:", e)
