# Name mangling

Name mangling is a mechanism in Python to avoid naming conflicts in subclasses. This is particularly useful in the context of inheritance where a subclass might have an attribute or method with the same name as in the superclass.

In Python, any identifier of the form `__spam` (at least two leading underscores, at most one trailing underscore) is textually replaced with `_classname__spam`, where `classname` is the current class name with leading underscore(s) stripped.

```python
class MyClass:
    def __init__(self):
        self.__private_var = 10

    def access_private_var(self):
        return self.__private_var

# Create an instance of MyClass
obj = MyClass()

print(obj.access_private_var())  # Outputs: 10
print(obj.__private_var)  # Raises AttributeError: 'MyClass' object has no attribute '__private_var'
print(obj._MyClass__private_var)  # Outputs: 10
```

In this example, __private_var is a private variable due to name mangling. It can't be accessed directly using obj.__private_var, but it can be accessed using the mangled name obj._MyClass__private_var.

This feature helps to create a sort of "private" variables or methods, which cannot be directly accessed but can be accessed through a special syntax if needed. However, it's generally considered a bad practice to access these "private" variables or methods directly, as they are intended for internal use within the class.

## Magic methods

Magic methods in Python, also known as dunder methods (short for double underscore methods), are special methods that you can define to add "magic" to your classes. They are always surrounded by double underscores (e.g., __init__, __str__).

Here are some commonly used magic methods:

__init__(self, ...): This method is used for initializing an object. It sets the initial state of the object.

__str__(self): This method should return a string, and is used when we use the str() function on our object or when we use print().

__eq__(self, other): This method checks if this object is equal to other.

__len__(self): This method should return the "length" of the object, whatever that means for the object.

__getitem__(self, key): This method is used to access the object using obj[key] syntax.

__setitem__(self, key, value): This method is used to set the value of obj[key] to value.

Here's an example of a class with some magic methods:

```python
class MagicClass:
    def __init__(self, name):
        self.name = name
        self.data = {}

    def __str__(self):
        return f"MagicClass named {self.name}"

    def __eq__(self, other):
        if isinstance(other, MagicClass):
            return self.name == other.name
        return False

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

# Create an instance of MagicClass
magic = MagicClass("GitHub Copilot")

# Use __str__
print(magic)  # Outputs: MagicClass named GitHub Copilot

# Use __eq__
print(magic == MagicClass("GitHub Copilot"))  # Outputs: True

# Use __getitem__ and __setitem__
magic["language"] = "Python"
print(magic["language"])  # Outputs: Python
```
