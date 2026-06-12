# Python Course
- [Youtube Link: Python Full Course for Beginners - From Zero to Hero](https://www.youtube.com/watch?v=Rq5gJVxz55Q)

## Chapter 1 - Python Fundamentals

### Setup your Environment (VS Code)

- Press `ctrl+shift+P`, then type `Python:Select Interpreter` then select the python that you've installed.
- ``ctrl+shift+` `` - to open a new terminal, you can open multiple terminal by using ``ctrl+shift+` ``, then you can select **bash** for example
- ``ctrl+` `` - to open again a previously opened terminal
- `python3 --version` - run this on terminal to verify your python version for linux, `py --version` for windows
- `python3` - run this on terminal to run python repo, to quit type `quit()`
- Press `ctrl+shift+P`, then type `Preferences:Open Keyboard Shortcuts`. Type `Run python file`. Double-click keybinding to assign `ctrl+R`.
- **VS Extensions** - Python, autopep8, Material Icon Theme, One Dark Pro


### Comments
- `#` - used to make comments/notes
- `ctrl+/` - select all the texts that you want to be a comment then press `ctrl+/`
- `shift+alt+down` - copy an entire line


### print() function
- `print()` is a python built-in function that displays messages on the output screen. Example: `print("Hello World!")`
- **Escape Sequences**

![alt text](images/essentials/2026-06-11_20-34.png)

Example:
```py
print("Hi \"Python\"")  # To print Hi "Python"
print('Hi \'Python\'')  # To print Hi 'Python'
print('Hi "Python"')    # To print Hi "Python"
print("Path: C:\\Users\\John")  # To print Path: C:\Users\John
print("Message1\n")     # To print a space line after your message
print("Message1\tMessage2") # To put a tab space between the words
```
- **Triple Quotes** - for Python to allow multiples lines inside the triple quotes
![alt text](images/essentials/2026-06-11_21-26.png)


### Variables
- `=` - to assign variables. Example:
```py
name = "John"
print("My name is", name)     # Output is: My name is John
# The comma provided space between is and name
```
- You can't use on variable names: <br>
    hyphen(-), start with a number, characters like '!', keywords like 'if' or 'for'
- **Python Naming Conventions**
![alt text](images/essentials/2026-06-12_13-16.png)

### input() function
- To get something from the user. Example:
```py
name = input("Enter Your Name:")   # This is a dynamic value
country = "Germany" # This is hard-coded (static) value
print(name, "comes from", country)
```
- **Dynamic value** - data entered by the user that can vary each time the program runs
- **Hard-coded (static) value** - fixed piece of data written directly into your code that never changes at runtime


### Data Types
![alt text](images/essentials/2026-06-12_14-34.png)
```py
# Data Types
a = 10      # int
b = 3.14    # float
c = "Hello" # str
d = 'Hi'    # str
e = "1234"  # str
f = True    # bool
g = False   # bool
h = None    # NoneType
i = ""      # str - blank
j = " "     # str - empty
```

### Functions and Methods
![alt text](images/essentials/2026-06-12_13-43.png)

![alt text](images/essentials/2026-06-12_13-54.png)

![alt text](images/essentials/2026-06-12_14-04.png)

#### Examples of Functions
- `type()` - is a built-in function that returns the data type of a value.
- `len()` - is a built-in function that gives the total count of items inside a value. Examples:
```py
text = "hi"
number = 10

print(type(text))   # <class 'str'>
print(type(number)) # <class 'int'>

print(len(text))   # 2
print(len(number)) # TypeError. int has no length value
```
#### Examples of Methods
- `upper()` - is a method of the class str that converts all the letters to uppercase.
- `bit_length()` - is a method of the class int that returns the length of a number in binary. Examples:
```py
text = "hi"
number = 10

print(text.upper()) # HI
print(number.upper()) # AttributeError. int has no attribute upper
print(number.bit_length())  # 4
```
<br>
<br>

## Chapter 2 - Python Strings

### String Functions - Categories
![alt text](images/essentials/2026-06-12_14-50.png)

### type()
- is a built-in function that returns the data type of a value. Example:
```py
name = "John"
age = 24

print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
```
### str()
- is a built-in function that converts any value into string value. Example:
```py
age  = 24

print("Your age is:" + age)         # This will cause an Error
# To correct this use the str function
print("Your age is:" + str(age))    # Your age is:24
# If you want to permanently convert your int variable to str
age = str(age)
```
### len()
- is a built-in function that gives the total count of items inside a value. Example:
```py
password = "123a"
print(len(password))    # 4
# This is useful if a web app requires a minimum number of char for password
if len(password) < 8:
    print("Your password is too short!")
# Take note that it will count everything even spaces
name = "  John"
print(len(name))    # Output will be 6 because 4 + 2 spaces
```



<br>
<br>

## Chapter 3 - Python Numbers

<br>
<br>

## Chapter 4 - Python Logic & Operators

<br>
<br>

## Chapter 5 - Python Conditional Statements

<br>
<br>

## Chapter 6 - Python Loops

<br>
<br>

## Chapter 7 - Python Data Structures

<br>
<br>

## Chapter 8 - Python Functions 