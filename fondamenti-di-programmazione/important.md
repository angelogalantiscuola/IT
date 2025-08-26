## Various

  https://lp.jetbrains.com/python-developers-survey-2022/

  https://adventofcode.com/ for school


## What is a Tech Stack?

[link to video](https://www.youtube.com/watch?v=Sxxw3qtb3_g)

## devops

1. **Writing Code**: This is where a developer writes the code for an application. Their responsibilities include writing optimal and correct code, maintaining code, fixing bugs, and building new features.
2. **Building**: This is the process of compiling the software. Compiling takes computer code and translates it into machine code. The build process usually builds the main program as well as its libraries.
3. **Packaging**: This involves how you intend to transport your software (executables, libraries, resource files, folder structures, etc.) to the end user. This might mean you create an installer, or just pack everything into a zip file or something.
4. **Deploying**: This is the final step of the software getting where it is meant to be and getting installed and running. This can involve various methods, such as:
    - Emailing your zipped software to someone with written instructions of how to unzip and run.
    - Uploading it to a web server for download.
    - Installing it on a local server.
    - **Deploying it on a remote server**, such as those provided by cloud service providers like Google Cloud, Amazon Web Services (AWS), etc. This usually involves transferring your application files to the server, setting up the necessary environment, and starting the application.

In the modern IT world, there’s a concept called DevOps where **the process of getting the software hosted and running on a server is treated as continuous with the software development process, instead of distinct from it**. This helps in making the process more streamlined and efficient.

## LBYL and EAFP   
LBYL and EAFP are two different approaches to error handling in programming.

**LBYL** stands for **"Look Before You Leap"**. This approach emphasizes checking for potential errors before attempting an operation. This can be done by using explicit checks, such as if statements, or by using try-except blocks. The goal of LBYL is to prevent errors from happening in the first place.

**EAFP** stands for **"Easier to Ask for Forgiveness than Permission"**. This approach emphasizes not checking for potential errors before attempting an operation. Instead, the code is allowed to fail, and an error handler is used to deal with the failure. The goal of EAFP is to make the code more concise and readable.

```python
def divide_lbyl(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
```

```python
def divide_eafp(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Cannot divide by zero"
```

