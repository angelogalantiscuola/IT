# recursion and iteration

## iterative factorial

``` python
# function that iteratively calculate the factorial of a number n given as parameter
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
```

## recursive factorial

``` python
# function that recursively calculate the factorial of a number n given as parameter
def factorial_recursive(n):
   if n == 0:
      return 1
   else:
      return n * factorial_recursive(n-1)
```
