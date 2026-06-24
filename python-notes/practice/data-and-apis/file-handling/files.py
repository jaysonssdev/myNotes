import os

file = open("names.txt", "r")
# print(file.read())
# print(file.read(4))
# print(file.readline())
# print(file.readline())

# using loop
for line in file:
    print(line)

file.close()

# try-except-finally
try:
    file = open("no_file.txt")
    print(file.read())
except:
    print("The file you want to read doesn't exist.")
finally:
    file.close()

# Append
file = open("names.txt", "a")
file.write("Neil\n")
file.close()

file = open("names.txt")
print(file.read())
file.close()

# Write (overwrite)
file = open("context.txt", "w")
file.write("I deleted all of the context")
file.close()

file = open("context.txt")
print(file.read())
file.close()

# 2 Ways to Create Files
# Opens a file for writing, creates the file if it does not exist
file = open("name_list.txt", "w")
file.close()
# Creates the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
    file = open("dave.txt", "x")
    file.close()

# Delete a file
# Avoid an error if the file that you want to delete doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file that you wish to delete doesn't exist")

# with keyword
with open("more_names.txt") as file:
    content = file.read()

with open("names.txt", "w") as file:
    file.write(content)
