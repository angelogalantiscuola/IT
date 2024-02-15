%% Begin Waypoint %%
- [classes_and_objects](./classes_and_objects.md)
- [magic_methods](./magic_methods.md)
- [multiple_inheritance](./multiple_inheritance.md)
- [python_OOP_mindmap](./python_OOP_mindmap.md)
- [UML_class_diagram](./UML_class_diagram.md)

%% End Waypoint %%


```table-of-contents
```
# OOP - Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to design applications. In OOP, objects are self-contained entities that store data and code. Classes are blueprints for creating objects.

## Four Pillars of OOP

Python is a multi-paradigm programming language that supports Object-Oriented Programming (OOP). Here are some specific features of Python regarding OOP:

1. Classes and Instances: Python allows you to define classes using the class keyword and create instances of these classes.

2. Inheritance: Python supports single and `multiple inheritance`, allowing classes to inherit attributes and methods from one or more other classes.

3. Encapsulation: Python doesn't have strict access modifiers like private or protected as in other languages. However, it uses a convention: a variable or method prefixed with an underscore (_) is intended for `internal use`, and a double underscore (__) invokes `name mangling` to avoid naming conflicts in subclasses.

4. Polymorphism: Python supports polymorphism, meaning that a subclass can override a method of its superclass.

5. `Magic Methods`: Python provides magic methods, also known as dunder methods (double underscore methods), such as __init__, __str__, __eq__, etc. These methods provide special syntactic features or do special things. For example, __init__ is a constructor method and __str__ returns a printable string representation of the object.

## Simple Example

```python
class Dog:
    """A class to represent a dog."""

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"Woof! My name is {self.name} and I am a {self.breed}.")

my_dog = Dog("Fido", "Golden Retriever", 3)

my_dog.bark()
```

## Benefits of OOP

Here are some of the benefits of using OOP in Python:

- OOP makes it easier to model real-world entities and their relationships.
- OOP helps to reduce code duplication and make it more reusable.
- OOP makes code more modular and easier to maintain.
- OOP makes code more flexible and extensible.

## Example of each of the four main pillars of OOP in Python

```python
class Animal:
    """An abstract class to represent an animal."""

    def __init__(self, name):
        self.name = name

    # Abstract method
    def make_sound(self):
        pass

# Concrete subclasses
class Dog(Animal):
    """A class to represent a dog."""

    def make_sound(self):
        print(f"Woof! My name is {self.name}.")

class Cat(Animal):
    """A class to represent a cat."""

    def make_sound(self):
        print(f"Meow! My name is {self.name}.")

# **Encapsulation:** The `Animal` class encapsulates the `name` attribute and the `make_sound()` method. This means that the `name` attribute can only be accessed and modified through the `Animal` class methods.

# **Inheritance:** The `Dog` and `Cat` classes inherit from the `Animal` class. This means that they inherit all of the attributes and methods of the `Animal` class.

# **Polymorphism:** The `Dog` and `Cat` classes override the `make_sound()` method that is inherited from the `Animal` class. This allows them to implement their own custom behavior for the `make_sound()` method.

# Example usage:

# Create a dog and a cat object
dog = Dog("Fido")
cat = Cat("Garfield")

# Call the make_sound() method on the dog and cat objects
dog.make_sound()
cat.make_sound()
```
