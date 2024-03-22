# Modules, Library, Packages

%% Begin Waypoint %%

- [[decorators]]
- **examples**

- [[modules]]
- **[packages](./packages/packages.md)**

%% End Waypoint %%

- **Module**: A module in Python is **a single file** containing Python definitions and statements. The file name is the module name with the suffix `.py` added. You can use any Python source file as a module by executing an import statement in some other Python source file. For example, `math` is a module in Python's standard library.

- **Library**: A library in Python is **a collection of related functionality encapsulated as reusable code**. It can be a single module (like the `math` module) or a collection of related modules. Libraries provide a way of reusing code across different projects and can be built-in (like `math`, `itertools`, `sys`, etc.) or installed from external sources (like `numpy`, `requests`, etc.).

- **Package**: A package in Python is a specific type of **library that organizes related modules into a directory hierarchy**. It's essentially a directory that contains a special file `__init__.py` (which may be empty) and can contain other Python files (modules) or sub-packages. A package can be a part of a larger library and provides a way of grouping related modules together in a structured manner.

In summary, while **all packages are libraries** (as they are reusable code), not all libraries are packages. **A library becomes a package when it has a directory-based structure for organizing related modules**. A module is a single file that can be part of a library or a package.

> [!NOTE]
> Pillow is a library in Python, but it's also structured as a package.
> When we say Pillow is a library, we mean it's a collection of modules and functions that provide capabilities for handling and manipulating images in Python.
> When we say Pillow is a package, we mean it's organized in a specific way. It's a directory that contains multiple related modules (files) and possibly other sub-packages (sub-directories).
> So, in summary, Pillow can be referred to as both a library (in the sense of being a collection of reusable code) and a package (in the sense of its organizational structure).

## Function and library

**A function is a block of code** that performs a specific task and can be reused in different places. A function has a name, a set of parameters, and a return value. A function can be defined by the user or by the library.
**A library is a collection of functions** (and possibly other resources) that provide some functionality or service. A library can contain one or more functions, depending on how it organizes its code.

> [!NOTE]
> An analogy for a library and a function is a book and a chapter. A book is a collection of chapters that provide some information or knowledge. A book can contain one or more chapters, depending on how it organizes its content. A chapter is a section of text that covers a specific topic and can be read independently. A chapter has a title, a number, and a summary. A chapter can be written by the author or by another source.
