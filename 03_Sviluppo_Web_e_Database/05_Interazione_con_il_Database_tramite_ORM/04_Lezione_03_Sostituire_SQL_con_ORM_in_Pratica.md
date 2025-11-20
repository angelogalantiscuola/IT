# Lezione 3: Sostituire SQL con l'ORM (CRUD in Pratica)

Abbiamo definito i nostri modelli e integrato Peewee nella nostra applicazione Flask. Ora è il momento del passo finale e più gratificante: riscrivere la logica delle nostre route per usare l'ORM.

L'obiettivo è eliminare ogni traccia di SQL grezzo e di gestione manuale del database (`get_db`, `conn.execute`, etc.) dai nostri Blueprints, rendendo il codice più pulito, più sicuro e interamente orientato agli oggetti.

### 1. Riepilogo della Sintassi CRUD di Peewee

Ricordiamo i metodi che useremo per le operazioni di base. `User` e `Post` sono le nostre classi modello.

*   **Create (`INSERT`):** `Model.create(field=value, ...)`
*   **Read (`SELECT`):**
    *   Singolo oggetto: `Model.get_or_none(Model.field == value)`
    *   Lista di oggetti: `Model.select().where(...)`
*   **Update (`UPDATE`):** `oggetto.field = new_value`, seguito da `oggetto.save()`
*   **Delete (`DELETE`):** `oggetto.delete_instance()`

---

### 2. Refactoring del Blueprint di Autenticazione (`app/auth.py`)

Iniziamo con il file `app/auth.py`.

**Prima (`flask_2` con SQL):**
*   Importavamo `get_db`.
*   Usavamo `db.execute('SELECT ...')` per trovare un utente.
*   Usavamo `db.execute('INSERT ...')` per creare un utente.

**Dopo (Refactoring con Peewee):**

```python
# app/auth.py (versione finale con Peewee)

from flask import (
    Blueprint, render_template, request, redirect, url_for, session
)
from werkzeug.security import generate_password_hash, check_password_hash
# Importiamo i nostri modelli ORM
from app.models import User
from functools import wraps

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username or not password:
            error = 'Username e password sono obbligatori.'
        
        # CONTROLLO CON PEEWEE
        elif User.get_or_none(User.username == username):
            error = f"L'utente {username} è già registrato."

        if error is None:
            # Hashing della password
            password_hash = generate_password_hash(password)
            # CREAZIONE CON PEEWEE
            User.create(username=username, password=password_hash)
            
            return redirect(url_for('auth.login'))
        
        # Flash message per l'errore (opzionale, ma buona pratica)
        from flask import flash
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # LETTURA CON PEEWEE
        user = User.get_or_none(User.username == username)

        error = None
        if user is None or not check_password_hash(user.password, password):
            error = 'Username o password non corretti'

        if error is None:
            session.clear()
            session['user_id'] = user.id # Accediamo all'attributo .id dell'oggetto
            return redirect(url_for('posts.home'))

        from flask import flash
        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('posts.home'))

# Il decoratore rimane quasi uguale, ma punta a 'auth.login'
def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
```

### 3. Refactoring del Blueprint dei Post (`app/posts.py`)

Applichiamo la stessa trasformazione a `app/posts.py`.

```python
# app/posts.py (versione finale con Peewee)

from flask import (
    Blueprint, render_template, request, redirect, url_for, session, abort
)
# Importiamo i modelli e il decoratore
from app.models import Post, User
from app.auth import login_required

bp = Blueprint('posts', __name__)

@bp.route('/')
def home():
    # SELECT CON PEEWEE
    # Peewee esegue automaticamente il JOIN grazie al ForeignKeyField
    posts = Post.select().order_by(Post.created.desc())
    return render_template('posts/home.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        if not title or not content:
            # Gestione errore...
            pass
        else:
            # CREATE CON PEEWEE
            Post.create(title=title, content=content, author=session['user_id'])
            return redirect(url_for('posts.home'))

    return render_template('posts/create.html')

# Funzione di utilità per prendere un post (ora usa l'ORM)
def get_post(post_id, check_author=True):
    post = Post.get_or_none(Post.id == post_id)
    if post is None:
        abort(404)
    if check_author and post.author.id != session['user_id']:
        abort(403)
    return post

@bp.route('/<int:post_id>/edit', methods=('GET', 'POST'))
@login_required
def edit(post_id):
    post = get_post(post_id)

    if request.method == 'POST':
        # UPDATE CON PEEWEE
        post.title = request.form['title']
        post.content = request.form['content']
        post.save() # Il metodo .save() esegue la query UPDATE
        return redirect(url_for('posts.home'))

    return render_template('posts/edit.html', post=post)

@bp.route('/<int:post_id>/delete', methods=('POST',))
@login_required
def delete(post_id):
    post = get_post(post_id)
    # DELETE CON PEEWEE
    post.delete_instance()
    return redirect(url_for('posts.home'))
```

### 4. Aggiornare i Template: da Dizionario a Oggetto

L'ultimo passo è aggiornare i nostri template. Invece di ricevere dizionari (o `sqlite3.Row`), ora ricevono oggetti `Post` e `User`. L'accesso ai dati cambia dalla sintassi con le parentesi quadre (`post['title']`) alla sintassi con il punto (`post.title`).

**Esempio in `posts/home.html`:**

```html
<!-- templates/posts/home.html (ciclo for aggiornato) -->
{% for post in posts %}
    <article>
        <!-- Nuova sintassi a oggetti -->
        <h2>{{ post.title }}</h2>
        <!-- Grazie alla relazione, possiamo accedere all'autore con post.author -->
        <p><small>Pubblicato il: {{ post.created.strftime('%Y-%m-%d') }} by {{ post.author.username }}</small></p>
        <p>{{ post.content }}</p>
        
        {% if session.user_id == post.author.id %}
            <a href="{{ url_for('posts.edit', post_id=post.id) }}">Modifica</a>
            <form action="{{ url_for('posts.delete', post_id=post.id) }}" method="post" style="display:inline;">
                <button type="submit" onclick="return confirm('Sei sicuro?');">Elimina</button>
            </form>
        {% endif %}
    </article>
    <hr>
{% endfor %}
```
*   Nota `post.author.username`: questa è la magia dell'ORM! Peewee capisce la relazione e ci permette di navigare dagli oggetti `Post` agli oggetti `User` correlati in modo del tutto naturale.

### Esercizio Finale del Capitolo
1.  **Elimina** il file `app/db.py` e la cartella `instance/` (Peewee la ricreerà).
2.  **Sostituisci** il contenuto di `app/auth.py` e `app/posts.py` con il nuovo codice basato su Peewee.
3.  **Aggiorna tutti i template** (`home.html`, `edit.html`, etc.) per usare la notazione a punto (`.`) per accedere agli attributi degli oggetti.
4.  Avvia l'applicazione (`python run.py`).

Dovrebbe funzionare esattamente come prima, ma internamente il codice è ora molto più pulito, più sicuro, e allineato con le moderne pratiche di sviluppo software.