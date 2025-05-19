
#* Poo - Python

# Object Oriented Programming - Poo - It is a programming paradigm that uses objects and classes
# to organize and structure the code. In Python, everything is an object, and you can use Poo to
# create your own classes and objects. Here's a basic introduction to Poo in Python:

# 1. **Classes and Objects:**

# In Poo, a **class** is a model or template for creating objects. An **object** is an instance
# particular to a class.

class Person:
     def __init__(self, name, age):
         self.name = name
         self.age = age

     def greet(self):
         print(f"Hello, I am {self.name} and I am {self.age} years old.")

# Create an object of the Person class

john = Person("John", 25)

# Access the attributes and methods of the object

print(john.name) # Juan
john.greet() # Print: Hello, I'm Juan and I'm 25 years old.

# 2. **Methods and Attributes:**

# - **Methods:**
# Functions defined within a class. They can access the attributes of the class.

# - **Attributes:**
# Variables that store information about the object.

# 3. **The `__init__` Method:**

# It is a special method used to initialize the attributes of an object when it is created.

# 4. **Encapsulation:**

# Encapsulation is the concept of limiting access to certain components of an object and hiding the
# implementation details.

class BankAccount:
     def __init__(self, initial_balance):
         self.__balance = initial_balance # Private attribute

     def get_balance(self):
         return self.__balance

     def deposit(self, quantity):
         if quantity > 0:
             self.__balance += quantity

     def withdraw(self, quantity):
         if quantity > 0 and quantity <= self.__balance:
             self.__balance -= quantity

account = BankAccount(1000)
print(account.get_balance()) # 1000

account.deposit(500)
print(account.get_balance()) # 1500

account.withdraw(200)
print(account.get_balance()) # 1300

# 5. **Inheritance:**

# Inheritance allows a class to inherit attributes and methods from another class. The class that inherits is called
# derived class or subclass, and the class from which it is inherited is called the base class or superclass.

class Animal:
     def __init__(self, name):
         self.name = name

     def make_sound(self):
         pass

class Dog(Animal):
     def make_sound(self):
         return "Woof!"

class Cat(Animal):
     def make_sound(self):
         return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name) # Buddy
print(dog.make_sound()) # Woof!

print(cat.name) # Whiskers
print(cat.make_sound()) # Meow!

# 6. **Polymorphism:**
# Polymorphism allows objects of different classes to be treated as objects of the same base class.

def make_sound(animal):
     return animal.make_sound()

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(make_sound(dog)) # Woof!
print(make_sound(cat)) # Meow!

# These are just some basics of Poo in Python. The Poo is a powerful paradigm that
# allows you to organize and structure your code in a more efficient and maintainable way.
# Practice and experiment to strengthen your skills in object-oriented programming!
