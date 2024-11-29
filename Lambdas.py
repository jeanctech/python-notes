
#* Lambdas - Python

# Lambda functions in Python are anonymous functions, that is, unnamed functions. Are crated using the
# `lambda` keyword and are useful when you need a simple function for a specific operation. Here's a basic
# description of how lambda functions work:

#? Basic Syntax:

# General syntax of a lambda function
function_name = lambda x: x * 2

#* - **`function_name`:**
# It can be any valid variable name, but it is not necessary since lambda functions are anonymous
# functions.

#* - **`arguments`:**
# The parameters that the lambda function takes.

#* - **`expression`:**
# The expression that is evaluated and returned as a result.

#? Examples:

#* Example 1:
# Function that doubles a number:

duplicate = lambda x: x * 2
result = duplicate(5)
print(result) # Prints: 10

#* Example 2:
# Function that adds two numbers:

sum = lambda x, y: x + y
result = sum(3, 4)
print(result) # Prints: 7

#*Example 3:
# Function that checks if a number is even:

is_even = lambda x: x % 2 == 0
print(is_even(6)) # Print: True
print(is_even(7)) # Print: False

#? Use in Higher Order Functions:

# Lambda functions are commonly used in conjunction with higher order functions such as `map()`, `filter()`,
# and `reduce()`.

#* Using `map()`:

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares) # Prints: [1, 4, 9, 16, 25]

#* Using `filter()`:

numbers = [1, 2, 3, 4, 5]
pairs = list(filter(lambda x: x % 2 == 0, numbers))
print(pairs) # Prints: [2, 4]

#? Limitations of Lambda Functions:

#* - **Simplicity:**
# Lambda functions are designed to be simple and concise. If you need more complex logic, it is better to
# use a function defined with `def`.

#* - **Lack of documentation:**
# Being anonymous, lambda functions lack docstrings, which can make them difficult to understand. its
# purpose without further comment.

# Lambda functions are a powerful and useful tool in Python, especially in situations where
# small, specific functions are needed. However, it is important to use them in moderation and
# consider the clarity and readability of the code.