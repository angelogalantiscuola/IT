# Lezione 3: Organizzare le Route con i Blueprints

Nella lezione precedente abbiamo creato un'architettura a pacchetto con una Application Factory, ma la nostra applicazione è ancora "vuota": non ha route.

Ora risolveremo questo problema spostando la logica delle route dal nostro vecchio `app.py` di `flask_1` in moduli separati, utilizzando i **Blueprints**.

### 1. Cos'è un Blueprint?

Un **Blueprint** è un oggetto di Flask che ti permette di registrare un insieme di route, template, file statici e altre operazioni in modo modulare.

Pensa a un Blueprint come a una "mini-applicazione" o a un "componente" che può essere collegato all'applicazione principale. Questo è il meccanismo perfetto per implementare la **Separazione delle Responsabilità**.

Noi creeremo due Blueprints:
1.  **`auth_bp`**: Per tutte le route relative all'autenticazione (`/register`, `/login`, `/logout`).
2.  **`posts_bp`**: Per tutte le route relative ai post (`/`, `/create`, `/edit`, `/delete`).

### 2. Creare il Blueprint per l'Autenticazione

Iniziamo con le route di autenticazione. Apriremo il file `app/auth.py` (che avevamo creato vuoto) e lo popoleremo.

**1. Definire il Blueprint**
All'inizio del file, creiamo un'istanza di `Blueprint`.

```python
# app/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db
from functools import wraps

# Creiamo il Blueprint 'auth'
# Il secondo argomento, __name__, dice al Blueprint dove è definito.
# url_prefix aggiunge '/auth' davanti a tutte le route di questo blueprint.
bp = Blueprint('auth', __name__, url_prefix='/auth')
```

**2. Spostare le Funzioni delle Route**
Ora, copia le funzioni `register`, `login`, e `logout` dal tuo vecchio `app.py` di `flask_1` e incollale in `app/auth.py`.

*   **Importante:** La sintassi delle route cambia leggermente. Invece di `@app.route(...)`, useremo `@bp.route(...)`.

```python
# app/auth.py (continuazione)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    # ... (incolla qui la logica della funzione 'register' da flask_1) ...
    # Assicurati che il template restituito sia 'auth/register.html'
    if request.method == 'POST':
        # ... logica ...
        if error is None:
            # ... logica db ...
            return redirect(url_for('auth.login')) # Nota: 'auth.login'
        # ...
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    # ... (incolla qui la logica della funzione 'login' da flask_1) ...
    if request.method == 'POST':
        # ... logica ...
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            # Reindirizziamo alla homepage, che è nel blueprint 'posts'
            return redirect(url_for('posts.home'))
        # ...
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    # ... (incolla qui la logica della funzione 'logout' da flask_1) ...
    session.clear()
    return redirect(url_for('posts.home'))
```

**3. La Nuova Sintassi di `url_for()`**
Hai notato `url_for('auth.login')`? Poiché le nostre route ora sono organizzate in Blueprints, dobbiamo specificare a Flask dove trovare la funzione. La sintassi è `url_for('nome_blueprint.nome_funzione')`.

**4. Spostare il Decoratore `@login_required`**
Il nostro decoratore `@login_required` è una funzionalità legata all'autenticazione, quindi `app/auth.py` è il posto perfetto per lui. Copialo dal vecchio `app.py`.

```python
# app/auth.py (aggiungere il decoratore)

# ... (blueprint e route) ...

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
```
Ora potremo importarlo da `app.auth` in altri file.

### 3. Creare il Blueprint per i Post

Ripetiamo lo stesso processo per le route relative ai post nel file `app/posts.py`.

```python
# app/posts.py
from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from app.db import get_db
from app.auth import login_required # Importiamo il nostro decoratore!

# Questa volta non usiamo un url_prefix, perché vogliamo che la homepage
# risponda a '/', non a '/posts/'.
bp = Blueprint('posts', __name__)

@bp.route('/')
def home():
    # ... (Copia la logica della funzione 'home' da flask_1) ...
    # ... Assicurati che il template sia 'posts/home.html' ...
    pass # Da implementare

# ... (Copia qui le altre funzioni: 'create', 'edit', 'delete' da flask_1) ...
# ... (Ricorda di usare @bp.route e di aggiornare i nomi dei template e gli url_for) ...
# ... (Aggiungi @login_required dove serve) ...

# Esempio per la route 'create'
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    # ... (logica di create) ...
    # Alla fine, reindirizza a 'posts.home'
    return redirect(url_for('posts.home'))
```

### 4. Registrare i Blueprints nell'Application Factory

Abbiamo creato i Blueprints, ma la nostra applicazione non sa ancora che esistono. Dobbiamo "registrarli" all'interno della nostra funzione `create_app()` in `app/__init__.py`.

```python
# app/__init__.py (versione aggiornata)

# ... (import e configurazione) ...
def create_app():
    app = Flask(...)
    # ... (configurazione) ...

    # ... (inizializzazione db) ...

    # === REGISTRAZIONE DEI BLUEPRINTS ===
    from . import auth
    app.register_blueprint(auth.bp)

    from . import posts
    app.register_blueprint(posts.bp)

    # Poiché la nostra homepage (definita nel blueprint 'posts') deve
    # essere accessibile da '/', aggiungiamo una regola.
    # 'posts.home' è l'endpoint (nome_blueprint.nome_funzione)
    app.add_url_rule('/', endpoint='posts.home')
    # === FINE REGISTRAZIONE ===

    return app
```

### 5. Esercizio: Completare il Refactoring
1.  **Sposta i template** nelle sottocartelle corrette:
    *   `login.html` e `register.html` vanno in `app/templates/auth/`.
    *   `home.html`, `create.html`, `edit.html` vanno in `app/templates/posts/`.
2.  **Completa il codice** in `app/auth.py` e `app/posts.py` copiando la logica dal vecchio `app.py` di `flask_1`.
3.  **Adatta tutto il codice** alle nuove convenzioni:
    *   Usa `@bp.route` invece di `@app.route`.
    *   Aggiorna i percorsi dei template in `render_template` (es. `'auth/login.html'`).
    *   Aggiorna **tutte** le chiamate a `url_for` con la sintassi `nome_blueprint.nome_funzione`.
4.  Avvia l'applicazione con `python run.py`.

Se tutto è stato collegato correttamente, l'applicazione funzionerà di nuovo, ma questa volta il suo codice sarà pulito, organizzato per funzionalità e pronto a crescere senza diventare un caos.````