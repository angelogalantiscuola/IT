# Piano di Lavoro: Modulo 02 - Basi dello Sviluppo Web e API REST

## 1. Obiettivi di Apprendimento

### Prerequisiti

- Completamento con successo del Modulo 01 (Fondamenti di Database).
- Comprensione di base del formato dati JSON.

### Competenze in Uscita

Al termine di questo modulo, lo studente sarà in grado di:

- Descrivere il modello di comunicazione client-server che è alla base del web.
- Spiegare il ciclo di una richiesta HTTP/HTTPS (richiesta, header, body, risposta, status code).
- Distinguere lo scopo dei principali metodi HTTP (GET, POST, PUT, DELETE).
- Definire cosa sia un'API e, in particolare, una Web API.
- Spiegare i principi fondamentali dello stile architetturale REST (risorse, endpoint, statelessness).
- Comprendere il ruolo di un Web Server Gateway Interface (WSGI/ASGI).
- Scrivere un semplice script Python utilizzando la libreria `requests` per consumare un'API REST pubblica.
- Comprendere il concetto di codice asincrono e la sua utilità nel contesto web.

## 2. Contenuti Teorici

Questo modulo fornisce il vocabolario e i concetti essenziali per capire come le applicazioni comunicano su Internet. I file si troveranno nella sottocartella `lessons/`.

1.  **Il Protocollo del Web**:

    - `02_HTTP.md`: Il protocollo HTTP, metodi, status code.
    - `03_HTTPS.md`: La sicurezza nella comunicazione web.

2.  **Architettura delle Applicazioni Web**:

    - `04_API.md`: Definizione di API e Web API.
    - `05_REST.md`: I principi dell'architettura REST.
    - `06_Endpoint.md`: Cosa sono e come si usano gli endpoint.
    - `07_WSGI_ASGI.md`: Il ponte tra il server web e l'applicazione Python.

3.  **Concetti Moderni**:
    - `08_Asynchronous_Code.md`: Introduzione al concetto di asincronia.
    - `09_Web_Framework.md`: A cosa serve un web framework (introduzione a Flask/FastAPI).

## 3. Attività Pratiche / Esercitazioni

Le attività pratiche di questo modulo sono focalizzate sull'interazione con API esistenti per capirne il funzionamento "dal vivo".

- **Esplorazione di API Pubbliche**: Utilizzando strumenti come `curl` da terminale o estensioni di VS Code (es. Thunder Client), gli studenti faranno richieste a API pubbliche (es. [JSONPlaceholder](https://jsonplaceholder.typicode.com/), API di GitHub) per analizzare le richieste e le risposte JSON.
- **Creazione di un Client Python**: Gli studenti scriveranno uno script Python che utilizza la libreria `requests` per:
  - Eseguire una richiesta `GET` a un'API per recuperare una lista di dati (es. una lista di post o utenti).
  - Eseguire una richiesta `POST` per inviare nuovi dati.
- **Client-Server Semplice**: Analisi e esecuzione del codice di `server.py` e `client.js` per vedere in azione un ciclo completo di richiesta-risposta tra un frontend basilare e un backend Python.

## 4. Metodologie di Valutazione

- Un quiz teorico per verificare la comprensione dei concetti chiave (HTTP, REST, API, client-server).
- Una verifica pratica in cui si chiede di scrivere uno script Python con `requests` che interagisca con un'API pubblica per risolvere un problema specifico (es. "trova l'utente con l'ID X e stampa il suo indirizzo email").

## 5. Strumenti Necessari

- Python 3.x.
- La libreria `requests` (da installare con `pip install requests`).
- Visual Studio Code con estensioni opzionali per testare API (es. Thunder Client).
- Accesso a Internet.