import os
import json
from flask import Flask
from app.database import init_db, get_db_connection
from werkzeug.security import generate_password_hash

# Import and register blueprints
from app.routes.auth import auth
from app.routes.entries import entries
from app.routes.profile import profile


# Configuration
class Config:
    SECRET_KEY = "your-secret-key-here"  # Change this to a secure secret key
    MYSQL_HOST = "localhost"
    MYSQL_USER = "x"
    MYSQL_PASSWORD = "x"
    MYSQL_DATABASE = "world"


def create_app(config=None):
    app = Flask(__name__)

    # Load default configuration
    app.config.from_object(Config)

    # Override with passed config if provided
    if config:
        app.config.update(config)

    # Initialize database
    init_db()

    # Create initial user
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        ("x", generate_password_hash("x")),
    )
    conn.commit()
    cursor.close()
    conn.close()

    # Populate database from JSON
    json_path = os.path.join(app.static_folder, "messages.json")
    if os.path.exists(json_path):
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

    app.register_blueprint(auth)
    app.register_blueprint(entries)
    app.register_blueprint(profile)

    return app


# Create the application instance
app = create_app()
