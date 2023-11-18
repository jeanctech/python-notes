
#* Tuples - Python

# In Python, a tuple is a data structure similar to a list, but unlike lists, Tuples are immutable,
# meaning you can't change their contents once they've been created. Here I present basic information
# about how to work with tuples in Python:

#? Tuple Creation:

# You can create tuples using `()` parentheses and separating elements with commas.

my_tuple = (1, 2, 3, 4, 5)
names = ("Juan", "Ana", "Carlos")
mix = (1, "two", True, 3.14)

# You can also create a tuple without parentheses, simply separating the elements with commas.

my_tuple_without_parentheses = 1, 2, 3

#? Access to Elements:

# As with lists, you can access the elements of a tuple using indexes.

my_tuple = (10, 20, 30, 40, 50)
first_item = my_tuple[0] # 10
second_item = my_tuple[1] # 20

# You can also use negative indexes and slicing in a similar way to lists.

#? Tuple Immutability:

# Unlike lists, tuples cannot be modified after they are created. This means that you cannot add, remove,
# or modify elements of a tuple once it has been created.

my_tuple = (1, 2, 3)
# This will generate an error
my_tuple[0] = 10

#? Basic Operations on Tuples:

# - **Tuple Concatenation:**

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2 # (1, 2, 3, 4, 5, 6)

# - **Repetition of Tuples:**

replicated_tuple = tuple1 * 3 # (1, 2, 3, 1, 2, 3, 1, 2, 3)

#? Tuple Unpacking:

# You can assign the elements of a tuple to individual variables on a single line.

coordinates = (10, 20, 30)
x, y, z = coordinates
print(x) #10
print(y) #20
print(z) #30

#? Advantages of Tuples:

#* - **Immmutability:**
# Tuples are useful when you need to ensure that the data does not change.

#* - **Efficiency:**
# Tuples are more efficient in terms of space and processing time than lists.

#? When to Use Tuples:

# - When data should not change over time.
# - To represent sets of heterogeneous elements that form a single entity (e.g. `(x, y, z)` coordinates).

# These are some basics on how to work with tuples in Python. Although they are similar to the lists, the
# immutability of tuples makes them useful in specific situations. Explore and practice to strengthen your
# understanding of tuples in Python!