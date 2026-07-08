# Import the function to be tested from the main module.
from src.weather.main import get_weather


# Define a test function for the 'get_weather' function.
# Test functions in pytest should start with 'test_'.
def test_get_weather_hot():
    # Call the 'get_weather' function with a temperature greater than 20.
    result = get_weather(25)
    # Assert that the result is "hot", as expected for temperatures above 20.
    assert result == "hot"


# Define another test function for the 'get_weather' function.
def test_get_weather_cold():
    # Call the 'get_weather' function with a temperature less than or equal to 20.
    result = get_weather(15)
    # Assert that the result is "cold", as expected for temperatures 20 or below.
    assert result == "cold"


# Define a test case for the boundary condition (temperature exactly 20).
def test_get_weather_boundary():
    # Call the 'get_weather' function with a temperature of exactly 20.
    result = get_weather(20)
    # Assert that the result is "cold", as per the function's logic (<= 20 is "cold").
    assert result == "cold"
