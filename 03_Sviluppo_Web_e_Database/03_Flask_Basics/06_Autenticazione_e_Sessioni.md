# Lezione 5: Autenticazione e Gestione delle Sessioni

La nostra applicazione sta prendendo forma, ma al momento è un sistema "aperto": chiunque può visitare qualsiasi pagina e, in futuro, potrebbe eseguire qualsiasi azione. Per creare un'area riservata, abbiamo bisogno di un sistema di **autenticazione**.

L'autenticazione è il processo che permette a un utente di dimostrare la propria identità, tipicamente tramite username e password.

In questa lezione implementeremo il flusso completo:
1.  **Registrazione** di un nuovo utente.
2.  **Login** di un utente esistente.
3.  Uso delle **sessioni** per mantenere l'utente "loggato".

### 1. Sicurezza delle Password: Mai Salvarle in Chiaro!

Questo è il concetto di sicurezza più importante di questa lezione. Sarebbe un errore gravissimo salvare le password degli utenti così come sono nel database. Se il database venisse compromesso (un "data breach"), tutte le password sarebbero immediatamente visibili.

**La soluzione è l'Hashing.**
Un **hash** è il risultato di una funzione matematica che trasforma una stringa di testo (la password) in una stringa di lunghezza fissa, in modo **non reversibile**.

*   `"password123"`  ->  `(hash function)`  ->  `"pbkdf2:sha256:..."`
*   È impossibile risalire da `"pbkdf2:..."` a `"password123"`.

Flask, tramite la libreria **Werkzeug** (installata automaticamente), ci fornisce gli strumenti perfetti per questo:
*   `generate_password_hash(password)`: Crea un hash sicuro di una password.
*   `check_password_hash(hash, password)`: Confronta una password fornita dall'utente con un hash salvato nel database.

### 2. Preparare il Database per gli Utenti

Dobbiamo aggiungere una tabella `users` al nostro database. Aggiorniamo il nostro file `schema.sql`:

```sql
-- schema.sql (aggiungere alla fine del file)

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
```
*   `UNIQUE`: Questo vincolo assicura che non possano esistere due utenti con lo stesso username.

Dopo aver modificato `schema.sql`, **riesegui lo script `init_db.py`** per ricreare il database con la nuova tabella.

### 3. Implementare la Registrazione Utente

**1. Creare il Template di Registrazione (`register.html`)**
Crea un nuovo file `templates/register.html`:
```html
<!-- templates/register.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Registrati</h1>
    <form method="post">
        <label for="username">Username</label>
        <input name="username" id="username" required>
        <br><br>
        <label for="password">Password</label>
        <input type="password" name="password" id="password" required>
        <br><br>
        <input type="submit" value="Registrati">
    </form>
{% endblock %}
```

**2. Creare la Route per la Registrazione in `app.py`**
Aggiungiamo la logica per gestire la registrazione.

```python
# app.py (aggiungere queste importazioni e la nuova route)

# ... altre importazioni ...
# Aggiungiamo 'session' e le funzioni di hashing
from flask import Flask, render_template, request, url_for, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

# ... app, get_db_connection, etc. ...

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        error = None

        if not username or not password:
            error = 'Username e password sono obbligatori.'
        
        # Controlliamo se l'username esiste già
        elif conn.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone() is not None:
            error = f"L'utente {username} è già registrato."

        if error is None:
            # Hashamo la password prima di salvarla!
            password_hash = generate_password_hash(password)
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                         (username, password_hash))
            conn.commit()
            conn.close()
            # Reindirizziamo l'utente alla pagina di login dopo la registrazione
            return redirect(url_for('login'))
        
        conn.close()
        # Se c'è un errore, lo mostreremo (in un modo più elegante in futuro)
        return error, 400

    return render_template('register.html')
```

### 4. Il Concetto di Sessione

HTTP è un protocollo "stateless" (senza stato): ogni richiesta è indipendente dalle altre. Come fa il server a "ricordarsi" che l'utente ha appena fatto il login?

La soluzione è la **sessione**. Quando un utente fa il login con successo:
1.  Il server crea un identificativo di sessione unico.
2.  Salva questo identificativo in un **cookie** nel browser dell'utente.
3.  Per ogni richiesta successiva, il browser invia automaticamente il cookie.
4.  Il server legge il cookie e sa chi è l'utente.

Flask gestisce tutto questo in modo quasi trasparente tramite l'oggetto `session`. Per usarlo, dobbiamo impostare una **chiave segreta (`SECRET_KEY`)** per firmare crittograficamente i cookie di sessione.

Aggiungi questa riga subito dopo la creazione dell'app in `app.py`:
```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'la-tua-chiave-segreta-super-casuale' # Cambia questa chiave!
```
**Nota:** In un'applicazione reale, questa chiave non dovrebbe mai essere scritta nel codice, ma caricata da una variabile d'ambiente.

### 5. Implementare Login e Logout

**1. Creare il Template di Login (`login.html`)**
```html
<!-- templates/login.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Login</h1>
    <form method="post">
        <label for="username">Username</label>
        <input name="username" id="username" required>
        <br><br>
        <label for="password">Password</label>
        <input type="password" name="password" id="password" required>
        <br><br>
        <input type="submit" value="Login">
    </form>
{% endblock %}
```

**2. Creare le Route per Login e Logout in `app.py`**
```python
# app.py

# ... (tutto il codice precedente) ...

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user is None or not check_password_hash(user['password'], password):
            return 'Username o password non corretti', 401

        # Il login ha successo! Salviamo l'ID dell'utente nella sessione.
        session.clear()
        session['user_id'] = user['id']
        
        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    # Per fare il logout, basta pulire la sessione.
    session.clear()
    return redirect(url_for('home'))
```

### 6. Aggiornare la Navbar
Infine, aggiorniamo `base.html` per mostrare i link corretti a seconda che l'utente sia loggato o meno. Possiamo controllare se `session['user_id']` esiste.

```html
<!-- templates/base.html (navbar aggiornata) -->
<nav>
    <a href="{{ url_for('home') }}">Home</a>
    <a href="{{ url_for('create') }}">Nuovo Post</a>
    
    <!-- Logica condizionale con Jinja2 -->
    {% if not session.user_id %}
        <a href="{{ url_for('register') }}">Registrati</a>
        <a href="{{ url_for('login') }}">Login</a>
    {% else %}
        <a href="{{ url_for('logout') }}">Logout</a>
    {% endif %}
</nav>
```

Ora hai un sistema di autenticazione funzionante! Prova a registrare un nuovo utente, fare il login e il logout. Nella prossima lezione, useremo questo sistema per proteggere le pagine.