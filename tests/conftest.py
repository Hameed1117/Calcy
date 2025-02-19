"""
Pytest configuration file to enable `pytest --num_records=N` for test data generation.
"""
from tests.faker_generator import generate_fake_number, generate_fake_operation
from calculator.calculator import Calculator

def pytest_addoption(parser):
    """Add command-line option to generate N test cases."""
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test cases to generate")

def generate_test_data(num_records):
    """Generate test data dynamically based on --num_records argument."""
    test_data = []
    for _ in range(num_records):
        num_one = generate_fake_number()
        num_two = generate_fake_number() if generate_fake_operation() != "divide" else generate_fake_number() + 1
        operation = generate_fake_operation()
        expected = getattr(Calculator, operation)(num_one, num_two)
        test_data.append((operation, num_one, num_two, expected))
    return test_data

def pytest_generate_tests(metafunc):
    """Dynamically generate test cases using Faker when --num_records is passed."""
    if "operation" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        test_data = generate_test_data(num_records)
        metafunc.parametrize("operation, num_one, num_two, expected", test_data)
