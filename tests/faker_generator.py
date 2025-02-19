"""
Module to generate fake test data using the Faker library.
"""
from faker import Faker

fake = Faker()

def generate_fake_number() -> int:
    """Generate a random integer between 1 and 100."""
    return fake.random_int(min=1, max=100)

def generate_fake_operation() -> str:
    """Randomly select a valid arithmetic operation."""
    return fake.random_element(elements=["add", "subtract", "multiply", "divide"])
