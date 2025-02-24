# calculator/plugins/joke/__init__.py
import random
from calculator.commands.command import Command

class JokeCommand(Command):
    def __init__(self):
        self.jokes = [
            "Why did the math book look sad? Because it had too many problems.",
            "I told a joke about a calculator... It wasn't very calculating.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet."
        ]
    def execute(self):
        return random.choice(self.jokes)

def get_command():
    return ("joke", JokeCommand(), 0)
