
#* Error Types - Python

# In Python, errors are mainly divided into three categories: syntax errors, exceptions
# and logical errors. Each type is described below:

# 1. Syntax Errors:

# Syntax errors occur when the Python interpreter cannot understand the code due to a incorrect structure.
# These errors occur during the code analysis phase before the program to run. Some common examples are:

# Syntax error example
print("Hello") #* Missing closing parenthesis

# This type of error is easily detected and must be corrected before running the program.

# 2. Exceptions:

# Exceptions are errors that occur during program execution. They may be due to inputs unexpected, not
# permitted operations, or unforeseen conditions. Some common examples of exceptions include:

# - `ZeroDivisionError`:
# Division by zero.

# - `TypeError`:
# Incorrect data type for an operation.

# - `IndexError`:
# Index out of range.

# - `FileNotFoundError`:
# File not found.

# Exception example
result = 10 / 0 # This raises a ZeroDivisionError

# 3. Logical Errors:

# Logical errors, also known as runtime errors, occur when the program does not produce the expected
# result due to an error in the code logic. These errors do not generate exceptions and syntax errors,
# but they can lead to incorrect results. They are more difficult to detect why the program runs without
# throwing errors.

# Example of logical error
def sum_squares(n):
     sum = 0
     for i in range(n):
         sum += i # Should be sum += i**2
     return sum

result = sum_squares(5) # Should be 30, but is 10

# Error Handling with `try`, `except`, `else`, and `finally`:

# You can handle exceptions using `try`, `except`, `else`, and `finally` blocks. This mechanism
# allows the program to take specific actions when an exception occurs.

try:
     result = 10 / 0
except ZeroDivisionError:
     print("Error: Division by zero.")
else:
     print("The operation was successful.")
finally:
     print("This block will always be executed.")

# `assert`:

# The `assert` statement checks whether an expression is true. If false, raises an `AssertionError`.
# It is useful for catching logical errors during development and debugging.

age = 15
assert age >= 18, "You are a minor."

# These are some of the common error types in Python and how to handle them. It is crucial to understand
# how address and prevent errors to write more robust and reliable code.
