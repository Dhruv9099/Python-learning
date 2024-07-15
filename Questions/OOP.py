# OOP is a paradigm that uses objects and classes. It focuses on using objects that interact with one another.


# Object-Oriented Programming example
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an instance of Dog
dog = Dog("Buddy", 5)
print(dog.bark())




# Procedural Programming
# Procedural programming is a paradigm derived from structured programming. It is based on the concept of procedure calls, where procedures (also known as routines or functions) are the main building blocks.


# Procedural programming example
def greet(name):
    return f"Hello, {name}!"

# Calling the procedure
print(greet("Alice"))
