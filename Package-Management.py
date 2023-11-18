
#* Package Management - Python

# In Python, a package is a way to organize and structure modules in a hierarchical directory. Packages
# allow modularity and code reuse. Here is a basic description how to manage packages in Python:

#? Structure of a Package:

# The basic structure of a package includes a directory that contains a special file called `__init__.py`.
# This file may be empty or may contain initialization code for the package.

'''
My Package/
|-- __init__.py
|-- module1.py
|-- module2.py
|-- subpackage/
| |-- __init__.py
| |-- module3.py
| |-- module4.py
'''

#? Creating a Package:

# To create a package, simply create a directory and place the `__init__.py` files and modules that you
# want to include in the package.

#? Importing Modules from a Package:

# You can import modules from a package in several ways:

# Import a specific module
from My_Module import module_0

# Import the entire package (and access modules with dot notation)
import My_Module
My_Module.module1.function()

# Import a specific module from a subpackage
from My_Module import module_3

#? Usage of `__init__.py`:

# The `__init__.py` file is executed when the package is imported. You can use it to initialize
# variables, configure the package, or perform other initialization tasks.

#? Relative Packages:

# You can use relative imports to reference modules within the same package. This is done
# using the dot (`.`) instead of the absolute package name.

#* Relative import example

from . My_Module import My_Module_1
from . My_Module import My_Module_2

#? Package Distribution:

# If you want to distribute your package for others to install, you can use tools like `setuptools`
# and create a `setup.py` file. Then, you can package your package and distribute it via Python
# Package Index (PyPI).

#? Example of `setup.py`:

from setuptools import setup, find_packages

setup(
     name='my_package',
     version='0.1',
     packages=find_packages(),
     install_requires=[
         # List of package dependencies
     ],
)

#? Creating an Installable Package:

#* 1.
# Organize your package as a directory structure with a `__init__.py` at each level.
#* 2.
# Create a `setup.py` file in the root directory of your package.
#* 3.
# Run `python setup.py sdist` to create a distributable source file.
#* 4.
# Publish your package on PyPI or share the generated file.

#? Package Installation:

# After you package your package, others can install it using `pip`:

#* pip install my_package

# These are the basics of working with packages in Python. Packages are a way Effective at organizing and
# sharing code in larger projects.
