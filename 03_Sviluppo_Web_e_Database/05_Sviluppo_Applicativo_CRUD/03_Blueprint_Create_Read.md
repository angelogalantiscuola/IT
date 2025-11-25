# Lezione 2: Visualizzare e Creare i Post

Ora che abbiamo il repository, dobbiamo aggiornare il nostro sito per usarlo.
Non creeremo nuovi file: modificheremo `app/main.py` per mostrare i post veri invece di quelli finti.

### 1. Aggiornare la Homepage (`app/main.py`)

Apri `app/main.py`. Dobbiamo:
1.  Importare il repository.
2.  Aggiornare la funzione `index` per leggere dal DB.
3.  Aggiungere la route `create` per scrivere nuovi post.

Sostituisci il contenuto con questo:

```python
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from app.repositories import post_repository

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # 1. Prendiamo i post veri dal database
    posts = post_repository.get_all_posts()
    
    # 2. Passiamo la variabile 'posts' al template
    return render_template('index.html', posts=posts)

@bp.route('/about')
def about():
    return render_template('about.html')

# --- NUOVA ROUTE: CREAZIONE POST ---
@bp.route('/create', methods=('GET', 'POST'))
def create():
    # Protezione: Se non sei loggato, vai al login
    if g.user is None:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Il titolo è obbligatorio.'

        if error is not None:
            flash(error)
        else:
            # Creiamo il post usando l'ID dell'utente loggato (g.user['id'])
            post_repository.create_post(title, body, g.user['id'])
            return redirect(url_for('main.index'))

    return render_template('blog/create.html')
```

### 2. Aggiornare il Template `index.html`

Apri `app/templates/index.html`. Ora i dati che arrivano (`posts`) sono oggetti reali del database, non stringhe. Dobbiamo accedere ai campi giusti (`title`, `body`, `username`).

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Blog della Classe</h1>
  
  <!-- Mostra il tasto 'Nuovo' solo se sei loggato -->
  {% if g.user %}
    <a href="{{ url_for('main.create') }}" class="btn">Scrivi un nuovo post</a>
    <hr>
  {% endif %}

  {% for post in posts %}
    <article>
      <header>
          <!-- Titolo del post -->
          <h2>{{ post['title'] }}</h2>
          <!-- Info autore e data -->
          <small>Scritto da <strong>{{ post['username'] }}</strong> il {{ post['created'].strftime('%Y-%m-%d') }}</small>
      </header>
      
      <!-- Corpo del post -->
      <p>{{ post['body'] }}</p>
      
      <!-- Tasto Modifica (visibile solo all'autore) -->
      {% if g.user and g.user['id'] == post['author_id'] %}
        <a href="{{ url_for('main.update', id=post['id']) }}">Modifica</a>
      {% endif %}
    </article>
    <hr>
  {% endfor %}
{% endblock %}
```

### 3. Creare il Template `blog/create.html`

Crea la cartella `app/templates/blog/` e dentro il file `create.html`.

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Nuovo Post</h1>
  <form method="post">
    <label for="title">Titolo</label>
    <input name="title" id="title" required>

    <label for="body">Testo del post</label>
    <textarea name="body" id="body" rows="5" required></textarea>

    <input type="submit" value="Pubblica">
  </form>
{% endblock %}
```