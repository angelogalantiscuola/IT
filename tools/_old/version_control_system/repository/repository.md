# repository

%% Begin Waypoint %%

- [[env_file]]
- [[gitignore]]
- [[virtual_environment]]

%% End Waypoint %%

A repository is **a storage space where your project files are stored**. It's **like a folder on your computer**, but it has some special features that make it easier to work with your project files. For example, a repository can keep track of changes you make to your files, so you can see what was changed, who changed it, and why. This is useful when you're working on a project with other people, as it helps you avoid overwriting each other's changes.

## How to

### How to create a repo on GitHub

1. Sign in to your GitHub account.
2. Click on the '+' icon at the top right corner of the page, then select 'New repository'.
3. Enter a name for your repository in the 'Repository name' field.
4. You can add an optional description in the 'Description' field.
5. Choose the visibility for your repository (public or private).
6. You can initialize the repository with a README, .gitignore, or license if you want:
    - **README**: This is where you can give important information about your project like what it does, how to set it up, how to use it, etc. It's the first file people will see when they visit your repository, so it's a good place to put any essential information.
    - **.gitignore**: This is a file where you can specify other files or directories that you don't want Git to track. For a Python project, you might want to ignore files like `__pycache__`, `.pyc` files, environment files, etc. GitHub can automatically create a .gitignore file for Python when you create a new repository. (see [.gitignore](gitignore.md))
    - **License**: This is where you specify the terms under which others can use, copy, modify, and distribute your software. It's important to choose a license that fits your needs. GitHub can help you choose a license when you create a new repository
    - **.env** is a plain text file that is used to store environment variables (see [.env](env_file.md))
7. Click on 'Create repository' to create your new repository.

### How to clone the repository in VS Code

- Open VS Code.
- Press `Ctrl+Shift+P` to open the command palette.
- Type `Git: Clone` and press `Enter`.
- Paste the URL of your GitHub repository and press `Enter`.
- Choose a directory on your local machine where you want to clone the repository and press `Enter`.
- A new VS Code window will open with your cloned repository.

### How to sync your edits between VS Code and GitHub

- Make your changes in the VS Code editor.
- When you're ready to commit your changes, click on the source control icon on the left sidebar (or press `Ctrl+Shift+G`).
- Enter a commit message in the text box at the top and press `Ctrl+Enter` to commit your changes.
- To push your changes to GitHub, click on the three dots (...) in the top right corner of the source control view, then select `Push`.
  - This is like saying "send my changes" to GitHub. When you make changes to your code locally (on your computer) and you want these changes to be reflected on your GitHub repository, you `push` these changes. This updates your online repository with your local changes.
- To pull any changes from GitHub, click on the three dots (...) in the top right corner of the source control view, then select `Pull`.
  - This is like saying "get the latest changes" from GitHub. If there are changes on the GitHub repository that are not on your local machine, you `pull` these changes. This updates your local copy with the latest changes from your online repository.
