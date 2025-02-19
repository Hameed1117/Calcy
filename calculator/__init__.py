"""Calculator Module"""
from typing import List
from calculator.operations import Operations
from calculator.calculations import Calculations
from calculator.calculation import Calculation

class Calculator:
    """Calculator Class"""
    @staticmethod
    def add(num1: float, num2: float) -> float:
        """Add two numbers"""
        calculation = Calculation(num1, num2, Operations.add)
        Calculations.add_calculation(calculation)
        return calculation.result
    
    @staticmethod
    def subtract(num1: float, num2: float) -> float:
        """Subtract two numbers"""
        calculation = Calculation(num1, num2, Operations.subtract)
        Calculations.add_calculation(calculation)
        return calculation.result
    
    @staticmethod
    def multiply(num1: float, num2: float) -> float:
        """Multiply two numbers"""
        calculation = Calculation(num1, num2, Operations.multiply)
        Calculations.add_calculation(calculation)
        return calculation.result
    
    @staticmethod
    def divide(num1: float, num2: float) -> float:
        """Divide two numbers"""
        calculation = Calculation(num1, num2, Operations.divide)
        Calculations.add_calculation(calculation)
        return calculation.result
    