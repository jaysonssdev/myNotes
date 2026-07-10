# create a pytest for the 'save_user' function from 'src/mock_database/main.py'
# use mocker for the database
from src.mock_database.main import save_user


def test_save_user(mocker):
    # mock the sqlite3.connect function so we can pretend to connect to the database
    mock_connect = mocker.patch("src.mock_database.main.sqlite3.connect")
    # create a mock database connection object
    mock_conn = mock_connect.return_value
    # create a mock cursor object
    mock_cursor = mock_conn.cursor.return_value
    
    # call the 'save_user' function with some test data
    save_user("test_user", 25)
    
    # assert that the connect function was called with the correct arguments
    mock_connect.assert_called_once_with("users.db")
    # assert that the cursor was created on the mock connection
    mock_conn.cursor.assert_called_once()
    # assert that the cursor execute function was called with the correct SQL statement and arguments
    mock_cursor.execute.assert_called_once_with("INSERT INTO users (name, age) VALUES (?, ?)", ("test_user", 25))
    # assert that the commit function was called on the mock connection
    mock_conn.commit.assert_called_once()
    # assert that the close function was called on the mock connection
    mock_conn.close.assert_called_once()
