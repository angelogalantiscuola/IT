# Lezione 3: Il Motore di Template Jinja2

Restituire stringhe come `"Questa è la Homepage"` va bene per i test, ma un sito vero usa l'HTML.
Flask usa **Jinja2**, un motore potente che ci permette di:
1.  Separare la logica (Python) dalla presentazione (HTML).
2.  Costruire layout riutilizzabili (per non copiare-incollare la navbar su ogni pagina!).

### 1. Creare la Struttura dei Template

Nella cartella `app/`, crea una cartella `templates`.

```text
app/
├── templates/
│   ├── base.html    <-- Il layout maestro
│   ├── index.html   <-- La home specifica
│   └── about.html   <-- La about specifica
```

### 2. Il Layout Base (`base.html`)

Questo file contiene lo scheletro comune a TUTTE le pagine: `<html>`, `<head>`, la Navbar e il Footer. Usa i **blocchi** (`{% block %}`) per definire le zone che le pagine figlie potranno riempire.

```html
<!-- app/templates/base.html -->
<!doctype html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Blog Scolastico{% endblock %}</title>
    <!-- Qui potremmo linkare un CSS -->
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        nav a { margin-right: 10px; text-decoration: none; color: blue; }
        hr { border: 0; border-top: 1px solid #ccc; }
    </style>
</head>
<body>
    <nav>
        <h1>Blog 5^A</h1>
        <!-- url_for genera l'URL dal nome della funzione -->
        <!-- Sintassi Blueprint: 'nome_blueprint.nome_funzione' -->
        <a href="{{ url_for('main.index') }}">Home</a>
        <a href="{{ url_for('main.about') }}">Chi Siamo</a>
    </nav>
    <hr>

    <!-- Qui mostreremo i messaggi flash (errori/conferme) in futuro -->
    <main>
        {% block content %}{% endblock %}
    </main>

    <hr>
    <footer>
        <small>&copy; 2024 - Classe 5^A Informatica</small>
    </footer>
</body>
</html>
```

### 3. Le Pagine Figlie (`index.html`)

Le pagine specifiche non devono riscrivere l'HTML di base. Devono solo "estendere" `base.html` e riempire i blocchi.

```html
<!-- app/templates/index.html -->
{% extends 'base.html' %}

{% block title %}Home - Blog{% endblock %}

{% block content %}
    <h2>Benvenuti!</h2>
    <p>Questo è il blog ufficiale del nostro corso di informatica.</p>
    
    <!-- Esempio di logica nel template -->
    <h3>Ultimi aggiornamenti:</h3>
    <ul>
    {% for news in notizie %}
        <li>{{ news }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```

E anche `about.html`:

```html
<!-- app/templates/about.html -->
{% extends 'base.html' %}

{% block content %}
    <h2>Chi Siamo</h2>
    <p>Siamo gli studenti della 5^A e stiamo imparando Flask!</p>
{% endblock %}
```

### 4. Collegare i Template alle Route

Torniamo in `app/main.py` e aggiorniamo le funzioni per usare `render_template`.

```python
# app/main.py
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Simuliamo dei dati presi da un database (per ora finti)
    notizie_fittizie = [
        "Abbiamo imparato i Blueprint",
        "Configurato Jinja2",
        "Il progetto sta prendendo forma"
    ]
    # Passiamo la variabile 'notizie' al template
    return render_template('index.html', notizie=notizie_fittizie)

@bp.route('/about')
def about():
    return render_template('about.html')
```

### Conclusione Modulo 3
Ora abbiamo un sito multipagina, con un layout coerente e codice organizzato.
Manca solo una cosa: **i dati veri**.
Nel prossimo modulo, collegheremo il database e creeremo il nostro primo **Repository**.