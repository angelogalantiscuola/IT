from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

# app = Flask(__name__)
app = Flask(__name__, static_url_path="", static_folder=os.path.dirname(__file__))

CORS(app)

users = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Doe"},
]
next_id = 3


@app.route("/")
def index():
    return send_from_directory(os.path.dirname(__file__), "index.html")


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route("/users", methods=["POST"])
def add_user():
    global next_id
    new_user = request.get_json()
    new_user["id"] = next_id
    next_id += 1
    users.append(new_user)
    return jsonify(new_user)


if __name__ == "__main__":
    app.run(debug=True)
