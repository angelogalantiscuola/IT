# Programming paradigms

Programming paradigms are a way to classify programming languages based on their features. Languages can be classified into multiple paradigms. Some of the common programming paradigms include:

1. **Procedural Programming**: It is a programming paradigm, derived from structured programming, based on the concept of the procedure call. Procedures, also known as routines, subroutines, or functions, simply contain a series of computational steps to be carried out.

```python
def calculate_area(length, width):
    return length * width
```

2. **Object-oriented Programming (OOP)**: It is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
```

3. **Functional Programming**: It is a programming paradigm where programs are constructed by applying and composing functions. It is a declarative programming paradigm in which function definitions are trees of expressions that each return a value, rather than a sequence of imperative statements which change the state of the program.

```python
def multiply_by_two(n):
    return n * 2

numbers = [1, 2, 3, 4]
doubled_numbers = map(multiply_by_two, numbers)
```
4. **Declarative Programming**: It is a programming paradigm that expresses the logic of a computation without describing its control flow. Many languages applying this style attempt to minimize or eliminate side effects by describing what the program should accomplish, rather than describing how to go about accomplishing it.

```sql
SELECT name FROM students WHERE grade > 90;
```

```html
<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
```

5. **Logic Programming**: It is a programming paradigm which is largely based on formal logic. Any program written in a logic programming language is a set of sentences in logical form, expressing facts and rules about some problem domain.

```prolog
father(john, jim).
father(john, ann).

sibling(X, Y) :- father(Z, X), father(Z, Y), X \= Y.
```
