# Lezione 3: Refactoring delle Route per Usare i Repository

Nelle lezioni precedenti abbiamo creato il nostro Data Access Layer, isolando tutto il codice SQL nei moduli "repository". Ora, i nostri file `auth.py` e `posts.py` sono pronti per essere "puliti".

L'obiettivo di questa lezione è riscrivere le nostre view function in modo che non parlino più direttamente con il database. Invece, delegheranno tutte le operazioni di persistenza ai repository che abbiamo appena creato. Questo completerà il disaccoppiamento della nostra architettura.

### 1. Refactoring del Blueprint di Autenticazione (`app/auth.py`)

Iniziamo con il file che gestisce la registrazione e il login. Rimuoveremo ogni importazione di `get_db` e ogni chiamata a `db.execute`.

```python
# app/auth.py (versione finale con Repository Pattern)

from flask import (
    Blueprint, render_template, request, redirect, url_for, session, g, flash
)
from werkzeug.security import generate_password_hash, check_password_hash
# NON importiamo più 'get_db'!
# Importiamo invece il nostro repository
from app.data import user_repository
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
        
        # CHIAMATA AL REPOSITORY
        elif user_repository.find_by_username(username) is not None:
            error = f"L'utente {username} è già registrato."

        if error is None:
            password_hash = generate_password_hash(password)
            # CHIAMATA AL REPOSITORY
            user_repository.create(username, password_hash)
            return redirect(url_for('auth.login'))
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        
        # CHIAMATA AL REPOSITORY
        user = user_repository.find_by_username(username)

        if user is None or not check_password_hash(user['password'], password):
            error = 'Username o password non corretti'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('posts.home'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('posts.home'))

# Questa funzione ora usa il repository per caricare l'utente
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = user_repository.find_by_id(user_id)

# Il decoratore non cambia, ma si appoggia a g.user caricato prima
def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
```
*   **Risultato:** Il file `auth.py` ora è responsabile **solo** della logica di autenticazione e HTTP. Non ha idea di come gli utenti vengano salvati o recuperati.

### 2. Refactoring del Blueprint dei Post (`app/posts.py`)

Applichiamo la stessa, radicale pulizia al nostro file `posts.py`.

```python
# app/posts.py (versione finale con Repository Pattern)

from flask import (
    Blueprint, render_template, request, redirect, url_for, g, abort, flash
)
# Importiamo il decoratore e i repository
from app.auth import login_required
from app.data import post_repository

bp = Blueprint('posts', __name__)

@bp.route('/')
def home():
    # CHIAMATA AL REPOSITORY
    posts = post_repository.find_all()
    return render_template('posts/home.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = 'Il titolo è obbligatorio.'

        if error is not None:
            flash(error)
        else:
            # CHIAMATA AL REPOSITORY
            post_repository.create(title, content, g.user['id'])
            return redirect(url_for('posts.home'))

    return render_template('posts/create.html')

@bp.route('/<int:post_id>/edit', methods=('GET', 'POST'))
@login_required
def edit(post_id):
    # CHIAMATA AL REPOSITORY
    post = post_repository.find_by_id(post_id)
    if post is None:
        abort(404)
    
    if post['author_id'] != g.user['id']:
        abort(403)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # ... validazione ...

        # CHIAMATA AL REPOSITORY
        post_repository.update(post_id, title, content)
        return redirect(url_for('posts.home'))

    return render_template('posts/edit.html', post=post)

@bp.route('/<int:post_id>/delete', methods=('POST',))
@login_required
def delete(post_id):
    post = post_repository.find_by_id(post_id)
    if post is None:
        abort(404)
    if post['author_id'] != g.user['id']:
        abort(403)

    # CHIAMATA AL REPOSITORY
    post_repository.delete(post_id)
    return redirect(url_for('posts.home'))
```
*   **Risultato:** Anche `posts.py` è ora pulito. Le sue funzioni orchestrano il flusso: ricevono una richiesta, chiedono al repository di compiere un'azione sui dati, e restituiscono una risposta.

### 3. L'Architettura Finale a 3 Livelli

Con questo refactoring, abbiamo creato una classica e robusta **architettura a 3 livelli**:

1.  **Livello di Presentazione (Presentation Layer):**
    *   **Cosa:** I nostri template HTML (`templates/`).
    *   **Responsabilità:** Visualizzare i dati e fornire un'interfaccia all'utente.

2.  **Livello Applicativo/Logico (Application/Business Logic Layer):**
    *   **Cosa:** I nostri Blueprints (`auth.py`, `posts.py`).
    *   **Responsabilità:** Gestire le richieste HTTP, validare l'input, gestire le sessioni e orchestrare le operazioni. **È il "cervello" dell'applicazione.**

3.  **Livello di Accesso ai Dati (Data Access Layer):**
    *   **Cosa:** I nostri Repository (`user_repository.py`, `post_repository.py`).
    *   **Responsabilità:** Comunicare con il database. È l'**unico** strato che conosce il linguaggio SQL e la struttura delle tabelle.

Questa separazione è il segreto per costruire applicazioni complesse che rimangono facili da capire, modificare e far crescere nel tempo.

### Esercizio Finale del Capitolo
1.  Sostituisci il contenuto dei tuoi file `app/auth.py` e `app/posts.py` con il nuovo codice.
2.  Avvia l'applicazione (`python run.py`).
3.  Testa tutte le funzionalità: registrazione, login, creazione, modifica ed eliminazione dei post.

L'applicazione dovrebbe funzionare esattamente come prima, ma ora la sua struttura interna è infinitamente superiore.