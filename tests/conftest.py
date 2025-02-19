"""
Pytest configuration file to enable `pytest --num_records=N` for test data generation.
"""
import pytest
from tests.faker_generator import generate_fake_number, generate_fake_operation
from calculator.calculator import Calculator

def pytest_addoption(parser):
    """Add command-line option to generate N test cases."""
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test cases to generate")

@pytest.fixture(scope="session")
def generate_test_data(request):
    """Generate test data based on --num_records argument."""
    num_records = request.config.getoption("--num_records")
    test_data = []
    for _ in range(num_records):
        num_one = generate_fake_number()
        num_two = generate_fake_number() if generate_fake_operation() != "divide" else generate_fake_number() + 1
        operation = generate_fake_operation()
        expected = getattr(Calculator, operation)(num_one, num_two)
        test_data.append((operation, num_one, num_two, expected))
    return test_data
