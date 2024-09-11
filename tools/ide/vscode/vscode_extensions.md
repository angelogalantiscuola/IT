# Vscode extensions

## Improved performance for Python

### ms-python.python
This is the official Microsoft Python extension for Visual Studio Code. It provides features such as IntelliSense, linting, debugging, code navigation, code formatting, Jupyter notebook support, refactoring, variable explorer, test explorer, and more!

### ms-python.vscode-pylance
Pylance is a Visual Studio Code extension that uses the Language Server Protocol to communicate with VS Code. Pylance uses static type information, if available, to provide a richer IntelliSense experience.
It provides features like: Rich auto-completions and IntelliSense, Type checking (when type information is available), Function signature help, Go to Definition/Declaration, Find References, Rename symbol, Quick fixes and code refactorings.

## Linter

A linter is a tool that analyzes source code to identify errors, stylistic issues, and potential bugs.
It is a **static code analysis tool**, which means that it analyzes the code without actually executing it.

Benefits of using a linter:

- Improved code quality: Linters can help to identify and fix errors and stylistic issues in your code, which can make your code more readable, maintainable, and bug-free.
- Reduced development time: Linters can help to catch errors early in the development process, which can save you time and effort later on.
- Increased consistency: Linters can help to enforce coding standards and conventions, which can make your code more consistent and easier to understand.

### ms-python.pylint
This extension integrates the pylint utility into VS Code. pylint is a Python static code analysis tool which looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.

## Formatters

A formatter is a tool or program that takes data as input and arranges it in a specific format for output.
Formatters can be used for a variety of purposes, including:

- Converting data from one format to another: For example, a CSV formatter can convert a CSV file to a JSON file.
- **Prettifying data**: For example, a code formatter can indent and align code to make it more readable.
- Validating data: For example, an HTML formatter can check that an HTML file is well-formed.

### ms-python.black-formatter
This is an extension that integrates the Black Python code formatter into VS Code. Black is a highly opinionated, deterministic formatter that can automatically format your Python code to look more consistent and adhere to PEP 8 style guide.

### ms-python.isort
This extension integrates the isort utility into VS Code. isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.

## Virtual environment

### wolfieshorizon.python-auto-venv
This extension automatically detects Python virtual environments associated with your Python projects in VS Code.

## All-in-one

### charliermarsh.ruff
This is a Visual Studio Code extension for Ruff, a very fast Python `linter` and code `formatter`, written in Rust. It can be used to replace Flake8, Black, isort, pyupgrade, and more, while executing much faster than any individual tool. 
