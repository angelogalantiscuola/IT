# Lezione 2: Integrazione di Peewee nell'Applicazione Flask

Nella lezione precedente, abbiamo definito i nostri modelli `User` e `Post` nel file `app/models.py`. Tuttavia, la nostra applicazione Flask non sa ancora nulla di loro né di come usare Peewee per gestire la connessione al database.

In questa lezione, modificheremo la nostra **Application Factory** per:
1.  Inizializzare la connessione al database per Peewee.
2.  Gestire automaticamente l'apertura e la chiusura della connessione ad ogni richiesta.
3.  Creare le tabelle del database a partire dai nostri modelli.

### 1. Il Ciclo di Vita della Connessione in un'App Web

Un'applicazione web gestisce più richieste contemporaneamente. È fondamentale che ogni richiesta abbia una connessione al database pulita e che questa venga chiusa correttamente al termine della richiesta per non sprecare risorse.

Peewee, come la maggior parte degli ORM, fornisce degli "agganci" (hooks) per gestire questo ciclo:
*   **Prima di una richiesta (`before_request`):** Apriremo la connessione al database.
*   **Dopo una richiesta (`after_request`):** Chiuderemo la connessione al database.

Flask ci permette di registrare funzioni che vengono eseguite automaticamente in questi momenti, garantendo una gestione della connessione robusta e automatica.

### 2. Aggiornare l'Application Factory (`app/__init__.py`)

Questo è il momento di mettere mano al cuore della nostra applicazione e sostituire il vecchio sistema di gestione del database con quello nuovo basato su Peewee.

**1. Rimuovere il Vecchio Sistema**
Per prima cosa, eliminiamo il vecchio codice di gestione del database.
*   **Elimina il file `app/db.py`**. Non ci serve più!
*   In `app/__init__.py`, **rimuovi** l'importazione `from . import db` e la chiamata `db.init_app(app)`.

**2. Integrare Peewee**
Ora, modifichiamo `app/__init__.py` per integrare Peewee.

```python
# app/__init__.py (versione aggiornata con Peewee)
import os
from flask import Flask
# Importiamo il nostro oggetto 'db' dal file dei modelli
from app.models import db as database # Usiamo un alias per chiarezza

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database.db'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # === INTEGRAZIONE DI PEEWEE ===

    # 1. Inizializziamo il nostro "proxy" del database con il percorso
    #    specifico di questa istanza dell'app.
    database.init(app.config['DATABASE'])

    # 2. Definiamo le funzioni "hook" per gestire la connessione
    @app.before_request
    def before_request():
        """Apre la connessione al DB prima di ogni richiesta."""
        database.connect()

    @app.after_request
    def after_request(response):
        """Chiude la connessione al DB dopo ogni richiesta."""
        database.close()
        return response

    # 3. Creiamo le tabelle a partire dai modelli, se non esistono già.
    #    Questo è un modo semplice per inizializzare il DB.
    from app.models import User, Post
    with app.app_context():
        database.create_tables([User, Post], safe=True)

    # === FINE INTEGRAZIONE ===

    # Registriamo i Blueprints (questo rimane uguale)
    from . import auth
    app.register_blueprint(auth.bp)

    from . import posts
    app.register_blueprint(posts.bp)

    app.add_url_rule('/', endpoint='posts.home')

    return app
```

**Analizziamo le modifiche:**

1.  **`database.init(...)`**: Abbiamo "attivato" il `db` proxy che avevamo definito in `app/models.py`, dicendogli quale file di database usare.
2.  **`@app.before_request` e `@app.after_request`**: Questi sono decoratori di Flask. Le funzioni decorate con essi verranno eseguite automaticamente prima e dopo ogni singola richiesta che l'applicazione riceve. Questo automatizza completamente la gestione della connessione.
3.  **`database.create_tables(...)`**: Questa potente funzione di Peewee ispeziona le nostre classi `User` e `Post`, le traduce in comandi `CREATE TABLE IF NOT EXISTS`, e le esegue. Abbiamo eliminato la necessità di avere un file `schema.sql` e un comando `flask init-db`.

### 3. Cosa Abbiamo Ottenuto?

*   **Codice più Pulito:** Abbiamo rimosso un intero file (`db.py`) e la necessità di un comando separato per inizializzare il database.
*   **Gestione Automatica:** Non dovremo mai più scrivere `get_db()` o `db.close()` nelle nostre funzioni delle route. Il sistema di "hook" di Flask e Peewee si occupa di tutto.
*   **Single Source of Truth:** La definizione della struttura del nostro database ora vive in un unico posto: il file `app/models.py`. Se vogliamo aggiungere una colonna, la aggiungiamo al modello, non a un file `.sql`.

### Prossimo Passo

La nostra applicazione ora è configurata per usare Peewee, ma le nostre route in `auth.py` e `posts.py` contengono ancora il vecchio codice SQL.

Nella prossima lezione, che sarà l'ultima parte del refactoring, entreremo in quei file e sostituiremo ogni riga di accesso al database con la nuova, elegante sintassi dell'ORM.