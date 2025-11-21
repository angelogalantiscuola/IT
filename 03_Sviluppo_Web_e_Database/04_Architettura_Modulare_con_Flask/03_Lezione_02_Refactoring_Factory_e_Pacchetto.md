# Lezione 2: Refactoring con Application Factory e Struttura a Pacchetto

Nella lezione precedente abbiamo capito *perché* dobbiamo ristrutturare la nostra applicazione. In questa lezione, passiamo alla pratica e iniziamo il refactoring da `flask_1` a `flask_2`.

Introdurremo due cambiamenti strutturali fondamentali:
1.  Trasformeremo la nostra applicazione in un **pacchetto Python**.
2.  Implementeremo il pattern **Application Factory**.

### 1. Il Pattern Application Factory

Fino ad ora, abbiamo creato l'oggetto `app` a livello globale, all'inizio del nostro file `app.py`:

```python
app = Flask(__name__)

@app.route('/')
def home():
    ...
```

Questo approccio semplice ha un problema: l'applicazione viene creata e configurata non appena il file viene importato. Questo rende difficile, ad esempio, usare configurazioni diverse per lo sviluppo e per la produzione.

La soluzione è il pattern **Application Factory**. Invece di creare `app` globalmente, la creiamo all'interno di una funzione, che possiamo chiamare `create_app()`.

**I vantaggi sono enormi:**
*   **Configurazione Dinamica:** Possiamo passare dei parametri alla funzione `create_app()` per configurare l'applicazione in modi diversi.
*   **Testabilità:** È molto più facile testare un'applicazione se possiamo creare istanze multiple con configurazioni specifiche per i test.
*   **Prevenzione di Import Circolari:** In progetti complessi, questo pattern aiuta a evitare un tipo di errore molto comune in cui due file cercano di importarsi a vicenda.

### 2. Da File a Pacchetto Python

Per organizzare il nostro codice in più file, non possiamo più avere un singolo `app.py`. Dobbiamo trasformare la nostra applicazione in un **pacchetto Python**.

Un pacchetto è semplicemente una cartella che contiene un file speciale chiamato `__init__.py`. La presenza di questo file dice a Python che la cartella non è una semplice cartella, ma un modulo che può essere importato.

---

### Mettiamoci al Lavoro: Il Refactoring Passo Passo

**1. Creare la Nuova Struttura del Progetto `flask_2`**

Inizia creando una nuova cartella `flask_2`. Al suo interno, crea la seguente struttura di file e cartelle (per ora, la maggior parte saranno vuoti):

```
flask_2/
├── .venv/
├── instance/                 # Cartella per il DB e file di config. non tracciati
│   └── database.db           # (verrà creato qui)
├── app/                      # Il nostro pacchetto applicativo
│   ├── __init__.py           # Il cuore della factory
│   ├── db.py                 # Logica per la gestione del DB
│   ├── schema.sql
│   └── templates/
│       └── base.html
└── run.py                    # Lo script per avviare l'applicazione
```
*   **Sposta** i file `schema.sql` e `templates/base.html` dal vecchio progetto `flask_1` nelle posizioni correnti.

**2. Creare l'Application Factory (`app/__init__.py`)**

Questo file è ora il punto di ingresso della nostra applicazione. È qui che definiamo la funzione `create_app()`.

```python
# app/__init__.py
import os
from flask import Flask

def create_app():
    # 1. Creiamo e configuriamo l'istanza dell'app
    #    instance_relative_config=True dice a Flask che i file di configurazione
    #    sono relativi alla cartella 'instance'.
    app = Flask(__name__, instance_relative_config=True)

    # 2. Impostiamo una configurazione di default
    app.config.from_mapping(
        SECRET_KEY='dev', # Cambia questa chiave in produzione!
        # Impostiamo il percorso del nostro database SQLite
        DATABASE=os.path.join(app.instance_path, 'database.db'),
    )

    # 3. Assicuriamoci che la cartella 'instance' esista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 4. Registriamo le funzioni del database con l'app
    from . import db
    db.init_app(app)

    # Nelle prossime lezioni, registreremo qui i nostri Blueprints

    return app
```

**3. Centralizzare la Gestione del Database (`app/db.py`)**

Ora estraiamo tutta la logica di gestione del database dal vecchio `app.py` e la mettiamo in un file dedicato. Questo è un perfetto esempio di Separazione delle Responsabilità.

```python
# app/db.py
import sqlite3
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        # current_app è un oggetto speciale di Flask che punta all'applicazione
        # che sta gestendo la richiesta corrente.
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not in None:
        db.close()

# Funzioni per inizializzare il database da linea di comando
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# Creiamo un comando personalizzato per il terminale
@click.command('init-db')
def init_db_command():
    """Pulisce i dati esistenti e crea nuove tabelle."""
    init_db()
    click.echo('Database inizializzato.')

# Funzione per registrare le nostre funzioni con l'app Flask
def init_app(app):
    # dice a Flask di chiamare close_db dopo aver restituito la risposta
    app.teardown_appcontext(close_db)
    # aggiunge il nostro nuovo comando al terminale di Flask
    app.cli.add_command(init_db_command)
```

**4. Creare lo Script di Avvio (`run.py`)**

Poiché l'applicazione ora viene creata da una funzione, abbiamo bisogno di un punto di ingresso per avviarla. Questo è il ruolo di `run.py`, che si trova al di fuori del nostro pacchetto `app`.

```python
# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

*   **Importante:** `from app import create_app` funziona perché `app/` è un pacchetto (grazie a `__init__.py`) e `create_app` è definita al suo interno.

**5. Inizializzare e Avviare la Nuova Applicazione**

Ora che la struttura è pronta, proviamo a usarla.

**1. Inizializzare il Database**
Apri il terminale nella cartella `flask_2` (con l'ambiente virtuale attivo). Grazie al nostro nuovo comando, possiamo inizializzare il database in modo pulito:
```bash
# Dobbiamo dire a Flask dove trovare la nostra applicazione
export FLASK_APP=run.py  # Su Windows CMD usa 'set' invece di 'export'

# Ora eseguiamo il nostro comando personalizzato
flask init-db
```
Se controlli, vedrai che è stato creato il file `instance/database.db`.

**2. Avviare l'Applicazione**
Ora, avvia l'applicazione con il nuovo script:
```bash
python run.py
```
L'applicazione si avvierà come prima. Tuttavia, se provi a visitare `http://127.0.0.1:5000`, otterrai un errore 404 Not Found. **Questo è normale!** Perché? Perché non abbiamo ancora definito nessuna route. Il nostro `create_app()` crea un'app vuota.

Nella prossima lezione, risolveremo questo problema spostando le nostre vecchie route all'interno dei **Blueprints** e registrandole sulla nostra nuova applicazione. Per ora, abbiamo gettato le fondamenta della nostra architettura professionale.