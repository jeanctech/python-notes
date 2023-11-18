
#* Modules - Python

# In Python, a module is a file that contains Python definitions and declarations. You can use modules to
# organize your code more effectively and reuse functions, classes and variables in different parts of
# your program. Here is a basic description of how to work with modules in Python:

#? Creating a Module:

# To create a module, simply save your code in a file with the extension `.py`. For example,
# if you have the following code in a file called `My_Module.py`:

# Content of my_module.py

def greet(name):
     print(f"Hello, {name}!")

PI = 3.1416

class MyClass:
     def __init__(self, value):
         self.value = value

     def get_value(self):
         return self.value


#? Importing a Module:

# You can import a module into another script using the `import` keyword.

import My_Module

My_Module.greet("John")

object = My_Module.MyClass(42)
print(object.get_value())
print(My_Module.PI)


#? Import with Aliases:

# You can assign an alias to a module to simplify its use.

import My_Module as mm

mm.greet("Ana")

object = mm.MyClass(7)
print(object.get_value())
print(mm.PI)

#? Selective Import:

# You can also import only certain elements of the module.

from My_Module import greet, PI

greet("Carlos")
print(PI)

#? Importing All Content:

# You can import the entire contents of a module, but be aware that this can cause your code
# be less readable and prone to name conflicts.

from My_Module import *

greet("Maria")
print(PI)

#? Relative Routes and Packages:

# If you have a set of modules organized in directories, you can use relative paths or create
# a package.

'''
My project/
|-- main.py
|-- my_package/
| |-- __init__.py
| |-- module1.py
| |-- module2.py
'''

# In the `main.py` file, you can import modules from the package:

from My_Module import My_Module_1, My_Module_2

My_Module.greet("Peter")

#? Direct Execution of a Module:

# You can run a module as a script directly. The code inside the `if __name__ == block
# "__main__":` will only be executed if the module is run directly and not if it is imported into another script.

# Content of my_module.py

def greet(name):
     print(f"Hello, {name}!")

PI = 3.1416

class MyClass:
     def __init__(self, value):
         self.value = value

     def get_value(self):
         return self.value

if __name__ == "__main__":
     greet("Unknown user")
     object = MyClass(10)
     print(object.get_value())
     print(PI)

# When you run `my_module.py` as a script, the `if __name__ == "__main__":` block will be executed.

#*Bash
# python my_module.py

# These are some basics on how to work with modules in Python. The modules allow you organize and reuse
# your code effectively, making your code easier to maintain and readable program. Practice and experiment
# to strengthen your skills in using modules in Python!
