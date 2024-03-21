# Packages

%% Begin Waypoint %%

- **examples**

- [[packages-ai]]
- [[packages-all]]

%% End Waypoint %%

## Difference between module and package

In Python, a module is a single **file** containing Python code, while a package is a **directory** containing multiple modules and sub-packages. A package must contain an additional `__init__.py` file to distinguish it from a regular directory. **The distinction between module and package is just at the file system level.**

## How to create a package

Here is an example of how to create and use a package in Python. Suppose you want to create a package named math with two modules named arithmetic and algebra. You need to create a directory named `math` and add two files named `arithmetic.py` and `algebra.py` inside it. You also need to add an empty file named `__init__.py` inside the math directory. The files can contain some functions or classes related to math operations.

Here's the structure of the files:

``` text=
.
├── main.py
└── math
    ├── __init__.py
    ├── arithmetic.py
    └── algebra.py
```

In this structure:

- `main.py` is your main Python script where you will import and use the `math` package.
- `math` is the directory that represents your package.
- `__init__.py` is an empty file that indicates to Python that `math` is a package.
- `arithmetic.py` and `algebra.py` are the modules in your package. They can contain any functions or classes related to math operations.

For example, `arithmetic.py` can have this code:

```python
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y
```

And `algebra.py` can have this code:

```python
def solve_quadratic(a, b, c):
  # some code to solve ax^2 + bx + c = 0
  return roots
```

To use the package, you need to import it in your program using the import statement with dot notation. For example, you can create another file named `main.py` with this code:

```python
from math import arithmetic, algebra

print(add(2, 3))
print(solve_quadratic(1, -5, 6))
```
