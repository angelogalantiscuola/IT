# temp

## level of abstraction in programming languages

I see. The level of abstraction in programming languages indicates how close a particular language is to the hardware¹. The lower the level of abstraction, the more details and low-level operations the programmer has to deal with². The higher the level of abstraction, the more features and functionalities the language provides to simplify and automate complex tasks².

For example, machine code is the lowest level of abstraction, as it consists of binary instructions that can be executed directly by the processor⁴. Assembly language is a level above machine code, as it uses symbolic names for memory locations and operations instead of binary codes⁴. However, assembly language is still specific to the hardware and has to be translated into machine code by an assembler⁴.

C++ is a high-level language that can be compiled into machine code by a compiler⁴. However, C++ is also considered a low-level language compared to other high-level languages because it allows direct access to memory addresses and low-level operations through pointers³. C++ is often used for writing system software such as operating systems and compilers³.

Python is a higher-level language than C++, as it uses an interpreter or a virtual machine to execute its programs⁴. Python offers greater abstraction than C++, such as dynamic typing, automatic memory management, multiple paradigms and built-in data structures³. Python is often used for scripting, web development and data analysis³.

Prolog is one of the highest-level languages, as it uses logic programming to express problems and solutions in terms of facts and rules instead of procedures or functions⁴. Prolog abstracts away many details such as control flow, data structures and algorithms from the programmer⁴. Prolog is mainly used for artificial intelligence applications such as natural language processing and expert systems⁴.

## python

python dates

python try except

python classes
<https://www.programiz.com/python-programming/operator-overloading>

python backend
<https://www.w3schools.com/django/index.php>

python data types list, tuple, set, and dictionary

A list is a collection that is ordered and changeable. Lists are written with square brackets [ ].
A tuple is a collection that is ordered and unchangeable. Tuples are written with round brackets ( ).
A set is a collection that is unordered and unindexed. Sets are written with curly brackets { }.

An example of using tuples over lists is storing constants that will never change, such as days of the week or months of the year.

Sets are more efficient than lists for membership tests, such as checking if an item is contained within a collection. Sets use hash tables underneath, which make in operation very fast1.

## package

==read this==
<https://www.pythoncentral.io/how-to-create-a-python-package/>

Okay, here is an example of how to create and use a package in Python. Suppose you want to create a package named math with two modules named arithmetic and algebra. You need to create a directory named math and add two files named arithmetic.py and algebra.py inside it. You also need to add an empty file named \_\_init\_\_.py inside the math directory³. The files can contain some functions or classes related to math operations. For example, arithmetic.py can have this code:

```python
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y
```

And algebra.py can have this code:

```python
def solve_quadratic(a, b, c):
  # some code to solve ax^2 + bx + c = 0
  return roots
```

To use the package, you need to import it in your program using the import statement with dot notation². For example, you can create another file named main.py with this code:

```python
import math.arithmetic as arith
import math.algebra as alg

print(arith.add(2, 3))
print(alg.solve_quadratic(1, -5, 6))
```

This will print 5 and [3.0, 2.0] when you run main.py. You can also import specific functions or classes from a module using the from ... import ... syntax². Do you understand?

Source: Conversation with Bing, 2/23/2023(1) How to Create a Python Package - Python Central. <https://www.pythoncentral.io/how-to-create-a-python-package/> Accessed 2/23/2023.
(2) Create and Access a Python Package - GeeksforGeeks. <https://www.geeksforgeeks.org/create-access-python-package/> Accessed 2/23/2023.
(3) How to Create and Upload Your First Python Package to PyPI. <https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/> Accessed 2/23/2023.
(4) Python Modules and Packages – An Introduction – Real Python. <https://realpython.com/python-modules-packages/> Accessed 2/23/2023.

Okay, here is an example of how to create and use a package in Python. Suppose you want to create a package named math with two modules named arithmetic and algebra. You need to create a directory named math and add two files named arithmetic.py and algebra.py inside it. You also need to add an empty file named \_\_init\_\_.py inside the math directory³. The files can contain some functions or classes related to math operations. For example, arithmetic.py can have this code:

```python
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y
```

And algebra.py can have this code:

```python
def solve_quadratic(a, b, c):
  # some code to solve ax^2 + bx + c = 0
  return roots
```

To use the package, you need to import it in your program using the import statement with dot notation². For example, you can create another file named main.py with this code:

```python
import math.arithmetic as arith
import math.algebra as alg

print(arith.add(2, 3))
print(alg.solve_quadratic(1, -5, 6))
```

This will print 5 and [3.0, 2.0] when you run main.py. You can also import specific functions or classes from a module using the from ... import ... syntax². Do you understand?

Source: Conversation with Bing, 2/23/2023(1) How to Create a Python Package - Python Central. <https://www.pythoncentral.io/how-to-create-a-python-package/> Accessed 2/23/2023.
(2) Create and Access a Python Package - GeeksforGeeks. <https://www.geeksforgeeks.org/create-access-python-package/> Accessed 2/23/2023.
(3) How to Create and Upload Your First Python Package to PyPI. <https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/> Accessed 2/23/2023.
(4) Python Modules and Packages – An Introduction – Real Python. <https://realpython.com/python-modules-packages/> Accessed 2/23/2023.

### what is the difference between module and package in python

In Python, a module is a single **file** containing Python code, while a package is a **directory** containing multiple modules and sub-packages. A package must contain an additional \_\_init\_\_.py file to distinguish it from a regular directory. **The distinction between module and package is just at the file system level.**

Any Python file is a module, its name being the file's base name/module's \_\_name\_\_ property without the .py extension.
A package is a collection of Python modules, i.e., a package is a directory of Python modules containing an additional \_\_init\_\_.py file.
The \_\_init\_\_.py distinguishes a package from a directory that just happens to contain a bunch of Python scripts.
Packages can be nested to any depth, provided that the corresponding directories contain their own \_\_init\_\_.py file.

When you import a module or a package, the corresponding object created by Python is always of type module. This means that the distinction between module and package is just at the file system level. Note, however, when you import a package, only variables/functions/classes in the \_\_init\_\_.py file of that package are directly visible, not sub-packages or modules.

### script vs module vs package

Programmers can write a script in a text editor of their choice and save it in the .py extension. Running the script is as simple as using the Python command in the terminal.

In contrast, a module is a Python program that programmers can import into other programs or directly in the interactive mode of the Python shell. The term “module” is not strictly defined in Python; it serves as an umbrella term for reusable code.

Python packages typically comprise several modules. Physically, a package is a folder of modules, and it may contain more folders that have more folders and modules.

Package folders typically contain an \_\_init\_\_.py file, which indicates to Python that the directory is a package. The file may be empty or have code that needs to be executed when the package is initialized.
[src](https://www.pythoncentral.io/how-to-create-a-python-package/)
