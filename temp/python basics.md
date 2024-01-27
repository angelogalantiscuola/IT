
```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
maxLevel: 0 # Include headings up to the speficied level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```


## Python basics
### Best practices

Here are some best practices for writing Python code:

1. Use descriptive variable names: Variable names should be descriptive and easy to understand. Avoid using single-letter variable names or abbreviations that may not be clear to others.

2. Follow PEP 8 guidelines: PEP 8 is the official style guide for Python code. Following these guidelines can make your code more readable and consistent. Some examples include using 4 spaces for indentation, using `snake_case` for variable names, and using uppercase for constants.

3. Write docstrings: Docstrings are used to document your code and explain what it does. They should be included at the beginning of functions, classes, and modules.

4. Use meaningful comments: Comments should be used sparingly and only when necessary. They should explain why something is being done, not what is being done (which should be clear from the code itself).

5. Avoid global variables: Global variables can make your code harder to understand and debug. Instead, use function arguments and return values to pass data between functions.

6. Handle errors gracefully: Your code should handle errors gracefully and provide helpful error messages to users. Use try/except blocks to catch errors and handle them appropriately.

7. Use built-in functions and modules: Python has many built-in functions and modules that can save you time and make your code more efficient. Use them whenever possible instead of reinventing the wheel.

8. Write unit tests: Unit tests are used to test individual pieces of code and ensure that they work as expected. They should be included in your codebase and run automatically as part of your development process.

These are just a few best practices for writing Python code. Following these guidelines can make your code more readable, maintainable, and efficient.


### Common mistakes

Here are some common mistakes to avoid when writing Python code:

1. Not following PEP 8 guidelines: PEP 8 is the official style guide for Python code. Not following these guidelines can make your code harder to read and understand.

2. Using global variables: Global variables can make your code harder to understand and debug. Instead, use function arguments and return values to pass data between functions.

3. Not handling errors: Your code should handle errors gracefully and provide helpful error messages to users. Use try/except blocks to catch errors and handle them appropriately.

4. Not using built-in functions and modules: Python has many built-in functions and modules that can save you time and make your code more efficient. Use them whenever possible instead of reinventing the wheel.

5. Not writing docstrings: Docstrings are used to document your code and explain what it does. They should be included at the beginning of functions, classes, and modules.

6. Using single-letter variable names: Variable names should be descriptive and easy to understand. Avoid using single-letter variable names or abbreviations that may not be clear to others.

7. Not writing unit tests: Unit tests are used to test individual pieces of code and ensure that they work as expected. They should be included in your codebase and run automatically as part of your development process.

8. Not using virtual environments: Virtual environments allow you to create isolated environments for your Python projects. This can help avoid conflicts with other packages and make it easier to manage dependencies.

These are just a few common mistakes to avoid when writing Python code. By following best practices and avoiding these mistakes, you can write more efficient, readable, and maintainable code.


### Debugging

Debugging is an important part of the development process. Here are some tips for debugging Python code:

1. Use print statements: One of the simplest ways to debug Python code is to use print statements to output the values of variables and other data. This can help you identify where the problem is occurring and what values are causing the issue.

2. Use a debugger: Python has several built-in debuggers, including pdb and ipdb. These tools allow you to step through your code line-by-line and inspect the values of variables and other data.

3. Check your assumptions: Sometimes the problem with your code is not a bug, but an incorrect assumption. Make sure you understand the problem you're trying to solve and the data you're working with.

4. Simplify your code: If you're having trouble identifying the problem, try simplifying your code. Remove unnecessary code and focus on the part that's causing the issue.

5. Use error messages: Python provides helpful error messages that can give you clues about what's causing the problem. Make sure you read the error message carefully and understand what it's telling you.

6. Use logging: Logging is a way to record events in your code and can be helpful for debugging. You can use the built-in logging module to log messages at different levels (e.g. debug, info, warning, error).

7. Ask for help: If you're still having trouble debugging your code, don't be afraid to ask for help. Reach out to colleagues, online communities, or other resources for assistance.

These are just a few tips for debugging Python code. Remember, debugging can be a time-consuming process, but it's an important part of writing high-quality code.


### Best practices for writing functions

Here are some best practices for writing Python functions:

1. Use descriptive function names: Function names should be descriptive and easy to understand. They should describe what the function does and what arguments it expects.

2. Keep functions short and focused: Functions should do one thing and do it well. If a function is too long or does too many things, it can be hard to understand and debug.

3. Use function arguments and return values: Functions should take arguments and return values to pass data between them. Avoid using global variables, as they can make your code harder to understand and debug.

4. Write docstrings: Docstrings are used to document your code and explain what it does. They should be included at the beginning of functions and describe what the function does, what arguments it expects, and what it returns.

5. Use default arguments: Default arguments can make your code more flexible and easier to use. They allow you to provide a default value for an argument if one is not provided by the caller.

6. Avoid side effects: Functions should not have side effects, such as modifying global variables or printing output. Instead, they should return a value that can be used by the caller.

7. Handle errors gracefully: Your functions should handle errors gracefully and provide helpful error messages to users. Use try/except blocks to catch errors and handle them appropriately.

8. Write unit tests: Unit tests are used to test individual pieces of code and ensure that they work as expected. They should be included in your codebase and run automatically as part of your development process.

These are just a few best practices for writing Python functions. By following these guidelines, you can write functions that are easy to understand, maintain, and debug.

