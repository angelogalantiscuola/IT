# Lezione 2: Form, POST e Autenticazione

Ora che abbiamo il database pronto, costruiamo le pagine per registrarci e fare login.
Useremo un nuovo Blueprint: `auth`.

### 1. Concetto Chiave: La "Doppia Vita" di una Route

Spesso in Flask una singola funzione gestisce due momenti diversi:
1.  **Metodo GET**: L'utente arriva sulla pagina. Il server deve solo **mostrare il form vuoto**.
2.  **Metodo POST**: L'utente ha compilato il form e premuto "Invia". Il server riceve i dati e deve **elaborarli**.

Nel codice useremo un `if request.method == 'POST':` per distinguere questi due momenti.

### 2. Concetto Chiave: La Sessione (La "Memoria" del Server)

Prima di scrivere il codice del Login, dobbiamo capire un problema fondamentale del Web: **Il server ha l'amnesia.**

Il protocollo HTTP è **Stateless** (senza stato). Ogni volta che chiedi una pagina, il server ti tratta come se fossi un perfetto sconosciuto, anche se hai inserito la password 10 secondi fa.

**Come facciamo a farci riconoscere?**
Usiamo una **Sessione**. Immaginala come il **braccialetto di un villaggio turistico**:
1.  All'ingresso (Login), mostri i documenti (Username/Password).
2.  Se i documenti sono validi, la reception (Server) ti mette un braccialetto (Cookie di Sessione).
3.  Da quel momento, per entrare in piscina o al bar, non mostri più i documenti: mostri solo il polso col braccialetto.

In Flask, la sessione si comporta come un dizionario che "sopravvive" tra una richiesta e l'altra. I dati vengono salvati in un **Cookie firmato** crittograficamente (ecco perché nel Modulo 3 abbiamo impostato la `SECRET_KEY`!).

### 3. Il Blueprint Auth (`app/auth.py`)

Crea il file `app/auth.py`.

```python
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# werkzeug.security ci offre strumenti professionali per la crittografia
from werkzeug.security import check_password_hash, generate_password_hash
from app.repositories import user_repository

# url_prefix='/auth' significa che tutte le route qui inizieranno con /auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    # CASO 2: POST (L'utente ha inviato i dati)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username obbligatorio.'
        elif not password:
            error = 'Password obbligatoria.'

        if error is None:
            # Hashiamo la password (MAI salvarla in chiaro!)
            hashed_pwd = generate_password_hash(password)
            
            # Chiamiamo il Repository
            success = user_repository.create_user(username, hashed_pwd)
            
            if success:
                return redirect(url_for('auth.login'))
            else:
                error = f"L'utente {username} è già registrato."

        flash(error)

    # CASO 1: GET (Mostriamo il form)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        
        # 1. Cerchiamo l'utente nel DB
        user = user_repository.get_user_by_username(username)

        if user is None:
            error = 'Username non corretto.'
        # 2. Verifichiamo la password
        elif not check_password_hash(user['password'], password):
            error = 'Password non corretta.'

        if error is None:
            # 3. GESTIONE SESSIONE (Mettiamo il "braccialetto")
            # Puliamo eventuali vecchie sessioni
            session.clear()
            # Salviamo l'ID dell'utente nel cookie di sessione
            session['user_id'] = user['id']
            
            # Ora il browser ricorderà chi siamo!
            return redirect(url_for('main.index'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    # Per uscire, "tagliamo il braccialetto"
    session.clear()
    return redirect(url_for('main.index'))
```

### 4. Il "Middleware": Riconoscere l'utente ovunque

C'è un ultimo problema da risolvere.
Flask gestisce il cookie di sessione, ma dentro al cookie c'è solo un numero (es. `user_id = 15`).
Nelle nostre pagine web, però, noi vogliamo scrivere "Ciao, **Mario**" o controllare "Sei **Admin**?". Non ci basta il numero 15, ci servono tutti i dati dell'utente.

Sarebbe noioso e ripetitivo dover scrivere il codice per cercare l'utente nel database in **ogni singola pagina** del sito.

**La Soluzione: `before_app_request`**
Flask ci permette di definire una funzione che viene eseguita **automaticamente prima** di qualsiasi altra cosa. È come i controlli di sicurezza in aeroporto: tutti devono passarci prima di andare al gate (alla Route).

Aggiungi questa funzione in `app/auth.py` (sotto le importazioni, prima delle route):

```python
@bp.before_app_request
def load_logged_in_user():
    """
    Questa funzione viene eseguita AUTOMATICAMENTE prima di ogni richiesta,
    indipendentemente dalla pagina che l'utente vuole visitare.
    """
    # 1. Controlliamo se nello "zaino" della sessione c'è un ID utente
    user_id = session.get('user_id')

    if user_id is None:
        # Nessun ID = Utente non loggato (Utente Anonimo)
        g.user = None
    else:
        # C'è un ID = Utente loggato.
        # Andiamo subito nel DB a prendere tutti i suoi dati (nome, email, ecc.)
        # e li mettiamo nell'oggetto globale 'g', accessibile ovunque.
        g.user = user_repository.get_user_by_id(user_id)
```

**Come funziona il flusso (Timeline):**
Immagina che un utente clicchi sul link "Home Page":

1.  **Click:** La richiesta arriva al server.
2.  **Intercettazione:** Flask vede il decoratore `@bp.before_app_request`. Ferma tutto e chiama `load_logged_in_user()`.
3.  **Caricamento:** La funzione controlla la sessione, trova l'ID, scarica i dati dal DB e riempie `g.user`.
4.  **Esecuzione:** Solo ora Flask chiama la funzione della route (`index()`).
5.  **Risultato:** Quando `index()` parte, trova `g.user` già pronto all'uso, senza dover fare nulla!


### 5. Aggiornare `base.html` per i Messaggi Flash

Quando usiamo `flash(error)`, Flask mette il messaggio in una coda speciale. Dobbiamo dire all'HTML di mostrarlo.

Apri `app/templates/base.html` e aggiungi questo blocco **sopra** `{% block content %}`:

```html
    <!-- Zona Messaggi Flash (Errori e Conferme) -->
    <header>
        <!-- get_flashed_messages() svuota la coda dei messaggi e li restituisce -->
        {% for message in get_flashed_messages() %}
            <div class="flash" style="background: #ffdddd; padding: 10px; margin-bottom: 10px; border: 1px solid red;">
                {{ message }}
            </div>
        {% endfor %}
    </header>
```

### 6. Registrazione e Template

Per finire il lavoro:

1.  **Registra il Blueprint**: Apri `app/__init__.py` e aggiungi `app.register_blueprint(auth.bp)`.
2.  **Crea i Template**: Crea la cartella `app/templates/auth/` e crea i file `login.html` e `register.html`.

Esempio minimo di `app/templates/auth/login.html`:
```html
{% extends 'base.html' %}

{% block content %}
  <h2>Log In</h2>
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    
    <input type="submit" value="Log In">
  </form>
{% endblock %}
```