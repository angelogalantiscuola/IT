# Functions

%% Begin Waypoint %%
- [[args and kwargs]]
- [[built-in functions]]
- [[type_hinting]]

%% End Waypoint %%

## Functions in Math

The concept of a function in programming is borrowed from mathematics.

`y=f(x)` for example `3=√9`

- f is the function name (square root)
- x is the input (9)
- y is the output (3)

## Functions in Programming

A function is a reusable piece of code that performs a specific task. Functions are fundamental to programming, as they allow you to structure your code in a modular way, making it more organized, reusable, and easier to understand.

In most programming languages, a function is `defined` using a def or function keyword, followed by a `name` of your choice. It can take `parameters` (input values), and return a `result` (output value).

Here's a simple example of a function in Python:

```python
def greet(name): # function definition
    return "Hello, " + name # return value 

result = greet("Pippo") # function call
print(result) # Hello, Pippo
```

> [!NOTE]
> A related topic is [Type hinting](type_hinting.md)

### Procedure

A procedure is a function without output, the return value is None.
A procedure can have: no input values, a single input value, or multiple input values.

```python
def say_hello() -> None:
    print("Hello, world!")

def greet(name:str) -> None:
    print("Hello, " + name)

def greet_personally(first_name:str, last_name:str) -> None:
    print("Hello, " + first_name + " " + last_name)
```

### Function

A function can have: no input values, a single input value, or multiple input values.

```python
def get_greeting() -> str:
    return "Hello, world!"

def length_of_string(s: str) -> int:
    number_of_characters = 0
    for i in s:
        number_of_characters += 1
    return number_of_characters

def add_numbers(a: int, b: int) -> int:
    return a + b
```

A function can also have multiple input values and multiple output values.

```python
def calculate_area_and_perimeter(length: float, width: float) -> tuple[float]:
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
```

#### Second degree equation example

```python
from math import sqrt


# parameterless function or zero-argument function
def ask_data_to_user() -> list[int]:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    return [a, b, c]


# function
def calculate_solutions(a: int, b: int, c: int) -> list[float] | None:
    delta = b * b - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        solution1 = -b / (2 * a)
        solution2 = solution1
    else:
        solution1 = (-b + sqrt(delta)) / (2 * a)
        solution2 = (-b - sqrt(delta)) / (2 * a)
    return [solution1, solution2]


# procedure or void function
def print_results(solutions: list[float] | None) -> None:
    if solutions is not None:
        x1, x2 = solutions
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    else:
        print("No real solutions.")


a, b, c = ask_data_to_user()  # input
solutions = calculate_solutions(a, b, c)  # processing
print_results(solutions)  # output
```
