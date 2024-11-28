
#* Classes - Python

# In Python, a class is a template for creating objects. Objects are instances of a
# class, and each object can have associated attributes and methods. Here is a basic description of
# how to work with classes in Python:

#? Definition of a Class:

# To define a class in Python, use the `class` keyword, followed by the class name and
# colon `:`. The body of the class contains attributes and methods.

class Person:
     def __init__(self, name, age):
         self.name = name
         self.age = age

     def greet(self):
         print(f"Hello, I am {self.name} and I am {self.age} years old.")

# In this example, `Person` is the name of the class. The `__init__` function is a special constructor
# which is called when a new object of the class is created. `self` is a reference to the current object
# and is used to access the object's attributes.

#? Object Creation:

# Once you have defined a class, you can create objects (instances of the class) using the syntax
# of function call.

john = Person("John", 25)
ana = Person("Ana", 30)

john.greet() # Print: Hello, I'm Juan and I'm 25 years old.
ana.greet() # Print: Hello, I am Ana and I am 30 years old.

#? Attributes and Methods:

#* - **Attributes:**
# They are variables that store information about the object.

#* - **Methods:**
# They are functions defined within a class and operate on the attributes of the object.

#? The `__init__` Method:

# It is a special method called a constructor. It runs automatically when a new object is created and
# is used to initialize the object's attributes.

#? Access to Attributes and Methods:

# You can access the attributes and methods of an object using dot notation.

john_name = john.name
john.greet()

#? Encapsulation:

# In Python, there is no strict encapsulation like in some other programming languages, but you can
# conventionally indicate that an attribute or method is "private" by adding an underscore before the
# name.

class Car:
     def __init__(self, make, model):
         self._brand = make
         self._model = model

     def get_information(self):
         return f"{self._brand} {self._model}"

my_car = Car("Toyota", "Camry")
print(my_car._brand) # "Private" access


#? Inheritance:

# Allows a class (subclass) to inherit attributes and methods from another class (superclass).

class Animal:
     def make_sound(self):
         print("Makes some sound")

class Dog(Animal):
     def make_sound(self):
         print("Woof!")

class Cat(Animal):
     def make_sound(self):
         print("Meow!")

dog = Dog()
cat = Cat()

dog.make_sound() # Print: Woof!
cat.make_sound() # Print: Meow!

# These are some basics on how to work with classes in Python. Classes are
# fundamentals in Object Oriented Programming - Poo and allow you to organize and structure
# your code more efficiently and reusable. Practice and experiment to strengthen your
# skills in using classes in Python!.