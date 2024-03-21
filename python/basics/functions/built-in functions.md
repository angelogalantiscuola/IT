# Built-in Functions

[Built-in Functions — Python 3.12.0 documentation](https://docs.python.org/3/library/functions.html)

- **Logical Operations:**
  - `all()`: Returns `True` if all items in an iterable are true, otherwise it returns `False`.
  - `any()`: Returns `True` if any item in an iterable is true. If the iterable is empty, return `False`.

- **Type Conversion:**
  - `ascii()`: Returns a string containing a printable representation of an object and escapes the non-ASCII characters in the string using \\x, \\u, or \\U escapes.
  - `bin()`: Converts an integer number to a binary string prefixed with “0b”.
  - `chr()`: Returns a string representing a character whose Unicode code point is the integer specified.
  - `hex()`: Converts an integer to a lowercase hexadecimal string prefixed with “0x”.

- **Iterables and Iterators:**
  - `dir()`: Returns all properties and methods of the specified object, without the values.
  - `enumerate()`: Adds a counter to an iterable and returns it in the form of an enumerating object.
  - `filter()`: Returns an iterator from the elements of an iterable for which a function returns true.
  - `iter()`: Returns an iterator object.
  - `map()`: Applies a function to all items in an input list and returns a list containing the results.
  - `next()`: Retrieves the next item from the iterator.

- **File Operations:**
  - `open()`: Opens a file and returns it as a file object.

- **Output Functions:**
  - `print()`: Prints the specified message to the screen, or other standard output device.

- **Object-Oriented Programming (OOP) and Class Related Functions**:
  - `property()`: Used to get, set, and delete a property of a class.
  - `super()`: Used to call a method from a parent or sibling class.

- **Type Conversion and Inspection Functions**:
  - `type()`: Returns the type of an object.
  - `repr()`: Returns a string containing a printable representation of an object.

- **Sequence Handling Functions**:
  - `range()`: Generates a sequence of numbers within a given range.
  - `zip()`: Returns an iterator of tuples, where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
  - `sorted()`: Returns a new sorted list from elements in an iterable.

- **Namespace and Variable Handling Functions**:
  - `vars()`: Returns the `__dict__` attribute of an object which can be a module, class, instance, or any object having the `__dict__` attribute.
