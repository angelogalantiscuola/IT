"""
Simple example of a web server using Flask
To run it use a command with this syntax:
flask --app file_name_without_extension run
For example:
flask --app flask_example run
"""

from flask import Flask, send_from_directory, url_for
from markupsafe import escape
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ciao")
def ciao():
    return "<h1>Ciao, Mondo!</h1>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/square_number/<int:number>')
def square_number(number):
    return f'The square of {number} is {number**2}!'


@app.route('/draw_a_segment/<int:x_1>/<int:y_1>/<int:x_2>/<int:y_2>')
def draw_a_segment(x_1, y_1, x_2, y_2):
    # use matplotlib to draw a segment in a file and return the file name
    plt.plot([x_1, x_2], [y_1, y_2])
    plt.savefig('segment.png')
    # create a div with the image
    temp = url_for('static', filename='segment.png')
    return f'<div><img src="{temp}" alt="segment" width="500" height="500"></div>' 

