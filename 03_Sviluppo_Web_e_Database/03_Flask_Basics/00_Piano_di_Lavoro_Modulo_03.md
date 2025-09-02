# Piano di Lavoro: Modulo 03 - Backend con Flask: Le Basi

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Completamento con successo dei Moduli 01 (Database e SQL) e 02 (Basi del Web).
*   Solida comprensione di Python, inclusi dizionari, liste e funzioni.
*   Conoscenza di base di HTML.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Inizializzare e configurare un progetto web di base con Flask.
*   Definire URL (route) e associarli a funzioni Python per gestire le richieste HTTP.
*   Utilizzare il motore di template Jinja2 per creare pagine HTML dinamiche.
*   Gestire l'invio di dati da un client al server tramite form HTML (metodo POST).
*   Implementare un'applicazione completa con funzionalità CRUD (Create, Read, Update, Delete) interagendo direttamente con un database MariaDB.
*   Implementare un sistema di autenticazione utente con registrazione, login e gestione delle sessioni.
*   Proteggere specifiche route per consentire l'accesso solo agli utenti autenticati.
*   Utilizzare i "flash messages" per fornire feedback all'utente dopo un'azione.
*   Scrivere query SQL parametrizzate in Python per prevenire attacchi di SQL Injection.

## 2. Contenuti Teorici
Questo modulo è fortemente orientato alla pratica. La teoria sarà introdotta contestualmente alla costruzione dell'applicazione `flask_1`.

*   **Introduzione a Flask**: Cos'è un micro-framework, il suo ciclo di richiesta-risposta.
*   **Routing**: L'uso del decoratore `@app.route()` per mappare URL a funzioni.
*   **Templating con Jinja2**:
    *   La funzione `render_template()`.
    *   Sintassi di base: `{{ ... }}` per le variabili, `{% ... %}` per la logica.
    *   Ereditarietà dei template (`{% extends %}`, `{% block %}`).
    *   Uso di `url_for()` per generare URL dinamicamente.
*   **L'Oggetto `request`**: Accedere ai dati di una richiesta in arrivo (`request.method`, `request.form`, `request.args`).
*   **Sessioni Utente**: L'oggetto `session` di Flask per memorizzare informazioni tra una richiesta e l'altra e gestire lo stato di login.
*   **Interazione con il Database**:
    *   Utilizzo della libreria `mysql-connector-python`.
    *   Flusso: connessione -> creazione cursore -> esecuzione query -> commit -> chiusura.
    *   Importanza delle query parametrizzate per la sicurezza.

## 3. Attività Pratiche / Esercitazioni

L'attività principale del modulo sarà la **costruzione incrementale dell'applicazione `flask_1`**.

1.  **Setup del Progetto**: Creazione della struttura delle cartelle (`static`, `templates`), dell'ambiente virtuale e installazione di Flask.
2.  **Prime Route**: Creazione di una pagina "Home" e di una pagina "About" con template statici.
3.  **Visualizzazione Dati**: Lettura dei dati dal database (tabella `entries`) e loro visualizzazione dinamica in una tabella HTML.
4.  **Autenticazione Utente**:
    *   Creazione della tabella `users` nel database.
    *   Implementazione delle route e dei template per la registrazione (`/register`) e il login (`/login`).
    *   Uso di `werkzeug.security` per l'hashing delle password.
    *   Implementazione del logout.
5.  **Funzionalità CRUD Protette**:
    *   Creazione di un decoratore `@login_required` per proteggere le route.
    *   Implementazione dei form e della logica di backend per creare, modificare ed eliminare le "entries", accessibili solo agli utenti loggati.

## 4. Metodologie di Valutazione

*   Valutazione incrementale del codice prodotto durante lo sviluppo dell'applicazione `flask_1`.
*   Una verifica pratica in cui viene fornita un'applicazione Flask parzialmente completa e si chiede allo studente di implementare una funzionalità mancante (es. aggiungere la funzionalità di ricerca o una nuova route protetta).
*   Analisi della correttezza e della sicurezza del codice di interazione con il database.

## 5. Strumenti Necessari

*   Python 3.x e `venv`.
*   Flask (`pip install Flask`).
*   `mysql-connector-python` (`pip install mysql-connector-python`).
*   `Werkzeug` (installato automaticamente con Flask).
*   VS Code.
*   Server MariaDB locale.