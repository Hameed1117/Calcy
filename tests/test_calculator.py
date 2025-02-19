"""
Test cases for the advanced calculator module
"""
import pytest
from calculator.calculator import Calculator, Calculations

@pytest.fixture
def clear_calculations():
    """Fixture to clear calculation history before and after tests"""
    Calculations.clear_history()
    yield
    Calculations.clear_history()

@pytest.mark.parametrize("num_one, num_two, expected", [
    (3, 2, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(clear_calculations, num_one, num_two, expected):
    """Test addition operation"""
    assert Calculator.add(num_one, num_two) == expected

@pytest.mark.parametrize("num_one, num_two, expected", [
    (3, 2, 1),
    (-1, -1, 0),
    (0, 5, -5)
])
def test_subtract(clear_calculations, num_one, num_two, expected):
    """Test subtraction operation"""
    assert Calculator.subtract(num_one, num_two) == expected

@pytest.mark.parametrize("num_one, num_two, expected", [
    (3, 2, 6),
    (-1, 2, -2),
    (0, 5, 0)
])
def test_multiply(clear_calculations, num_one, num_two, expected):
    """Test multiplication operation"""
    assert Calculator.multiply(num_one, num_two) == expected

@pytest.mark.parametrize("num_one, num_two, expected", [
    (10, 2, 5),
    (-6, 3, -2),
    (5, 2, 2.5)
])
def test_divide(clear_calculations, num_one, num_two, expected):
    """Test division operation"""
    assert Calculator.divide(num_one, num_two) == expected

def test_divide_by_zero(clear_calculations):
    """Test division by zero throws an exception"""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)

def test_calculation_history(clear_calculations):
    """Test calculation history stores operations correctly"""
    Calculator.add(1, 1)
    Calculator.subtract(2, 1)
    Calculator.multiply(2, 3)
    Calculator.divide(8, 4)

    history = Calculations.get_history()
    assert len(history) == 4
    assert str(Calculations.get_last_calculation()) == "8 / 4 = 2.0"

def test_clear_history(clear_calculations):
    """Test clearing the calculation history"""
    Calculator.add(1, 1)
    assert len(Calculations.get_history()) == 1
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0
