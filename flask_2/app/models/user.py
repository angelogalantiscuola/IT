from werkzeug.security import generate_password_hash, check_password_hash
from ..database import get_db_connection


class User:
    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password

    # @staticmethod because we don't need instance access (self)
    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if user_data:
            # ** unpacks user_data dictionary into keyword arguments for User constructor
            return User(**user_data)
        return None

    @staticmethod
    def get_by_username(username):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if user_data:
            return User(**user_data)
        return None

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        if self.id:
            # Update existing user
            cursor.execute(
                "UPDATE users SET username = %s WHERE id = %s", (self.username, self.id)
            )
        else:
            # Create new user
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (self.username, generate_password_hash(self.password)),
            )
            self.id = cursor.lastrowid

        conn.commit()
        cursor.close()
        conn.close()

    def verify_password(self, password):
        return check_password_hash(self.password, password)
