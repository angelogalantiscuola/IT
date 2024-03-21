%% Begin Waypoint %%


%% End Waypoint %%


[Glossary — Python 3.12.0 documentation](https://docs.python.org/3/glossary.html#term-iterator)


- **Object-Oriented Programming**
    - abstract base class
    - attribute
    - object
    - method
    - magic method
    - special method

- **Functions**
    - argument
    - callable
    - callback
    - decorator
    - key function
    - lambda
    - parameter

- **Documentation**
    - docstring
    - PEP
    - triple-quoted string

- **Programming Concepts**
    - duck-typing
    - immutable
    - namespace
    - statement
    - type
    - type alias

- **Generators**
    - generator
    - generator iterator

- **Iterables**
    - iterable
    - iterator

- **Modules and Packages**
    - module
    - package

- **Python Environment**
    - virtual environment



**abstract base class**: ABCs introduce virtual subclasses, which are classes that don’t inherit from a class

**argument**: A value passed to a function (or method) when calling the function. 
- _keyword argument_: an argument preceded by an identifier
- _positional argument_: an argument that is not a keyword argument

**attribute**: A value associated with an object which is usually referenced by name using dotted expressions.

**callable**: A callable is an object that can be called

**callback**: A subroutine function which is passed as an argument to be executed at some point in the future.

**decorator**: A function returning another function, usually applied as a function transformation using the `@wrapper` syntax.

**docstring**: A string literal which appears as the first expression in a class, function or module.

**duck-typing**: A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck, it must be a duck.”)

**generator**: A function which returns a generator iterator. It looks like a normal function except that it contains `yield` expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the `next()` function.

**generator iterator**: An object created by a generator function. Each `yield` temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). When the generator iterator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

**immutable**: An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.

**iterable**: An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects. Iterables can be used in a `for` loop and in many other places where a sequence is needed (`zip()`, `map()`, …). When an iterable object is passed as an argument to the built-in function `iter()`, it returns an iterator for the object. 

**iterator**: An object representing a stream of data. Repeated calls to the iterator’s `__next__()` method (or passing it to the built-in function `next()`) return successive items in the stream. When no more data are available a `StopIteration` exception is raised instead.

**key function**: A key function or collation function is a callable that returns a value used for sorting or ordering. 

**lambda**: An anonymous inline function consisting of a single expression which is evaluated when the function is called.

**magic method**: An informal synonym for special method.

**method**: A function which is defined inside a class body.

**module**: An object that serves as an organizational unit of Python code. Modules are loaded into Python by the process of importing.

**namespace**: The place where a variable is stored. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts.

**object**: Any data with state (attributes or value) and defined behavior (methods).

**package**: A Python module which can contain submodules or recursively, sub-packages.

**parameter**: A named entity in a function (or method) definition that specifies an argument (or in some cases, arguments) that the function can accept. There are five kinds of parameter:
- _positional-or-keyword_
- _positional-only_
- _keyword-only_
- _var-positional_
- _var-keyword_
`- def func(*args, **kwargs): ...`

**PEP**: Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment.

**special method**: A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores.

**statement**: A statement is part of a suite (a “block” of code). A statement is either an expression or one of several constructs with a keyword, such as if, while or for.

**triple-quoted string**: A string which is bound by three instances of either a quotation mark (”) or an apostrophe (‘). They allow you to include unescaped single and double quotes within a string and they can span multiple lines without the use of the continuation character, making them especially useful when writing docstrings.

**type**: The type of a Python object determines what kind of object it is; every object has a type.

**type alias**: A synonym for a type, created by assigning the type to an identifier. Type aliases are useful for simplifying type hints.

**virtual environment**: A cooperatively isolated runtime environment that allows Python users and applications to install and upgrade Python distribution packages without interfering with the behaviour of other Python applications running on the same system.