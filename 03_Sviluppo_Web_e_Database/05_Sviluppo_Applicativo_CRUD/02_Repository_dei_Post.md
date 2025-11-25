# Lezione 1: Il Repository dei Post e le Relazioni SQL

Il cuore di un blog sono i post. Un post non vive da solo: è scritto da un **Autore**.
In SQL, questa è una relazione **Molti-a-Uno**: molti post possono essere scritti dallo stesso utente.

Nel nostro repository, dovremo scrivere query che collegano le due tabelle (`post` e `user`) usando la clausola `JOIN`.

### 1. Creare `app/repositories/post_repository.py`

Questo file gestirà tutte le operazioni sui post.

```python
from app.db import get_db

def find_all():
    """
    Recupera tutti i post.
    Esegue una JOIN con la tabella user per ottenere anche lo username dell'autore.
    """
    db = get_db()
    # Spiegazione Query:
    # SELECT p.*, u.username: Prendi tutto del post e SOLO lo username dell'utente
    # FROM post p: 'p' è un soprannome (alias) per la tabella post
    # JOIN user u: 'u' è un soprannome per la tabella user
    # ON p.author_id = u.id: Collega le righe dove l'ID combacia
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        ORDER BY p.created DESC
    """
    return db.execute(query).fetchall()

def find_by_id(post_id):
    """Recupera un singolo post per ID (con JOIN per l'autore)."""
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        WHERE p.id = ?
    """
    # fetchone() perché ci aspettiamo un solo risultato
    post = db.execute(query, (post_id,)).fetchone()
    return post

def create(title, body, author_id):
    """Crea un nuovo post."""
    db = get_db()
    db.execute(
        'INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)',
        (title, body, author_id)
    )
    db.commit()

def update(post_id, title, body):
    """Aggiorna un post."""
    db = get_db()
    db.execute(
        'UPDATE post SET title = ?, body = ? WHERE id = ?',
        (title, body, post_id)
    )
    db.commit()

def delete(post_id):
    """Elimina un post."""
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (post_id,))
    db.commit()
```