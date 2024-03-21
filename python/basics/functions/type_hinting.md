# Typing

In programming, typing refers to `how a language handles and categorizes its data types`. There are two main categories of typing: static typing and dynamic typing.

## Static typing

Static typing (or strongly typed): In statically typed languages, variables have a `specific type`, and that type `cannot change` over the course of the program. The type of each variable is known at `compile time`, which can help catch errors early. Examples of statically typed languages include Java, C++, and Rust.

## Dynamic typing

Dynamic typing (or weakly typed): In dynamically typed languages, variables can hold values of `any type`, and their type `can change` over the course of the program. The type of each variable is checked at `runtime`, which can provide more flexibility but may also lead to runtime errors. Examples of dynamically typed languages include Python, JavaScript, and Ruby.

## Type hinting

However, Python also supports type hinting, which allows you to specify the expected type of a variable or function return value. This can `help catch certain types of errors and improve code readability`, but it doesn't change the fact that Python is fundamentally a dynamically typed language. The type hints are `optional` and are `not enforced` by the Python interpreter.

Here's an example of type hinting in Python:

```python
def combine_elements(a: int, b: str, c: list[str]) -> str:
    return f"{a}, {b}, {', '.join(c)}"

# Usage
result = combine_elements(5, "Hello", ["Alice", "Bob", "Charlie"])
print(result)  # Outputs: 5, Hello, Alice, Bob, Charlie
```

### Important links on type hinting

[Python Types Intro - FastAPI (tiangolo.com)](https://fastapi.tiangolo.com/python-types/)

<https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html>

<https://docs.python.org/3/library/typing.html>
