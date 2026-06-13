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

print(len(text))   # Result is 2
print(len(number)) # TypeError. int has no length value
```
#### Examples of Methods
- `upper()` - is a method of the class str that converts all the letters to uppercase.
- `bit_length()` - is a method of the class int that returns the length of a number in binary. Examples:
```py
text = "hi"
number = 10

print(text.upper()) # Result is HI
print(number.upper()) # AttributeError. int has no attribute upper
print(number.bit_length())  # Result is 4
```
<br>
<br>

## Chapter 2 - Python Strings

### String Functions - Categories
![alt text](images/essentials/2026-06-12_14-50.png)

### Types
#### type()
- is a built-in function that returns the data type of a value. Example:
```py
name = "John"
age = 24

print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
```
- #### str()
- is a built-in function that converts any value into string value. Example:
```py
age  = 24

print("Your age is:" + age)         # This will cause an Error
# To correct this use the str function
print("Your age is:" + str(age))    # Your age is:24
# If you want to permanently convert your int variable to str
age = str(age)
```
### Math
#### len()
- is a built-in function that gives the total count of items inside a value. Example:
```py
password = "123a"
print(len(password))    # Result is 4
# This is useful if a web app requires a minimum number of char for password
if len(password) < 8:
    print("Your password is too short!")
# Take note that it will count everything even spaces
name = "  John"
print(len(name))    # Output will be 6 because 4 + 2 spaces
```
#### count()
- is a built-in method that returns how often a word appears in the string. Output is int. Example:
```py
text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""
print(text.count("Python"))     # Result is 2
```
### Transformations
#### replace()
- is a built-in method that swaps part of the text with something new. Output is str. Example:
```py
date = "2026/06/12"
print(date.replace("/", "-"))  # Result is 2026-06-12 

phone = "176-1234-56"
print(phone.replace("-", ""))  # Result is 176123456 
# Replacing 2 or more
price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))  # Result is 1299.99
```
#### "string" + "string"
- joins two or more strings into one. Example:
```py
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)   # Result is John Doe
```
#### f{}
- f-string is a modern way to format and build strings. Example:
```py
name = "John"
age = 34
is_student = False
# Old style
print("My name is " + name + ", I am" + str(age) + " years old, and student status is " + str(is_student) + ".")
# New style using f-string
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")
```
#### split()
- is a built-in method that breaks a string into smaller parts. Output is a list. Example:
```py
stamp = "2026-09-20 14:30"
# To separate them by their space
print(stamp.split(" "))     # Result is ['2026-09-20', '14:30']
```
#### "string" * number
- repeats the string multiple times. Output is str. Example:
```py
print("ha" * 3)     # Result is hahaha
print("#" * 10)     # Result is ########## 
```
#### Indexing and Slicing
![alt text](images/essentials/2026-06-12_22-32.png)
![alt text](images/essentials/2026-06-12_22-38.png)
![alt text](images/essentials/2026-06-12_22-40.png)
![alt text](images/essentials/2026-06-12_22-42.png)
![alt text](images/essentials/2026-06-12_22-46.png)

```py
# Extract 1 character (Indexing)
text = "Python"
print(text[0])      # Result is P
print(text[-1])     # Result is n
# Extacting more than 1 character (Slicing)
date = "2026-06-12"
print(date[0:4])    # Result is 2026
print(date[:4])     # Result is also 2026
print(date[-2:])    # Result is 12
```
### Cleaning
#### lstrip(), rstrip(), strip()
- are built-in methods to clean white spaces.
- use `lstrip()` to clean white space/s on the left
- use `rstrip()` to clean white space/s on the right
- use `strip()` to clean white space/s on both left and right
```py
text = " Engineering"
print(text.lstrip())    # Result is Engineering
text = "Engineering  "
print(text.rstrip())    # Result is Engineering
text = "  Engineering "
print(text.strip())     # Result is Engineering
text = "###Abc123##"
print(text.strip("#"))  # Result is Abc123
```
#### lower(), upper()
- are built-in methods that are used for case conversion
```py
text = "python PROGRAMMING"
print(text.lower())     # Result is python programming
print(text.upper())     # Result is PYTHON PROGRAMMING
# Comparing data example
search = "Email ".lower().strip()
data = " emAil".lower().strip()
print(search == data)   # Result is True
```
### Search
#### startswith(), endswith(), in, find()
- are used to search characters
![alt text](images/essentials/2026-06-13_12-44.png)
```py
phone = "+63-919-1234567"
print(phone.startswith("+63"))      # Result is True

email = "john@gmail.com"
print(email.endswith("gmail.com"))  # Result is True

print("@" in email)                 # Result is True

# One of the best use of using find() is if you want to splice inconsistent number of characters
phone1 = "+63-919-1234567"
phone2 = "63-917-7654321"
phone3 = "0063-920-1357901"
# Using splice - but we need to count the index
print(phone1.[4:])  # Result is 919-1234567
print(phone2.[3:])  # Result is 917-7654321
print(phone3.[5:])  # Result is 920-1357901
# Using find() - so that you don't have to count the index
print(phone1[phone1.find("-")+1:])  # Result is 919-1234567
print(phone2[phone2.find("-")+1:])  # Result is 917-7654321
print(phone3[phone3.find("-")+1:])  # Result is 920-1357901
```
### Validation
#### isalpha()
- is a built-in method that checks if the string has only letters. Output is boolean. Example:
```py
country = "USA"
print(country.isalpha())    # Result is True
```

#### isnumeric()
- is a built-in method that checks if the string has only numbers. Output is boolean. Example:
```py
phone = "09181234567"
print(phone.isnumeric())    # Result is True
```

<br>
<br>

## Chapter 3 - Python Numbers
![alt text](images/essentials/2026-06-13_13-38.png)

### Types
#### type()
- is a built-in function that returns the data type of a value. Example:
```py
x = 5
y = 5.7
z = 2 + 3j

print(type(x))  # Result is <class 'int'>
print(type(y))  # Result is <class 'float'>
print(type(z))  # Result is <class 'complex'>
```
#### int()
- is a built-in function that converts compatible value into int value. Output is int. Example:
```py
x = "24"
print(type(x))  # Result is str
x = int(x)      
print(type(x))  # Result is now int
```
#### float()
- is a built-in function that converts compatible value into float value. Output is float. Example:
```py
x = 3           # int that will be converted to float
print(int(x))   # Result is 3.0
y = "3.14"      # str that will be converted to float
print(int(y))   # Result is 3.14
```
#### complex()
- is a built-in function that creates a complex number using real and imaginary parts. Output is complex. Example:
```py
x = 3   # real
y = 4   # will become the imaginary
print(complex(x,y))     # Result is 3+4j
```

### Math Operators
```py
print(2 + 3)    # Addition. Result is 5
print(5 - 3)    # Subtraction. Result is 2
print(4 * 2)    # Multiplication. Result is 8
print(7 / 2)    # Division. Result is 3.5
print(7 // 2)   # Floor Division - it divides two numbers and rounds down. Result is 3
print(7 % 2)    # Remainder. Result is 1
print(2 ** 3)   # Exponential. Result is 8

# How to Shortcut. Example:
x = 2
x = x + 3
# You can write it just like this:
x = 2
x += 3  # Result is also 5
```

### Rounding
#### abs()
- is a built-in function that returns the absolute (non-negative) value of a number. Output is int. Example:
```py
print(abs(2 - 10))  # Result is 8
```
#### floor(), ceil(), round()
![alt text](images/essentials/2026-06-13_15-42.png)









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