# Data and APIs 

## Python File Handling
- [Youtube Link: Python File Handling](https://www.youtube.com/watch?v=BRrem1k3904&list=PL0Zuz27SZ-6MQri81d012LwP5jvFZ_scc&index=23)

### rawx
- r = Read
- a = Append
- w = Write
- x = Create

### Reading Files
- You will get an error if the file doesn't exist.

```py
file = open('names.txt', 'r')   # 'r' is not required because it is the default
print(file.read())   

# To read just the first 4 characters of the file:
print(file.read(4))

# To read just the first line of the file:
print(file.readline())          # Repeat this command line twice if you want to see the 2 lines, 3x for 3 lines, and so on

# To loop all the lines:
for line in file:
    print(line)
```

### Closing Files
- If you open a file, it is IMPORTANT TO CLOSE THE FILE, especially if you made some changes and you want to reflect the changes on the actual file.
```py
file.close()
```

### Using try-except-finally
- To avoid getting errors when opening a file that doesn't exist, use `try-except-finally`
```py
try:
    file = open('no_file.txt')
    print(file.read())
except:
    print("The file you want to read doesn't exist.")
finally:
    file.close()
```

### Append Files
- Creates a file if it doesn't exist.
```py
file = open('names.txt', 'a')
file.write('Neil')
file.close()
# Then read the file to check your changes
file = open('names.txt')
print(file.read())
file.close()
```

### Write / Overwrite files
```py
# To overwrite everything inside a file
file = open('context.txt', 'w')
file.write('I deleted all of the context')
file.close()
# Then read the file to check your changes
file = open('context.txt')
print(file.read())
file.close()
```

### Two Ways to Create Files
- Opens a file for writing, creates the file if it does not exist
```py
file = open('name_list.txt', 'w')
file.close()
# Now name_list.txt has been created
```
- Creates the specified file but returns an error if the file exists, we need to `import os` first
```py
if not os.path.exists('dave.txt'):
    file = open('dave.txt', 'x')
    file.close()
# Now dave.txt file has been created
```

### Deleting files
- Avoid an error if the file that you want to delete doesn't exist
```py
if os.path.exists('dave.txt'):
    os.remove('dave.txt')
else:
    print("The file that you wish to delete doesn't exist")
```

### with keyword
- In this example we will restore the content of "names.txt" by copying "more_names.txt"
```py
with open('more_names.txt') as file:
    content = file.read()

with open('names.txt', 'w') as file:
    file.write(content)
```
<br>
<br>
<br>

## JSON in Python - Read & Write
- [Youtube Link: Read & Write JSON Files in Python](https://www.youtube.com/watch?v=vrs5MVYkats)

### What is JSON?
- JSON stands for `JavaScript Object Notation`
- Used across almost every programming language
- Represents data in a structured, readable text format
- It is mainly used to:
    - store data
    - transfer data between programs
    - work with APIs
    - save configuration files

### JSON Structure and Syntax
```js
{
    "name": "Asha",
    "age": 22,
    "is_student": true,
    "skills": ["Python", "Data Analysis"]
}
```
- **Key Rules:**
    - Keys and Strings must be inside `double quotes("")` 
    - Boolean values are in lower case - `true` and `false`
    - `null` represents no value
    - Functions, comments, trailing commas are NOT ALLOWED

### JSON Data Types

![alt text](images/data-and-apis/2026-06-23_18-57.png)

### JSON Functions in Python

![alt text](images/data-and-apis/2026-06-23_19-03.png)

- `dumps()` - converts Python data into a JSON formatted string. Use `dumps()` when you want to send data over a network, store it in a database, or simply print it in JSON format.
```py
import json     # Always "import json" to import json modules

# Example: Convert a Python dict to json string
student_dict = {
    'name': 'Jamie',
    'age': 12,
    'city': 'New York'
}
print(type(student_dict))   # Result is <class 'dict'>
# To convert it to a json string
json_str1 = json.dumps(student_dict)
print(type(json_str1))      # Result is <class 'str'>
```

- `loads()` - takes a JSON string and converts it to a Python object. Use `loads()` when your JSON is in a variable, API response, or coming from the internet, not a file.
```py
# To convert a json, you need to wrap it first with single quotes ('), and put it in a variable.
# If it has multiple lines, wrap it with triple quotes (''')
import json

text = '{"name": "Sam", "age": 14}'
data = json.loads(text)
print(data)             # Result is {'name': 'Sam', 'age': 14}
print(type(data))       # Result is <class 'dict'>
```

- `dump()` - writes a Python object directly into a `JSON file`.
```py
import json

student_dict = {
    'name': 'Jamie',
    'age': 12,
    'city': 'New York'
    'marks': [80, 92, 75]
    'languages': ['English', 'French']
}

with open('mydata.json', 'w') as f:         # "mydata.json" is the name of the json file that you want to create
    json.dump(student_dict, f, indent = 4)  # this means you want to use the dump function to write student_dict to f, and the 'indent=4' to fix the indention format of the created json file to become more readable
```

- `load()` - reads a JSON file and converts it into a Python object
```py
import json

with open('mydata.json', 'r') as f:         # reads the json file
    output = json.load(f)  
print(output)       # Result is like student_dict above
```

### Summary

![alt text](images/data-and-apis/2026-06-23_20-01.png)

<br>
<br>
<br>

## CSV in Python - Read & Write
- [Youtube Link: How to Work with CSV Files in Python: Built-in CSV Module Tutorial](https://www.youtube.com/watch?v=sfTUVXfC0X0)

### What is CSV?
- CSV stands for `Comma-Separated Values`
- Datas are represented in rows and columns
- First row contains the column names, and rows below hold the actual data or records
- Individual values are separated by commas
- CSV files can be opened by a text editor (example below), but much readable in Excel

![alt text](images/data-and-apis/2026-06-23_20-31.png)

### How to Read a CSV File using Loop
- You can loop to print each row but this is difficult to read
- Example (data.csv) for practice

![alt text](images/data-and-apis/2026-06-24_12-04.png)

```py
with open('data.csv', 'r') as f:   # it's okay not to put "r" as read is the default
    for row in f:
        print(row)
```

### How to Read a CSV File as Python Lists
- `reader` function is used to read csv files that put them on python lists. You need to import the csv module to use this.
```py
import csv

with open('data.csv', 'r') as f:
    data = csv.reader(f)        # use the reader function (from csv module) on f then put it in a variable
    for row in data:
        print(row)   
```
Output: Each row is in separated python list.

![alt text](images/data-and-apis/2026-06-24_12-26.png)

- If you want to print only the 'firtsname' and the 'email', put their `indexes` 0 and 2

```py
import csv

with open('data.csv', 'r') as f:
    data = csv.reader(f)    
    for row in data:
        print(row[0], row[2])   # specify the `index`
```
Output:

![alt text](images/data-and-apis/2026-06-24_12-34.png)

- If you want to skip the headers row ('firstname','lastname','email', 'age'), use the `next` function.
```py
import csv

with open('data.csv', 'r') as f:
    data = csv.reader(f) 
    next(data)                  # use the 'next' function
    for row in data:
        print(row[0], row[2])
```
Output:

![alt text](images/data-and-apis/2026-06-24_12-43.png)

### How to Read a CSV File as Python Dictionaries
- `DictReader` function is used to read csv files that put them on python dictionaries. You need to import the csv module to use this.
```py
import csv

with open('data.csv', 'r') as f:
    data = csv.DictReader(f)    
    for row in data:
        print(row)     
```
Output: Headers as key, and Datas as values

![alt text](images/data-and-apis/2026-06-24_13-48.png)

- For example, if you want to read the key 'email' only
```py
import csv

with open('data.csv', 'r') as f:
    data = csv.DictReader(f)    
    for row in data:
        print(row['email'])     # Specify the Key/s that you want
```
Output:

![alt text](images/data-and-apis/2026-06-24_13-54.png)


### How to Write a CSV File using writer()
- To use an existing CSV file and create a new CSV file with this data. Put `with open()` inside its `with open()` and use the `writer` function.
```py
import csv

# To create a new csv file with the same content with the old csv file but change the delimiter to semi-colon(;)
with open('data.csv', 'r') as old_csv:                      # 'data.csv' is the existing csv file that you need to read
    with open('new_data.csv', 'w', newline='') as new_csv:  # 'new_data.csv is the name of the new csv file, use newline='' argument to avoid having spaces between lines
        old_data = csv.reader(old_csv)                      # reader function to read the existing csv file
        new_data = csv.writer(new_csv, delimiter=';')       # writer function to create and write a new csv file, and use semi-colon as a new delimiter
        for row in old_data:
            new_data.writerow(row)                          # use writerow function on the new csv file
```
Output: A new csv file named 'new_data.csv'.

![alt text](images/data-and-apis/2026-06-24_13-23.png)

### How to Read a CSV File with different delimiter
```py

import csv

with open('new_data.csv', 'r') as f:
    data = csv.reader(f, delimiter=';')     # To read the new_data.csv that has different delimiter
    for row in data:
        print(row)   
```
Output: The output python lists will automatically have comma as a delimiter

![alt text](images/data-and-apis/2026-06-24_12-26.png)


### How to Write a CSV File using DictWriter()
```py
import csv

with open('data.csv', 'r') as old_csv:                      
    with open('new_data.csv', 'w', newline = '') as new_csv:  
        old_data = csv.DictReader(old_csv)
        field_name = ['firstname', 'lastname', 'email', 'age']      # You need to specify the fields, since this is a dictionary you can change the order of the fields/columns if you want. Example: If you want 'age' to go first instead of 'email'                
        new_data = csv.DictWriter(new_csv, fieldnames = field_name) # Then put its variable in this 'fieldnames' argument      
        new_data.writeheader()                                      # Use the writerheader on the new csv to include the headers
        for row in old_data:
            new_data.writerow(row)                         
```
Output:

![alt text](images/data-and-apis/2026-06-24_14-18.png)

- If you want to create a new csv file but not include a field like the 'age'.
```py
import csv

with open('data.csv', 'r') as old_csv:                      
    with open('new_data.csv', 'w', newline = '') as new_csv:  
        old_data = csv.DictReader(old_csv)
        field_name = ['firstname', 'lastname', 'email']             # Don't include the 'age' field here                  
        new_data = csv.DictWriter(new_csv, fieldnames = field_name)  
        for row in old_data:
            del row['age']                                          # Then delete the each 'age' row here
            new_data.writerow(row)                         
```
Output:

![alt text](images/data-and-apis/2026-06-24_14-20.png)

<br>
<br>
<br>

## API Requests in Python
- [Youtube Link: Master Python Requests In 15 Minutes. Call Any API](https://www.youtube.com/watch?v=Xnbef8F_Yfc&t=10s)

### Requests Theory
#### URLs and Endpoints

![alt text](images/data-and-apis/2026-06-24_14-45.png)

#### Request and Response

![alt text](images/data-and-apis/2026-06-24_14-47.png)

- Example:

![alt text](images/data-and-apis/2026-06-24_14-50.png)

#### HTTP Status Codes

![alt text](images/data-and-apis/2026-06-24_14-52.png)

#### HTTP Methods

![alt text](images/data-and-apis/2026-06-24_14-55.png)

### Setup / Install (using VS Code)

#### Using venv
1. Open your project folder in VS Code.
```
cd /path/to/your/project
code .
```
2. Create and activate the environment by opening the built-in terminal in VS Code. Run your setup commands here:
```
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```
3. Select the Python Interpreter in VS Code. 
    - Press Ctrl + Shift + P to open the Command Palette
    - Type Python: Select Interpreter and select it.
    - Look for the option that shows .venv or ./venv/bin/python
    - Click it to select it.

4. Test the setup by creating a new file named test.py in VS Code and paste this snippet:
```py
import requests

response = requests.get('https://httpbin.org')
print(f'Status Code: {response.status_code}')
```
#### Using uv (recommended)
1. Open your project folder in VS Code.
2. Initialize it: `uv init .`
3. Add your library: `uv add requests`
4. Choose the interpreter in VS Code (Ctrl + Shift + P -> Python: Select Interpreter -> Choose the one created by uv).
5. Write your code in 'main.py'
6. Run it safely using: `uv run main.py`

### Basic Requests Demo
```py
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print('Status code:', response.status_code)
print('Content-Type:', response.headers.get('Content-Type'))

data = response.json()  # parse JSON into a Python dict
print('Post title:', data['title'])
```
- Then run your script `uv run main.py`.
- Output:

![alt text](images/data-and-apis/2026-06-24_18-22.png)


### Query Parameters (Get request)
```py
import requests

url = "https://reqres.in/api/users"
parameter = {'page': 2}

response = requests.get(url, params=parameter) # params argument to add the params on the url
print('Final URL:', response.url)   # shows ?page=2

response.raise_for_status()         # raises error for 4xx/5xx

data = response.json()
print('Page:', data['page'])
for user in data['data']:
    print(user['email'])
```
- Then run your script `uv run main.py`.
- Output:

![alt text](images/data-and-apis/2026-06-24_18-24.png)

### Body (Post request)
```py
import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {                                 
    'title': 'Hello from Python',
    'body': 'This is a test post.',
    'userId': 1,
}                           # python dict to represent JSON

response = requests.post(url, json=payload) # json=payload argument is the data that you want to create/inject

print('Status code:', response.status_code) # To check if your post request is successful
data = response.json()
print(data)
```
- Then run your script `uv run main.py`
- Output: Notice that the status code is 201, which means that the post request is successful.

![alt text](images/data-and-apis/2026-06-24_18-47.png)


### Error Handling
```py
import requests

try:
    # httpbin /delay/3 waits 3 seconds before responding
    response = requests.get('https://httpbin.org/delay/3', timeout=1)   # timeout=1 means you need to get a reply in 1 second
    response.raise_for_status()     # raises error for 4xx/5xx
    print('Success:', response.json()0
except requests.exceptions.Timeout: # be specific when making exception when you're trying to handle errors 
    print('Request timed out')
except requests.exceptions.RequestException as e:
    print('Request failed:', e)
```
- Then run your script `uv run main.py`
- Output: Request timed out because it took more than 1 second to reply

![alt text](images/data-and-apis/2026-06-24_19-25.png)


### Authorization
- Sometimes when you're working with an API, you will generate something called an **API Token** or an **Authorication Token**. This is something that needs to be sent alongside your request to verify that you are who you say you are, so you can perform some restrictive actions.
```py
import requests

TOKEN = 'AAAAA67bnjhg768797hkjhkjh98789hk'
BASE_URL = 'https://api.x.com/2/users/by/username/TechWithTimm'

auth = {
    'Authorization': f'Bearer {TOKEN}',
}

response = requests.get(BASE_URL, headers=auth) # add your api token on headers argument)

print('Status code:', response.status_code)
print('URL:', response.url)

try:
    data = response.json()
    print(data)
except ValueError:
    print('Response is not JSON.')
    print(response.text)
```
- Then run your script `uv run main.py`
- Output: Notice that you got a 200 status code, but you will get an error if you're not authorized.

![alt text](images/data-and-apis/2026-06-24_19-48.png)

