from app.db import get_db
from datetime import datetime

def get_all_posts():
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
    posts = db.execute(query).fetchall()
    # Converti 'created' da stringa a datetime
    result = []
    for post in posts:
        post_dict = dict(post)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        result.append(post_dict)
    return result

def get_post_by_id(post_id):
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
    if post:
        post_dict = dict(post)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        return post_dict
    return post

def create_post(title, body, author_id):
    """Crea un nuovo post."""
    db = get_db()
    db.execute(
        'INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)',
        (title, body, author_id)
    )
    db.commit()

def update_post(post_id, title, body):
    """Aggiorna un post."""
    db = get_db()
    db.execute(
        'UPDATE post SET title = ?, body = ? WHERE id = ?',
        (title, body, post_id)
    )
    db.commit()

def delete_post(post_id):
    """Elimina un post."""
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (post_id,))
    db.commit()