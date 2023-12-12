
## WSGI
WSGI is the Web Server Gateway Interface. It is **a specification that describes how a web server communicates with web applications written in Python**.
Between the server and the application, there is a WSGI middleware component.

> Imagine you’re at a restaurant in a foreign country and you don’t speak the language. You need a translator to communicate your order to the waiter. In this scenario, you’re the Python web application, the waiter is the web server, and WSGI is the translator.


## ASGI
ASGI is **a standard interface between async-capable Python web servers, frameworks, and applications**. It is a successor to WSGI, and it’s designed to be a superset of WSGI. Unlike WSGI, ASGI allows multiple, **asynchronous events** per application. This means it can handle **multiple requests** at the same time, making it more efficient.

Main Python ASGI web servers:
- `Uvicorn`
- `Hypercorn`
- `Daphne`

ASGI framework: a set of tools and libraries in Python that helps in building asynchronous web applications
- `Starlette`
- `FastAPI` built on top of `Starlette`
- `Asgineer`


User (Browser) -->  Web Server  --> ASGI Framework --> Application Code

Here’s what each component does:

1. **User (Browser)**: This is where the request originates, typically a web browser.
2. **Web Server (Uvicorn, Daphne, Hypercorn)**: This is the ASGI server that receives the request from the user. It translates the HTTP request into an ASGI scope and a pair of callables (receive, send).
3. **ASGI Framework (Starlette, FastAPI)**: This is the ASGI framework that takes the ASGI scope and callables, and processes them according to the application-specific logic.
4. **Application Code (Your Python code)**: This is your application code that defines what to do with the request and how to respond.
