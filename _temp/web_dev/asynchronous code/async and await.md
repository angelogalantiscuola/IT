[Concurrency and async / await - FastAPI (tiangolo.com)](https://fastapi.tiangolo.com/async/#async-and-await)

Modern versions of Python have a very intuitive way to define asynchronous code. This makes it look just like normal "sequential" code and do the "awaiting" for you at the right moments.

For `await` to work, it has to be inside a function that supports this asynchronicity. To do that, you just declare it with `async def`:

```python
async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    return burgers
```

...instead of `def`:

```python
# This is not asynchronous
def get_sequential_burgers(number: int):
    # Do some sequential stuff to create the burgers
    return burgers
```

So, if you are using a library that tells you that you can call it with `await`, you need to create the _path operation functions_ that uses it with `async def`, like in:

```python
@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers
```

## More technical details

You might have noticed that `await` can only be used inside of functions defined with `async def`.

But at the same time, functions defined with `async def` have to be "awaited". So, functions with `async def` can only be called inside of functions defined with `async def` too.

So, about the egg and the chicken, how do you call the first `async` function?

If you are working with **FastAPI** you don't have to worry about that, because that "first" function will be your _path operation function_, and FastAPI will know how to do the right thing.
