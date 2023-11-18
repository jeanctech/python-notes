
#* Dictionaries - Python

# In Python, a dictionary is a data structure that allows you to store key-value pairs. each key
# must be unique, and the key and value can be of any type. Here I present basic information
# on how to work with dictionaries in Python:

#? Creation of Dictionaries:

# You can create dictionaries using `{}` curly braces and specifying key-value pairs.

my_dictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}

# You can also use the `dict()` function to create dictionaries.

other_dictionary = dict(key1="value1", key2="value2", key3="value3")

#? Access to Elements:

# You can access the values of a dictionary using keys.

my_dictionary = {"name": "John", "age": 25, "city": "Example"}

print(my_dictionary["name"]) # "John"
print(my_dictionary["age"]) # 25

#? Modification and Addition of Elements:

# You can modify the value of an existing key or add new key-values.

my_dictionary = {"name": "John", "age": 25, "city": "Example"}
my_dictionary["age"] = 26 # Modification
my_dictionary["gender"] = "male" # Adding new key-value

#? Element Removal:

# You can use the `del` keyword to delete a key and its associated value.

my_dictionary = {"name": "John", "age": 25, "city": "Example"}
del my_dictionary["city"] # Delete the key "city"

### Dictionaries Methods:

#? Python provides several built-in methods for working with dictionaries. Some examples:

my_dictionary = {"name": "John", "age": 25, "city": "Example"}

# Get all keys
keys = my_dictionary.keys()

# Get all values
values = my_dictionary.values()

# Get key-value pairs as tuples
items = my_dictionary.items()

#? Iteration on Dictionaries:

# You can iterate over the keys, values, or key-value pairs of a dictionary using `for` loops.

my_dictionary = {"name": "John", "age": 25, "city": "Example"}

# Iterate over keys
for key in my_dictionary:
     print(key)

# Iterate over the values
for value in my_dictionary.values():
     print(value)

# Iterate over key-value pairs
for key, value in my_dictionary.items():
     print(key, value)

#? Defaultdict and OrderedDict:

# Python also provides other variants of dictionaries such as `defaultdict` which allows you to assign
# defaults to non-existent keys, and `OrderedDict` which maintains the insertion order of the
# items.

from collections import defaultdict, OrderedDict

#defaultdict
default_dict = defaultdict(int)
default_dict["a"] += 1 # Does not generate error even if "a" is not present

#OrderedDict
ordered_dict = OrderedDict()
ordered_dict["b"] = 2
ordered_dict["a"] = 1
print(ordered_dict) # OrderedDict([('b', 2), ('a', 1)])

# These are just some basics on how to work with dictionaries in Python. The
# dictionaries are versatile and powerful data structures that are widely used in
# Python programming. Experiment and practice to improve your understanding of dictionaries in Python!