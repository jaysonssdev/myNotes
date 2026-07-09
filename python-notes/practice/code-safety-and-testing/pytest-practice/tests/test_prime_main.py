# Import the pytest library, which is a testing framework for Python
import pytest

# Import the 'is_prime' function from the main module in the src/prime directory
from src.prime.main import is_prime


# Test function for the 'is_prime' function
# The @pytest.mark.parametrize decorator is used to define a parameterized test
# The first argument is the name of the test function
# The second argument is a list of tuples, where each tuple contains the arguments to be passed to the test function
# The third argument is the name of the test function, which is defined below
@pytest.mark.parametrize("number, expected", [
(1, False), (2, True), (3, True), (4, False), (5, True), (6, False), (7, True), (8, False), (9, False), (10, False)])
def test_is_prime(number, expected):
    # Call the 'is_prime' function with the given 'number' argument
    result = is_prime(number)
    # Assert that the result is equal to the expected value
    assert result == expected
