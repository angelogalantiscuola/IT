# temp

Here is the selected text in a Markdown block:

> **Library**: In Python, a library is a collection of modules. It's a way to bundle code into reusable and shareable files. Libraries can contain built-in modules (written in C) like `math`, `itertools`, `sys`, etc., and modules written in Python. Libraries provide reusable functionality for various tasks.

Pillow is a library in Python, but it's also structured as a package.

When we say Pillow is a library, we mean it's a collection of modules and functions that provide capabilities for handling and manipulating images in Python.

When we say Pillow is a package, we mean it's organized in a specific way. It's a directory that contains multiple related modules (files) and possibly other sub-packages (sub-directories). When you import Pillow, you're typically accessing specific modules or functions within this package.

So, in summary, Pillow can be referred to as both a library (in the sense of being a collection of reusable code) and a package (in the sense of its organizational structure).

- **Library**: In Python, a library is a collection of modules. It's a way to bundle code into reusable and shareable files. Libraries can contain built-in modules (written in C) like `math`, `itertools`, `sys`, etc., and modules written in Python. Libraries provide reusable functionality for various tasks.

- **Module**: A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` added. Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`. You can use any Python source file as a module by executing an import statement in some other Python source file.

- **Package**: A package in Python is a way of organizing related modules into a directory hierarchy. It is simply a directory that contains a special file `__init__.py` (which may be empty) and can contain other python files or sub-packages. For example, the `os` package in Python's standard library contains modules like `os.path` and `os.stat`.

### Function vs library

> [!NOTE]
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
