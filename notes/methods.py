
#* Methods - Python

# In Python, methods are functions defined within a class. Each object created from the class can call
# these methods to perform certain operations or manipulate the attributes of the object. Here is a basic
# description of how to work with methods in Python:

# Method Definition:

# Methods are defined within a class in a similar way to functions, but are linked to the class and can
# access the attributes of the instance using the `self` keyword.

class Car:
     def __init__(self, make, model):
         self.make = make
         self.model = model
         self.power_state = False

     def turn(self):
        self.power_state = True
        print(f"The car {self.make} {self.model} is on.")

     def shutdown(self):
         self.power_state = False
         print(f"The car {self.make} {self.model} is off.")

# In this example, the `Car` class has three methods: `__init__` (the constructor), `ignite`, and
# `shutdown`. The `__init__` method is executed automatically when creating a new object, and the
# methods `turn on` and `turn off` are actions that the car can perform.

# Method Call:

# To call a method, use dot notation on the object followed by the method name and parentheses.

my_car = Car("Toyota", "Camry")
my_car.turn()
my_car.shutdown()

# Methods with Parameters:

# Methods can accept parameters in the same way as functions.

class Calculator:
     def add(self, a, b):
         return a + b

     def subtract(self, a, b):
         return a - b

calc = Calculator()
sum_result = calc.sum(5, 3)
subtraction_result = calc.subtract(8, 2)

# Class Methods and Static Methods:

# - **Class Methods:**

# They are defined with the `@classmethod` decorator and take the class as their first parameter instead of the
# instance. They can be called on the class and on the instances.

class MyClass:
     value = 0

     @classmethod
     def increment_value(cls):
         cls.value += 1

MyClass.incrementar_valor() # Called in the class
print(MyClass.value) # Prints: 1

# - **Static Methods:**

# They are defined with the `@staticmethod` decorator and do not take the class or instance as their
# first parameter They can be called in class.

class Utilities:
     @staticmethod
     def add(a, b):
         return a + b

result = Utilities.sumar(3, 4) # Called in the class

# Special Methods:

# Some methods in Python have a special meaning and are called automatically in certain situations. Some
# examples include `__str__` to represent the text string of an object and `__len__` to get the length of
# an object.

class Point:
     def __init__(self, x, y):
         self.x = x
         self.y = y

     def __str__(self):
         return f"({self.x}, {self.y})"

p = Point(1, 2)
print(str(p)) # Prints: (1, 2)

# These are some basics on how to work with methods in Python. The methods are essential in Object
# Oriented Programming - Poo and allow the interaction and manipulation of objects effectively. Practice
# and experiment to strengthen your skills in using methods!
