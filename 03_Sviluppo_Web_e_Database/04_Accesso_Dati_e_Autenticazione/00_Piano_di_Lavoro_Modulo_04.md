# Piano di Lavoro: Modulo 04 - Accesso ai Dati e Autenticazione

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Struttura dell'app creata nel Modulo 03.
*   Conoscenza del linguaggio SQL (dal Modulo 01).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Collegare un'applicazione Flask a un database **SQLite**.
*   Applicare il **Repository Pattern** per separare la logica SQL dalle route HTTP.
*   Scrivere query SQL (`INSERT`, `SELECT`) all'interno di funzioni Python dedicate (repository).
*   Gestire l'invio di dati tramite **Form HTML** (metodo POST).
*   Implementare un sistema di **Autenticazione** completo (Registrazione, Login, Logout).
*   Comprendere e applicare l'hashing delle password per la sicurezza dei dati.
*   Gestire lo stato dell'utente tramite le **Sessioni**.

## 2. Contenuti Teorici e Pratici

In questo modulo daremo "memoria" alla nostra applicazione. Invece di scrivere SQL disordinato dentro le route, creeremo subito un modulo dedicato alla gestione dei dati.

*   **Lezione 01: Il Database e il Repository Pattern**
    *   **Teoria:** Perché separare l'SQL dal codice web. Introduzione al Data Access Layer.
    *   **Pratica:** Creazione di `app/db.py` (connessione) e `app/schema.sql`. Creazione della cartella `app/repositories/`. Implementazione del primo repository: `user_repository.py`. Scrittura delle funzioni `create_user` e `get_user_by_username` usando **SQL puro**.

*   **Lezione 02: Form HTML e Metodo POST**
    *   **Teoria:** Differenza tra GET e POST. L'oggetto `request` di Flask. Sicurezza dei dati input.
    *   **Pratica:** Creazione del Blueprint `auth.py`. Creazione dei template `register.html` e `login.html`. Collegamento dei form alle route che chiamano le funzioni del repository.

*   **Lezione 03: Gestione Sessioni e Sicurezza**
    *   **Teoria:** Statelessness di HTTP e necessità delle sessioni. Hashing delle password (mai in chiaro!).
    *   **Pratica:** Uso di `werkzeug.security`. Implementazione della logica di Login (verifica password -> avvio sessione) e Logout. Protezione delle route base.

## 3. Attività Principale: Sistema di Login
Gli studenti estenderanno il blog implementando la registrazione e l'accesso degli utenti.
Alla fine del modulo, sarà possibile registrarsi, fare login e vedere il proprio nome nella navbar (gestione dinamica del menu). Tutto il codice SQL sarà confinato nel file `user_repository.py`.

## 4. Metodologie di Valutazione
*   Verifica della separazione delle responsabilità: **zero SQL nei file Blueprint (`auth.py`)**.
*   Corretto utilizzo delle query parametrizzate nel repository per prevenire SQL Injection.
*   Funzionamento del flusso di autenticazione.