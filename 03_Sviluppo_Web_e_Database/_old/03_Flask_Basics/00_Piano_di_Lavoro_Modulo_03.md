# Piano di Lavoro: Capitolo 03 - Backend con Flask: Le Basi

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Completamento con successo dei Capitoli 01 (Database e SQL) e 02 (Basi del Web).
*   Solida comprensione di Python, inclusi dizionari, liste e funzioni.
*   Conoscenza di base di HTML.

### Competenze in Uscita
Al termine di questo capitolo, lo studente sarà in grado di:
*   Spiegare cos'è un web framework e perché si utilizza.
*   Inizializzare e configurare un progetto web di base con Flask.
*   Definire URL (route) e associarli a funzioni Python per gestire le richieste HTTP.
*   Utilizzare il motore di template Jinja2 per creare pagine HTML dinamiche e riutilizzabili.
*   Gestire l'invio di dati da un client al server tramite form HTML (metodo POST).
*   Interagire con un database **SQLite** da un'applicazione Flask, eseguendo query SQL parametrizzate.
*   Implementare un'applicazione completa con funzionalità CRUD (Create, Read, Update, Delete).
*   Implementare un sistema di autenticazione utente con registrazione, login e gestione delle sessioni.
*   Proteggere specifiche route per consentire l'accesso solo agli utenti autenticati.

## 2. Contenuti Teorici e Pratici (Lezioni)
Questo capitolo è fortemente orientato alla pratica. La teoria sarà introdotta contestualmente alla costruzione incrementale dell'applicazione `flask_1`.

*   **Lezione 01: Introduzione a Flask e Struttura del Progetto**
    *   **Teoria:** Cos'è un framework, la filosofia di Flask, il ciclo richiesta-risposta.
    *   **Pratica:** Setup del progetto, installazione delle dipendenze, creazione della prima route "Hello, World!".

*   **Lezione 02: Il Livello di Presentazione con Jinja2**
    *   **Teoria:** Server-Side Rendering, sintassi di Jinja2, ereditarietà dei template (pattern `base.html`).
    *   **Pratica:** Creazione di template HTML che estendono una struttura base e visualizzano dati passati da Flask.

*   **Lezione 03: Visualizzare Dati dal Database**
    *   **Teoria:** Pattern per la gestione della connessione a un database SQLite in Flask.
    *   **Pratica:** Esecuzione di query `SELECT` e visualizzazione dinamica dei risultati in una tabella HTML.

*   **Lezione 04: Gestione dei Form e Creazione di Dati**
    *   **Teoria:** Metodo POST, l'oggetto `request`, il pattern Post/Redirect/Get.
    *   **Pratica:** Creazione di un form HTML per l'inserimento di nuovi dati e implementazione della logica `INSERT` nel database.

*   **Lezione 05: Autenticazione e Gestione delle Sessioni**
    *   **Teoria:** Sicurezza delle password (hashing e salting con `werkzeug.security`), il concetto di sessione HTTP.
    *   **Pratica:** Implementazione del flusso completo di registrazione, login e logout utilizzando le sessioni di Flask.

*   **Lezione 06: Protezione delle Route e Funzionalità CRUD Complete**
    *   **Teoria:** Creazione di decoratori personalizzati in Python.
    *   **Pratica:** Scrittura di un decoratore `@login_required` per proteggere le route. Implementazione della logica di modifica (`UPDATE`) ed eliminazione (`DELETE`) dei dati.

## 3. Attività Principale: Progetto `flask_1`
L'attività centrale del capitolo sarà la **costruzione incrementale dell'applicazione `flask_1`**. Si partirà da un file vuoto e, lezione dopo lezione, si aggiungeranno nuove funzionalità fino ad ottenere un blog o un diario online completo, con gestione utenti e post.

## 4. Metodologie di Valutazione
*   Valutazione incrementale del codice prodotto durante lo sviluppo dell'applicazione `flask_1`.
*   Una verifica pratica in cui viene fornita un'applicazione Flask parzialmente completa e si chiede allo studente di implementare una funzionalità mancante (es. aggiungere la funzionalità di ricerca o una nuova route protetta).
*   Analisi della correttezza e della sicurezza del codice di interazione con il database (uso corretto delle query parametrizzate).

## 5. Strumenti Necessari
*   Python 3.x e `venv`.
*   Flask (`pip install Flask`).
*   La libreria `sqlite3` (inclusa in Python, non serve installazione).
*   `Werkzeug` (installato automaticamente con Flask).
*   Un client per database SQLite per ispezionare il file del database (es. l'estensione **SQLite per VS Code**).