
#* Control Structure - Python

# Control structures in Python allow you to modify the flow of program execution.
# The main control structures in Python are as follows:

#? 1. **Selection Structures:**

#* - **if-elif-else:**

# Allows code blocks to be executed depending on the evaluation of conditions.

age = 18

if age < 18:
     print("You are a minor.")
elif 18 <= age < 65:
     print("You are an adult.")
else:
     print("You are an older adult.")

#? 2. **Iteration Structures:**

#* - **for:**

# Iterates over the elements of a sequence (such as a list, tuple, or string).

for i in range(5):
     print(i)

#* - **while:**

# Execute a block of code as long as a condition is true.

counter = 0

while counter < 5:
     print(counter)
     counter += 1

#? 3. **Flow Control Structures:**

#* - **break:**
# Exit the current loop.

for i in range(10):
     if i == 5:
         break
     print(i)

#* - **continue:**
# Jump to the next iteration of the loop.

for i in range(10):
     if i == 5:
         continue
     print(i)

#? 4. **Exception Structures:**

#* - **try-except:**
# Allows exceptions (errors) to be handled in a controlled manner.

try:
     result = 10 / 0
except ZeroDivisionError:
     print("Error: division by zero.")

#? 5. **Context Structures:**

#* - **with:**
# Used to manage resources, such as files, efficiently.

with open("file.txt", "r") as file:
     content = file.read()
     print(content)

# These control structures are fundamental to Python development and allow you to control the
# Program execution flow effectively. Use them as needed in your programs to
# meet the specific requirements of your business logic.
