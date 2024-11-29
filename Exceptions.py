
# * Exceptions - Python

# In Python, exceptions are events that interrupt the normal flow of execution of a program
# when an error occurs. Handling exceptions allows you to write more robust code and anticipate possible
# issues. Here's a basic description of how to work with exceptions in Python:

# ? `try` and `except` block:

# Use the `try` block to surround code that could throw an exception. If a
# exception, the code inside the `except` block will be executed.

try:
    result = 10 / 0  # This will raise a ZeroDivisionError exception
except ZeroDivisionError:
    print("Error: Division by zero.")

# ? Generic Exception Handling:

# You can use `except` without specifying an exception type to handle any type of exception. Without
# However, this should be done with caution, as it can hide unexpected errors.

try:
    result = 10 / 0
except:
    print("An error occurred.")

# ? `else` and `finally` block:

# * - **`else`:**
# Executed if no exception is raised in the `try` block.

# * - **`finally`:**
# It is always executed, regardless of whether an exception was raised or not. Useful for cleaning tasks,
# like closing files or network connections.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print("The result is:", result)
finally:
    print("This block will always be executed.")

# ? Catching Multiple Exceptions:

# You can catch different types of exceptions in the same `except` block.

try:
    list = [1, 2, 3]
    element = list[5]  # This will raise an IndexError exception
except IndexError:
    print("Error: Index out of range.")
except Exception as e:
    print("An error occurred:", e)

# ? Throwing Exceptions:

# You can manually raise an exception using the `raise` keyword.

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot Divide by Zero.")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)

# ? Custom Exceptions:

# You can define your own exceptions by creating a new class that inherits from `Exception` or one of its
# subclasses.


class MyError(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    raise MyError("This is a custom error.")
except MyError as e:
    print(e)

# ? `assert`:

# `assert` is a statement that checks whether an expression is true and, if not, throws a
# `AssertionError` exception.

age = 15
assert age >= 18, "You are a minor."

# These are some basics on how to work with exceptions in Python. The proper management of
# exceptions is essential to write robust code and foresee possible problems during execution
# of the program. Practice and experiment to strengthen your exception handling skills!