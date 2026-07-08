# Import the 'add' function from the 'main' module.
# This allows us to use the 'add' function in our tests.
from src.add.main import add


# Define a test function for the 'add' function.
# Pytest discovers test functions if their name starts with 'test_'.
def test_add_positive_numbers():
    # Call the 'add' function with positive integers 1 and 2.
    # The expected result is 3.
    result = add(1, 2)
    # Assert that the 'result' is equal to the expected value (3).
    # If the assertion fails, pytest will report a test failure.
    assert result == 3


# Define another test function for adding zero to a number.
def test_add_zero():
    # Call the 'add' function with 5 and 0.
    # The expected result is 5.
    result = add(5, 0)
    # Assert that the 'result' is equal to the expected value (5).
    assert result == 5


# Define a test function for adding negative numbers.
def test_add_negative_numbers():
    # Call the 'add' function with -1 and -1.
    # The expected result is -2.
    result = add(-1, -1)
    # Assert that the 'result' is equal to the expected value (-2).
    assert result == -2


# Define a test function for adding a positive and a negative number.
def test_add_positive_and_negative():
    # Call the 'add' function with 10 and -5.
    # The expected result is 5.
    result = add(10, -5)
    # Assert that the 'result' is equal to the expected value (5).
    assert result == 5
