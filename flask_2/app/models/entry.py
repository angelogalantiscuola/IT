from ..database import get_db_connection


class Entry:
    def __init__(self, id=None, name=None, message=None):
        self.id = id
        self.name = name
        self.message = message

    @staticmethod
    def get_all(search=None):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        if search:
            cursor.execute(
                "SELECT * FROM entries WHERE name LIKE %s OR message LIKE %s",
                ("%" + search + "%", "%" + search + "%"),
            )
        else:
            cursor.execute("SELECT * FROM entries")

        entries = [Entry(**entry) for entry in cursor.fetchall()]
        cursor.close()
        conn.close()
        return entries

    @staticmethod
    def get_by_id(entry_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM entries WHERE id = %s", (entry_id,))
        entry_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if entry_data:
            return Entry(**entry_data)
        return None

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        if self.id:
            # Update existing entry
            cursor.execute(
                "UPDATE entries SET name = %s, message = %s WHERE id = %s",
                (self.name, self.message, self.id),
            )
        else:
            # Create new entry
            cursor.execute(
                "INSERT INTO entries (name, message) VALUES (%s, %s)",
                (self.name, self.message),
            )
            self.id = cursor.lastrowid

        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        if not self.id:
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM entries WHERE id = %s", (self.id,))
        conn.commit()
        cursor.close()
        conn.close()
