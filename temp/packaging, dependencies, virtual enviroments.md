
python-poetry/poetry: Python packaging and dependency management made easy
https://github.com/python-poetry/poetry

There are several tools available to handle virtual environments in Python. Some popular ones include virtualenv, venv (which comes with Python 3),

When working with repositories and virtual environments, it’s a good practice to create a separate virtual environment for each repository or project. This allows you to keep the dependencies for each project isolated and makes it easier to manage them.

Here are some steps you can follow to handle repositories and virtual environments:

Create a virtual environment: For each repository or project, create a new virtual environment by running the command python3 -m venv /path/to/new/virtual/environment. This will create a new directory at the specified path with the necessary files and directories for the virtual environment.

Activate the virtual environment: Before you can use the virtual environment, you need to activate it. On Windows, you can do this by running the activate.bat script located in the Scripts subdirectory of the virtual environment directory. On Unix or MacOS, you can do this by running the source /path/to/virtual/environment/bin/activate command.

Install packages: Once the virtual environment is activated, you can use pip to install packages into it. Any packages you install while the virtual environment is active will only be available within that virtual environment.

Save dependencies: It’s a good idea to save the dependencies for your project in a file such as requirements.txt. You can do this by running the command pip freeze > requirements.txt. This will create a file with a list of all the packages installed in the virtual environment and their versions. You can then commit this file to your repository so that others can easily install the same dependencies.

Deactivate the virtual environment: When you’re done using the virtual environment, you can deactivate it by running the deactivate command.

The order in which you create the virtual environment and clone the repository doesn’t really matter. You can do either one first.

If you clone the repository first, you can then create a new virtual environment within the repository’s root directory. This way, the virtual environment will be contained within the repository’s directory.
