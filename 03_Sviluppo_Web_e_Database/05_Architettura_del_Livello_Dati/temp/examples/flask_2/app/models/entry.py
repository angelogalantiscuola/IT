from ..database import get_db_connection
from typing import Optional, List, Dict, Any, Union, Sequence
from mysql.connector.cursor import MySQLCursor


class Entry:
    def __init__(self, id: int, name: str, message: str):
        self.id = id
        self.name = name
        self.message = message


    @staticmethod
    def _row_to_entry(row: Dict[str, Any] | Sequence[Any] | None) -> Optional['Entry']:
        """Convert a database row to an Entry object."""
        if not row:
            return None
        
        if isinstance(row, dict):
            id_val = row.get('id')
            name_val = row.get('name')
            msg_val = row.get('message')
            if id_val is None or name_val is None or msg_val is None:
                return None
            
            try:
                id_int = int(id_val)
                name_str = str(name_val)
                msg_str = str(msg_val)
            except (ValueError, TypeError):
                return None
            
            return Entry(id=id_int, name=name_str, message=msg_str)
        
        # Handle tuple/sequence
        if len(row) < 3:
            return None
        
        id_val, name_val, msg_val = row[0], row[1], row[2]
        if id_val is None or name_val is None or msg_val is None:
            return None

        try:
            id_int = int(id_val)
            name_str = str(name_val)
            msg_str = str(msg_val)
        except (ValueError, TypeError):
            return None
        
        return Entry(id=id_int, name=name_str, message=msg_str)

    @staticmethod
    def get_all(search: Optional[str] = None) -> List['Entry']:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        if search:
            cursor.execute(
                "SELECT * FROM entries WHERE name LIKE %s OR message LIKE %s",
                ("%" + search + "%", "%" + search + "%"),
            )
        else:
            cursor.execute("SELECT * FROM entries")

        results = cursor.fetchall()
        entries = []
        for row in results:
            entry = Entry._row_to_entry(row)
            if entry:
                entries.append(entry)

        cursor.close()
        conn.close()
        return entries

    @staticmethod
    def get_by_id(entry_id: int) -> Optional['Entry']:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM entries WHERE id = %s", (entry_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return Entry._row_to_entry(row)

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
