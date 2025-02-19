"""
Advanced Calculator Module
This module provides a calculator with history tracking.
"""
from typing import List  # Removed unused Tuple import

class Calculation:
    """Represents a single arithmetic operation"""
    def __init__(self, operand_one: float, operand_two: float, operation: str, result: float) -> None:
        self.operand_one = operand_one
        self.operand_two = operand_two
        self.operation = operation
        self.result = result

    def __str__(self) -> str:
        """Returns a string representation of the calculation"""
        return f"{self.operand_one} {self.operation} {self.operand_two} = {self.result}"


class Calculations:
    """Manages history of calculations"""
    _history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        """Adds a new calculation to history"""
        cls._history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Returns the history of calculations"""
        return cls._history

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Returns the most recent calculation"""
        return cls._history[-1] if cls._history else None

    @classmethod
    def clear_history(cls) -> None:
        """Clears the history of calculations"""
        cls._history.clear()


class Calculator:
    """Calculator class that performs arithmetic operations"""

    @staticmethod
    def add(num_one: float, num_two: float) -> float:
        """Returns the sum of two numbers"""
        result = num_one + num_two
        Calculations.add_calculation(Calculation(num_one, num_two, "+", result))
        return result

    @staticmethod
    def subtract(num_one: float, num_two: float) -> float:
        """Returns the difference between two numbers"""
        result = num_one - num_two
        Calculations.add_calculation(Calculation(num_one, num_two, "-", result))
        return result

    @staticmethod
    def multiply(num_one: float, num_two: float) -> float:
        """Returns the product of two numbers"""
        result = num_one * num_two
        Calculations.add_calculation(Calculation(num_one, num_two, "*", result))
        return result

    @staticmethod
    def divide(num_one: float, num_two: float) -> float:
        """Returns the quotient of two numbers, raises ZeroDivisionError if denominator is zero"""
        if num_two == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = num_one / num_two
        Calculations.add_calculation(Calculation(num_one, num_two, "/", result))
        return result
