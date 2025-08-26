from flask import Flask, request, render_template

app = Flask(__name__)

# GET and POST are two different types of HTTP methods.

# GET: It is used to retrieve data from a server. 
# It's safe and idempotent, meaning that it can be called multiple times 
# without different outcomes. 
# It should not be used when dealing with sensitive data or to modify the server state.

# POST: It is used to send data to a server to create/update a resource. 
# The data sent to the server with the POST method is stored in the request body. 
# POST requests are never cached and do not remain in the browser history.


@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        # this is a POST request
        # we'll access the data from the form using request.form
        name = request.form.get('name')
        age = request.form.get('age')
        return 'You posted: Name - ' + str(name) + ', Age - ' + str(age)
    else:
        # this is a GET request, show the form
        return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)