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