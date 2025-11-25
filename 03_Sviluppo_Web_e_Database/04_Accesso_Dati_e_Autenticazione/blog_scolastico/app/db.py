import sqlite3
from flask import current_app, g

def get_db():
    """Restituisce la connessione al database per la richiesta corrente."""
    # 'g' è uno zaino temporaneo di Flask. 
    # Se la connessione c'è già, la riusiamo. Se no, la creiamo.
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE']
        )
        # Questa riga serve per poter chiamare le colonne per nome (user['username'])
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    """Chiude la connessione alla fine della richiesta."""
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    """Registra la funzione di chiusura automatica."""
    # Dice a Flask: "Quando hai finito di caricare la pagina, chiudi sempre il DB"
    app.teardown_appcontext(close_db)