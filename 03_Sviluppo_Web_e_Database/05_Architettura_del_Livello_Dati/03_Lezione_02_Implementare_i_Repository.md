# Lezione 2: Implementare i Repository

Nella lezione precedente abbiamo capito *perché* dobbiamo separare la logica di accesso ai dati. Ora passiamo alla pratica e creiamo il nostro **Data Access Layer** utilizzando il Repository Pattern.

L'obiettivo di questa lezione è creare i nuovi moduli "repository" e spostare al loro interno tutto il codice che interagisce direttamente con il database.

### 1. Creare la Struttura per i Repository

Per prima cosa, creiamo una nuova cartella all'interno del nostro pacchetto `app` per ospitare i moduli del nostro livello dati. Chiameremo questa cartella `data`.

```
flask_2/
└── app/
    ├── __init__.py
    ├── auth.py
    ├── data/                 # <-- NUOVA CARTELLA
    │   ├── user_repository.py  # <-- NUOVO FILE
    │   └── post_repository.py  # <-- NUOVO FILE
    ├── db.py
    ├── posts.py
    └── ...
```
*   Creeremo un file per ogni entità principale che gestiamo. Per ora, `user_repository.py` si occuperà della tabella `users` e `post_repository.py` della tabella `posts`.

### 2. Implementare il `user_repository.py`

Apriamo il file `app/data/user_repository.py`. Il suo compito è fornire tutte le funzioni necessarie per interagire con la tabella `users`.

Identifichiamo le operazioni che il nostro `auth.py` compie sulla tabella `users`:
1.  Trovare un utente dato il suo username (per il login).
2.  Trovare un utente dato il suo ID (per caricare l'utente in sessione).
3.  Creare un nuovo utente (per la registrazione).

Ora, traduciamo queste operazioni in funzioni.

```python
# app/data/user_repository.py

from app.db import get_db

def find_by_username(username):
    """
    Trova un utente nel database dato il suo username.
    Restituisce una riga (sqlite3.Row) o None se non trovato.
    """
    db = get_db()
    user = db.execute(
        'SELECT * FROM users WHERE username = ?', (username,)
    ).fetchone()
    return user

def find_by_id(user_id):
    """
    Trova un utente nel database dato il suo ID.
    Restituisce una riga (sqlite3.Row) o None se non trovato.
    """
    db = get_db()
    user = db.execute(
        'SELECT * FROM users WHERE id = ?', (user_id,)
    ).fetchone()
    return user

def create(username, password_hash):
    """
    Crea un nuovo utente nel database.
    """
    db = get_db()
    db.execute(
        'INSERT INTO users (username, password) VALUES (?, ?)',
        (username, password_hash)
    )
    db.commit()
```
*   **Osservazioni:**
    *   Questo file ora è l'**unico** che importa `get_db()`.
    *   Le funzioni hanno nomi chiari che descrivono la loro intenzione (`find_by_username` invece di una generica `execute`).
    *   La logica SQL è completamente incapsulata qui.

### 3. Implementare il `post_repository.py`

Facciamo lo stesso per le operazioni sui post. Apriamo `app/data/post_repository.py`.

Identifichiamo le operazioni che `posts.py` compie sulla tabella `posts`:
1.  Ottenere tutti i post per la homepage.
2.  Ottenere un singolo post dato il suo ID.
3.  Creare un nuovo post.
4.  Aggiornare un post esistente.
5.  Eliminare un post.

```python
# app/data/post_repository.py

from app.db import get_db

def find_all():
    """Recupera tutti i post, unendo i dati dell'autore."""
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, content, created, author_id, username'
        ' FROM posts p JOIN users u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return posts

def find_by_id(post_id):
    """Recupera un singolo post dato il suo ID."""
    db = get_db()
    post = db.execute(
        'SELECT p.id, title, content, created, author_id, username'
        ' FROM posts p JOIN users u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (post_id,)
    ).fetchone()
    return post

def create(title, content, author_id):
    """Crea un nuovo post."""
    db = get_db()
    db.execute(
        'INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)',
        (title, content, author_id)
    )
    db.commit()

def update(post_id, title, content):
    """Aggiorna un post esistente."""
    db = get_db()
    db.execute(
        'UPDATE posts SET title = ?, content = ? WHERE id = ?',
        (title, content, post_id)
    )
    db.commit()

def delete(post_id):
    """Elimina un post."""
    db = get_db()
    db.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    db.commit()
```

### 4. Gestire la Logica dell'Utente in Sessione
Notiamo che nel nostro vecchio `posts.py` c'è una logica che carica i dati dell'utente loggato. Questa è una logica trasversale, non legata a una specifica route. Il posto migliore per questa logica è nel Blueprint di autenticazione, usando un decoratore speciale di Flask.

In `app/auth.py`, aggiungiamo questa funzione:

```python
# app/auth.py (aggiungere questa funzione)

from flask import g # 'g' è un oggetto speciale di Flask per i dati della richiesta

# ... (altre importazioni) ...
from .data import user_repository # Importiamo il nostro nuovo repository

# ... (bp, e altre route) ...

@bp.before_app_request
def load_logged_in_user():
    """
    Carica i dati dell'utente dalla sessione in g.user,
    se l'utente è loggato.
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        # Usiamo il repository per caricare i dati dell'utente
        g.user = user_repository.find_by_id(user_id)
```
*   `@bp.before_app_request`: Questo decoratore dice a Flask di eseguire questa funzione **prima di ogni richiesta**, dopo che il Blueprint è stato registrato.
*   `g`: È un oggetto speciale di Flask che dura solo per il tempo di una singola richiesta. È il posto perfetto per memorizzare dati a cui diverse parti del codice potrebbero aver bisogno di accedere, come i dati dell'utente loggato.

### Prossimo Passo

Abbiamo creato con successo il nostro Data Access Layer. Tutto il nostro codice SQL ora vive in un posto solo, ben organizzato e isolato.

I nostri file `auth.py` e `posts.py` sono ancora pieni del vecchio codice SQL. Nella prossima lezione, li "puliremo", sostituendo tutto il codice di accesso al database con semplici chiamate alle funzioni che abbiamo appena scritto.