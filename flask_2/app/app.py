from flask import Flask, redirect, url_for
from .database import init_db, get_db_connection
from werkzeug.security import generate_password_hash


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.update(
        SECRET_KEY="your-secret-key-here",
        MYSQL_HOST="localhost",
        MYSQL_USER="x",
        MYSQL_PASSWORD="x",
        MYSQL_DATABASE="world",
    )

    # Initialize database
    with app.app_context():
        init_db()

        # Create initial user if needed
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                ("x", generate_password_hash("x")),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    # Register blueprints
    from .routes.auth import auth
    from .routes.entries import entries
    from .routes.profile import profile

    app.register_blueprint(auth)
    app.register_blueprint(entries)
    app.register_blueprint(profile)

    # Add root route
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    return app
