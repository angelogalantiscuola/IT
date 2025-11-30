# Lezione 1: Prepararsi al Cloud (Gunicorn e Requirements)

Fino ad ora abbiamo lanciato il sito con `flask run` o `python run.py`.
Questo va bene sul tuo PC, ma è pericoloso su Internet. Il server di sviluppo di Flask è come uno scooter: comodo per brevi distanze, ma non puoi usarlo per trasportare merci in autostrada.

Per andare online ("in Produzione"), ci serve un **Camion**. Ci serve **Gunicorn**.

### 1. Installare Gunicorn

Gunicorn (Green Unicorn) è un server **WSGI** professionale. Gestisce molte richieste contemporaneamente, è stabile e sicuro.

Apri il terminale (col venv attivo) e installalo:
```bash
pip install gunicorn
```

### 2. Provare Gunicorn in locale

Possiamo testarlo subito. Invece di `python run.py`, scrivi nel terminale:

```bash
# Sintassi: gunicorn nome_file:nome_variabile_app
gunicorn run:app
```

Se vedi partire il server (di solito sulla porta 8000), funziona!
Puoi spegnerlo con `CTRL+C`.

### 3. Il file `requirements.txt`

Quando caricheremo il codice sul Cloud (Render.com), il server remoto riceverà solo i nostri file `.py`. Non avrà le librerie installate (`flask`, `gunicorn`, ecc.).

Dobbiamo fornirgli una "Lista della Spesa". In Python, questa lista si chiama `requirements.txt`.

Generala automaticamente con questo comando:
```bash
pip freeze > requirements.txt
```

Apri il file creato. Dovrebbe contenere righe come:
```text
Flask==3.0.0
gunicorn==21.2.0
Werkzeug==3.0.1
...
```

### 4. Il file `.gitignore`

Assicuriamoci di non caricare file inutili o pericolosi su GitHub.
Crea un file chiamato `.gitignore` nella cartella principale (se non c'è già) e scrivi:

```text
# Ignora la cartella dell'ambiente virtuale
.venv/
venv/

# Ignora i file compilati di Python
__pycache__/
*.pyc

# Ignora il database locale e i segreti (IMPORTANTE!)
instance/
.env
```

Ora siamo pronti per configurare la sicurezza.