
#* Files Objects - Python

# In Python, file manipulation is done by using the `file` object. Here there is a brief description of
# how to work with files in Python:

#? Open a file:
# You can open a file using the `open()` function which returns a `file` object. The first argument is the
# name of the file and the second argument is the mode in which the file will be opened
# (reading, writing, etc.).

# Open a file for reading
file = open('file.txt', 'r')

# Open a file for writing
file = open('file.txt', 'w')

# Open a file in binary mode for writing
file = open('file.bin', 'wb')

#? File opening modes:

#* - ``r'`:
# Reading (default).
#* - ``w'`:
# Writing. If the file already exists, it is truncated; if not, it is created.
#* - ``a'`:
# Addition. Open the file to add content to the end.
#* - ``b'`:
# Binary mode.
#* - ``x'`:
# Creates the file, but gives an error if it already exists.
#* - ``t'`:
# Text mode (default).

#? File operations:

#* File reading:

# Read the entire content of the file
content = file.read()

# Read a line from the file
line = file.readline()

# Reads all lines from the file and returns them as a list
lines = file.readlines()

#? Writing to files:

# Write a string to the file
file.write("Hello, world!")

# Write a list of strings to the file
file.writelines(["Line 1", "Line 2", "Line 3"])

#? Closing files:

# It is important to close the file after you have finished working with it to free up resources.

file.close()

#? Using the `with` block:

# To ensure that a file is closed correctly after use, you can use the block `with`, which automatically 
# closes the file upon exiting the block:

with open('file.txt', 'r') as file:
     content = file.read()
     # Perform operations on the file within this block
# The file will be automatically closed when exiting the block

# This is a safer way to work with files, as it ensures that they are closed even if an exception occurs
# during execution.
