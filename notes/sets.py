
#* Sets - Python

# In Python, a set is an unordered collection without duplicate elements. Sets are useful
# to perform operations such as union, intersection, difference, and more. Here I present information
# basic on how to work with sets in Python:

# Creating Sets:

# You can create sets using curly braces `{}` or the `set()` function.

empty_set = set() # creates an empty set
number_set = {1, 2, 3, 4, 5}
letter_set = set("abcdef")

# Basic Operations with Sets:

# - **Add Elements:**

set = {1, 2, 3}
set.add(4)
set.update({5, 6})

# - **Delete Elements:**

set = {1, 2, 3, 4, 5}
set.remove(3)
set.discard(4)

# `remove` removes the specified element and raises an error if the element is not present, while
# that `discard` removes the element if it is present, but does not raise an error if it is not found.

# - **Set Operations:**

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
union_AB = A.union(B) # or also A | b

# Intersection
intersection_AB = A.intersection(B) # or also A & B

# Difference
difference_AB = A.difference(B) # or also A - B

# Symmetric Difference (elements that are in A or B, but not both)
symmetric_difference_AB = A.symmetric_difference(B) # or also A ^ B

# Verification of Membership:

# You can check if an element is present in a set using the `in` keyword.

set = {1, 2, 3, 4, 5}
print(3 in set) # True
print(6 in set) # False

# Iteration on Sets:

# You can iterate over the elements of a set using a `for` loop.

set = {1, 2, 3, 4, 5}
for element in set:
     print(element)

# Empty a Set:

# You can clear an array using the `clear()` method.

set = {1, 2, 3}
set.clear() # empty set

# Immutable Sets:

# Python also has an immutable set type called "frozenset". Unlike the sets
# regular, "frozensets" cannot be modified after they are created.

immutable_set = frozenset([1, 2, 3])

# Sets are useful when you need to perform set math operations or when you want
# make sure there are no duplicate elements in a collection.
# Experiment and practice to get familiar with handling sets in Python!
