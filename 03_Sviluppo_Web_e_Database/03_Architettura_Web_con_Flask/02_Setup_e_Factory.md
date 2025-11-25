# Lezione 1: Setup Professionale e Application Factory

In questo modulo faremo un salto di qualità. Non scriveremo più tutto il codice in un solo file. Impareremo a organizzare il progetto come fanno i professionisti Python.

Prima di scrivere codice, dobbiamo capire due concetti fondamentali di Python e Flask.

### 1. Concetto Chiave: Pacchetti e `__init__.py`

In Python, come facciamo a dire che una cartella non è solo un contenitore di file, ma un **Modulo** (o Pacchetto) che contiene codice che vogliamo importare e usare?

Lo facciamo creando all'interno della cartella un file speciale chiamato `__init__.py` (due underscore prima e dopo).

*   **Senza `__init__.py`**: La cartella è solo una directory del sistema operativo.
*   **Con `__init__.py`**: La cartella diventa un **Pacchetto Python**.

Quando Python vede questo file, sa che può trattare quella cartella come se fosse una libreria. Il codice scritto dentro `__init__.py` viene eseguito automaticamente appena il pacchetto viene importato.

### 2. Concetto Chiave: La Cartella `instance`

Quando sviluppi un'applicazione web, ci sono file che riguardano il codice (che è uguale per tutti gli sviluppatori) e file che riguardano la **configurazione locale** (che cambiano da computer a computer).

Flask usa una cartella standard chiamata `instance/` per contenere:
1.  **I Segreti:** Chiavi di sicurezza, password (che non vanno mai condivise).
2.  **Il Database:** Il file del database SQLite (che cambia mentre usi l'app).

Questa cartella è speciale perché **non dovrebbe mai essere condivisa** (ad esempio su GitHub). È lo spazio "privato" dell'applicazione sul tuo computer.

### 3. Concetto Chiave: L'Application Factory

Nei tutorial base, spesso si vede:
```python
app = Flask(__name__)  # Creato globalmente
```
Questo ha un difetto: l'applicazione viene creata subito, appena avvii Python. Non puoi cambiarne la configurazione facilmente.

Il pattern **Application Factory** (Fabbrica di Applicazioni) risolve il problema. Invece di creare l'app come variabile globale, scriviamo una **funzione** che crea e restituisce l'app.

```python
def create_app():
    app = Flask(...)
    return app
```
È come avere uno stampino (la funzione): possiamo usarlo per creare l'applicazione quando vogliamo e come vogliamo.

---

### Mettiamoci al Lavoro: Il Codice

Ora creiamo la struttura.

**1. Struttura delle Cartelle**
Crea una cartella `blog_scolastico` e al suo interno questa struttura:

```text
blog_scolastico/
├── .venv/              <-- Il tuo ambiente virtuale
├── instance/           <-- Cartella vuota (per ora)
├── app/                <-- Cartella del pacchetto
│   └── __init__.py     <-- File vuoto (per ora)
└── run.py              <-- File vuoto (per ora)
```

**2. Scriviamo la Factory (`app/__init__.py`)**
Apri `app/__init__.py`. Questo codice definisce come "nasce" la nostra applicazione. Lo terremo pulito e semplice.

```python
import os
from flask import Flask

def create_app():
    # 1. Creiamo l'istanza di Flask
    # instance_relative_config=True dice a Flask: 
    # "Cerca la cartella 'instance' fuori da 'app', non dentro."
    app = Flask(__name__, instance_relative_config=True)

    # 2. Configurazione di base
    # Qui impostiamo le variabili fondamentali.
    app.config.from_mapping(
        # SECRET_KEY serve a Flask per firmare i dati sicuri (es. sessioni).
        # 'dev' va bene per sviluppare, ma in produzione andrà cambiata.
        SECRET_KEY='dev',
        # Diciamo a Flask dove salvare il file del database SQLite
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),
    )

    # 3. Assicuriamoci che la cartella 'instance' esista fisicamente.
    # Se non esiste (es. è la prima volta che avvii), Flask la crea.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 4. Una route di prova per vedere se funziona
    @app.route('/hello')
    def hello():
        return 'Ciao! La Factory funziona correttamente.'

    return app
```


**3. L'Entry Point (`run.py`)**
Ora ci serve un file per "accendere" la fabbrica. Questo file sta fuori dalla cartella `app`.

Apri `run.py` e scrivi:

```python
# Importiamo la funzione create_app dal pacchetto 'app'
# Questo è possibile perché 'app' ha un file __init__.py!
from app import create_app

# Chiamiamo la fabbrica per ottenere l'applicazione
app = create_app()

# Se questo file viene eseguito direttamente (non importato), avvia il server
if __name__ == '__main__':
    app.run(debug=True)
```

### 4. Verifica Finale

1.  Apri il terminale nella cartella `blog_scolastico`.
2.  Attiva l'ambiente virtuale (se non l'hai fatto).
3.  Esegui il comando:
    ```bash
    python run.py
    ```
4.  Se leggi `Running on http://127.0.0.1:5000`, apri il browser a quell'indirizzo e aggiungi `/hello`.

Se vedi il messaggio di saluto, hai creato con successo un'architettura Flask professionale!