# Args and Kwargs

`*args` and `**kwargs` allow you to pass multiple arguments or keyword arguments to a function
These are the two **unpacking operator** (`*`) and (`**`)

- Use a single asterisk (`*`) to unpack iterables
- Use two asterisks (`**`) to unpack dictionaries
[Python args and kwargs: Demystified – Real Python](https://realpython.com/python-kwargs-and-args/)

```python
def example_function(*args, **kwargs):
    for arg in args:
        print(f"Arg: {arg}") # Arg: 1, Arg: 2, Arg: 3
    for key, value in kwargs.items():
        print(f"Keyword Arg: {key} = {value}") # Keyword Arg: name = Alice, Keyword Arg: age = 25

# Usage
example_function(1, 2, 3, name="Alice", age=25)
```
