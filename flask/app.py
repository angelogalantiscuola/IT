import json
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify,
)
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = "your-secret-key-here"  # Change this to a secure secret key


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="x",
        password="x",
        database="world",
    )


def populate_db_from_json():
    json_path = os.path.join(app.static_folder, "messages.json")
    with open(json_path) as f:
        messages = json.load(f)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM entries")
    count = cursor.fetchone()[0]

    if count == 0:
        for message in messages:
            cursor.execute(
                "INSERT INTO entries (name, message) VALUES (%s, %s)",
                (message["name"], message["message"]),
            )
        conn.commit()

    cursor.close()
    conn.close()


@app.route("/")
def list_entries():
    search = request.args.get("search")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if search:
        cursor.execute(
            "SELECT * FROM entries WHERE name LIKE %s OR message LIKE %s",
            ("%" + search + "%", "%" + search + "%"),
        )
    else:
        cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("list.html", entries=entries)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Check if username exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            cursor.close()
            conn.close()
            flash("Username already exists")
            return redirect(url_for("register"))

        # Create new user
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, generate_password_hash(password)),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("list_entries"))
        flash("Invalid username or password")
    return render_template("login.html")


@app.route("/password_reset_request", methods=["GET", "POST"])
def password_reset_request():
    if request.method == "POST":
        _ = request.form["email"]
        # Logic to send password reset email goes here
        flash("Password reset email sent")
        return redirect(url_for("login"))
    return render_template("password_reset_request.html")


@app.route("/password_reset/<token>", methods=["GET", "POST"])
def password_reset(token):
    if request.method == "POST":
        _ = request.form["password"]
        # Logic to reset the password goes here
        flash("Password has been reset")
        return redirect(url_for("login"))
    return render_template("password_reset.html", token=token)


@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/entries/new", methods=["GET", "POST"])
def create_entry():
    if "user_id" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO entries (name, message) VALUES (%s, %s)"
        values = (name, message)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("list_entries"))
    return render_template("create.html")


@app.route("/entries/<int:id>", methods=["GET"])
def read_entry(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM entries WHERE id = %s", (id,))
    entry = cursor.fetchone()
    cursor.close()
    conn.close()
    if entry:
        return render_template("read.html", entry=entry)
    return jsonify({"message": "Entry not found"}), 404


@app.route("/entries/<int:id>/edit", methods=["GET", "POST"])
def update_entry(id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM entries WHERE id = %s", (id,))
    entry = cursor.fetchone()
    if not entry:
        cursor.close()
        conn.close()
        return jsonify({"message": "Entry not found"}), 404
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        sql = "UPDATE entries SET name = %s, message = %s WHERE id = %s"
        values = (name, message, id)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("list_entries"))
    cursor.close()
    conn.close()
    return render_template("update.html", entry=entry)


@app.route("/entries/<int:id>/delete", methods=["GET", "POST"])
def delete_entry(id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM entries WHERE id = %s", (id,))
    entry = cursor.fetchone()
    if not entry:
        cursor.close()
        conn.close()
        return jsonify({"message": "Entry not found"}), 404
    if request.method == "POST":
        sql = "DELETE FROM entries WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("list_entries"))
    cursor.close()
    conn.close()
    return render_template("delete.html", entry=entry)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (session["user_id"],))
    user = cursor.fetchone()
    if request.method == "POST":
        username = request.form["username"]
        # Logic to update user profile goes here
        cursor.execute(
            "UPDATE users SET username = %s WHERE id = %s",
            (username, session["user_id"]),
        )
        conn.commit()
        flash("Profile updated")
    cursor.close()
    conn.close()
    return render_template("profile.html", user=user)


if __name__ == "__main__":
    conn = get_db_connection()
    cursor = conn.cursor()

    # Drop users table if exists
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS entries")

    # Create users table
    cursor.execute("""
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(80) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)
    # Insert initial user
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        ("x", generate_password_hash("x")),
    )

    # Create entries table
    cursor.execute("""
        CREATE TABLE entries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(80) NOT NULL,
            message VARCHAR(200) NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    # Populate the database with messages from JSON file
    populate_db_from_json()

    app.run(debug=True)
