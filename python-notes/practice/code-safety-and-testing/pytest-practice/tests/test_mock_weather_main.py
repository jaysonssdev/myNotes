import pytest
from src.mock_weather.main import get_weather  

def test_get_weather(mocker):   # this 'mocker' will work because we installed the pytest-mock earlier)
    # Mock requests.get
    mock_get = mocker.patch("src.mock_weather.main.requests.get") # 'main' came from 'main.py', 'requests' came from 'import requests', and 'get' came from '.get{f"https://api....}'

    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

    # Call function
    result = get_weather("Dubai")

    # Assertions
    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")