# Lezione 2: Routing Modulare con i Blueprints

Nel file `__init__.py` abbiamo scritto una route (`/hello`). Se scrivessimo tutte le route del nostro blog lì dentro, il file diventerebbe presto ingestibile.

Flask risolve questo problema con i **Blueprints**.
Un Blueprint è come una "mini-applicazione" che contiene un gruppo di route correlate (es. tutte le pagine pubbliche, tutte le pagine di admin, etc.).

### 1. Creare il Blueprint per le Pagine Statiche

Creiamo un nuovo file `app/main.py`. Questo modulo gestirà le pagine principali del sito (Home, About).

```python
from flask import Blueprint

# 1. Creiamo l'oggetto Blueprint
# 'main' è il nome del blueprint
# __name__ aiuta Flask a trovare le risorse
bp = Blueprint('main', __name__)

# 2. Definiamo le route usando @bp invece di @app
@bp.route('/')
def index():
    return "Questa è la Homepage del Blog (dal Blueprint)"

@bp.route('/about')
def about():
    return "Pagina Chi Siamo (dal Blueprint)"
```

### 2. Registrare il Blueprint nella Factory

Creare il file non basta. Dobbiamo dire alla nostra "Fabbrica" di usare questo nuovo componente.

Torna in `app/__init__.py` e aggiungi queste righe **prima** del `return app`:

```python
# app/__init__.py

def create_app(test_config=None):
    # ... (codice precedente: setup app, config, os.makedirs) ...

    # --- REGISTRAZIONE BLUEPRINTS ---
    from . import main
    app.register_blueprint(main.bp)
    # --------------------------------

    return app
```

### 3. Verificare il Funzionamento

Riavvia il server (`python run.py`).
*   Vai su `http://127.0.0.1:5000/`. Dovresti vedere il messaggio della Homepage.
*   Vai su `http://127.0.0.1:5000/about`. Dovresti vedere il messaggio About.

### Perché lo facciamo?
Immagina di lavorare in team.
*   Tu lavori su `main.py` (Pagine pubbliche).
*   Il tuo compagno lavora su `auth.py` (Login/Registrazione).
*   Un altro lavora su `posts.py` (Articoli del blog).

Ognuno lavora sul suo file. I conflitti sono ridotti al minimo. Questa è **architettura modulare**.