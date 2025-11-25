# Lezione 2: Blueprint Blog e Protezione delle Route

Ora costruiamo le route per visualizzare e creare i post.
Useremo un nuovo Blueprint: `blog`.

In questa lezione impareremo anche a **proteggere una pagina**: faremo in modo che se un utente non è loggato, venga rispedito alla pagina di login.

### 1. Il Blueprint `app/blog.py`

Crea il file `app/blog.py`.

```python
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
# Importiamo solo il repository, niente decoratori complessi!
from app.repositories import post_repository

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    # Homepage: mostra tutti i post
    posts = post_repository.find_all()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    # --- PROTEZIONE DELLA ROUTE ---
    # Controlliamo manualmente se l'utente è loggato.
    # Se g.user è None, significa che non c'è una sessione attiva.
    if g.user is None:
        return redirect(url_for('auth.login'))
    # ------------------------------

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Il titolo è obbligatorio.'

        if error is not None:
            flash(error)
        else:
            # Creiamo il post collegandolo all'ID dell'utente corrente
            post_repository.create(title, body, g.user['id'])
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```

### 2. Registrazione

In `app/__init__.py`:
```python
from . import blog
app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index') # Rende la home del blog la home del sito
```

### 3. Template `blog/index.html`

Crea `app/templates/blog/index.html`. 
Nota come usiamo `post['username']` (grazie alla JOIN fatta nel repository).

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Blog</h1>
  
  <!-- Mostra il tasto 'Nuovo' solo se loggato -->
  {% if g.user %}
    <a href="{{ url_for('blog.create') }}">Scrivi un nuovo post</a>
  {% endif %}

  {% for post in posts %}
    <article>
      <header>
          <h2>{{ post['title'] }}</h2>
          <small>Scritto da {{ post['username'] }} il {{ post['created'].strftime('%Y-%m-%d') }}</small>
      </header>
      <p>{{ post['body'] }}</p>
      
      <!-- Se l'utente corrente è l'autore, mostra il tasto Modifica -->
      {% if g.user['id'] == post['author_id'] %}
        <a href="{{ url_for('blog.update', id=post['id']) }}">Modifica</a>
      {% endif %}
    </article>
    <hr>
  {% endfor %}
{% endblock %}
```