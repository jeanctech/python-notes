
#* List Comprehension - Python

# List comprehension, also known as "list comprehension" in English, is a concise and
# expressive way to create lists in Python. Provides a more readable and efficient way to generate lists
# apply expressions to each element of another sequence (or even multiple sequences). Here you have one
# basic description of how list comprehensions work:

# Basic Syntax:

# The general syntax of a list comprehension is as follows:

new_list = [x**2 for x in range(10)]
print(new_list)

# - **`expression`:**
# The expression that is evaluated and added to the new list.
# - **`element`:**
# The variable that takes values from the sequence.
# - **`sequence`:**
# The sequence from which the elements are taken.
# - **`condition` (optional):**
# A condition that filters the elements of the sequence.

# Examples:

# Basic Example:

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

# Conditions:

# Create a list of even numbers from 0 to 9
pairs = [x for x in range(10) if x % 2 == 0]
print(pairs)

# Nested Understandings:

# Create a list of tuples with all combinations of two elements from two lists
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
combinations = [(letter, number) for letter in list1 for number in list2]
print(combinations)

# Conditional Expressions:

# Create a list of squares of even numbers and cubes of odd numbers
numbers = range(10)
results = [x**2 if x % 2 == 0 else x**3 for x in numbers]
print(results)

# Benefits:

# 1. **Readability:**
# List comprehensions are more concise and easier to read than traditional loops.
# 2. **Efficiency:**
# In many cases, list comprehensions are more efficient than creating lists using
# loops.

# Considerations:

# - **Do not abuse:**
# Although they are powerful, it is important not to overuse list comprehensions to maintain
# code readability.
# - **Generators:**
# In situations where you work with large data sets and do not need to store all the
# elements in memory, consider using generators instead of list comprehensions.

# List comprehensions are a valuable tool in Python for efficiently creating lists
# and expressive. Try different examples and experiment to become familiar with their use.
