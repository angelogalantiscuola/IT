# virtual environment

Think of it like a separate box for each of your Python projects. Inside this box, you can have whatever toys (packages) you want and it won't mess up the toys in your other boxes (other projects).

> [!NOTE]
> For example, let's say you have two projects: Project A and Project B. Project A needs version 1 of a package, but Project B needs version 2 of the same package. If you install both versions globally, they might conflict with each other. But if you use a virtual environment for each project, you can have version 1 in Project A's environment and version 2 in Project B's environment, and they won't interfere with each other.

## Definition

In Python, a virtual environment is an isolated environment where you can install packages without affecting your global Python installation. It's a way to manage dependencies on a per-project basis. When you activate a virtual environment, any packages you install will only be available within that environment. This is useful because **different projects might require different versions of the same package, and using a virtual environment for each project can help prevent conflicts between them.**

## Creating and Managing a Virtual Environment

1. **Create a virtual environment**: You can create a virtual environment using the `venv` module that comes with Python. Open a terminal, navigate to your project directory, and run the following command:

    ```bash
    python -m venv .venv
    ```

    This will create a new virtual environment named `myenv` in your project directory:

    - `python`: This is the command to start the Python interpreter.
    - `-m`: This is a command-line option for the Python interpreter that allows you to run a module as a script. In other words, it lets you run a Python module from the command line.
    - `venv`: This is the name of the Python module that you're running with the `-m` option. The `venv` module is used to create virtual environments in Python.
    - `.venv`: This is the argument that you're passing to the `venv` module. It specifies the name of the virtual environment that you want to create. In this case, you're creating a virtual environment named `.venv`.

2. **Activate the virtual environment**: Before you can use the virtual environment, you need to activate it. The command to do this depends on your operating system:
    - On Windows, run: `myenv\Scripts\activate`
    - On Unix or MacOS, run: `source myenv/bin/activate`

3. **Install packages**: Once the virtual environment is activated, you can install packages using `pip`. For example, to install the requests package, you would run: `pip install requests`. **The packages you install will only be available in the current virtual environment.**

4. **Deactivate the virtual environment**: When you're done working in the virtual environment, you can deactivate it by running: `deactivate`. This will return you to your global Python environment.


A Python virtual environment is a tool that helps to **keep dependencies required by different projects separate** by creating isolated Python virtual environments for them. It’s a way to have multiple, parallel instances of the Python interpreter, each with different sets of packages and different configurations.

Here’s a brief explanation of its main components:
- **Isolated Environment**: Each virtual environment contains a discrete copy of the Python interpreter, including copies of its support utilities. This isolation helps to avoid conflicts between different versions of libraries used in different projects.
- **Package Management**: When used from within a virtual environment, common installation tools such as pip will install Python packages into the virtual environment without needing to be told to do so explicitly. This allows each project to have its own directory to store third-party packages.
- **Portability and Reproducibility**: Virtual environments are considered disposable – it should be simple to delete and recreate it from scratch. This makes it easier to share your project with others, as you can provide a list of the exact versions of the packages your project depends on.

[12. Virtual Environments and Packages — Python 3.12.1 documentation](https://docs.python.org/3/tutorial/venv.html)
