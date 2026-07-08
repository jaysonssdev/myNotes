# Python Code Safety and Testing

## Python Exception Handling
- [Youtube Link: Python Exception Handling Tutorial for Beginners](https://www.youtube.com/watch?v=PHzm_Iox1mE&list=PL0Zuz27SZ-6MQri81d012LwP5jvFZ_scc&index=19)
- Exception handling allows your program to deal with unexpected events (errors) without crashing.

### The Basic Syntax
The standard structure uses `try`, `except`, `else`, and `finally` blocks.
- `try` - Code that might throw an error.

- `except` - Code that runs if an error occurs.

- `else` - Runs only if no exceptions were raised in the try block.

- `finally` - Always runs, regardless of whether an exception occurred (ideal for closing files or connections).

```py
# Simple Example:
try:
    # Attempting to perform a risky operation
    number = int(input("Enter a number to divide 10 by: "))
    
    # If the user enters '0', Python internally raises a ZeroDivisionError
    result = 10 / number 

except ZeroDivisionError:
    # This block specifically catches the division by zero error
    print("Error: You cannot divide by zero! Please try a non-zero number.")

except ValueError:
    # This catches errors where the input cannot be converted to an integer
    # (e.g., if the user types 'hello' instead of '5')
    print("Error: That is not a valid number.")

else:
    print(f"Result: {result}")  # This line only runs if no error occurred above

finally:
    # This block executes no matter what happened in the try or except blocks
    # It is typically used to close files or clean up connections
    print("Execution attempt finished.")
```
- **Pro Tip:** Always catch specific exceptions rather than using a bare `except:`. Like in the previous example, we provided 'ZeroDivisionError' and 'ValueError' exception names. Using a bare `except` can mask bugs and make debugging significantly harder.

### How to know which Exceptions to catch?
- You don't need to memorize them all! You can see the error type in the **Traceback** (the red text Python displays when a program crashes).

- For example, if your code crashes, look at the very last line of the error message:
`ZeroDivisionError: division by zero.`
The first part of that line is the name of the exception you need to use in your `except` block.

<br>
<br>
<br>

## Python Logging
- [Youtube Link: Python Logging](https://www.youtube.com/watch?v=urrfJgHwIJA)
- Instead of using `print()` statements to debug, use the built-in `logging` module. It allows you to track code execution, record errors, and control the verbosity of your output.

### Logging Levels (in order of severity)
- `logging.debug()` - Detailed information, typically for diagnosing problems.

- `logging.info()` - Confirmation that things are working as expected.

- `logging.warning()` - An indication that something unexpected happened (e.g., "disk space low").

- `logging.error()` - A more serious problem; the software couldn't perform a function.

- `logging.critical()` - A serious error indicating the program may be unable to continue.

### Basic Setup

```py
import logging

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,    # This means it will log debug to critical
    # if you set this to INFO - it will log info to critical; WARNING - will log warning to critical; ERROR - will log error to critical; CRITICAL - will only log critical

    format='%(asctime)s - %(levelname)s - %(message)s', # the output format of your logs
    filename='app.log',     # the file name of your log
    filemode='w'            # this means write mode
)

# This logs Variable values
x = 2
logging.debug(f"The value of x is {x}.")

# This logs simple status message
logging.info("Application started.")
logging.warning("This is a warning message.")
logging.error("An error occurred!")
```

### Logging Exceptions

```py
import logging

# Configuration sets up how and where to save the logs
logging.basicConfig(
    level=logging.INFO, # Only messages of level INFO and above will be recorded
    format='%(asctime)s - %(levelname)s - %(message)s', # Defines the structure of the log entry
    filename='app.log', # Name of the file to save logs to
    filemode='a' # 'a' means append (add to the file rather than deleting it)
)

# This logs a simple status message
logging.info("The application has started.")

try:
    x = 10 / 0
except ZeroDivisionError:
    # logging.exception is special: it logs the error AND the full 
    # 'Traceback' (the exact line number and code path where it failed).
    # This is incredibly useful for debugging later.
    logging.exception("Caught an expected error:")

logging.info("The application is closing.")
```

### Custom Loggers, Handlers, Formatters
- Using the basic `logging.basicConfig` is great for simple scripts, but as your project grows, you’ll want to use **custom loggers**.

- Think of custom loggers like having different "channels" for your messages. You might have one logger for your database operations and another for your user authentication. This allows you to turn logging on or off for specific parts of your application without affecting the rest.

- Here is an example showing how to create and use a custom logger.
```py
import logging

# 1. Create a custom logger object
# __name__ is a special variable that gives the logger the name of the file
# e.g., if this file is named 'main.py', the logger name is 'main'
logger = logging.getLogger(__name__)

# 2. Set the logging level for this specific logger
# DEBUG is the lowest level, meaning we want to see everything
logger.setLevel(logging.DEBUG)

# 3. Create a "Handler"
# A handler decides where the log message goes (file, console, email, etc.)
# Here we use StreamHandler to send messages to the console (screen)
# If you want to save the logs into a file -Example: logging.FileHandler('test.log')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 4. Create a "Formatter"
# This dictates how the log message will look
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# 5. Add the handler to the logger
logger.addHandler(console_handler)

# --- Using our custom logger ---

def perform_task():
    logger.debug("This is a debug message for technical details.")
    logger.info("Task is starting...")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        # Logging with 'error' level and including the exception details
        logger.error("A critical math error occurred!", exc_info=True)

perform_task()
```

#### Why use Custom Loggers?

- **Isolation:** You can configure the database logger to write to a file, while keeping the `user_auth` logger printing to the console.

- **Hierarchy:** You can create child loggers (e.g., `logger = logging.getLogger('my_app.database')`). If you set the level on the parent `my_app`, it can automatically apply to the children.

- **Granularity:** You can silence third-party libraries that are too "chatty" while keeping your own code’s logs active.

#### Key Components Checklist
When creating custom loggers, you are essentially assembling these three parts:

1. **Logger:** The entry point where you call `logger.info()`.

2. **Handler:** The destination (File, Console, etc.).

3. **Formatter:** The visual style of your log entries.

<br>
<br>
<br>

## Pytest
- [Youtube Link: Pytest Tutorial – Pytest Tutorial](https://www.youtube.com/watch?v=EgpLj86ZHFQ)
- Testing framework for Python
- Auto-dicovery of tests
- Rich assertion introspection
- Support parameterized and fixture-based testing

### Installation & Setup
Install the dependencies pytest and pytest-mock:
- `uv add pytest pytest-mock`
- or, if you still using pip:
    - `pip install pytest`
    - `pip install pytest-mock`

### Importance of Unit Testing
- **Unit Test** is the smallest type of test and it's typically testing one very small component of code, like function, method, or class.
- To ensure that you get the expected outcome or result from a small unit of code.
- So if we do get an error, we can isolate where it comes from and fix it very easily
- Aside from unit test, we can also make other test like integration test, system test, and end-to-end test that have their own purposes.

### Folder Structure
- The most conventional and robust way to structure a Python project when using `uv` and `pytest` is the src layout.
- When you use `uv`, your code is typically managed as an editable package during development. This ensures `pytest` can seamlessly import your `main.py` and other modules without messy, brittle hacks like modifying `sys.path`.
- The **conventional folder structure**
```
my-project/
├── .venv/                  # Managed automatically by uv
├── src/                    # The source directory
│   └── my_project/         # Your actual package (snake_case)
│       ├── __init__.py     # Makes this folder a package
│       ├── main.py         # Your application entry point
│       └── utils.py
├── tests/                  # Your testing directory
│   ├── __init__.py         # Optional, but helps pytest avoid name collisions
│   ├── conftest.py         # Shared pytest fixtures (optional)
│   └── test_main.py        # Tests targeting main.py
├── .gitignore
├── pyproject.toml          # Project configuration and metadata
├── README.md
└── uv.lock                 # Managed automatically by uv
```

#### Crucial Steps to Make this Work Perfectly

1. Define your package in `pyproject.toml`
    - Since you have a `src/` directory, `uv` needs to know your project is a buildable package. Your `pyproject.toml` should look like this:
```
[project]
name = "pytest-practice"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "pytest>=9.1.1",
    "pytest-mock>=3.15.1",
]

[tool.pytest.ini_options]
pythonpath = ["."]
```
Note: If you scaffolded your project using `uv init --package`, `uv` already generated this layout and the `build-system` configuration for you.

2. Write the Import in your Test File
    - Because `uv` installs your local package in "editable" mode inside the `.venv`, you import `main.py` inside `tests/test_main.py` using **absolute imports**:
```py
# tests/test_main.py
from my_project.main import my_function

def test_my_function():
    assert my_function() == "expected_result"
```
3. Keep `main.py` import-safe
    - When `pytest` imports `main.py`, you don't want your whole application to immediately execute. Ensure the code that actually runs your script is wrapped inside a standard boilerplate block:
```py
# src/my_project/main.py
def my_function():
    return "expected_result"

def run():
    print(my_function())

if __name__ == "__main__":
    run()
```

4. How to execute your tests
    - Because `uv` isolates dependencies cleanly, you should run your test suite by prepending your test command with `uv run`:
```
uv run pytest
```
This forces `pytest` to run inside your virtual environment where your `src/` files are completely visible to your environment path.


<br>

### Writing Your First Test & Assertion
- Let's say we have a Python file named 'main.py'
```py
# main.py
def get_weather(temp):
    if temp > 20:
        return "hot"
    else:
        return "cold"
```
- We will create a separate Python test file named 'test_main.py' specifically for the 'main.py'.
- Requirements: You need to import the code that you want to test, and you need to write a function that contains an assertion. - `assert` is a built-in debugging keyword used to test if a specific condition is 'True'
```py
# test_main.py
from main import get_weather    # this is the function that we want to test from the file 'main.py'

# this is the test function for the function 'get_weather'. It is important to put 'test' on its function name for pytest to detect it.
def test_get_weather():         
    assert get_weather(21) == "hot"  # If the condition is True, it means our test case passes. If False, the test case fails.
```
- To run this test, open Terminal and run:
`pytest test_main.py`
- This test should pass because '21 > 20', which means 'hot == hot'. It will fail if you put `assert get_weather(21) == "cold"` or `assert get_weather(18) == "hot"`
- **Note:** If you're using `uv`:
    - `uv run pytest test_main.py`
    - Useful Variations:
        - `uv run pytest` - to run all tests
        - `uv run pytest -v` - to run with verbose output
        - `uv run pytest test_main.py::test_function_name` - to run a specific test function
    
- Another example:
```py
# main.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```
```py
# test_main.py
from main import add, divide    # import the 2 functions from 'main.py'
import pytest

def test_add():     
    # provide multiple assertions to make sure that you cover as many things as possible
    assert add(2, 3) == 5, "2 + 3 should be 5"
    assert add(-1, 1) == 0, "-1 + 1 should be 0"
    assert add(0, 0) == 0, "0 + 0 should be 0"

def test_divide():
    # this test is to ensure that the error is being raised if you divide a number by zero, and the exact words "Cannot divide by zero"
    with pytest.raises(ValueError, match="Cannot divide by zero"):      
        divide(10, 0)
```
- This test on those 2 functions should pass as all are True

### Fixtures
- **Fixtures** - is something that you can have run before every single test.
- One thing you can do with fixtures is it will run a setup step that you gives you a fresh start or instance **before every test runs**. See example below:
```py
# main.py
# a class that have some initialization, we can add a user but won't allow you to create a duplicate user
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True

    def get_user(self, username):
        return sel.users.get(username)
```

```py
# test_main.py
import pytest
from main import UserManager

# We add a fixture to create an independent test for each - test_add_user and test_add_duplicate_user. Because you want to isolate each test, so that one test can't affect the other.
@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test."""
    return UserManager()

# This test checks if we can add a user
def test_add_user(user_manager): # <- Inject here the 'user_manager' fixture that you created from above
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_Manager.get_user("john_doe") == "john@example.com"

# This test checks if it doesn't allow us to create a duplicate
def test_add_duplicate_user(user_manager): # <- Inject here the 'user_manager' fixture that you created from above
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com")
```

### Parameterized Testing
- **Parameterized testing** allows you to run a single test function multiple times with different sets of input data. Instead of writing repetitive test functions for varying conditions, you define the test logic once and provide a list of arguments to pass into it.
```py
# main.py
# a function that checks if a number is a prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
```py
# test_main.py
import pytest
from main import is_prime

# To avoid creating multiple tests for different number output, we use parameterized testing using '.mark.parameterize'
@pytest.mark.parameterize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (19, True),
    (25, False),
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected
```

### Mocking
- A lot of times when you write tests, there's part of your code that relies on something that's not active in a testing environment.
- For example, this front end code (main.py) that relies on a back end API in order to be working properly, but you don't want to reach or spin up the back end API, or setup all of these different dependencies just to test the fron end. So what you should do is **mock or create a fake version** of that dependency in this case the back end API that returns some fake data.
```py
# main.py
import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/v1/{city}") # you can't control this API, and you don't want your test to fail because this back end may someday fails
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch weather data")
```
```py
# test_main.py
import pytest
from main import get_weather

def test_get_weather(mocker):   # this 'mocker' will work because we installed the pytest-mock earlier)
    # Mock requests.get
    mock_get = mocker.patch("main.requests.get") # 'main' came from 'main.py', 'requests' came from 'import requests', and 'get' came from '.get{f"https://api....}'

    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

    # Call function
    result = get_weather("Dubai")

    # Assertions
    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")
```

**Mocking a Database example:**
- This is your production code (db.py) that interacts with the real SQLite database.
```py
# db.py
import sqlite3

def save_user(name, age):
    # Establish a connection to the local SQLite database file named 'users.db'
    conn = sqlite3.connect("users.db")
    
    # Create a cursor object, which allows you to execute SQL commands
    cursor = conn.cursor()
    
    # Execute the SQL statement using parameterized queries to safely insert data
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    
    # Save (commit) the changes permanently to the database file
    conn.commit()
    
    # Close the database connection to free up system resources
    conn.close()
```
- This is your test file (test_db.py). It uses the `mocker` fixture to intercept the real database calls and replace them with fake objects (mocks).
```py
# Import the actual function we want to test from our app code
from db import save_user

def test_save_user(mocker):
    """
    Test if save_user correctly connects to the database and runs the SQL.
    'mocker' is a pytest fixture that simplifies creating and cleaning up mocks.
    """
    
    # 1. Intercept the real 'sqlite3.connect' function.
    # From this point on, calling sqlite3.connect will return a fake connection object ('mock_conn').
    mock_conn = mocker.patch("sqlite3.connect")
    
    # 2. Set up the chain of return values for our mock.
    # When sqlite3.connect() runs, it returns mock_conn.
    # When mock_conn.cursor() runs, it returns a fake cursor object.
    # We store that fake cursor in 'mock_cursor' so we can inspect it later.
    mock_cursor = mock_conn.return_value.cursor.return_value

    # 3. Execute the code under test.
    # This runs the production logic, but it uses our fake database objects behind the scenes.
    save_user("Alice", 30)

    # 4. Verify that the application attempted to open the correct database file.
    mock_conn.assert_called_once_with("users.db")
    
    # 5. Verify that the application attempted to run the correct SQL query with the right data.
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30)
    )
```

### Testing an API
- Here is a simple, self-contained example of testing a REST API using `pytest`.To run this code, you will need the `requests` library installed (`uv add requests`).
- This test (test_api.py) uses a real, free online API (://typicode.com) that developers use for testing. It fetches a single placeholder "To-Do" item and verifies the results.
```py
# Import the requests library to send HTTP network requests
import requests

def test_get_todo_item():
    """
    Test that fetching a specific to-do item from the API works correctly.
    """
    # 1. Define the target API endpoint URL
    url = "https://typicode.com"
    
    # 2. Send a live HTTP GET request to the API and store the response
    response = requests.get(url)
    
    # 3. Verify the HTTP Status Code is 200 (OK / Success)
    assert response.status_code == 200
    
    # 4. Convert the raw text response from the API into a Python dictionary (JSON format)
    data = response.json()
    
    # 5. Verify the API data contains the exact expected key-value pairs
    assert data["id"] == 1                  # Checks if the ID matches our request
    assert data["userId"] == 1              # Checks if the owner ID is correct
    assert "title" in data                  # Ensures the 'title' key exists in the response
    assert data["completed"] is False       # Checks the boolean status of the task
```

#### Key API Testing Concepts
- `requests.get(url)` - Sends a real network request over the internet to the server.
- `response.status_code` - Every API response comes with a 3-digit status code. `200` means successful, `404` means not found, and `500` means server error. Testing this first prevents your test from crashing on broken data.
- `response.json()` - Most modern APIs talk in JSON format. This method instantly turns that JSON string into a normal Python dictionary so you can look up values using keys (like `data["id"]`).
