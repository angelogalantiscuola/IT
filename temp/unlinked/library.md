### Function vs library

> An analogy for a library and a function is a book and a chapter. A book is a collection of chapters that provide some information or knowledge. A book can contain one or more chapters, depending on how it organizes its content. A chapter is a section of text that covers a specific topic and can be read independently. A chapter has a title, a number, and a summary. A chapter can be written by the author or by another source.

**A function is a block of code** that performs a specific task and can be reused in different places. A function has a name, a set of parameters, and a return value. A function can be defined by the user or by the library.
**A library is a collection of functions** (and possibly other resources) that provide some functionality or service. A library can contain one or more functions, depending on how it organizes its code.

For example, suppose you want to use a function that calculates the factorial of a number. The factorial of a number n is the product of all positive integers less than or equal to n. The function can be defined by the user as follows:

```python
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)
```

This is a **user-defined function** that can be used in different places in the program.

Alternatively, the function can be provided by a library, such as the math library in Python. The math library contains many functions that perform mathematical operations, such as sqrt, sin, cos, etc. To use the function from the library, you need to import the library and call the function with its name and argument:

```python
import math
math.factorial(5)
```

This is a **library function** that can also be used in different places in the program. The difference is that the user does not need to define or know how the function works internally, as it is already implemented by the library.