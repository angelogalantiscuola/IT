# Lezione 4: Gestione dei Form e Creazione di Dati

Un'applicazione web non è solo per la consultazione; deve essere interattiva. La forma più comune di interazione è l'invio di dati dall'utente al server, tipicamente tramite un **form HTML**.

In questa lezione, implementeremo la funzionalità per creare un nuovo post nel nostro blog. Impareremo a gestire le richieste `POST` in Flask, a leggere i dati inviati e a salvarli nel nostro database SQLite.

### 1. Il Metodo HTTP `POST`

Fino ad ora, il nostro browser ha sempre fatto richieste di tipo `GET`. Una richiesta `GET` serve per **richiedere** dati da un server.

Quando un utente deve **inviare** dati al server (come il titolo e il contenuto di un nuovo post), si usa una richiesta `POST`. I dati inviati in una richiesta `POST` non sono visibili nell'URL, ma viaggiano nel **corpo (body)** della richiesta.

### 2. Creare il Template con il Form HTML

Per prima cosa, creiamo la pagina che conterrà il form per inserire un nuovo post.

Crea un nuovo file `templates/create.html`:

```html
<!-- templates/create.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Crea un Nuovo Post</h1>

    <!--
        Il tag <form> definisce il form.
        - action="": Lasciandolo vuoto, il form verrà inviato allo stesso URL della pagina corrente.
        - method="post": Specifica che i dati devono essere inviati con una richiesta POST.
    -->
    <form method="post">
        <label for="title">Titolo</label>
        <br>
        <input type="text" name="title" placeholder="Titolo del post" required>
        <br><br>
        
        <label for="content">Contenuto</label>
        <br>
        <textarea name="content" placeholder="Contenuto del post" rows="5" cols="40" required></textarea>
        <br><br>

        <button type="submit">Crea Post</button>
    </form>
{% endblock %}
```
*   **Importante:** L'attributo `name` di ogni campo (`<input>`, `<textarea>`) è la **chiave** che useremo in Flask per accedere al valore inserito dall'utente.

### 3. Gestire Richieste `GET` e `POST` in un'Unica Route

Ora, dobbiamo creare la route in `app.py` che gestirà la pagina di creazione. Questa route dovrà fare due cose diverse:
1.  Se la richiesta è `GET`: deve semplicemente mostrare il form vuoto.
2.  Se la richiesta è `POST`: deve leggere i dati inviati, salvarli nel database e poi reindirizzare l'utente da qualche altra parte.

Per fare questo, dobbiamo importare nuovi oggetti da Flask: `request`, `redirect`, e `url_for`.

Modifica `app.py`:

```python
# app.py

# Aggiungiamo request, url_for e redirect alle nostre importazioni
from flask import Flask, render_template, request, url_for, redirect
import sqlite3

# ... (il resto del codice, inclusa get_db_connection, rimane uguale) ...
app = Flask(__name__)

def get_db_connection():
    # ...
    
# La route per la homepage rimane la stessa
@app.route('/')
def home():
    # ...

# NUOVA ROUTE per la creazione di un post
@app.route('/create', methods=('GET', 'POST'))
def create():
    # Se la richiesta è di tipo POST, significa che l'utente ha inviato il form
    if request.method == 'POST':
        # 1. Leggiamo i dati dal form usando l'oggetto 'request'
        title = request.form['title']
        content = request.form['content']

        # Semplice validazione: assicuriamoci che i campi non siano vuoti
        if not title or not content:
            # Qui potremmo mostrare un messaggio di errore, per ora è semplice
            return "Titolo e contenuto sono obbligatori!", 400

        # 2. Inseriamo i dati nel database
        conn = get_db_connection()
        # Usiamo i segnaposto '?' per prevenire SQL Injection!
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                     (title, content))
        conn.commit()
        conn.close()

        # 3. Reindirizziamo l'utente alla homepage per vedere il nuovo post
        return redirect(url_for('home'))

    # Se la richiesta è di tipo GET, mostriamo semplicemente il form
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
```

### 4. Il Pattern Post/Redirect/Get (PRG)

Nella nostra funzione, dopo aver salvato i dati con `POST`, non abbiamo restituito un template, ma abbiamo fatto un `redirect`.

```python
return redirect(url_for('home'))
```

Questo è un pattern molto importante chiamato **Post/Redirect/Get**. Perché si usa?
Immagina se avessimo restituito una pagina di successo. Se l'utente avesse poi ricaricato la pagina (premendo F5), il browser avrebbe inviato di nuovo la stessa richiesta `POST`, creando un post duplicato!

Con il redirect, il browser dell'utente viene "istruito" a fare una nuova richiesta `GET` alla homepage. Se ora l'utente ricarica la pagina, ricaricherà semplicemente la homepage, senza inviare di nuovo i dati.

### 5. Aggiornare la Navbar

Per accedere facilmente alla pagina di creazione, aggiungiamo un link nella nostra navbar in `templates/base.html`.

```html
<!-- templates/base.html (navbar aggiornata) -->
<nav>
    <a href="{{ url_for('home') }}">Home</a>
    <!-- Aggiungiamo il link alla pagina di creazione -->
    <a href="{{ url_for('create') }}">Nuovo Post</a>
    <a href="/about">About</a>
</nav>
```
*   Nota l'uso di `url_for('create')`. Usiamo il nome della funzione Python, non l'URL.

### 6. Testare il Flusso

1.  Avvia la tua applicazione (`python app.py`).
2.  Dalla homepage, clicca sul link "Nuovo Post".
3.  Verrai portato alla pagina `/create`, che mostra il form.
4.  Compila il form e clicca "Crea Post".
5.  Se tutto è andato a buon fine, verrai reindirizzato alla homepage, dove ora vedrai il tuo nuovo post in cima alla lista!

Abbiamo appena implementato la "C" (Create) e la "R" (Read) del nostro sistema **CRUD** (Create, Read, Update, Delete).