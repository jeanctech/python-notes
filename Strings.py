
#* Strings - Python

# In Python, strings are sequences of characters. Here is information on how working with strings in
# Python:

#? Chain Creation:

# You can create strings using single quotes (`'`) or double quotes (`"`). Both ways are equivalents.

simple_string = 'Hello, world!'
double_string = "Hello, world!"

#? Character Access:

# You can access individual characters in a string using indexes. Note that in Python, indexes start
# from 0.

message = "Hello"
first_char = message[0] # 'H'
second_char = message[1] # 'o'

#? Chain Length:

# You can get the length of a string using the `len()` function.

message = "Hello"
length = len(message) #4

#? String Concatenation:

# You can concatenate (join) strings using the `+` operator.

greeting = "Hello"
name = "John"
full_message = greeting + ", " + name # "Hello, Juan"

#? String Methods:

# Python provides several built-in methods for manipulating strings. Some examples:

message = "hello world"

# Convert to uppercase
uppercase = message.upper() # "HELLO WORLD"

# Convert to lowercase
lowercase = message.lower() # "hello world"

# Capitalize the first letter
capitalized = message.capitalize() # "Hello world"

#Count occurrences of a substring
count = message.count("o") #2

# Replace part of the string
replaced = message.replace("world", "friends") # "hello friends"

#* String Formatting:

# There are several ways to format strings in Python, but one of the most common is using f-strings
# (available as of Python 3.6).

name = "Anna"
age = 25
formatted_greeting = f"Hello, {name}. You are {age} years old."
print(formatted_greeting)

# Output: "Hello, Ana. You are 25 years old."

#* Negative Indices:

# You can use negative indices to count from the end of the string.

message = "Hello"
last_character = message[-1] # 'a'

# These are just some basics about handling strings in Python. The chains are fundamentals in programming,
# and Python provides many powerful tools to work with they. Explore and experiment to get the most out of
# string handling in Python!
