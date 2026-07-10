import pytest
import requests

def test_get_api(mocker):
    # 1. Patch requests.get using the native mocker fixture
    mock_get = mocker.patch("requests.get")

    # 2. Configure the nested mock response return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "data": [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
    }

    # 3. Call the function under test
    result = requests.get("https://typicode.com")

    # 4. Assertions
    assert result.status_code == 200
    assert result.json() == {"data": [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]}
    
    # Optional: Verify that requests.get was actually called correctly
    mock_get.assert_called_once_with("https://typicode.com")
