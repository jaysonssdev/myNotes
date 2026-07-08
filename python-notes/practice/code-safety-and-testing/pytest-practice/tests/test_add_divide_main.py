# Import the pytest library, which is a testing framework for Python
import pytest

# Import the functions to be tested from the main module in the src/add-divide directory
from src.add_divide.main import add, divide


# Test function for the 'add' function
def test_add():
    # Assert that 1 + 2 equals 3, verifying the basic addition functionality
    assert add(1, 2) == 3
    # Assert that 0 + 0 equals 0, checking edge case with zeros
    assert add(0, 0) == 0
    # Assert that -1 + 1 equals 0, verifying addition with negative numbers
    assert add(-1, 1) == 0
    # Assert that -1 + -1 equals -2, checking addition of two negative numbers
    assert add(-1, -1) == -2


# Test function for the 'divide' function
def test_divide():
    # Assert that 6 divided by 3 equals 2, verifying basic division
    assert divide(6, 3) == 2
    # Assert that 5 divided by 2 equals 2.5, checking division with float result
    assert divide(5, 2) == 2.5
    # Assert that 0 divided by 1 equals 0, checking division where numerator is zero
    assert divide(0, 1) == 0


# Test function for the 'divide' function to check for ValueError when dividing by zero
def test_divide_by_zero():
    # Use pytest.raises to check if a ValueError is raised when dividing by zero
    with pytest.raises(ValueError):
        # Attempt to divide by zero, which should trigger the ValueError
        divide(1, 0)
