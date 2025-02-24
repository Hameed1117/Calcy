# calculator/__init__.py
import sys
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
    """
    command_map = {}
    base_path = os.path.dirname(__file__)
    plugins_path = os.path.join(base_path, "plugins")
    if not os.path.isdir(plugins_path):
        return command_map
    for finder, plugin_name, ispkg in pkgutil.iter_modules([plugins_path]):
        if ispkg:
            try:
                module = importlib.import_module(f"calculator.plugins.{plugin_name}")
                if hasattr(module, "get_command"):
                    cmd_tuple = module.get_command()  # (name, instance, expected_args)
                    command_name, command_instance, _ = cmd_tuple  # We don't enforce arg count here
                    command_map[command_name] = command_instance
            except Exception as e:
                print(f"Failed to load plugin {plugin_name}: {e}")
    return command_map

def print_menu(command_map):
    """Print available commands vertically."""
    print("Available commands:")
    for cmd in command_map:
        print(f" - {cmd}")

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        # Load plugins and register each command with the handler.
        plugins = load_plugins()
        for name, cmd_instance in plugins.items():
            self.command_handler.register_command(name, cmd_instance)

    def start(self):
        print("Welcome to the Advanced Calculator!")
        print("Type 'menu' to display available commands.")
        # Add a built-in 'menu' command if not provided by plugins:
        self.command_handler.register_command("menu", MenuCommand(self.command_handler.commands))
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
            except Exception as e:
                print("Error:", e)

# A simple built-in menu command implemented as a plugin fallback.
class MenuCommand:
    def __init__(self, command_map):
        self.command_map = command_map

    def execute(self, *args):
        print_menu(self.command_map)
