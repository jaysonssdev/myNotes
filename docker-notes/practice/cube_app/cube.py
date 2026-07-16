import sys

# Get the argument from the command line
input_arg = sys.argv[1]

# Convert the text input into a number
number = float(input_arg)

# Check if the number is actually a whole integer
if number.is_integer():
    number = int(number)

# Calculate the cube
cube = number**3

# Print the final result
print(f"Number is: {number}.\nIts cube is: {cube}")
