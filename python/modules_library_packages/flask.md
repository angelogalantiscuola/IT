# Flask

Flask is a lightweight **web application framework** written in Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It provides functionalities for routing, template engine. It is a **microframework** that doesn’t include an ORM (Object Relational Manager) or such features.

Here is a simple example of a Flask application:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

In this example, `@app.route('/')` is a decorator that tells Flask what URL should trigger the function `hello_world()`. When you navigate to the root URL of your server in a web browser, Flask triggers this function and returns its result to the browser.

## Main functionalities

Flask provides several core functionalities that make it a powerful and flexible web framework:

1. **Routing**: Flask allows you to map URLs to Python functions. These functions, known as view functions, return responses to be displayed on the web page corresponding to the **URL**.

2. **Templates**: Flask uses a template engine called **Jinja2** that allows you to build dynamic web pages. You can insert values into web pages dynamically based on the context provided to the template.

3. **Request Handling**: Flask provides a request object for each HTTP request. This object contains the data sent by the client, allowing you to handle different types of requests (GET, POST, etc.) and access the data they contain.

4. **Response Handling**: Flask allows you to construct HTTP responses to send back to the client. You can specify the data, status code, headers, and more.

5. **Sessions**: Flask provides a way to remember information from one request to another. This is useful for storing user-specific data, like items in a shopping cart.

### Routing

Routing in Flask is a mechanism to **map specific URLs to associated functions**. These functions are called view functions and are responsible for handling requests to the application and returning responses to the client.

Here's a basic example of routing in Flask:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'
```

In this example, the `@app.route('/')` decorator tells Flask to call the `home()` function and return its result when the user navigates to the root URL (`/`). Similarly, `@app.route('/about')` maps the URL `/about` to the `about()` function.

Flask's routing also supports variable rules, where sections of the URL can be marked as variables that get passed to the view function. For example:

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username
```

In this case, any value put in place of `<username>` in the URL will be passed to the `show_user_profile` function as the `username` argument.

### Templates

Flask uses a templating engine called **Jinja2** that allows you to build dynamic web pages. Templates are a way to separate your Python logic from your HTML content. You can insert values into your HTML with expressions surrounded by `{{ }}`.

Here's a basic example of a Flask application using a template:

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
        return render_template('hello.html', name=name)
```

In this example, when the user navigates to `/hello/<name>`, the `hello` function is called. This function then renders the `hello.html` template, passing it the `name` variable.

The `hello.html` file might look something like this:

```html
<!DOCTYPE html>
<html>
<body>

<h1>Hello {{ name }}!</h1>

</body>
</html>
```

In this template, `{{ name }}` is a placeholder for the value of the `name` variable that was passed to the template from the `hello` function. When the template is rendered, every occurrence of `{{ name }}` is replaced with the actual value of `name`.

Templates can include a variety of control structures, such as conditionals and loops. For example:

```html
{% if name %}
    <h1>Hello {{ name }}!</h1>
{% else %}
    <h1>Hello, World!</h1>
{% endif %}
```

In this example, if `name` is defined and not an empty string, then `Hello {{ name }}!` is displayed. Otherwise, `Hello, World!` is displayed.


