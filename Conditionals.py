
#* Conditionals - Python

# In Python, conditional structures allow you to execute specific code based on whether or not it is true.
# not a condition. Code blocks within conditional structures are indented, which
# means that indentation is crucial to determining which code belongs to which block. Here you have
# an overview of conditional structures in Python:

#? 1. **if - elif - else:**

# The `if` structure is used to perform a conditional check. You can use `elif`
# (short for "else if") to add additional conditions, and `else` to provide a block of
# code that will be executed if none of the above conditions are true.

age = 18

if age < 18:
     print("You are a minor.")
elif 18 <= age < 65:
     print("You are an adult.")
else:
     print("You are an older adult.")

#? 2. **Comparison Operators:**

# Comparison operators are used in conditions. Some examples include:

# - `==` (equals)
# - `!=` (not equal to)
# - `<` (less than)
# - `>` (greater than)
# - `<=` (less than or equal to)
# - `>=` (greater than or equal to)

#? 3. **Logical Operators:**

# Logical operators (`and`, `or`, `not`) allow you to combine multiple conditions.

temperature = 25

if temperature > 30 or temperature < 0:
     print("It's too hot or too cold.")
elif 0 <= temperature <= 30:
     print("The temperature is comfortable.")

#? 4. **Ternary Operator:**

# The ternary operator provides a concise way to write a conditional expression in a single
# line.

age = 20
message = "You are of legal age." if age >= 18 else "You are a minor."
print(message)

#? 5. **None and Empty Structures:**

# You can use the `None` keyword to represent a null value. Furthermore, the structures
# Conditionals can be used to check whether a list, string, or other object is empty.

my_list = []

if not my_list:
     print("The list is empty.")
else:
     print("The list is not empty.")

#? 6. **if Nested:**

# You can nest multiple `if` structures to handle more complex conditions.

note = 75

if note >= 90:
     print("A")
elif note >= 80:
     print("B")
elif note >= 70:
     print("C")
else:
     print("F")

# These are some of the basic constructs for working with conditional structures in Python.
# Practice with different conditions and scenarios to improve your understanding and skills in using
# conditionals.
