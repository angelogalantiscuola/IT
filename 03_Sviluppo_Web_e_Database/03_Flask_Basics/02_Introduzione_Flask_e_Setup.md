# Lezione 1: Introduzione a Flask e Struttura del Progetto

Nei capitoli precedenti abbiamo imparato la teoria del web (HTTP, API) e dei database (SQL). Ora è il momento di unire questi mondi e passare alla pratica. Per farlo, non partiremo da zero, ma useremo uno strumento che ci semplificherà enormemente la vita: un **Web Framework**.

In questo capitolo, useremo **Flask** per costruire la nostra prima applicazione web completa, passo dopo passo.

### 1. Cos'è un Web Framework? (Breve Riepilogo)

Come abbiamo visto, un framework è una "struttura" che risolve i problemi comuni e ripetitivi dello sviluppo software. Invece di dover gestire manualmente le complesse interazioni del protocollo HTTP, un web framework ci fornisce degli strumenti semplici per:

*   **Routing:** Associare un URL (es. `/contatti`) a una specifica funzione Python.
*   **Gestione Richieste/Risposte:** Accedere facilmente ai dati inviati dall'utente e formattare le risposte.
*   **Templating:** Generare pagine HTML dinamiche in modo efficiente e sicuro.

Useremo **Flask** perché è un **"micro-framework"**: è leggero, facile da imparare e non ci impone una struttura rigida, permettendoci di capire i concetti fondamentali in modo chiaro.

### 2. L'Anatomia di un Progetto Flask

Un progetto Flask ben organizzato segue una struttura di cartelle standard. Capire il ruolo di ogni componente è il primo passo per lavorare in modo ordinato.

```
progetto_flask_1/
├── .venv/                    # La cartella dell'ambiente virtuale (nascosta)
├── static/                   # Per file "statici" (CSS, immagini, JavaScript)
│   └── css/
│       └── style.css
├── templates/                # Per i file HTML (i nostri "template")
│   └── home.html
├── app.py                    # Il cuore della nostra applicazione Flask
└── database.db               # Il nostro database SQLite (verrà creato in seguito)
```

*   `app.py`: Questo file Python conterrà la logica principale della nostra applicazione: le definizioni delle route e le funzioni che interagiscono con il database.
*   `templates/`: Flask cercherà qui tutti i file HTML che gli chiederemo di renderizzare.
*   `static/`: Il browser dell'utente ha bisogno di accedere direttamente a file come fogli di stile (CSS) o immagini. Questa cartella è resa pubblicamente accessibile per questo scopo.
*   `.venv/`: La cartella che contiene una versione isolata di Python e tutte le librerie installate per questo specifico progetto.

### 3. Mettiamoci al Lavoro: Creare il Progetto

È il momento di scrivere del codice! Apri il tuo terminale e segui questi passaggi.

**1. Creare la Struttura delle Cartelle**
```bash
# Creiamo la cartella principale del progetto e ci entriamo
mkdir flask_1
cd flask_1

# Creiamo le sottocartelle per i template e i file statici
mkdir templates
mkdir static
```

**2. Creare e Attivare l'Ambiente Virtuale**
```bash
# Creiamo l'ambiente virtuale (usando .venv come nome)
python -m venv .venv

# Attiviamo l'ambiente
# Su macOS/Linux:
source .venv/bin/activate
# Su Windows (Git Bash o WSL):
# source .venv/Scripts/activate
```
Vedrai `(.venv)` apparire all'inizio del prompt del tuo terminale.

**3. Installare Flask**
Con l'ambiente attivo, installiamo la nostra unica dipendenza per ora:
```bash
pip install Flask
```

### 4. Il Nostro Primo "Hello, World!" con Flask

Ora apri la cartella `flask_1` con VS Code. Crea un nuovo file chiamato `app.py` e scrivi il seguente codice:

```python
# app.py

# 1. Importiamo la classe Flask dalla libreria che abbiamo installato
from flask import Flask

# 2. Creiamo un'istanza dell'applicazione Flask
#    __name__ è una variabile speciale di Python che ottiene il nome del modulo corrente.
#    Flask la usa per sapere dove cercare risorse come i template.
app = Flask(__name__)

# 3. Definiamo la nostra prima "route" usando un decoratore.
#    Questo dice a Flask: "Quando un utente visita l'URL principale ('/'),
#    esegui la funzione che si trova subito dopo (la funzione home)."
@app.route('/')
def home():
    # 4. Questa funzione viene chiamata "view function".
    #    Il valore che restituisce (return) è ciò che l'utente vedrà nel suo browser.
    return "<h1>Ciao Mondo! Benvenuto nella mia prima app Flask!</h1>"

# 5. Questa è una condizione standard in Python.
#    Assicura che il server di sviluppo venga avviato solo quando
#    questo script viene eseguito direttamente (e non quando viene importato).
if __name__ == '__main__':
    # 6. Avviamo l'applicazione.
    #    debug=True è utilissimo durante lo sviluppo:
    #    - Riavvia automaticamente il server ogni volta che salvi il file.
    #    - Mostra errori dettagliati nel browser se qualcosa va storto.
    app.run(debug=True)
```

### 5. Come Eseguire l'Applicazione

Assicurati di essere nel terminale con l'ambiente virtuale attivo e nella cartella `flask_1`. Esegui semplicemente:

```bash
python app.py
```

Vedrai un output simile a questo:
``` * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
```

Apri il tuo browser web e visita l'indirizzo `http://127.0.0.1:5000`. Congratulazioni, hai appena creato e lanciato la tua prima applicazione web!

### 6. Esercizio: Aggiungere una Nuova Pagina

Per consolidare quanto appreso, modifica il file `app.py` e aggiungi una nuova pagina.
*   Crea una nuova **route** che risponda all'URL `/about`.
*   Crea una **view function** chiamata `about()`.
*   La funzione deve restituire una semplice stringa di testo, come `"Questa è la pagina 'About' del nostro sito."`.

Salva il file, attendi che il server si riavvii automaticamente e prova a visitare `http://127.0.0.1:5000/about` nel tuo browser.