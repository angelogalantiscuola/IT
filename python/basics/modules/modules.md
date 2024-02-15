%% Begin Waypoint %%


%% End Waypoint %%

# Python modules

Python comes with a large standard library that includes several lightweight modules. Here are some of the simplest and most commonly used ones:

1. `math`: Provides mathematical functions. For example, `math.sqrt(x)` returns the square root of x.

2. `random`: Provides functions for generating random numbers. For example, `random.randint(a, b)` returns a random integer between a and b.

3. `datetime`: Provides classes for manipulating dates and times. For example, `datetime.datetime.now()` returns the current date and time.

4. `os`: Provides functions for interacting with the operating system. For example, `os.getcwd()` returns the current working directory.

5. `sys`: Provides access to some variables used or maintained by the Python interpreter. For example, `sys.argv` is a list in Python, which contains the command-line arguments passed to the script.

6. `json`: Provides methods to manipulate JSON data. For example, `json.loads(s)` parses a JSON string and returns a Python object.

## Math module

The math module in Python provides mathematical functions and constants. Here are some of the most commonly used features:

1. Constants: The math module provides constants like `math.pi` (the mathematical constant π) and `math.e` (the base of the natural logarithm).

2. Trigonometric Functions: Functions like `math.sin(x)`, `math.cos(x)`, and `math.tan(x)` return the sine, cosine, and tangent of x radians, respectively.

3. Exponential and Logarithmic Functions: `math.exp(x)` returns e raised to the power x, `math.log(x)` returns the natural logarithm of x, and `math.log10(x)` returns the base-10 logarithm of x.

4. Power and Square Root: `math.pow(x, y)` returns x raised to the power y, and `math.sqrt(x)` returns the square root of x.

5. Hyperbolic Functions: Functions like `math.sinh(x)`, `math.cosh(x)`, and `math.tanh(x)` return the hyperbolic sine, cosine, and tangent of x, respectively.

6. Rounding: `math.ceil(x)` returns the smallest integer greater than or equal to x, and `math.floor(x)` returns the largest integer less than or equal to x.

## Modules more in depth

In Python, everything is an object, including functions, classes, and even modules themselves.

For example, in the math module, functions like `sqrt` or `sin` are actually objects of type `'builtin_function_or_method'`. Constants like `pi` and `e` are objects of type `'float'`.

```python
import math

print(type(math.sqrt))  # Outputs: <class 'builtin_function_or_method'>
print(type(math.pi))  # Outputs: <class 'float'>
```

So, `when you import a module, you're actually creating an object` which groups together all the functions, classes, and variables defined in that module.

## List of attributes and methods of a module

```python
import math

# List of all the attributes and methods
print(dir(math))
print("\n")
# Filter out these special attributes
print([name for name in dir(math) if not name.startswith("__")])
print("\n")

# Get all attributes and methods
all_items = dir(math)

# Filter methods and attributes
methods = [
    item for item in all_items if callable(getattr(math, item)) and not item.startswith("__")
]
attributes = [
    item for item in all_items if not callable(getattr(math, item)) and not item.startswith("__")
]

print("Methods:", methods)
print("\n")
print("Attributes:", attributes)
print("\n")
```
