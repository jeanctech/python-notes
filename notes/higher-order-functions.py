
#* Higher Order Functions - Python

# Higher order functions in Python are functions that take other functions as arguments or
# return functions as a result. This concept is fundamental for functional programming and
# allows building more modular and flexible code. Here's a basic description of how they work
# higher order functions:

# Pass Functions as Arguments:

# Example 1:

#Map function

# The `map()` function applies a function to each element of an iterable and returns a new iterable with
# the results.

def square(x):
     return x**2

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)
print(list(squares)) # Prints: [1, 4, 9, 16, 25]

# Example 2:

# Custom Higher Order Function

def apply_operation(operation, list):
     return [operation(x) for x in list]

squares = apply_operation(lambda x: x**2, [1, 2, 3, 4, 5])
print(squares) # Prints: [1, 4, 9, 16, 25]

# Return Functions from Other Functions:

# Example 1:
# Function That Returns Another Function

def multiplier(n):
     def multiply(x):
         return x * n
     return multiply

times_two = multiplier(2)
times_three = multiplier(3)

print(times_two(5)) # Prints: 10
print(times_three(5)) # Prints: 15

# Example 2:
# Higher Order Function to Create Decorators

def decorator(function):
     def wrapper(*args, **kwargs):
         print("Before calling the function.")
         result = function(*args, **kwargs)
         print("After calling the function.")
         return result
     return wrapper

@decorator
def greet(name):
     print(f"Hello, {name}!")

greet("John")

# Anonymous Functions (Lambda) in Higher Order Functions:

# Example:
# Higher Order Function with Lambda Function

def apply_operation(operation, list):
     return [operation(x) for x in list]

squares = apply_operation(lambda x: x**2, [1, 2, 3, 4, 5])
print(squares) # Prints: [1, 4, 9, 16, 25]

# `map()`, `filter()`, and `reduce()`

# These built-in functions are additional examples of higher-order functions.

# `map()`:

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares) # Prints: [1, 4, 9, 16, 25]

# `filter()`:

numbers = [1, 2, 3, 4, 5]
pairs = list(filter(lambda x: x % 2 == 0, numbers))
print(pairs) # Prints: [2, 4]

# `reduce()`:

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product) # Prints: 120

# Higher order functions are an essential part of functional programming in Python. Allow
# write cleaner, modular and expressive code. Experiment with these examples and use them in your own
# code to improve your understanding and skills in Python.
