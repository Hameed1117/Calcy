"""
Main entry point for the calculator CLI.
Handles user input and exception handling.
"""
import sys
from calculator.calculator import Calculator

def main():
    """Main function to handle user input."""
    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage: python main.py <num1> <num2> <operation>")
        
        num_one, num_two, operation = sys.argv[1], sys.argv[2], sys.argv[3]

        try:
            num_one = float(num_one)
            num_two = float(num_two)
        except ValueError:
            print(f"Invalid number input: {num_one} or {num_two} is not a valid number.")
            return
        
        if operation not in ["add", "subtract", "multiply", "divide"]:
            print(f"Unknown operation: {operation}")
            return
        
        if operation == "divide" and num_two == 0:
            print("An error occurred: Cannot divide by zero")
            return

        result = getattr(Calculator, operation)(num_one, num_two)
        print(f"The result of {num_one} {operation} {num_two} is equal to {result}")

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
