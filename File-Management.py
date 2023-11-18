
#* File Management - Python

# In Python, file management is done using functions and methods provided by the module
# built-in `open` and other related modules, such as `os` and `shutil`. Here is a description
# basic how to work with files in Python:

#? Open a File:

# To open a file, we use the `open` function. You can specify the path to the file and the mode of
# opening (read, write, or both).

# Open a file in reading mode
read_file = open("file.txt", "r")

# Open a file in writing mode
write_file = open("new_file.txt", "w")

# Open a file in read and write mode
read_write_file = open("existing_file.txt", "r+")

#? Read Content of a File:

# You can read the contents of a file using the `read()`, `readline()`, or `readlines()` methods.

# Read all content
content = read_file.read()

# Read a line
line = read_file.readline()

# Read all lines in a list
lines = read_file.readlines()

#? Write to a File:

# You can write to a file using the `write()` method.

# Write a line
write_file.write("Hello, world!\n")

# Write multiple lines from a list
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
write_file.writelines(lines)

#? Close a File:

# It is important to close a file after working with it using the `close()` method.

read_file.close()
write_file.close()

#? Using Context Managers (`with`):

# It is recommended to use the `with` context when working with files. This ensures that the file is closed
# correctly even if an exception occurs.

with open("file.txt", "r") as file:
     content = file.read()
     # The file will be automatically closed upon exiting the "with" block

#? Move, Copy and Delete Files:

# The `shutil` module provides functions for more advanced operations, such as move, copy, and delete
# files.

import shutil

# Move a file
shutil.move("file.txt", "new_path/file.txt")

# Copy a file
shutil.copy("file.txt", "copy_file.txt")

# Delete a file
os.remove("file.txt")

#? Get File Information:

# The `os` module provides functions to obtain information about files, such as size, date of
# creation, etc.

import os

# Get the file size in bytes
size = os.path.getsize("file.txt")

# Get the file creation date
creation_date = os.path.getctime("file.txt")

# These are some basics on how to work with files in Python. Always remember to close
# the files after use and use context managers when possible. Also, be careful when
# perform operations that can modify or delete files, since these actions are irreversible.
