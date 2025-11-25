# Lezione 6: Protezione delle Route e Funzionalità CRUD Complete

Abbiamo un sistema di autenticazione funzionante, ma al momento non serve a molto: chiunque, anche un utente non loggato, può visitare l'URL `/create` e creare un nuovo post.

In questa lezione finale per il nostro progetto `flask_1`, impareremo a:
1.  **Proteggere le route** per renderle accessibili solo agli utenti autenticati.
2.  Implementare le funzionalità di **modifica (Update)** ed **eliminazione (Delete)** dei post.
3.  Associare ogni post al suo autore.

### 1. Proteggere le Route con un Decoratore

Potremmo aggiungere un controllo `if 'user_id' not in session:` all'inizio di ogni funzione che vogliamo proteggere. Ma questo sarebbe ripetitivo (violando il principio DRY).

La soluzione "Pythonica" è creare un **decoratore**. Un decoratore è una funzione speciale che "avvolge" un'altra funzione per aggiungervi delle funzionalità.

Creeremo un decoratore `@login_required` che controllerà se l'utente è in sessione. Se non lo è, lo reindirizzerà alla pagina di login.

Aggiungi questa funzione al tuo `app.py`, tipicamente dopo le importazioni:

```python
# app.py

# ... (importazioni) ...
from functools import wraps # Importiamo wraps

# ... (app, SECRET_KEY, get_db_connection, etc.) ...

# Definizione del nostro decoratore
def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        # Se 'user_id' non è nella sessione, l'utente non è loggato
        if 'user_id' not in session:
            # Reindirizziamo alla pagina di login
            return redirect(url_for('login'))
        # Altrimenti, eseguiamo la funzione originale che stiamo decorando
        return view(**kwargs)
    return wrapped_view
```
*   `@wraps(view)` è una convenzione che aiuta a mantenere il nome e le informazioni della funzione originale.

Ora, per proteggere una route, ci basterà aggiungere `@login_required` **sotto** il decoratore `@app.route()`:

```python
@app.route('/create', methods=('GET', 'POST'))
@login_required # <-- Ecco come si usa!
def create():
    # ... (il resto della funzione rimane uguale) ...
```
Prova ora: se fai il logout e provi a visitare `/create`, verrai automaticamente reindirizzato alla pagina di login.

### 2. Associare i Post agli Autori

Per sapere chi può modificare o eliminare un post, dobbiamo prima sapere chi l'ha scritto.

**1. Aggiornare lo Schema del Database**
Aggiungiamo una colonna `author_id` alla tabella `posts`, che sarà una chiave esterna verso la tabella `users`.

Modifica `schema.sql`:
```sql
-- schema.sql
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL, -- Aggiunta
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES users (id) -- Aggiunta
);
```
**Riesegui `init_db.py`** per applicare le modifiche. Dovrai anche modificare lo script per inserire un `author_id` nei post di esempio.

**2. Aggiornare la Logica di Creazione**
Modifichiamo la funzione `create()` in `app.py` per salvare l'ID dell'utente loggato insieme al post.

```python
# app.py - funzione create() aggiornata
@app.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author_id = session['user_id'] # Prendiamo l'ID dalla sessione

        # ... (validazione) ...

        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)',
                     (title, content, author_id)) # Aggiungiamo author_id
        conn.commit()
        conn.close()
        return redirect(url_for('home'))

    return render_template('create.html')
```

### 3. Implementare la Modifica di un Post (Update)

Il flusso di modifica richiede due passaggi:
1.  Mostrare un form pre-compilato con i dati attuali del post.
2.  Processare i dati inviati e aggiornare il database.

**1. Creare il Template `edit.html`**
```html
<!-- templates/edit.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Modifica Post</h1>
    <form method="post">
        <label for="title">Titolo</label>
        <!-- Usiamo 'value' per pre-compilare il campo -->
        <input name="title" id="title" value="{{ post['title'] }}" required>
        <br><br>
        <label for="content">Contenuto</label>
        <!-- Il contenuto della textarea va tra i tag di apertura e chiusura -->
        <textarea name="content" id="content" rows="5" required>{{ post['content'] }}</textarea>
        <br><br>
        <input type="submit" value="Salva Modifiche">
    </form>
{% endblock %}
```

**2. Creare la Route per la Modifica in `app.py`**
Questa route accetterà l'ID del post da modificare come parte dell'URL.

```python
# app.py

# Funzione di utilità per prendere un singolo post e controllare l'autore
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT p.id, title, content, created, author_id, username'
                        ' FROM posts p JOIN users u ON p.author_id = u.id'
                        ' WHERE p.id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        # abort(404) interrompe la richiesta e mostra un errore 404
        from flask import abort
        abort(404)
    return post

@app.route('/<int:post_id>/edit', methods=('GET', 'POST'))
@login_required
def edit(post_id):
    post = get_post(post_id)

    # Controlliamo che l'utente loggato sia l'autore del post
    if post['author_id'] != session['user_id']:
        from flask import abort
        abort(403) # Errore 403: Forbidden (accesso negato)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # ... (validazione) ...
        
        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?',
                     (title, content, post_id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))

    return render_template('edit.html', post=post)
```

### 4. Implementare l'Eliminazione di un Post (Delete)

L'eliminazione è più semplice: non serve un template, solo una route che esegua la query `DELETE` e poi faccia un redirect. Per sicurezza, useremo il metodo `POST`.

```python
# app.py

@app.route('/<int:post_id>/delete', methods=('POST',))
@login_required
def delete(post_id):
    post = get_post(post_id)
    # Controlliamo l'autorizzazione
    if post['author_id'] != session['user_id']:
        from flask import abort
        abort(403)

    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))
```

### 5. Aggiornare la Homepage per i Nuovi Link
Infine, modifichiamo `home.html` per mostrare i link "Modifica" e "Elimina" solo se l'utente è loggato ed è l'autore del post.

```html
<!-- templates/home.html (sezione del ciclo for aggiornata) -->
{% for post in posts %}
    <article>
        <h2>{{ post['title'] }}</h2>
        <p><small>Pubblicato il: {{ post['created'] }}</small></p>
        <p>{{ post['content'] }}</p>
        
        <!-- Mostra i link solo se l'utente è l'autore -->
        {% if session.user_id == post.author_id %}
            <a href="{{ url_for('edit', post_id=post.id) }}">Modifica</a>
            <!-- L'eliminazione usa un piccolo form per inviare una richiesta POST -->
            <form action="{{ url_for('delete', post_id=post.id) }}" method="post" style="display:inline;">
                <button type="submit" onclick="return confirm('Sei sicuro?');">Elimina</button>
            </form>
        {% endif %}
    </article>
    <hr>
{% endfor %}
```
*   **Nota:** Per far funzionare il controllo `session.user_id == post.author_id`, dobbiamo modificare la query nella funzione `home()` per includere l'`author_id` del post.

Congratulazioni! Ora hai un'applicazione web **CRUD** completa e funzionante, con un sistema di autenticazione e autorizzazione di base. Hai messo in pratica tutti i concetti fondamentali dello sviluppo backend con Flask.