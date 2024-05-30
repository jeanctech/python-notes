
#* Operators - Python

# In Python, operators are symbols that perform operations on one or more operands.
# Here you have one overview of the most common operators in Python:

#* 1. Arithmetic Operators:

# They perform basic mathematical operations.

# - **`+`**: Sum
# - **`-`**: Subtraction
# - **`*`**: Multiplication
# - **`/`**: Division (returns a floating point number)
# - **`//`**: Integer division (returns an integer)
# - **`%`**: Module (remainder of division)
# - **`**`**: Exponent

a = 10
b = 3

sum = a + b
subtraction = a - b
multiplication = a * b
division = a/b
integer_division = a // b
module = a % b
exponent = a ** b

print("Sum:", sum)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Integer Division:", integer_division)
print("Module:", module)
print("Exponent:", exponent)

#? 2. Comparison Operators:

# Compare two values and return a boolean result.

# - **`==`**: Equals
# - **`!=`**: Not equal to
# - **`<`**: Less than
# - **`>`**: Greater than
# - **`<=`**: Less than or equal to
# - **`>=`**: Greater than or equal to

x = 5
y = 8

equals = x == y
not_equal = x != y
less_than = x < y
greater_than = x > y
less_than_equal = x <= y
greater_or_equal = x >= y

print("Equal:", equals)
print("Not Equal:", not_equal)
print("Less Than:", less_than)
print("Greater Than:", greater_than)
print("Less than or Equal:", less_than_equal)
print("Greater or Equal:", greater_or_equal)

#* 3. Logical Operators:

# Combine boolean expressions.

# - **`and`**: Returns True if both expressions are True
# - **`or`**: Returns True if at least one expression is True
# - **`not`**: Negates the boolean expression

p = True
q = False

and_result = p and q
or_result = p or q
not_result = not p

print("And:", and_result)
print("Or:", or_result)
print("Not:", not_result)

#* 4. Assignment Operators:

# Assign a value to a variable.

# - **`=`**: Basic assignment
# - **`+=`**: Assignment with addition
# - **`-=`**: Assignment with subtraction
# - **`*=`**: Assignment with multiplication
# - **`/=`**: Assignment with division

number = 10
number += 5 # Equivalent to: num = num + 5
print("Number after addition:", number)

number -= 3 # Equivalent to: num = num - 3
print("Number after subtraction:", number)

number*= 2 # Equivalent to: num = num * 2
print("Number after multiplication:", number)

number /= 4 # Equivalent to: num = num / 4
print("Number after division:", number)

# These are some of the most common operators in Python. As you progress in your learning, you can meet
# more specialized and advanced operators. Experiment with these operators and practice to strengthen your
# Python skills!
