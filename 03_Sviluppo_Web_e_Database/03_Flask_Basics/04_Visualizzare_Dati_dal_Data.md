# Lezione 3: Visualizzare Dati dal Database

Finora, i dati che abbiamo mostrato nei nostri template erano "fissi", scritti direttamente nel codice Python. Un'applicazione web diventa davvero utile quando può interagire con una fonte di dati persistente, come un database.

In questa lezione, collegheremo la nostra applicazione Flask a un database **SQLite** per leggere delle informazioni e visualizzarle in una pagina web.

### 1. Preparazione del Database SQLite

A differenza di database come MariaDB, SQLite non richiede un server. L'intero database è contenuto in un singolo file. Useremo la libreria `sqlite3`, che è già inclusa in Python.

**1. Creare uno script per inizializzare il database**
Per mantenere il nostro `app.py` pulito, creiamo uno script separato che useremo solo una volta per creare il database e la sua struttura (lo "schema").

Crea un nuovo file chiamato `init_db.py`:
```python
# init_db.py
import sqlite3

# Stabiliamo una connessione al file del database.
# Se il file non esiste, verrà creato.
connection = sqlite3.connect('database.db')

# Leggiamo il contenuto del file schema.sql per creare le tabelle
with open('schema.sql') as f:
    connection.executescript(f.read())

# Chiudiamo la connessione
connection.close()
```

**2. Definire lo schema del database**
Crea un file chiamato `schema.sql`. Questo file conterrà i comandi SQL per creare le tabelle. Per ora, creiamo una semplice tabella per dei post di un blog.

```sql
-- schema.sql
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
```

**3. Eseguire lo script**
Ora, dal tuo terminale (con l'ambiente virtuale attivo), esegui lo script:
```bash
python init_db.py
```
Nella cartella del tuo progetto ora apparirà un nuovo file: `database.db`. Questo è il tuo database!

### 2. Il Pattern per la Gestione della Connessione in Flask

Come ci connettiamo al database da dentro la nostra applicazione? Potremmo aprire e chiudere una connessione in ogni funzione, ma è inefficiente e soggetto a errori.

Il pattern raccomandato in Flask è usare delle funzioni per gestire la connessione **per ogni richiesta**.

Modifichiamo il nostro `app.py`:

```python
# app.py
from flask import Flask, render_template
import sqlite3  # Importiamo la libreria sqlite3

app = Flask(__name__)

# Funzione per ottenere la connessione al database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    # Questa riga è importante: permette di accedere alle colonne per nome
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    # 1. Stabiliamo la connessione al database
    conn = get_db_connection()

    # 2. Eseguiamo la query SELECT
    #    Oriniamo i post dal più recente al più vecchio
    posts = conn.execute('SELECT * FROM posts ORDER BY created DESC').fetchall()

    # 3. Chiudiamo la connessione
    conn.close()
    
    # 4. Passiamo i dati al template
    return render_template('home.html', posts=posts)

# ... (il resto del file, come la route /about, rimane uguale)
# ...
if __name__ == '__main__':
    app.run(debug=True)
```

### 3. Visualizzare i Dati nel Template

Ora che la nostra funzione `home()` passa una lista di `posts` al template, dobbiamo modificare `home.html` per visualizzarli. Useremo un ciclo `for` di Jinja2.

Modifica `templates/home.html`:

```html
<!-- templates/home.html -->
{% extends "base.html" %}

{% block content %}
    <h1>Benvenuto nel Mio Blog!</h1>
    <hr>

    <!-- Inizia il ciclo per iterare su ogni 'post' nella lista 'posts' -->
    {% for post in posts %}
        <article>
            <h2>{{ post['title'] }}</h2>
            <p><small>Pubblicato il: {{ post['created'] }}</small></p>
            <p>{{ post['content'] }}</p>
        </article>
        <hr>
    {% endfor %}
    <!-- Fine del ciclo -->

{% endblock %}
```
*   `post['title']`: Poiché abbiamo usato `conn.row_factory = sqlite3.Row`, possiamo accedere ai dati di ogni post come se fossero un dizionario, usando il nome della colonna.

### 4. Aggiungere dei Dati di Prova

La nostra pagina ora è pronta a visualizzare i post, ma il database è vuoto!

Per aggiungere dei dati, possiamo usare un client SQLite per VS Code (come l'estensione "SQLite") oppure aggiungere temporaneamente qualche riga di codice al nostro `init_db.py`.

Modifica `init_db.py` e rieseguilo:

```python
# init_db.py (versione aggiornata)
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

# Creiamo un "cursore" per eseguire i comandi
cur = connection.cursor()

# Inseriamo due post di esempio
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Primo Post', 'Contenuto del primo post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Secondo Post', 'Contenuto del secondo post')
            )

# Applichiamo le modifiche
connection.commit()
connection.close()
```
Riesegui lo script dal terminale: `python init_db.py`. Questo cancellerà il vecchio database e ne creerà uno nuovo con i due post.

### 5. Lanciare l'Applicazione

Ora avvia di nuovo la tua applicazione Flask:
```bash
python app.py
```
Visita la homepage `http://127.0.0.1:5000`. Ora dovresti vedere i due post che abbiamo inserito nel database, visualizzati dinamicamente!

Abbiamo compiuto un passo fondamentale: la nostra interfaccia web ora non è più statica, ma è un riflesso dei dati contenuti nel nostro database.