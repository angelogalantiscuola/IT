# Lezione 3: Andiamo Live su Render.com

È il momento di pubblicare. Useremo **Render**, una piattaforma PaaS (Platform as a Service) che offre un piano gratuito.

### 1. Push su GitHub

Assicurati che tutto il tuo codice (con le modifiche di Gunicorn e dotenv) sia su GitHub.
1.  `git add .`
2.  `git commit -m "Preparazione per il deploy"`
3.  `git push`

### 2. Creare il Web Service su Render

1.  Vai su [dashboard.render.com](https://dashboard.render.com) e crea un account.
2.  Clicca su **"New +"** e scegli **"Web Service"**.
3.  Collega il tuo account GitHub e seleziona il repository del blog.

### 3. Configurazione

Render ti chiederà come avviare il sito. Compila così:

*   **Name:** `blog-classe-5a` (o quello che vuoi).
*   **Region:** Frankfurt (o quello più vicino).
*   **Branch:** `main`.
*   **Runtime:** Python 3.
*   **Build Command:** Qui diciamo a Render di installare le librerie E creare il database:
    ```bash
    pip install -r requirements.txt && python setup_db.py
    ```
*   **Start Command:** Qui diciamo come avviare il server:
    ```bash
    gunicorn run:app
    ```
*   **Plan:** Free.

### 4. Impostare le Variabili d'Ambiente

Scorri giù fino alla sezione **"Environment Variables"**.
Aggiungi una variabile:
*   **Key:** `SECRET_KEY`
*   **Value:** (Inventa una password sicura, diversa da quella locale).

### 5. Deploy!

Clicca su **"Create Web Service"**.
Render inizierà a scaricare il codice, installare le librerie ed eseguire `setup_db.py`.
Dopo qualche minuto, vedrai una spunta verde **"Live"** e un link tipo `https://blog-classe-5a.onrender.com`.

Cliccaci. Il tuo sito è online!

---

### ⚠️ ATTENZIONE: Il problema dei dati effimeri

Se provi a registrarti e creare un post, funzionerà.
Tuttavia, **se Render riavvia il server (o se fai un nuovo deploy), i dati spariranno.**

**Perché?**
I servizi Cloud gratuiti come questo usano dischi "effimeri". Ogni volta che riavvii, è come se ti dessero un computer nuovo di zecca. Il codice c'è, ma i file creati dopo (come `blog.sqlite`) vengono cancellati.

**Come si risolve nel mondo reale?**
In un progetto professionale, non useremmo SQLite. Useremmo un database esterno (come **PostgreSQL**) che vive su un server separato e non si cancella mai.
Per questo progetto scolastico, va bene usare SQLite per la dimostrazione, ma ricordate: **non è una memoria permanente**.