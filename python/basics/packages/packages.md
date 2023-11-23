%% Begin Waypoint %%


%% End Waypoint %%






## packages

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
