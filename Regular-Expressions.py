
#* Regular Expressions - Python

# In Python, regular expressions (regex) are sequences of characters that define a pattern of
# search. The `re` module provides functions for working with regular expressions. Here you have one
# basic description of how to use regular expressions in Python:

#? Import Module `re`:

import re

#? Principal functions:

#* 1. `re.match()`:

# This function looks for the pattern only at the beginning of the string.

import re

pattern = re.compile(r'\d+')
result = pattern.match('123abc')

if result:
     print("Match found:", result.group())
else:
     print("No match found.")

#? 2. `re.search()`:

# Search for the pattern anywhere in the string.

result = re.search(r'\d+', 'abc123def')

if result:
     print("Match found:", result.group())
else:
     print("No match found.")

#? 3. `re.findall()`:

# Find all occurrences of the pattern in the string and return a list.

result = re.findall(r'\d+', 'abc123def456ghi')

print("Matches found:", result)

#? 4. `re.finditer()`:

# Find all occurrences of the pattern in the string and return an iterator of objects
# coincidence.

iterator = re.finditer(r'\d+', 'abc123def456ghi')

for result in iterator:
     print("Match found:", result.group())

#? Common Symbols in Regular Expressions:

#* - **`.`:**
# Matches any character except a new line.
#* - **`^`:**
# Matches the start of the string.
#* - **`$`:**
# Matches the end of the string.
#* - **`*`:**
# Matches zero or more occurrences of the previous element.
#* - **`+`:**
# Matches one or more occurrences of the previous element.
#* - **`?`:**
# Matches zero or one repetition of the previous element.
#* - **`[]`:**
# Matches any character inside the square brackets.
#* - **`|`:**
# Works like an OR operator.
#* - **`()`:**
# Group regular expressions.

#? Examples of Use:

# Find email addresses
mail_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\ b')
text = "Contact: user@example.com, support@domain.com"

mail_results = mail_pattern.findall(text)
print("Emails found:", mail_results)

# Find phone numbers
phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
text = "Phone numbers: 123-456-7890, 987-654-3210"

phone_result = phone_pattern.findall(text)
print("Phones found:", phone_result)

# These are just basic examples of how to use regular expressions in Python. You can build patterns
# more complex to meet your specific needs. The official Python documentation for the
# module `re` provides additional details and more advanced use cases:
# [Re Module - Regular Expressions](https://docs.python.org/3/library/re.html).
