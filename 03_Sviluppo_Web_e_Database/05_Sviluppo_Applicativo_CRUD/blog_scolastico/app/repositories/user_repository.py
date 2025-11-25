# Importiamo la nostra funzione per prendere la connessione
from app.db import get_db

def create_user(username, password_hash):
    """Inserisce un nuovo utente."""
    db = get_db()
    try:
        db.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            (username, password_hash),
        )
        db.commit() # Salviamo le modifiche
        return True
    except db.IntegrityError:
        # Errore: lo username esiste già
        return False

def get_user_by_username(username):
    """Cerca un utente per nome."""
    db = get_db()
    user = db.execute(
        "SELECT * FROM user WHERE username = ?", (username,)
    ).fetchone()
    return user

def get_user_by_id(user_id):
    """Cerca un utente per ID."""
    db = get_db()
    user = db.execute(
        "SELECT * FROM user WHERE id = ?", (user_id,)
    ).fetchone()
    return user