import mysql.connector
from flask import current_app
from werkzeug.security import generate_password_hash
import json


def get_db_connection():
    return mysql.connector.connect(
        host=current_app.config["MYSQL_HOST"],
        user=current_app.config["MYSQL_USER"],
        password=current_app.config["MYSQL_PASSWORD"],
        database=current_app.config["MYSQL_DATABASE"],
    )


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Drop existing tables
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

    # Create entries table
    cursor.execute("""
        CREATE TABLE entries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(80) NOT NULL,
            message VARCHAR(200) NOT NULL
        )
    """)

    # Insert initial user
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        ("x", generate_password_hash("x")),
    )

    # Load initial entries from messages.json
    with open(current_app.root_path + "/static/messages.json") as f:
        messages = json.load(f)
        for message in messages:
            cursor.execute(
                "INSERT INTO entries (name, message) VALUES (%s, %s)",
                (message["name"], message["message"]),
            )

    conn.commit()
    cursor.close()
    conn.close()
