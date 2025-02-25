"""
Module for the 'usage' command plugin.
"""

from calculator.commands.command import Command


def _usage_text():
    """
    Return the usage help text.

    Returns:
        str: Help text describing available commands.
    """
    return (
        "Usage:\n"
        " add: Adds two numbers -> add <num1> <num2>\n"
        " subtract: Subtracts the second number from the first -> subtract <num1> <num2>\n"
        " multiply: Multiplies two numbers -> multiply <num1> <num2>\n"
        " divide: Divides the first number by the second -> divide <num1> <num2>\n"
        " history: Shows calculation history -> history\n"
        " greet: Greets the user -> greet\n"
        " joke: Tells a joke -> joke\n"
        " exit: Exits the application -> exit\n"
        " menu: Displays available commands -> menu\n"
        " usage: Shows this usage help ->usage\n"
    )


class UsageCommand(Command):
    """Command to display usage information."""

    def execute(self, *args):
        """
        Execute the usage command.

        Returns:
            str: The usage help text.
        """
        return _usage_text()


def get_command():
    """
    Returns:
        tuple: A tuple containing the command name, an instance of UsageCommand,
        and the expected number of arguments.
    """
    return ("usage", UsageCommand(), 0)
