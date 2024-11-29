
#* Functions - Python

# Functions in Python are reusable blocks of code that perform a specific task. Here
# you have basic information on how to work with functions in Python:

#? Definition of Functions:

# You can define a function using the `def` keyword, followed by the function name and
# parentheses that can contain the function parameters. The function definition ends with two
# points `:` and the function body is indented.

def greet(name):
     """
     This function prints a greeting.
     """
     print("Hello, " + name + "!")

#? Function Call:

# To call a function, simply type the name of the function followed by parentheses that
# contain the arguments (if any).

greet("John")

#? Parameters and Arguments:

# Parameters are variables that are defined in the function signature, while arguments are
# the actual values that are passed to the function when it is called.

def sum(a, b):
     result = a + b
     return result

#? Function call with arguments
sum_result = sum(3, 5)
print(sum_result) #8

#? Return Value:

# You can use the `return` keyword to return a value from a function. A function can
# have multiple `return`, but when one is reached, the function terminates.

def square(number):
     return number ** 2

square_result = square(4)
print(square_result) # 16

#? Arguments with Default Values:

# You can assign default values to the parameters of a function. These values are used if not
# A corresponding argument is provided during the function call.

def power(base, exponent=2):
     return base ** exponent

power_result = power(3)
print(power_result) #9

#? Functions with Variable Number of Arguments:

# You can use `*args` and `**kwargs` to allow a function to accept a variable number of
# positional and keyword arguments, respectively.

def print_args(*args, **kwargs):
     print("Positional arguments:", args)
     print("Keyword arguments:", kwargs)

print_args(1, 2, 3, name="John", age=25)

#? Scope of Variables (Scope):

# Variables defined inside a function have local scope, while those defined outside
# of a function have global scope.

global_variable = 10

def show_variable():
     local_variable = 5
     print("Local variable:", local_variable)
     print("Global variable:", global_variable)

show_variable()
print("Global variable outside the function:", global_variable)

#? Feature Documentation:

# You can include a docstring to describe the purpose and behavior of a function.

def sum(a, b):
     """
     This function returns the sum of two numbers.
     """
     return a + b

# These are some basics on how to work with functions in Python. The functions are essential for
# organizing and reusing code effectively. Experiment and practice to strengthen your skills in using
# functions!