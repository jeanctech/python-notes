
#* Inheritance - Python

# Inheritance is a fundamental concept in Object Oriented Programming - Poo that allows a
# class (called subclass or derived class) inherit attributes and methods from another class (called
# superclass** or base class). Inheritance facilitates code reuse and allows the creation of
# class hierarchies. Here is a more detailed description of inheritance in Python:

#? Basic Inheritance Syntax:

class Animal:
     def __init__(self, name):
         self.name = name

     def make_sound(self):
         return "Makes some sound"

# Derived class that inherits from Animal
class Dog(Animal):
     def make_sound(self):
         return "Woof!"

# Derived class that inherits from Animal
class Cat(Animal):
     def make_sound(self):
         return "Meow!"

# Create instances of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Access the attributes and methods of the superclass
print(dog.name) # Buddy
print(dog.make_sound()) # Woof!
print(cat.name) # Whiskers
print(cat.make_sound()) # Meow!

#? In this example, `Dog` and `Cat` are subclasses of the `Animal` class. They automatically inherit the constructor (`__init__`) and the `make_sound` method from the `Animal` class. However, they can override or extend these methods as needed.

#? Special and `super()` Methods:

# The `super()` function is used to call a method of the super class. Special methods, such as
# `__init__` and `__str__` can also be overridden in the subclass.

class Vehicle:
     def __init__(self, make, model):
         self.make = make
         self.model = model

     def get_information(self):
         return f"{self.brand} {self.model}"

# Subclass that inherits from Vehicle
class Car (Vehicle):
     def __init__(self, brand, model, color):
         super().__init__(brand, model) # Call the __init__ of the superclass
         self.color = color

     def get_information(self):
         vehicle_info = super().get_information()
         return f"{vehicle_info} of color {self.color}"

# Create instance of the subclass
my_car = Car("Toyota", "Camry", "blue")

# Access the attributes and methods of the superclass
print(my_car.get_information()) # Blue Toyota Camry

#? Multiple Inheritance:

# In Python, a class can inherit from multiple classes. This is known as multiple inheritance.

class A:
     def show(self):
         print("Class A")

class B:
     def show(self):
         print("Class B")

# Class that inherits from A and B
class C (A, B):
     pass

instance_c = C()
instance_c.show() # Will print "Class A", since A is the first in the list of base classes

# It is important to take into account the resolution of methods in multiple inheritance, since Python
# follows a specific order called Mro - Method Resolution Order.

# Inheritance is a powerful tool in Poo that allows you to build class hierarchies and organize
# your code more effectively. However, it is also important to use it sparingly and understand
# the associated design implications.
