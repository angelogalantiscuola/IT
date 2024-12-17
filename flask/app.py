from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="dbname",
    )


@app.route("/")
def list_entries():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("list.html", entries=entries)


@app.route("/add", methods=["GET", "POST"])
def add_entry():
    if request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO entries (name, message) VALUES (%s, %s)"
        values = (request.form["name"], request.form["message"])
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("list_entries"))
    return render_template("form.html")


if __name__ == "__main__":
    # Create table if it doesn't exist
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(80) NOT NULL,
            message VARCHAR(200) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

    app.run(debug=True)
