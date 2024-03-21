**Decorators wrap a function, modifying its behavior.**

In Python, a decorator is a design pattern that allows you to modify the functionality of a function or method by wrapping it in another function. This wrapping is done without modifying the original function’s source code. The outer function (the decorator) takes the original function as an argument and returns a modified version of it.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
```

In this example, `my_decorator` is a decorator that wraps the function `say_hello`. When `say_hello()` is called, it now also executes the code in `wrapper()` before and after calling the original function.

Python also provides a shortcut for applying decorators using the `@` symbol:

```python
@my_decorator
def say_hello():
    print("Hello!")
```

This code does the same thing as the previous example. The `@my_decorator` line is equivalent to `say_hello = my_decorator(say_hello)`.
