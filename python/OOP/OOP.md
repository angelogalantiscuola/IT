%% Begin Waypoint %%
- [associations](./associations.md)
- [OOP_in_Python](./OOP_in_Python.md)
- [python_OOP_mindmap](./python_OOP_mindmap.md)

%% End Waypoint %%

# OOP - Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to design applications. In OOP, objects are self-contained entities that store data and code. Classes are blueprints for creating objects.

## Four Pillars of OOP

OOP is based on four main pillars:

- **Encapsulation**: Encapsulation is the process of wrapping data and code together into a single unit. This makes it easier to manage and protect the data.
- **Abstraction**: Abstraction is the process of hiding the implementation details of an object and exposing only its essential functionality. This makes the code more reusable and easier to understand.
- **Inheritance**: Inheritance allows you to create new classes based on existing classes. This can help you to reuse code and avoid duplication.
- **Polymorphism**: Polymorphism allows objects of differe

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

# **Abstraction:** The `Animal` class is an abstract class. This means that it cannot be instantiated directly. Instead, it must be subclassed and the `make_sound()` method must be implemented in the subclasses. This allows us to define a common interface for all animals, without specifying the concrete implementation of each animal.

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
