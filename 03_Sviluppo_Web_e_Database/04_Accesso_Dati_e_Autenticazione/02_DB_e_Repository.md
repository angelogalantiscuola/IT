# Lezione 1: Database SQL e Repository Pattern

Finora il nostro sito mostrava dati statici (liste scritte a mano nel codice). Ora diamogli una memoria permanente.
Useremo **SQLite**, un database che salva tutto in un semplice file sul tuo computer. È perfetto per iniziare.

In questa lezione impareremo a:
1.  Connetterci al database in modo sicuro.
2.  Creare le tabelle (lo Schema).
3.  Usare il **Repository Pattern** per non sporcare il nostro codice Python con l'SQL.

### 1. Il modulo `app/db.py`: Gestire la Connessione

In Flask, la connessione al database deve essere aperta quando arriva una richiesta e **chiusa assolutamente** quando la richiesta finisce. Se non la chiudiamo, il server si bloccherà dopo poche visite.

Crea il file `app/db.py`.

#### Concetto Chiave: L'oggetto `g`
Flask ci mette a disposizione un oggetto speciale chiamato `g` (che sta per "global"). Immaginalo come uno **zaino** che dura solo per il tempo di una richiesta.
*   Arriva la richiesta -> Lo zaino è vuoto.
*   Ci serve il database -> Mettiamo la connessione nello zaino.
*   Ci serve di nuovo il database -> Lo prendiamo dallo zaino (senza riconnetterci).
*   Fine richiesta -> Lo zaino viene svuotato e la connessione chiusa.

Scriviamo il codice commentato:

```python
import sqlite3
import click # Libreria per creare comandi da terminale
from flask import current_app, g

def get_db():
    # Se 'db' non è ancora nello "zaino" g, lo creiamo
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            # detect_types serve a gestire le date.
            # SQLite salva le date come testo. Questa opzione dice a Python:
            # "Se leggi una colonna data, trasformala subito in un oggetto Date di Python"
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Questa riga ci permette di accedere ai dati usando i nomi delle colonne
        # (es. user['username']) invece che i numeri (user[1])
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    # Se c'è una connessione aperta, chiudila.
    db = g.pop('db', None)

    if db is not None:
        db.close()
```

### 2. Creare le Tabelle (Schema SQL)

Dobbiamo dire al database come sono fatti i nostri dati.
Crea il file `app/schema.sql`.

```sql
-- Se esistono già tabelle vecchie, le cancelliamo per ripartire da zero
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

-- Tabella Utenti
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL, -- UNIQUE: non possono esistere due user uguali
  password TEXT NOT NULL
);

-- Tabella Post
CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  -- Relazione: author_id punta all'id della tabella user
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```

### 3. Inizializzare il Database da Terminale

Ora ci serve un modo per eseguire questo codice SQL. Invece di usare un programma esterno, creeremo un comando personalizzato per Flask.
Vogliamo poter scrivere nel terminale `flask init-db` per resettare tutto.

Aggiungi questo codice alla fine di `app/db.py`:

```python
# ... (dopo la funzione close_db) ...

def init_db():
    """Cancella i dati esistenti e crea nuove tabelle."""
    db = get_db()
    # Leggiamo il file schema.sql
    with current_app.open_resource('schema.sql') as f:
        # Eseguiamo tutto l'SQL contenuto nel file
        db.executescript(f.read().decode('utf8'))

# @click.command crea un nuovo comando per il terminale chiamato 'init-db'
@click.command('init-db')
def init_db_command():
    """Cancella i dati esistenti e crea nuove tabelle."""
    init_db()
    click.echo('Database inizializzato.') # Stampa un messaggio di conferma

# Questa funzione serve a "registrare" tutto questo nella nostra applicazione
def init_app(app):
    # Diciamo a Flask: "Quando finisce una richiesta, chiama sempre close_db"
    app.teardown_appcontext(close_db)
    # Aggiungiamo il nostro nuovo comando al terminale
    app.cli.add_command(init_db_command)
```

### 4. Collegare tutto nella Factory

Ora dobbiamo dire alla nostra "Fabbrica" (`create_app`) di usare questo nuovo modulo `db`.

Apri `app/__init__.py` e aggiungi le due righe segnate:

```python
def create_app():
    # ... (codice precedente) ...

    # --- INIZIALIZZAZIONE DATABASE ---
    from . import db
    db.init_app(app)
    # -------------------------------
    
    # ... (registrazione blueprint) ...
    return app
```

### 5. Proviamo!

Apri il terminale e digita:
```bash
flask init-db
```
Se vedi la scritta `Database inizializzato.`, tutto funziona! Hai appena creato il file `instance/blog.sqlite` con le tabelle vuote.

---

### 6. Il Repository Pattern: Separare l'SQL

Ora che il DB c'è, come lo usiamo?
**NON** scriveremo codice SQL dentro le nostre pagine web (Route). È disordinato e pericoloso.

Creeremo un "Reparto Dati" dedicato.
Crea una cartella `app/repositories/` e dentro un file `user_repository.py`.

```python
# app/repositories/user_repository.py
from app.db import get_db

def create_user(username, password_hash):
    """
    Inserisce un nuovo utente nel DB.
    Restituisce True se ha successo, False se l'utente esiste già.
    """
    db = get_db()
    try:
        # Usiamo ? come segnaposto per i dati. È FONDAMENTALE per la sicurezza!
        # Previene l'SQL Injection.
        db.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            (username, password_hash),
        )
        # commit() serve per salvare le modifiche in modo definitivo
        db.commit()
        return True
    except db.IntegrityError:
        # Succede se lo username esiste già (violazione del vincolo UNIQUE)
        return False

def get_user_by_username(username):
    """
    Cerca un utente per nome.
    Restituisce l'oggetto riga o None se non trovato.
    """
    db = get_db()
    user = db.execute(
        "SELECT * FROM user WHERE username = ?", (username,)
    ).fetchone() # fetchone() prende il primo risultato trovato
    return user

def get_user_by_id(user_id):
    """Cerca un utente per ID."""
    db = get_db()
    user = db.execute(
        "SELECT * FROM user WHERE id = ?", (user_id,)
    ).fetchone()
    return user
```

**Cosa abbiamo ottenuto?**
Abbiamo nascosto la complessità dell'SQL. Nelle prossime lezioni, per creare un utente ci basterà scrivere:
`user_repository.create_user("mario", "password_segreta")`.
Pulito, semplice e professionale.