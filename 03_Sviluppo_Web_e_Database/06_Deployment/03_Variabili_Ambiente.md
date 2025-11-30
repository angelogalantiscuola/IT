# Lezione 2: Sicurezza e Variabili d'Ambiente

Apri il tuo file `app/__init__.py`. Probabilmente vedrai questo:
`SECRET_KEY='dev'`

Se carichi questo codice su GitHub, **chiunque nel mondo** potrà vedere la tua chiave segreta. Un hacker potrebbe falsificare i cookie di sessione ed entrare come amministratore nel tuo sito.

**Regola d'oro:** Mai scrivere password o chiavi segrete nel codice sorgente.

### 1. Cosa sono le Variabili d'Ambiente?

Sono variabili che vivono "fuori" dal codice, nel sistema operativo del server.
*   Sul tuo PC, le leggi da un file nascosto.
*   Su Render.com, le imposti in una schermata protetta.
*   Il codice Python le legge usando `os.environ.get()`.

### 2. Installare `python-dotenv`

Per gestire queste variabili comodamente sul nostro PC, usiamo una libreria:

```bash
pip install python-dotenv
# Ricordati di aggiornare i requirements!
pip freeze > requirements.txt
```

### 3. Creare il file `.env`

Crea un file chiamato `.env` nella cartella principale (accanto a `run.py`).
Scrivici dentro la tua chiave segreta vera:

```text
SECRET_KEY=una_stringa_lunga_e_difficile_da_indovinare_12345
```

(Nota: Assicurati che `.env` sia nel `.gitignore`! Non deve finire su GitHub).

### 4. Aggiornare `app/__init__.py`

Modifichiamo la Factory per leggere questa variabile.

```python
import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # MODIFICA QUI:
    # os.environ.get('NOME_VAR', 'valore_default')
    # Se trova SECRET_KEY nel sistema/file .env la usa.
    # Altrimenti usa 'dev' (utile per non bloccarci se manca il file).
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),
    )
    
    # ... resto del codice ...
```

### 5. Aggiornare `run.py`

Dobbiamo dire a Python di caricare il file `.env` all'avvio.

```python
from app import create_app
from dotenv import load_dotenv # Importa la libreria

# Carica le variabili dal file .env
load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

Ora il tuo codice è sicuro. Anche se il codice finisce su GitHub, la chiave segreta resta sul tuo computer.