
#* Lists - Python

# In Python, a list is a data structure that stores an ordered collection of elements. Here I present to
# you basic information about how to work with lists in Python:

#* List Creation:

# You can create lists using `[]` square brackets and separating elements with commas.

my_list = [1, 2, 3, 4, 5]
names = ["Juan", "Ana", "Carlos"]
mix = [1, "two", True, 3.14]

#* Access to Elements:

# You can access the elements of a list using indexes. The indices start from 0.

my_list = [10, 20, 30, 40, 50]
first_item = my_list[0] #10
second_item = my_list[1] #20

# You can also use negative indexes to count from the end of the list.

last_item = my_list[-1] # 50

#* Element Modification:

# You can modify individual elements of a list using indexes.

names = ["Juan", "Ana", "Carlos"]
names[1] = "Mary"
print(names) # ["Juan", "Maria", "Carlos"]

#* Operations on Lists:

#? Add Elements:

# - `append()`: Adds an element to the end of the list.

names = ["Juan", "Ana", "Carlos"]
names.append("Luis")
print(names) # ["Juan", "Ana", "Carlos", "Luis"]

# - `insert()`: Inserts an element at a specific position.

names = ["Juan", "Ana", "Carlos"]
names.insert(1, "Luis")
print(names) # ["Juan", "Luis", "Ana", "Carlos"]

#? Delete Elements:

# - `remove()`: Removes a specific element by value.

names = ["Juan", "Ana", "Carlos"]
names.remove("Ana")
print(names) # ["Juan", "Carlos"]

# - `pop()`: Removes an element at a specific position and returns that element.

names = ["Juan", "Ana", "Carlos"]
deleted_element = names.pop(1)
print(deleted_element) # "Ana"
print(names) # ["Juan", "Carlos"]

#* Length of a List:

# You can get the length of a list using the `len()` function.

names = ["Juan", "Ana", "Carlos"]
length = len(names) #3

#? List Slicing:

# You can get portions of a list using slicing.

my_list = [1, 2, 3, 4, 5]
portion = my_list[1:4] # [2, 3, 4]

#? List Methods:

# Python provides several built-in methods for working with lists. Some examples:

my_list = [3, 1, 4, 1, 5, 9, 2]

# Sort the list
my_list.sort() # [1, 1, 2, 3, 4, 5, 9]

# Add items from another list
my_list.extend([6, 5, 3]) # [1, 1, 2, 3, 4, 5, 9, 6, 5, 3]

# Count occurrences of an element
count = my_list.count(3) #2

# These are just some basics on how to work with lists in Python. The lists are a versatile and
# fundamental data structure in programming, and Python provides many tools powerful to manipulate.
# Experiment and practice to improve your understanding of lists in Python!